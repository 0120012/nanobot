from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from nanobot.bus.events import OutboundMessage
from nanobot.bus.queue import MessageBus
from nanobot.channels.discord import DiscordChannel, DiscordConfig


@pytest.mark.asyncio
async def test_handle_interaction_create_forwards_new_command() -> None:
    channel = DiscordChannel(
        DiscordConfig(enabled=True, token="bot-token", allow_from=["*"]),
        MessageBus(),
    )
    channel._handle_message = AsyncMock()

    payload = {
        "type": 2,
        "id": "evt-1",
        "token": "itk-1",
        "application_id": "app-1",
        "channel_id": "chan-1",
        "guild_id": "guild-1",
        "data": {"name": "new"},
        "member": {"user": {"id": "user-1"}},
    }
    await channel._handle_interaction_create(payload)

    channel._handle_message.assert_awaited_once()
    kwargs = channel._handle_message.await_args.kwargs
    assert kwargs["sender_id"] == "user-1"
    assert kwargs["chat_id"] == "chan-1"
    assert kwargs["content"] == "/new"
    assert kwargs["metadata"]["discord_interaction"]["application_id"] == "app-1"


@pytest.mark.asyncio
async def test_handle_interaction_create_forwards_stop_command() -> None:
    channel = DiscordChannel(
        DiscordConfig(enabled=True, token="bot-token", allow_from=["*"]),
        MessageBus(),
    )
    channel._handle_message = AsyncMock()

    payload = {
        "type": 2,
        "id": "evt-2",
        "token": "itk-2",
        "application_id": "app-2",
        "channel_id": "chan-2",
        "guild_id": "guild-2",
        "data": {"name": "stop"},
        "member": {"user": {"id": "user-2"}},
    }
    await channel._handle_interaction_create(payload)

    channel._handle_message.assert_awaited_once()
    kwargs = channel._handle_message.await_args.kwargs
    assert kwargs["sender_id"] == "user-2"
    assert kwargs["chat_id"] == "chan-2"
    assert kwargs["content"] == "/stop"
    assert kwargs["metadata"]["discord_interaction"]["application_id"] == "app-2"


@pytest.mark.asyncio
async def test_send_uses_interaction_webhook_for_slash_response() -> None:
    channel = DiscordChannel(
        DiscordConfig(enabled=True, token="bot-token", allow_from=["*"]),
        MessageBus(),
    )
    response = SimpleNamespace(raise_for_status=lambda: None)
    channel._http = SimpleNamespace(
        patch=AsyncMock(return_value=response),
        post=AsyncMock(return_value=response),
    )
    channel._stop_typing = AsyncMock()

    await channel.send(
        OutboundMessage(
            channel="discord",
            chat_id="chan-3",
            content="done",
            metadata={"discord_interaction": {"token": "itk-3", "application_id": "app-3"}},
        )
    )

    channel._http.patch.assert_awaited_once()
    patch_url = channel._http.patch.await_args.args[0]
    assert patch_url.endswith("/webhooks/app-3/itk-3/messages/@original")


@pytest.mark.asyncio
async def test_ensure_application_commands_registers_new_and_stop() -> None:
    channel = DiscordChannel(
        DiscordConfig(
            enabled=True,
            token="bot-token",
            application_id="app-4",
            allow_from=["*"],
        ),
        MessageBus(),
    )
    channel._http = SimpleNamespace()
    channel._send_payload = AsyncMock(return_value=True)

    await channel._ensure_application_commands()

    channel._send_payload.assert_awaited_once_with(
        "https://discord.com/api/v10/applications/app-4/commands",
        {"Authorization": "Bot bot-token"},
        [
            {"name": "help", "description": "Show available commands"},
            {"name": "new", "description": "Start a new conversation"},
            {"name": "restart", "description": "Restart the bot"},
            {"name": "status", "description": "Show bot status"},
            {"name": "stop", "description": "Stop the current task"},
        ],
        method="PUT",
    )


@pytest.mark.asyncio
async def test_handle_interaction_create_denies_unauthorized_user() -> None:
    channel = DiscordChannel(
        DiscordConfig(enabled=True, token="bot-token", allow_from=["allowed-user"]),
        MessageBus(),
    )
    response = SimpleNamespace(raise_for_status=lambda: None)
    channel._http = SimpleNamespace(post=AsyncMock(return_value=response))
    channel._handle_message = AsyncMock()

    payload = {
        "type": 2,
        "id": "evt-5",
        "token": "itk-5",
        "application_id": "app-5",
        "channel_id": "chan-5",
        "guild_id": "guild-5",
        "data": {"name": "new"},
        "member": {"user": {"id": "denied-user"}},
    }
    await channel._handle_interaction_create(payload)

    channel._http.post.assert_awaited_once()
    assert channel._http.post.await_args.kwargs["json"] == {
        "type": 4,
        "data": {"content": "Access denied.", "flags": 64},
    }
    channel._handle_message.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_interaction_create_stops_when_ack_fails() -> None:
    channel = DiscordChannel(
        DiscordConfig(enabled=True, token="bot-token", allow_from=["allowed-user"]),
        MessageBus(),
    )

    def _raise_status() -> None:
        raise RuntimeError("ack failed")

    channel._http = SimpleNamespace(post=AsyncMock(return_value=SimpleNamespace(raise_for_status=_raise_status)))
    channel._handle_message = AsyncMock()

    payload = {
        "type": 2,
        "id": "evt-6",
        "token": "itk-6",
        "application_id": "app-6",
        "channel_id": "chan-6",
        "guild_id": "guild-6",
        "data": {"name": "stop"},
        "member": {"user": {"id": "allowed-user"}},
    }
    await channel._handle_interaction_create(payload)

    channel._http.post.assert_awaited_once()
    channel._handle_message.assert_not_awaited()
