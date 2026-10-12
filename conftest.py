"""Use the real host test helpers when collecting this plugin archive."""
import sys
from pathlib import Path

_HOST = Path(__file__).resolve().parent.parent / "OctoBot"
sys.path.insert(0, str(_HOST))
# Anchor the existing host helper package before plugin test package discovery.
import tests.test_utils.config  # noqa: E402,F401


import pytest_asyncio
import asyncio
import aiohttp
import octobot_commons.databases as databases
import octobot_trading.modes as modes


@pytest_asyncio.fixture(autouse=True)
async def release_owned_http_sessions(monkeypatch):
    """Close sessions allocated by this case while their owning loops are alive."""
    sessions = []
    original_init = aiohttp.ClientSession.__init__

    def initialize_owned_session(session, *args, **kwargs):
        original_init(session, *args, **kwargs)
        sessions.append(session)

    monkeypatch.setattr(aiohttp.ClientSession, "__init__", initialize_owned_session)
    yield
    current_loop = asyncio.get_running_loop()
    for session in sessions:
        if session.closed:
            continue
        if session._loop is current_loop:
            await session.close()
        elif session._loop.is_running():
            await asyncio.wrap_future(asyncio.run_coroutine_threadsafe(session.close(), session._loop))
        else:
            raise RuntimeError("An owned HTTP session outlived its worker event loop")
    if any(session._loop is current_loop for session in sessions):
        # aiohttp schedules TLS transport shutdown after ClientSession.close.
        await asyncio.sleep(0.25)


@pytest_asyncio.fixture(autouse=True)
async def legacy_mode_run_context(monkeypatch):
    """Initialize the real run context required by current trading-mode inputs."""
    provider = databases.RunDatabasesProvider.instance()
    initialize = modes.AbstractTradingMode.initialize
    owned_ids = set()

    async def initialize_with_run_context(mode, *args, **kwargs):
        manager = mode.exchange_manager
        if manager.bot_id is None:
            manager.bot_id = manager.id
        if not provider.has_bot_id(manager.bot_id):
            await provider.add_bot_id(
                manager.bot_id,
                databases.RunDatabasesIdentifier(type(mode), enable_storage=False),
            )
            owned_ids.add(manager.bot_id)
        return await initialize(mode, *args, **kwargs)

    monkeypatch.setattr(modes.AbstractTradingMode, "initialize", initialize_with_run_context)
    yield
    for bot_id in owned_ids:
        if provider.has_bot_id(bot_id):
            await provider.remove_bot_id(bot_id).close()
