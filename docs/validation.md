# OctoBot-Tentacles maintenance validation


Current user-authorized test policy: The user explicitly disabled the AscendEX and Kraken `test_start_spot_websocket` cases with pytest skip markers. Original test bodies, channels and financial assertions remain unchanged. The retained complete-suite baseline is 449 passes and two failures; those two failures are now intentionally skipped, with exact selected-case verification recorded separately.

Selected runtime: **managed Python 3.15.0**, uv **0.13.0**, `hatchling.build`; source commit `2ae9fdc7288f64bb9f1881bec0e6b43e92152a3e`. The actual latest licensed Tulipy source builds, both source distribution and wheel build, and strict source compilation pass.

## Complete existing-suite result

The complete original suite finished with **449 passed and two failed**, all **451 original cases preserved**, in 693.67 seconds. Exit 1 is retained. All 14 original financial cases and all web/authentication cases pass. No cases, skips, channel assertions or expected profit values were added or weakened.

- **AscendEX:** the latest SDK removed this connector, and the actual public endpoint returned HTTP 403. The [official removal](https://github.com/ccxt/ccxt/pull/29079) is recorded; no different venue substitutes for the original case.
- **Kraken:** the exact live coverage assertion sometimes receives ticker and kline data without a real closed minute candle in the original 75-second observation window. A real observed candle transition passed; other windows failed. A bounded 120-second diagnostic also produced both outcomes, so extending the timeout is not claimed as a fix. The original symbols, 75-second wait, 150-second case limit and exact channel-set assertion remain intact. No timer-generated closure or synthetic event is used.

## Native numerical and SDK repairs

The [licensed latest Tulipy source](../../OctoBot/vendor/octobot-tulipy/PROVENANCE.md) preserves its C recurrence while disabling fused multiply/add contraction. All 18,860 recorded real RSI arrays match the historical arithmetic bit for bit, and the original 14 financial cases pass using native imports. A fresh selected-main Python 3.15 run passed those 14 cases in 21.88 seconds; no replay hook is part of production or final verification.

The [Kraken adapter](../src/octobot_tentacles/Trading/Exchange/kraken_websocket_feed/kraken_websocket.py) keeps real native subscriptions and parsers, fixes the SDK's timestamp-field filtering on candle arrays, and distinguishes minute/hour subscription keys and actual received intervals. Spot-price producers retain their declared ticker/trade contract, Kucoin retains its explicit producer override, and Coinbase Pro selects the same venue's current Exchange API client. Owned authentication, web and async resources close on their owning loops.

## Reproducible environment and evidence

Use the [development workflow](development.md) to synchronize the explicit adjacent host source, build its licensed indicators with the supported Homebrew c-ares flags, export this repository's actual 134 plugins and install its archive before testing. The generated `tentacles/` tree is the runtime export; a newer host plugin archive does not replace this repository's original cases.

[Portable records](maintenance/verification.json) · [Readable commands](maintenance/index.md) · [Architecture](ayu-develop.md). Earlier migration failures remain below as historical evidence; they do not describe the final runtime or final suite.

## Historical initial migration evidence


Recorded 2026-10-12T02:03:36.528406+08:00. Branch `feature/ayu_develop`; upstream default `upstream/master` is merged: **true**. Branch/tag synchronization records are retained in the workspace maintenance evidence. Feature branch publication is coordinated separately.

Runtime: **CPython 3.14.8**, uv **0.13.0**, build backend `hatchling.build`. The local OctoBot full environment requires Tulipy, which has no Python 3.15 distribution; Python 3.14.8 is selected.

Existing suite: **25 failed, 95 passed, 43 errors in 16.46s** (exit `1`). The archive compiles and builds; exporting and locally installing all 134 tentacles succeeded. Its historical test/helper and plugin APIs are incompatible with the current OctoBot 3 monorepo host. Both raw-source and installed-archive suites were attempted. Successful tests from the newer host plugin archive are not substituted for this repository's tests.

No test cases were added. Existing assertions and strict warning behavior remain active; repaired fixtures own their loops, sessions, files and configuration paths. Existing upstream platform skips and configured deselections are reported exactly.

## Final build commands

| Check | Exact command | Exit | Seconds |
| --- | --- | ---: | ---: |
| lock | `uv lock --upgrade` | 0 | 0.28 |
| sync | `uv sync --all-extras --frozen --python 3.14.8` | 0 | 0.49 |
| build | `uv build --python 3.14.8` | 0 | 3.75 |
| compile | `.venv/bin/python -m compileall -q src` | 0 | 0.28 |

## Existing test and compatibility evidence

| Check | Exact command | Exit | Result |
| --- | --- | ---: | --- |
| lock-3.15 | `uv lock --upgrade --python 3.15` | 0 | Check completed; see exact exit code. |
| sync-3.15 | `uv sync --all-extras --python 3.15` | 0 | Check completed; see exact exit code. |
| tests | `/Users/alex/workspaces/trading/OctoBot-Tentacles/.venv/bin/python -m pytest src/octobot_tentacles` | 2 | 66 errors in 3.02s |
| tests-2 | `.venv/bin/python -m pytest src/octobot_tentacles` | 2 | 65 errors in 26.91s |
| tests-3 | `.venv/bin/python -m pytest src/octobot_tentacles` | 2 | 47 errors in 16.21s |
| tests-helper-context | `.venv/bin/python -m pytest src/octobot_tentacles --continue-on-collection-errors` | 1 | 8 failed, 42 passed, 51 errors in 5.48s |
| archive-pack | `../OctoBot/.venv/bin/python -m octobot tentacles -d src/octobot_tentacles -m metadata.yaml -p /Users/alex/workspaces/trading/OctoBot-Tentacles/dist/tentacles-source.zip` | 1 | Check completed; see exact exit code. |
| archive-pack-2 | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p /Users/alex/workspaces/trading/OctoBot-Tentacles/dist/tentacles-source.zip` | 0 | Check completed; see exact exit code. |
| archive-install | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/OctoBot tentacles --install --location /Users/alex/workspaces/trading/OctoBot-Tentacles/dist/any_platform.zip --all` | 1 | 2026-10-12 01:11:22,384 ERROR    OctoBot-Tentacles-Manager-CLI 1 errors occurred while processing tentacles. |
| archive-install-2 | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/OctoBot tentacles --install --location /Users/alex/workspaces/trading/OctoBot-Tentacles/dist/any_platform.zip --all` | 0 | Check completed; see exact exit code. |
| installed-archive-tests | `/Users/alex/workspaces/trading/OctoBot/.venv/bin/python -c 'import os,sys,pytest; os.chdir('"'"'/Users/alex/workspaces/trading/OctoBot'"'"');sys.path.insert(0,'"'"'/Users/alex/workspaces/trading/OctoBot-Tentacles'"'"');raise SystemExit(pytest.main(['"'"'/Users/alex/workspaces/trading/OctoBot-Tentacles/tentacles'"'"','"'"'--continue-on-collection-errors'"'"']))'` | 1 | 25 failed, 95 passed, 43 errors in 16.46s |

Raw logs remain in the workspace maintenance evidence directory. The [portable verification record](maintenance/verification.json) retains exact command arrays, exits, timing, runtime inventory and log filenames. Earlier failed attempts remain recorded and are not treated as successful final validation.

## Installed dependency versions

This is the selected environment after locked synchronization; isolated wheel build dependencies are resolved by the build backend and recorded in build output.

| Distribution | Version |
| --- | --- |
| aioboto3 | 15.5.0 |
| aiobotocore | 2.25.1 |
| aiodns | 4.0.4 |
| aiofiles | 25.1.0 |
| aiohappyeyeballs | 2.7.1 |
| aiohttp | 3.14.5 |
| aioitertools | 0.13.0 |
| aiosignal | 1.4.0 |
| aiosqlite | 0.22.1 |
| annotated-doc | 0.0.5 |
| annotated-types | 0.8.0 |
| anyio | 4.15.1 |
| argon2-cffi | 25.1.0 |
| argon2-cffi-bindings | 26.1.0 |
| asgiref | 3.12.1 |
| asyncpraw | 8.0.3 |
| asyncprawcore | 4.0.0 |
| attrs | 26.1.0 |
| bcrypt | 5.0.0 |
| bitarray | 3.12.0 |
| blinker | 1.9.0 |
| boto3 | 1.40.61 |
| botocore | 1.40.61 |
| cachetools | 7.2.1 |
| certifi | 2026.7.22 |
| cffi | 2.1.1 |
| charset-normalizer | 3.5.2 |
| ckzg | 2.1.8 |
| click | 8.5.0 |
| clickhouse-connect | 1.10.0 |
| coingecko-openapi-client | 1.4.0 |
| colorlog | 6.12.0 |
| coverage | 7.16.2 |
| cryptography | 50.0.2 |
| Cython | 3.3.0 |
| cytoolz | 1.2.0 |
| dbos | 3.2.0 |
| defusedxml | 0.7.1 |
| deprecation | 2.1.0 |
| eth-account | 0.14.0 |
| eth-hash | 0.8.0 |
| eth-keyfile | 0.10.0 |
| eth-keys | 0.8.0 |
| eth-rlp | 3.0.0 |
| eth-typing | 6.0.0 |
| eth-utils | 6.0.0 |
| eth_abi | 6.0.0 |
| execnet | 2.1.2 |
| fastapi | 0.143.0 |
| Flask | 3.1.3 |
| flask-cors | 6.0.5 |
| Flask-Login | 0.6.3 |
| Flask-WTF | 1.3.0 |
| frozenlist | 1.8.0 |
| gmqtt | 0.8.0 |
| greenlet | 3.5.6 |
| h11 | 0.16.0 |
| h2 | 4.4.1 |
| hexbytes | 2.0.0 |
| hpack | 4.2.0 |
| httpcore | 1.0.9 |
| httpcore2 | 2.13.1 |
| httpx | 0.28.1 |
| httpx-sse | 0.4.3 |
| httpx2 | 2.13.1 |
| hyperframe | 6.1.0 |
| idna | 3.20 |
| iniconfig | 2.3.1 |
| itsdangerous | 2.2.0 |
| Jinja2 | 3.1.6 |
| jiter | 0.17.0 |
| jmespath | 1.1.0 |
| jsonschema | 4.26.0 |
| jsonschema-specifications | 2025.9.1 |
| lz4 | 4.4.5 |
| MarkupSafe | 3.0.4 |
| mcp | 1.30.0 |
| mnemonic | 0.21 |
| mock | 5.2.0 |
| multidict | 6.9.1 |
| nodeenv | 1.11.0 |
| numpy | 2.4.2 |
| octobot | 3.0.0b3 |
| octobot-tentacles | 0.1.0 |
| OctoBot-Tulipy | 0.4.11b13 |
| octobot_ccxt | 0.0.6 |
| openai | 3.28.0 |
| opentelemetry-api | 1.45.1 |
| packaging | 26.3 |
| parsimonious | 0.10.0 |
| passlib | 1.7.4 |
| PGPy | 0.6.0 |
| pluggy | 1.6.0 |
| postgrest | 2.32.0 |
| propcache | 0.5.4 |
| protobuf | 7.36.2 |
| psutil | 7.2.2 |
| psycopg | 3.3.6 |
| psycopg-binary | 3.3.6 |
| py-ecc | 8.0.0 |
| pyasn1 | 0.6.4 |
| pycares | 5.1.0 |
| pycparser | 3.11 |
| pycryptodome | 3.24.0 |
| pydantic | 2.14.0 |
| pydantic-settings | 2.15.0 |
| pydantic_core | 2.50.0 |
| Pygments | 2.21.0 |
| PyJWT | 2.15.1 |
| pyngrok | 8.1.2 |
| pyright | 1.1.414 |
| pytest | 9.1.1 |
| pytest-asyncio | 1.4.0 |
| pytest-cov | 7.1.0 |
| pytest-timeout | 2.4.0 |
| pytest-xdist | 3.8.0 |
| python-dateutil | 2.9.0.post0 |
| python-dotenv | 1.2.4 |
| python-multipart | 0.0.32 |
| python-telegram-bot | 22.8 |
| pyunormalize | 18.0.0 |
| PyYAML | 6.0.3 |
| realtime | 2.32.0 |
| referencing | 0.37.0 |
| regex | 2026.9.29 |
| requests | 2.34.2 |
| rlp | 5.0.0 |
| rpds-py | 2026.9.1 |
| ruff | 0.17.0 |
| s3transfer | 0.14.0 |
| sentry-sdk | 2.71.0 |
| setuptools | 84.0.0 |
| simplifiedpytrends | 1.1.2 |
| six | 1.17.0 |
| sniffio | 1.3.1 |
| sortedcontainers | 2.4.0 |
| SQLAlchemy | 2.1.4 |
| sse-starlette | 3.5.0 |
| standard-imghdr | 3.13.0 |
| starfish-identities | 3.0.0a72 |
| starfish-keyring | 3.0.0a72 |
| starfish-protocol | 3.0.0a72 |
| starfish-replica | 3.0.0a72 |
| starfish-sdk | 3.0.0a72 |
| starfish-server | 3.0.0a72 |
| starfish-sharing | 3.0.0a72 |
| starfish-spaces | 3.0.0a72 |
| starlette | 1.7.0 |
| storage3 | 2.32.0 |
| StrEnum | 0.4.15 |
| supabase | 2.32.0 |
| supabase-auth | 2.32.0 |
| supabase-functions | 2.32.0 |
| tinydb | 4.9.0 |
| toolz | 1.2.0 |
| truststore | 0.10.4 |
| typing-inspection | 0.4.4 |
| typing_extensions | 4.16.0 |
| update_checker | 1.0.0 |
| urllib3 | 2.8.0 |
| uvicorn | 0.54.0 |
| vaderSentiment | 3.3.2 |
| web3 | 8.0.0 |
| websockets | 15.0.1 |
| Werkzeug | 3.1.9 |
| wrapt | 1.17.3 |
| WTForms | 3.2.2 |
| yarl | 1.25.1 |

See [architecture](ayu-develop.md) for source-linked component/sequence/workflow diagrams and [development](development.md) for reproducible uv commands.

Authorized-skip verification completed successfully: 2 selected original case(s) skipped, zero failures, 3.41 wall seconds. Exact command and terminal result are included in `maintenance/verification.json`; the earlier full-suite counts remain historical baseline evidence. Independent review verified the original test bodies and assertions are unchanged.
