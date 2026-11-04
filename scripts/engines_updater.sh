#!/bin/bash

set -e
# Скрипт лежит в <repo>/scripts/, venv — в <repo>/venv/.
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
VENV_PY="$(dirname "$SCRIPT_DIR")/venv/bin/python"

# One run at a time: cron, admin_phone_bot and manual runs must not run pip on
# the same venv concurrently (a second run waits up to 30 min, then gives up).
exec 9>"/tmp/tg-ytdlp-engines-updater.lock"
if ! flock -w 1800 9; then
  echo "Another engines_updater.sh is still running, skipping." >&2
  exit 1
fi

# Определяем корректный интерпретатор Python.
# 1) Если передан PYTHON_BIN — используем его.
# 2) Иначе venv репозитория (основной сценарий cron/systemd).
# 3) Иначе python/python3 из PATH.

if [[ -n "${PYTHON_BIN}" ]]; then
  PY="${PYTHON_BIN}"
elif [[ -x "$VENV_PY" ]]; then
  PY="$VENV_PY"
elif command -v python >/dev/null 2>&1; then
  PY="python"
elif command -v python3 >/dev/null 2>&1; then
  PY="python3"
else
  echo "Error: neither 'python' nor 'python3' found in PATH." >&2
  exit 1
fi

echo "Using Python interpreter: ${PY}"

# yt-dlp
"${PY}" -m pip install --upgrade --pre "yt-dlp[default,curl-cffi]"

# curl_cffi - обновляем отдельно для поддержки новых версий impersonate
"${PY}" -m pip install --upgrade curl_cffi

# gallery-dl (from git: reinstall the package itself only, not requests & co.)
"${PY}" -m pip install -U --no-cache-dir --force-reinstall --no-deps \
  "git+https://github.com/mikf/gallery-dl.git@master"
"${PY}" -m pip install -U "requests>=2.11"

# pyrotgfork и TgCrypto
"${PY}" -m pip install --upgrade pyrotgfork
"${PY}" -m pip install --upgrade TgCrypto