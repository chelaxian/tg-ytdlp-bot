#!/bin/bash

set -euo pipefail

IMAGE_REPO_DEFAULT="brainicism/bgutil-ytdlp-pot-provider"
CONTAINER_NAME_DEFAULT="bgutil-provider"
PORT_DEFAULT="4416"

IMAGE_REPO="${IMAGE_REPO:-$IMAGE_REPO_DEFAULT}"
IMAGE_TAG="${IMAGE_TAG:-latest}"               # можно закрепить версию: IMAGE_TAG=1.3.1
IMAGE="${IMAGE_REPO}:${IMAGE_TAG}"
CONTAINER_NAME="${CONTAINER_NAME:-$CONTAINER_NAME_DEFAULT}"
PORT="${PORT:-$PORT_DEFAULT}"
HEALTHCHECK_TIMEOUT_SECONDS="${HEALTHCHECK_TIMEOUT_SECONDS:-10}"
# Повторы: Node может начать слушать порт чуть позже, чем docker run вернётся
HEALTHCHECK_RETRIES="${HEALTHCHECK_RETRIES:-15}"
HEALTHCHECK_RETRY_DELAY_SECONDS="${HEALTHCHECK_RETRY_DELAY_SECONDS:-1}"

# Опциональная синхронизация Python-плагина в venv бота, чтобы версии plugin/server не расходились
SYNC_PY_PLUGIN="${SYNC_PY_PLUGIN:-1}"          # 1=включено, 0=выключено
BOT_DIR_DEFAULT="/root/Telegram/tg-ytdlp-bot"
BOT_DIR="${BOT_DIR:-$BOT_DIR_DEFAULT}"
BOT_VENV_PIP="${BOT_VENV_PIP:-${BOT_DIR}/venv/bin/pip}"
BOT_VENV_PYTHON="${BOT_VENV_PYTHON:-${BOT_DIR}/venv/bin/python3}"
BOT_SYSTEMD_SERVICE="${BOT_SYSTEMD_SERVICE:-tg-ytdlp-bot}"

# Папка, где выполняется скрипт
#cd /mnt/c/Users/chelaxian/Desktop/tg-ytdlp-NEW || exit 1 

log() { echo "[$(date '+%F %T')] $*"; }
fail() { echo "[$(date '+%F %T')] ERROR: $*" >&2; exit 1; }

command -v docker >/dev/null 2>&1 || fail "docker не найден в PATH"

if ! docker info >/dev/null 2>&1; then
  fail "docker daemon недоступен (нет прав / сервис не запущен?)"
fi

# Проверяем, что порт не занят чужим контейнером
other_port_user="$(docker ps --format '{{.Names}} {{.Ports}}' | awk -v p=":${PORT}->" '$0 ~ p {print $1}' | grep -v "^${CONTAINER_NAME}$" || true)"
if [[ -n "${other_port_user}" ]]; then
  fail "Порт ${PORT} уже проброшен контейнером '${other_port_user}'. Остановите его или смените PORT/CONTAINER_NAME."
fi

log "Stopping old container (if exists): ${CONTAINER_NAME}"
if docker ps -a --format '{{.Names}}' | grep -qx "${CONTAINER_NAME}"; then
  # Останавливаем только если запущен
  if docker ps --format '{{.Names}}' | grep -qx "${CONTAINER_NAME}"; then
    docker stop "${CONTAINER_NAME}" >/dev/null
  fi
  docker rm "${CONTAINER_NAME}" >/dev/null
else
  log "No existing container named ${CONTAINER_NAME}"
fi

log "Pulling image: ${IMAGE}"
docker pull "${IMAGE}"

log "Starting new container: ${CONTAINER_NAME} on port ${PORT}"
docker run -d \
  --name "${CONTAINER_NAME}" \
  -p "${PORT}:4416" \
  --init \
  --restart unless-stopped \
  "${IMAGE}" >/dev/null

# Health-check (корень может отвечать 404 — это нормально, главное что TCP/HTTP живой)
log "Health-check: http://127.0.0.1:${PORT}/ (до ${HEALTHCHECK_RETRIES} попыток, timeout ${HEALTHCHECK_TIMEOUT_SECONDS}s)"
if command -v curl >/dev/null 2>&1; then
  http_code=""
  for ((i = 1; i <= HEALTHCHECK_RETRIES; i++)); do
    http_code="$(curl -sS -m "${HEALTHCHECK_TIMEOUT_SECONDS}" -o /dev/null -w '%{http_code}' "http://127.0.0.1:${PORT}/" 2>/dev/null || true)"
    if [[ "${http_code}" == "200" || "${http_code}" == "404" ]]; then
      break
    fi
    if [[ "${i}" -lt "${HEALTHCHECK_RETRIES}" ]]; then
      sleep "${HEALTHCHECK_RETRY_DELAY_SECONDS}"
    fi
  done
  if [[ "${http_code}" != "200" && "${http_code}" != "404" ]]; then
    log "Health-check failed (http ${http_code}). Последние логи контейнера:"
    docker logs --tail 50 "${CONTAINER_NAME}" || true
    fail "bgutil-provider не прошёл health-check"
  fi
  log "Health-check OK (http ${http_code})"
else
  log "curl не найден — пропускаю HTTP health-check"
fi

log "Done."

# Синхронизация python-плагина с сервером в Docker (рекомендуется при IMAGE_TAG=latest)
if [[ "${SYNC_PY_PLUGIN}" == "1" ]]; then
  if [[ -x "${BOT_VENV_PIP}" ]]; then
    log "Syncing Python plugin in venv: bgutil-ytdlp-pot-provider (pip -U)"
    "${BOT_VENV_PIP}" install -U bgutil-ytdlp-pot-provider >/dev/null
    plugin_ver="$("${BOT_VENV_PYTHON}" -c 'import importlib.metadata as m; print(m.version("bgutil-ytdlp-pot-provider"))' 2>/dev/null || true)"
    if [[ -n "${plugin_ver}" ]]; then
      log "Python plugin version: ${plugin_ver}"
    fi

    # Перезапуск бота, если он управляется systemd
    if command -v systemctl >/dev/null 2>&1; then
      if systemctl list-unit-files --type=service --no-pager 2>/dev/null | awk '{print $1}' | grep -qx "${BOT_SYSTEMD_SERVICE}.service"; then
        log "Restarting systemd service: ${BOT_SYSTEMD_SERVICE}"
        systemctl restart "${BOT_SYSTEMD_SERVICE}"
        # короткая проверка статуса
        if systemctl is-active --quiet "${BOT_SYSTEMD_SERVICE}"; then
          log "Service is active: ${BOT_SYSTEMD_SERVICE}"
        else
          log "Service is NOT active after restart: ${BOT_SYSTEMD_SERVICE}"
          systemctl status --no-pager -l "${BOT_SYSTEMD_SERVICE}" || true
          fail "bot service restart failed"
        fi
      else
        log "systemd service '${BOT_SYSTEMD_SERVICE}.service' not found; skipping restart"
      fi
    else
      log "systemctl not found; skipping bot restart"
    fi
  else
    log "Venv pip not found at ${BOT_VENV_PIP}; skipping Python plugin sync (set BOT_DIR/BOT_VENV_PIP or SYNC_PY_PLUGIN=0)"
  fi
else
  log "SYNC_PY_PLUGIN=0; skipping Python plugin sync"
fi
