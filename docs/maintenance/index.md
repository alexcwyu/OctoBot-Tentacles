# OctoBot-Tentacles: portable verification records

These records retain exact commands, outcomes, original-log hashes and available source snapshots. Failed, interrupted and earlier exploratory commands remain visible. A later focused pass proves only its own scope.

[Machine-readable records](verification.json) · [Validation](../validation.md) · [Engineering guide](../ayu-develop.md)

Original logs remain in the workspace maintenance evidence. Tracked source hashes exclude untracked additions and later edits, as stated in each captured snapshot.

| Check | Exit | Duration | Command |
| --- | ---: | ---: | --- |
| api-collection-check | 0 | 7.85s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--collect-only','--tb=short']))` |
| archive-install-2 | 0 | 5.88s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` |
| archive-install | 1 | 5.34s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` |
| archive-pack-2 | 0 | 4.93s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` |
| archive-pack | 1 | 0.05s | `../OctoBot/.venv/bin/python -m octobot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` |
| bounded-current-api-full-tests | -15 | 901.69s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=60','--tb=short']))` |
| build | 0 | 3.43s | `uv build --python 3.15` |
| compile | 0 | 1.25s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m compileall -q src` |
| converted-mode-focused-tests-2 | 0 | 20.71s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Mode/dca_trading_mode/tests','tentacles/Trading/Mode/index_trading_mode/tests','tentacles/Trading/Mode/grid_trading_mode/tests','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short']))` |
| converted-mode-focused-tests | 1 | 31.69s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Mode/dca_trading_mode/tests','tentacles/Trading/Mode/index_trading_mode/tests','tentacles/Trading/Mode/grid_trading_mode/tests','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short']))` |
| current-api-archive-install | 0 | 6.44s | `../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-archive-pack | 0 | 7.23s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-10 | 0 | 4.63s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-11 | 0 | 22.94s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-2 | 0 | 5.17s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-3 | 0 | 4.94s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-4 | 0 | 5.37s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-5 | 0 | 3.69s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-6 | 0 | 3.4s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-7 | 0 | 5.07s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-8 | 0 | 4.82s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export-9 | 0 | 5.43s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-export | 0 | 5.97s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| current-api-full-tests-2 | -15 | 914.82s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=90','--tb=short']))` |
| current-api-full-tests | -15 | 784.99s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` |
| current-api-install-10 | 0 | 18.07s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-2 | 0 | 3.7s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-3 | 0 | 4.05s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-4 | 0 | 3.56s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-5 | 0 | 3.74s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-6 | 0 | 5.23s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-7 | 0 | 3.56s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-8 | 0 | 4.8s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install-9 | 0 | 4.17s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-api-install | 0 | 5.21s | `env ALLOW_UNSIGNED_TENTACLES=true ../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| current-exchange-lock | 0 | 1.81s | `uv lock --upgrade` |
| current-exchange-sync | 0 | 0.75s | `uv sync --frozen --all-extras --python 3.14.8` |
| current-host-exchange-focused-tests | 1 | 53.8s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Evaluator/Strategies','tentacles/Meta/Keywords/scripting_library/tests/orders/order_types/test_multiple_orders_creation.py','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short','-p','bots_test_observer']))` |
| current-observed-existing-tests-2 | 1 | 297.96s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=120']))` |
| current-observed-existing-tests | -15 | 172.82s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=120']))` |
| current-sync | 0 | 5.27s | `uv sync --all-extras --python 3.14` |
| current-web-focused-tests-2 | 1 | 53.03s | `.venv/bin/python -m pytest tentacles/Services/Interfaces/web_interface/tests tentacles/Trading/Mode/trading_view_signals_trading_mode/tests tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py tentacles/Meta/Keywords/scripting_library/tests --tb=short` |
| current-web-focused-tests-3 | 1 | 52.89s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-4 | 1 | 38.84s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-5 | 1 | 37.67s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','tentacles/Meta/DSL_operators','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-6 | 1 | 68.37s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','tentacles/Meta/DSL_operators','--tb=short','-p','bots_test_observer']))` |
| current-web-focused-tests-7 | 1 | 47.12s | `env BOTS_REPO=tentacles .venv/bin/python -c import sys,pytest;sys.path.insert(0,'/tmp');raise SystemExit(pytest.main(['tentacles/Services/Interfaces/web_interface/tests','tentacles/Trading/Mode/trading_view_signals_trading_mode/tests','tentacles/Trading/Mode/dip_analyser_trading_mode/tests/test_dip_analyser_trading_mode.py','tentacles/Meta/Keywords/scripting_library/tests','tentacles/Meta/DSL_operators','--tb=short','-p','bots_test_observer','-o','faulthandler_timeout=60']))` |
| current-web-focused-tests | 1 | 5.21s | `.venv/bin/python -m pytest tentacles/Services/Interfaces/web_interface/tests --tb=short` |
| final-build-2 | 0 | 3.75s | `uv build --python 3.14.8` |
| final-build | 0 | 8.86s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.28s | `.venv/bin/python -m compileall -q src` |
| final-compile | 0 | 1.35s | `.venv/bin/python -m compileall -q src` |
| final-lock-2 | 0 | 0.28s | `uv lock --upgrade` |
| final-lock | 0 | 0.31s | `uv lock --upgrade` |
| final-selected-python315-compile | 0 | Nones | `.venv/bin/python -Werror -m compileall -q src conftest.py` |
| final-selected-python315-sync | 0 | Nones | `uv sync --all-extras --frozen --python 3.15.0` |
| final-sync-2 | 0 | 0.49s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 0.18s | `uv sync --all-extras --frozen --python 3.14.8` |
| host-archive-install | 0 | 11.06s | `../OctoBot/.venv/bin/OctoBot tentacles --install --location output/dist/any_platform.zip --all` |
| host-archive-pack | 0 | 9.33s | `../OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p dist/current-host.zip` |
| host-complete-deps-lock | 0 | 2.98s | `uv lock --upgrade` |
| host-complete-deps-sync | 0 | 1.42s | `uv sync --all-extras --dev` |
| host-interface-lock | 0 | 2.19s | `uv lock --upgrade` |
| host-interface-sync | 0 | 1.74s | `uv sync --all-extras --frozen --python 3.14` |
| host-port-tests-2 | 1 | 100.85s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` |
| host-port-tests | 1 | 2.99s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');import tests.test_utils.config;os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors','--rootdir=<workspace>/OctoBot-Tentacles']))` |
| installed-archive-tests | 1 | 18.28s | `<workspace>/OctoBot/.venv/bin/python -c import os,sys,pytest; os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors']))` |
| lock-3.15 | 0 | 0.24s | `uv lock --upgrade --python 3.15` |
| final-selected-python315-build | 0 | Nones | `uv build --python 3.15.0` |
| python315-complete-original-suite | 1 | 693.67s | `/tmp/octobot-tentacles-strict-fp-python315-control/bin/python -m pytest tentacles --tb=short` |
| scripting-existing-tests | 1 | 6.24s | `env BOTS_REPO=tentacles .venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'/tmp');sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Meta/Keywords/scripting_library/tests','--rootdir=<workspace>/OctoBot-Tentacles','--tb=short','-p','bots_test_observer']))` |
| sync-3.15 | 0 | 0.61s | `uv sync --all-extras --python 3.15` |
| tests-2 | 2 | 30.72s | `.venv/bin/python -m pytest src/octobot_tentacles` |
| tests-3 | 2 | 20.43s | `.venv/bin/python -m pytest src/octobot_tentacles` |
| tests-helper-context | 1 | 6.93s | `.venv/bin/python -m pytest src/octobot_tentacles --continue-on-collection-errors` |
| tests | 2 | 4.01s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m pytest src/octobot_tentacles` |
| websocket-lifecycle-diagnostic-tests-2 | 1 | 86.86s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short']))` |
| websocket-lifecycle-diagnostic-tests-3 | 0 | 81.81s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short']))` |
| websocket-lifecycle-diagnostic-tests | 1 | 84.11s | `.venv/bin/python -c import os,sys,pytest,faulthandler;faulthandler.dump_traceback_later(45,repeat=True);sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=300','--tb=short','-vv','-s']))` |
| websocket-lifecycle-existing-tests | -15 | 387.18s | `.venv/bin/python -c import os,sys,pytest;sys.path.insert(0,'<workspace>/OctoBot');os.chdir('<workspace>/OctoBot-Tentacles');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['tentacles/Trading/Exchange/binance_websocket_feed/tests','--rootdir=<workspace>/OctoBot-Tentacles','--timeout=90','--tb=short']))` |
