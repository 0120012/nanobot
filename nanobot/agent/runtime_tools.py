"""Shared workspace-scoped tool registration helpers."""

from pathlib import Path

from nanobot.agent.skills import BUILTIN_SKILLS_DIR
from nanobot.agent.tools.filesystem import EditFileTool, ListDirTool, ReadFileTool, WriteFileTool
from nanobot.agent.tools.registry import ToolRegistry
from nanobot.agent.tools.search import GlobTool, GrepTool
from nanobot.agent.tools.shell import ExecTool
from nanobot.agent.tools.web import WebFetchTool, WebSearchTool
from nanobot.config.schema import ExecToolConfig, WebSearchConfig


def register_workspace_tools(
    tools: ToolRegistry, *, workspace: Path, restrict_to_workspace: bool,
    exec_config: ExecToolConfig, web_search_config: WebSearchConfig, web_proxy: str | None,
) -> None:
    """Register the shared workspace-scoped base tools."""
    # Why: 主 agent 和独立 agent 必须复用同一套基础工具装配规则，避免后续多 agent 演进时出现能力漂移和隔离边界不一致。
    allowed_dir = workspace if restrict_to_workspace else None
    extra_read = [BUILTIN_SKILLS_DIR] if allowed_dir else None
    tools.register(ReadFileTool(workspace=workspace, allowed_dir=allowed_dir, extra_allowed_dirs=extra_read))
    for cls in (WriteFileTool, EditFileTool, ListDirTool, GlobTool, GrepTool):
        tools.register(cls(workspace=workspace, allowed_dir=allowed_dir))
    if exec_config.enable:
        tools.register(ExecTool(
            working_dir=str(workspace), timeout=exec_config.timeout,
            restrict_to_workspace=restrict_to_workspace, path_append=exec_config.path_append,
        ))
    tools.register(WebSearchTool(config=web_search_config, proxy=web_proxy))
    tools.register(WebFetchTool(proxy=web_proxy))
