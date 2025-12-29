#!/bin/bash
set -e

# Переходим в рабочую директорию приложения
cd /app || exit 1

# Функция для обработки сигналов завершения
cleanup() {
    echo "Получен сигнал завершения, останавливаем бота..."
    kill $BOT_PID 2>/dev/null || true
    wait $BOT_PID 2>/dev/null || true
    exit 0
}

# Устанавливаем обработчики сигналов
trap cleanup SIGTERM SIGINT

# Запускаем бота
echo "Запуск Telegram бота из директории: $(pwd)"
python magic.py &
BOT_PID=$!

echo "Бот запущен (PID: $BOT_PID)"

# Ждем завершения процесса
wait $BOT_PID
