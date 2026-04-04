"""Built-in slash command handlers."""

from __future__ import annotations

import asyncio
import os
import sys

from nanobot import __version__
from nanobot.bus.events import OutboundMessage
from nanobot.command.router import CommandContext, CommandRouter
from nanobot.utils.helpers import build_status_content


def _interaction_metadata(msg_metadata: object, *, render_as: str | None = None) -> dict:
    # Why: 统一透传 Discord interaction 信息，避免各命令各自拼装导致回填行为不一致。
    meta: dict = {}
    if isinstance(msg_metadata, dict) and isinstance(msg_metadata.get("discord_interaction"), dict):
        meta["discord_interaction"] = dict(msg_metadata["discord_interaction"])
    if render_as is not None:
        meta["render_as"] = render_as
    return meta


async def cmd_stop(ctx: CommandContext) -> OutboundMessage:
    """Cancel all active tasks and subagents for the session."""
    loop = ctx.loop
    msg = ctx.msg
    # Why: /stop 要按 session 维度止血，只取消当前会话下仍在运行的任务。
    tasks = loop._active_tasks.pop(msg.session_key, [])
    # Why: 先发取消信号并统计成功数，给用户一个可见的停止结果。
    cancelled = sum(1 for t in tasks if not t.done() and t.cancel())
    for t in tasks:
        try:
            # Why: 显式等待任务收尾，避免取消异常泄漏并确保资源清理完成。
            await t
        except (asyncio.CancelledError, Exception):
            pass
    # Why: 会话下可能还有子代理在后台执行，/stop 必须一并回收。
    sub_cancelled = await loop.subagents.cancel_by_session(msg.session_key)
    total = cancelled + sub_cancelled
    content = f"Stopped {total} task(s)." if total else "No active task to stop."
    return OutboundMessage(
        channel=msg.channel,
        chat_id=msg.chat_id,
        content=content,
        metadata=_interaction_metadata(msg.metadata),
    )


async def cmd_restart(ctx: CommandContext) -> OutboundMessage:
    """Restart the process in-place via os.execv."""
    msg = ctx.msg

    async def _do_restart():
        await asyncio.sleep(1)
        os.execv(sys.executable, [sys.executable, "-m", "nanobot"] + sys.argv[1:])

    asyncio.create_task(_do_restart())
    return OutboundMessage(
        channel=msg.channel,
        chat_id=msg.chat_id,
        content="Restarting...",
        metadata=_interaction_metadata(msg.metadata),
    )


async def cmd_status(ctx: CommandContext) -> OutboundMessage:
    """Build an outbound status message for a session."""
    loop = ctx.loop
    session = ctx.session or loop.sessions.get_or_create(ctx.key)
    ctx_est = 0
    try:
        ctx_est, _ = loop.memory_consolidator.estimate_session_prompt_tokens(session)
    except Exception:
        pass
    if ctx_est <= 0:
        ctx_est = loop._last_usage.get("prompt_tokens", 0)
    return OutboundMessage(
        channel=ctx.msg.channel,
        chat_id=ctx.msg.chat_id,
        content=build_status_content(
            version=__version__, model=loop.model,
            start_time=loop._start_time, last_usage=loop._last_usage,
            context_window_tokens=loop.context_window_tokens,
            session_msg_count=len(session.get_history(max_messages=0)),
            context_tokens_estimate=ctx_est,
        ),
        metadata=_interaction_metadata(ctx.msg.metadata, render_as="text"),
    )


async def cmd_new(ctx: CommandContext) -> OutboundMessage:
    """Start a fresh session."""
    loop = ctx.loop
    session = ctx.session or loop.sessions.get_or_create(ctx.key)
    # Why: 只归档本轮尚未 consolidate 的增量消息，避免重复归档已沉淀内容。
    snapshot = session.messages[session.last_consolidated:]
    # Why: /new 的语义是立即切断旧上下文，所以先清空再进入下一轮会话。
    session.clear()
    loop.sessions.save(session)
    # Why: 让后续读取强制拿到清空后的 session，避免旧缓存继续参与推理。
    loop.sessions.invalidate(session.key)
    if snapshot:
        # Why: 归档走后台任务，避免用户执行 /new 时被历史整理阻塞。
        loop._schedule_background(loop.memory_consolidator.archive_messages(snapshot))
    return OutboundMessage(
        channel=ctx.msg.channel, chat_id=ctx.msg.chat_id,
        content="New session started.",
        metadata=_interaction_metadata(ctx.msg.metadata),
    )


async def cmd_help(ctx: CommandContext) -> OutboundMessage:
    """Return available slash commands."""
    lines = [
        "🐈 nanobot commands:",
        "/new — Start a new conversation",
        "/stop — Stop the current task",
        "/restart — Restart the bot",
        "/status — Show bot status",
        "/help — Show available commands",
    ]
    return OutboundMessage(
        channel=ctx.msg.channel,
        chat_id=ctx.msg.chat_id,
        content="\n".join(lines),
        metadata=_interaction_metadata(ctx.msg.metadata, render_as="text"),
    )


def register_builtin_commands(router: CommandRouter) -> None:
    """Register the default set of slash commands."""
    router.priority("/stop", cmd_stop)
    router.priority("/restart", cmd_restart)
    router.priority("/status", cmd_status)
    router.exact("/new", cmd_new)
    router.exact("/status", cmd_status)
    router.exact("/help", cmd_help)
