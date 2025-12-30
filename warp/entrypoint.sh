#!/bin/bash
set -e

cd /data

# Инициализация wgcf, если конфигурации нет
if [ ! -f "wgcf-profile.conf" ]; then
    echo "Initializing wgcf..."
    wgcf register
    wgcf generate
fi

# Запуск WireGuard
echo "Starting WireGuard..."
wg-quick up wgcf-profile.conf

# Сохраняем процесс активным
tail -f /dev/null
