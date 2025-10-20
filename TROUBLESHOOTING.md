# 🔧 Bot Hanging Issues - Diagnosis and Fix

## Проблема
Телеграм бот зависает через ~15 минут после перезапуска, хотя сервис не падает. Причина - утечка потоков анимации и незакрытые HTTP-соединения.

## ✅ Исправления

### 1. Жесткие лимиты времени для анимаций
- **Файл**: `CONFIG/limits.py`
- **Добавлено**: `MAX_ANIMATION_DURATION = 14400` (4 часа)
- **Эффект**: Анимации принудительно останавливаются через 4 часа

### 2. Управление HTTP-соединениями
- **Файл**: `HELPERS/http_manager.py` (новый)
- **Функция**: Автоматическое закрытие соединений через 4 часа
- **Эффект**: Предотвращает CLOSE-WAIT состояния

### 3. Обновленные анимации
- **Файл**: `HELPERS/download_status.py`
- **Изменения**: Добавлены жесткие лимиты времени в `animate_hourglass()` и `cycle_progress()`
- **Эффект**: Потоки анимации не могут работать бесконечно

### 4. Системные настройки
- **Файл**: `_etc/systemd/system/tg-ytdlp-bot.service`
- **Добавлено**: `LimitNOFILE=65535`, `LimitNPROC=4096`
- **Эффект**: Увеличены лимиты ресурсов

## 🛠️ Установка исправлений

### 1. Применить TCP keepalive настройки
```bash
sudo ./scripts/configure_tcp_keepalive.sh
```

### 2. Перезапустить бота
```bash
sudo systemctl restart tg-ytdlp-bot
```

### 3. Мониторинг ресурсов
```bash
# Запустить мониторинг
./scripts/monitor_bot_resources.sh monitor

# Или проверить один раз
./scripts/monitor_bot_resources.sh check
```

## 🔍 Диагностика проблем

### Проверка потоков анимации
```bash
# Найти PID бота
pid=$(pgrep -f "python.*magic.py")

# Проверить потоки анимации
py-spy dump -p $pid | grep -c "animate_hourglass"
```

### Проверка HTTP-соединений
```bash
# Проверить CLOSE-WAIT соединения
ss -tuln | grep CLOSE-WAIT

# Проверить все сетевые соединения бота
lsof -p $pid -nP | grep -E 'TCP|UDP'
```

### Проверка файловых дескрипторов
```bash
# Количество открытых файлов
ls -1 /proc/$pid/fd | wc -l

# Детальная информация
lsof -p $pid | head -20
```

## 📊 Мониторинг

### Автоматический мониторинг
```bash
# Запустить в фоне
nohup ./scripts/monitor_bot_resources.sh monitor > /dev/null 2>&1 &

# Проверить логи
tail -f /var/log/bot-monitor.log
```

### Ручная проверка
```bash
# Быстрая проверка
./scripts/monitor_bot_resources.sh check

# Детальный отчет
./scripts/monitor_bot_resources.sh report
cat /tmp/bot-report.txt
```

## 🚨 Признаки проблем

### Критические
- Процесс в состоянии `D` (uninterruptible sleep)
- Более 5 потоков `animate_hourglass`
- Более 100 CLOSE-WAIT соединений
- Более 1000 открытых файловых дескрипторов

### Предупреждающие
- CPU использование > 90%
- Более 50 потоков
- Более 50 открытых сетевых соединений

## 🔄 Процедура восстановления

### При зависании бота
1. **Проверить состояние**:
   ```bash
   ./scripts/monitor_bot_resources.sh check
   ```

2. **Сгенерировать отчет**:
   ```bash
   ./scripts/monitor_bot_resources.sh report
   ```

3. **Перезапустить бота**:
   ```bash
   sudo systemctl restart tg-ytdlp-bot
   ```

4. **Проверить логи**:
   ```bash
   journalctl -u tg-ytdlp-bot -f
   ```

## 📈 Ожидаемые результаты

После применения исправлений:
- ✅ Анимации останавливаются через максимум 4 часа
- ✅ HTTP-соединения закрываются автоматически
- ✅ Нет накопления CLOSE-WAIT соединений
- ✅ Стабильная работа без зависаний
- ✅ Автоматическая очистка ресурсов при завершении

## 🔧 Дополнительные настройки

### Увеличение лимитов системы
```bash
# Добавить в /etc/security/limits.conf
* soft nofile 65535
* hard nofile 65535
* soft nproc 4096
* hard nproc 4096
```

### Мониторинг через cron
```bash
# Добавить в crontab
*/5 * * * * /path/to/scripts/monitor_bot_resources.sh check
```

## 📞 Поддержка

При возникновении проблем:
1. Запустите диагностику: `./scripts/monitor_bot_resources.sh report`
2. Проверьте логи: `journalctl -u tg-ytdlp-bot -n 100`
3. Перезапустите сервис: `sudo systemctl restart tg-ytdlp-bot`
