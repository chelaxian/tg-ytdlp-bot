#!/bin/bash

set -e

# Определяем корректный интерпретатор Python.
# 1) Если передан PYTHON_BIN — используем его.
# 2) Иначе пробуем python из PATH (например, из venv).
# 3) Если его нет, пробуем python3.

if [[ -n "${PYTHON_BIN}" ]]; then
  PY="${PYTHON_BIN}"
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

# gallery-dl
"${PY}" -m pip install -U --no-cache-dir --force-reinstall \
  "git+https://github.com/mikf/gallery-dl.git@master"

# pyrotgfork и TgCrypto
"${PY}" -m pip install --upgrade pyrotgfork
"${PY}" -m pip install --upgrade TgCrypto
