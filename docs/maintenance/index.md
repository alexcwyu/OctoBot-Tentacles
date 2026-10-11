# OctoBot-Tentacles: portable verification records

Full raw logs are retained in the workspace maintenance evidence, not distributed here. Hashes identify those original logs. A successful build or selected test subset does not imply a full test-suite pass. Commands containing <workspace> describe the original execution environment.

[Machine-readable records](verification.json) · [Repository validation summary](../validation.md)

## Executed commands

| Check | Exit | Duration | Command | Outcomes |
| --- | ---: | ---: | --- | --- |
| archive-install | 1 | 5.34s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` | See exit status; no test-count assertion. |
| archive-install-2 | 0 | 5.88s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles --install --location <workspace>/OctoBot-Tentacles/dist/any_platform.zip --all` | See exit status; no test-count assertion. |
| archive-pack | 1 | 0.05s | `../OctoBot/.venv/bin/python -m octobot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` | See exit status; no test-count assertion. |
| archive-pack-2 | 0 | 4.93s | `<workspace>/OctoBot/.venv/bin/OctoBot tentacles -d src/octobot_tentacles -m metadata.yaml -p <workspace>/OctoBot-Tentacles/dist/tentacles-source.zip` | See exit status; no test-count assertion. |
| build | 0 | 3.43s | `uv build --python 3.15` | Successfully built dist/octobot_tentacles-0.1.0.tar.gz<br>Successfully built dist/octobot_tentacles-0.1.0-py3-none-any.whl |
| compile | 0 | 1.25s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| current-sync | 0 | 5.27s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| final-build | 0 | 8.86s | `uv build --python 3.14.8` | Successfully built dist/octobot_tentacles-0.1.0.tar.gz<br>Successfully built dist/octobot_tentacles-0.1.0-py3-none-any.whl |
| final-build-2 | 0 | 3.75s | `uv build --python 3.14.8` | Successfully built dist/octobot_tentacles-0.1.0.tar.gz<br>Successfully built dist/octobot_tentacles-0.1.0-py3-none-any.whl |
| final-compile | 0 | 1.35s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-compile-2 | 0 | 0.28s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-lock | 0 | 0.31s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-lock-2 | 0 | 0.28s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-sync | 0 | 0.18s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| final-sync-2 | 0 | 0.49s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| installed-archive-tests | 1 | 18.28s | `<workspace>/OctoBot/.venv/bin/python -c import os,sys,pytest; os.chdir('<workspace>/OctoBot');sys.path.insert(0,'<workspace>/OctoBot-Tentacles');raise SystemExit(pytest.main(['<workspace>/OctoBot-Tentacles/tentacles','--continue-on-collection-errors']))` | 25 failed, 95 passed, 43 errors in 16.46s |
| lock-3.15 | 0 | 0.24s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| sync-3.15 | 0 | 0.61s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| tests | 2 | 4.01s | `<workspace>/OctoBot-Tentacles/.venv/bin/python -m pytest src/octobot_tentacles` | See exit status; no test-count assertion. |
| tests-2 | 2 | 30.72s | `.venv/bin/python -m pytest src/octobot_tentacles` | See exit status; no test-count assertion. |
| tests-3 | 2 | 20.43s | `.venv/bin/python -m pytest src/octobot_tentacles` | See exit status; no test-count assertion. |
| tests-helper-context | 1 | 6.93s | `.venv/bin/python -m pytest src/octobot_tentacles --continue-on-collection-errors` | 8 failed, 42 passed, 51 errors in 5.48s |
