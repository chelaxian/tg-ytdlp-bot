#!/bin/bash

# Простое обновление без venv: используем системный python/pip внутри контейнера
# yt-dlp
python -m pip install --upgrade --pre "yt-dlp[default,curl-cffi]"

# gallery-dl 
python -m pip install -U --no-cache-dir --force-reinstall \
  "git+https://github.com/mikf/gallery-dl.git@master"

# pyrogtgfork и TgCrypto 
python -m pip install --upgrade pyrotgfork
python -m pip install --upgrade TgCrypto