# Development

<!-- current-documentation-provenance -->
Documentation reviewed: 2026-10-13 · Git source base: `54b3948ffc13afd2291c5764435887b4257666be` · [Current architecture and feature guide](ayu-develop.md).
Historical execution commands/results below retain their original dates and scope; this metadata update is not a new application test run.
<!-- /current-documentation-provenance -->


## uv maintenance workflow (2026-10-12)

Selected complete environment: Python 3.15.0; build backend `hatchling.build`. The workspace uses uv 0.13.0. The complete native source build and original-suite results are recorded in [validation](validation.md).

```sh
export UV_PYTHON_PREFERENCE=only-managed
export PYCARES_USE_SYSTEM_LIB=1
export CFLAGS='-I/opt/homebrew/opt/c-ares/include'
export LDFLAGS='-L/opt/homebrew/opt/c-ares/lib'
uv python install 3.15.0
uv lock --upgrade
uv sync --all-extras --python 3.15.0
uv build --python 3.15.0
uv run --frozen --all-extras python -m compileall -q src/octobot_tentacles
../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip
ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all
uv run --frozen --all-extras python -m pytest tentacles --rootdir=. --continue-on-collection-errors
```

Keep source resources inside their package and preserve the repository's existing src layout. Rebuild after source/native/asset changes. Use the locked environment for final verification. Commands above are the standard workflow, not a promise that every existing suite currently passes; consult validation for exact outcomes and unresolved compatibility issues.

This plugin archive uses the adjacent current [OctoBot host](../../OctoBot) through an explicit uv source. Export and install this repository's 134 actual plugins before testing; `tentacles/` is the generated runtime tree. Run from this repository so its metadata registry is selected. The existing `tests/static` symlink shares the host's real market-data fixtures. The root `conftest.py` creates and closes the real run-database context required by current trading-mode inputs, then delegates initialization to the host. No replacement plugin archive or synthetic exchange messages are substituted for the existing cases. Live WebSocket cases require reachable public exchange endpoints and retain exact equality assertions over the current producers' declared channels. Their expected channels follow the host's `watchTicker` → `Ticker`, `watchOHLCV` → `Kline`/closed-only `OHLCV`, and `watchTrades` → `RecentTrade` contract. The host deliberately suppresses trade feeds when ticker data supplies spot prices; Kucoin explicitly overrides that suppression. Closed minute-candle checks wait 75 seconds and initialize their history from real REST responses.

The legacy Coinbase Pro plugin retains its user-facing name and selects the current `coinbaseexchange` REST/WebSocket implementation for the same Exchange API. The [Kraken feed adapter](../src/octobot_tentacles/Trading/Exchange/kraken_websocket_feed/kraken_websocket.py) compensates for the current SDK's dictionary-style timestamp filter on candle arrays: it obtains unchanged real venue candles and applies chronological ordering, `since` and `limit` through their numeric timestamp field. No synthetic candle or channel events are generated. AscendEX was [delisted from CCXT](https://github.com/ccxt/ccxt/pull/29079) on July 2, 2026; its original case remains a failure on the current dependency rather than being redirected to another venue.

The current [licensed Tulipy source build](../../OctoBot/vendor/octobot-tulipy/PROVENANCE.md) retains 0.4.11b13 and NumPy 2.4.2, with strict native multiply/add arithmetic. The original 14 financial cases pass without replay hooks or changes to expected returns. Python 3.15.0 also builds the complete dependency graph using the host's documented `PYCARES_USE_SYSTEM_LIB=1` Homebrew c-ares build flags, and passes the same native financial cases and strict source compilation. Complete live-suite outcomes remain recorded in validation.

Kraken's native SDK additionally uses a shared OHLCV subscription key for every interval of a symbol. The plugin's native client subclass includes the requested interval in subscription keys and the real received interval in resolution keys, while delegating parsing and subscriptions to the unchanged SDK methods. This prevents minute and hour consumers receiving each other's candle buffers. The host stops and awaits its actual feed tasks before closing their shared client, preventing pending subscriptions reopening sockets during shutdown.

The selected Python 3.15 full run passes 449 of the 451 original cases. AscendEX requires a connector removed from the latest SDK and its real public endpoint returned HTTP 403. Kraken’s exact live coverage case still requires a real minute-bar transition during its original 75-second observation window: an actual observed transition passed, while other windows received only live ticker/kline data. A bounded 120-second control also produced both passing and failing windows. The original symbols, 75-second wait, 150-second case timeout and exact channel-set assertion remain intact; no timer-generated closure or synthetic event is used.
