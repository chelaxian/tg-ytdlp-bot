# 🤖 tg-ytdlp-bot

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![PyroTGFork](https://img.shields.io/badge/PyroTGFork-Latest-green.svg)](https://github.com/pyrogram/pyrogram)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-Latest-red.svg)](https://github.com/yt-dlp/yt-dlp)
[![gallery-dl](https://img.shields.io/badge/gallery--dl-Latest-orange.svg)](https://github.com/mikf/gallery-dl)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://t.me/tgytdlp)

[🇺🇸 ENGLISH README](https://github.com/chelaxian/tg-ytdlp-bot/blob/main/README.md)

> 🎥 **Продвинутый Telegram-бот для скачивания видео, аудио и фото с более чем 1500 сайтов.**

Мощный Telegram-бот, который загружает видео, аудио и изображения с YouTube, TikTok, Instagram и более чем 1500 других платформ, используя yt-dlp и gallery-dl. Отличается расширенным выбором форматов, поддержкой кодеков, интеллектуальной обработкой субтитров, поддержкой прокси и прямыми ссылками на потоковое воспроизведение. \
<img width="320" height="938" alt="tgytdlp1" src="https://github.com/user-attachments/assets/7a8398da-0968-454d-8a60-f81cbfe13e2f" /><img width="323" height="938" alt="tgytdlp2" src="https://github.com/user-attachments/assets/4e1a9e46-0a37-4bfe-a440-70688929c2b3" />

---

## 📋 Оглавление

### 👥 Базовая часть (для обычных пользователей)
- [Быстрый старт](#-быстрый-старт)
- [Основные команды](#-основные-команды)
- [Языковой интерфейс](#-языковой-интерфейс)
- [Решение проблем](#-решение-проблем)

### 👨‍💼 Расширенная часть (для админов и продвинутых пользователей)
- [Установка](#-установка)
- [Конфигурация](#-конфигурация)
- [Лимиты и кулдауны](#-лимиты-и-кулдауны-configlimitspy)
- [Все команды пользователя](#-все-команды-пользователя)
- [Расширенные функции](#-расширенные-функции)
- [Команды администратора](#-команды-администратора)
- [Управление контентом](#-управление-контентом)
- [Обновление бота](#-обновление-бота)
- [Панель статистики](#-панель-статистики-порт-5555)
- [Разработка](#-разработка)
- [Лицензия и поддержкa](#-лицензия-и-поддержка)

---

# 👥 БАЗОВАЯ ЧАСТЬ

---

## 🚀 Быстрый старт

### Попробуйте бота прямо сейчас

**Демо боты:**
- 🇮🇹 [@tgytdlp_it_bot](https://t.me/tgytdlp_it_bot) - Основной IT бот
- 🇦🇪 [@tgytdlp_uae_bot](https://t.me/tgytdlp_uae_bot) - Сервер в ОАЭ
- 🇬🇧 [@tgytdlp_uk_bot](https://t.me/tgytdlp_uk_bot) - Сервер в Великобритании
- 🇫🇷 [@tgytdlp_fr_bot](https://t.me/tgytdlp_fr_bot) - Сервер во Франции

**Канал сообщества:** [@tg_ytdlp](https://t.me/tg_ytdlp)

**Зеркало:** [@tgytdlp](https://t.me/tgytdlp)

### Как использовать

1. **Отправьте ссылку на видео** боту
2. **Выберите качество** из интерактивного меню
3. **Скачайте** видео с вашими настройками

**Примеры:**

Одна ссылка:
```
https://youtube.com/watch?v=dQw4w9WgXcQ
```

Несколько ссылок (когда выбран формат качества):
```
https://youtube.com/watch?v=video1
https://youtube.com/watch?v=video2
https://youtube.com/watch?v=video3
```

**Поддерживаемые платформы:** YouTube, TikTok, Instagram, Twitter/X, Facebook, VK, Vimeo, и 1500+ других платформ.

---

## 📌 Основные команды

### Базовые команды

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/start` | Запустить бота | `/start` |
| `/help` | Показать справку | `/help` |
| `/settings` | Открыть настройки | `/settings` |
| `/usage` | Статистика использования | `/usage` |
| `/tags` | Все ваши теги | `/tags` |
| `/lang` | Изменить язык | `/lang ru` |

### Команды загрузки

| Команда | Описание | Пример |
|----------|-------------|---------|
| **Ссылка на видео** | Скачать видео (авто) | `https://youtube.com/watch?v=...` |
| `/vid` | Скачать видео | `/vid https://youtube.com/watch?v=...` |
| `/audio` | Скачать аудио | `/audio https://youtube.com/watch?v=...` |
| `/link` | Прямые ссылки на видео | `/link 720 https://youtube.com/watch?v=...` |
| `/img` | Скачать изображения | `/img https://instagram.com/p/...` |

### Быстрая настройка

```bash
# Выбор качества
/format 720    # 720p или ниже
/format 4k     # 4K или ниже
/format ask    # Всегда спрашивать качество

# Язык
/lang ru        # Русский
/lang en        # Английский
/lang ar        # Арабский

# Субтитры
/subs ru        # Русские субтитры
/subs en auto   # Английские с автопереводом
/subs off       # Отключить субтитры

# Настройки клавиатуры
/keyboard off     # Скрыть
/keyboard full    # Полная эмодзи клавиатура

# Прокси
/proxy on        # Включить прокси
/proxy off       # Выключить прокси
```

---

## 🌍 Языковой интерфейс

Поддерживается 25 языков с полным переводом интерфейса:

### Поддерживаемые языки

| Язык | Код | Название | Флаг |
|--------|------|-----------|------|
| 🇺🇸 Английский | `en` | English | 🇺🇸 |
| 🇷🇺 Русский | `ru` | Русский | 🇷🇺 |
| 🇸🇦 Арабский | `ar` | العربية | 🇸🇦 |
| 🇮🇳 Хинди | `in` | हिन्दी | 🇮🇳 |
| 🇨🇳 Китайский | `zh` | 中文 | 🇨🇳 |
| 🇪🇸 Испанский | `es` | Español | 🇪🇸 |
| 🇫🇷 Французский | `fr` | Français | 🇫🇷 |
| 🇧🇩 Бенгальский | `bn` | বাংলা | 🇧🇩 |
| 🇵🇹 Португальский | `pt` | Português | 🇵🇹 |
| 🇵🇰 Урду | `ur` | اردو | 🇵🇰 |
| 🇮🇩 Индонезийский | `id` | Bahasa Indonesia | 🇮🇩 |
| 🇯🇵 Японский | `ja` | 日本語 | 🇯🇵 |
| 🇵🇭 Филиппинский | `tl` | Filipino | 🇵🇭 |
| 🇳🇬 Хауса | `ha` | Hausa | 🇳🇬 |
| 🇻🇳 Вьетнамский | `vi` | Tiếng Việt | 🇻🇳 |
| 🇮🇹 Итальянский | `it` | Italiano | 🇮🇹 |
| 🇩🇪 Немецкий | `de` | Deutsch | 🇩🇪 |
| 🇹🇷 Турецкий | `tr` | Türkçe | 🇹🇷 |
| 🇰🇷 Корейский | `ko` | 한국어 | 🇰🇷 |
| 🇵🇱 Польский | `pl` | Polski | 🇵🇱 |
| 🇺🇦 Украинский | `uk` | Українська | 🇺🇦 |
| 🇮🇷 Персидский | `fa` | فارسی | 🇮🇷 |
| 🇹🇭 Тайский | `th` | ไทย | 🇹🇭 |
| 🇺🇿 Узбекский | `uz` | Oʻzbek | 🇺🇿 |
| 🇰🇿 Казахский | `kk` | Қазақ | 🇰🇿 |

**Быстрое переключение языка:**
```bash
/lang en  # 🇺🇸 English
/lang ru  # 🇷🇺 Русский
/lang ar  # 🇸🇦 العربية
/lang zh  # 🇨🇳 中文
# ... и другие 25 языков
```

---

## 🔧 Решение проблем

### Бот не запускается

**Причины:**
- Неверная конфигурация в `config.py`
- Неверные API ключи
- Нет прав администратора в каналах

**Решения:**
1. Проверьте все обязательные поля в конфигурации
2. Убедитесь что бот имеет права администратора во всех каналах
3. Проверьте версию Python (требуется 3.10+)

### Видео с YouTube не скачиваются

**Причины:**
- Устаревшие cookies
- Ограничение по возрасту
- IP-блокировка

**Решения:**
1. Отправьте `/check_cookie` для проверки YouTube cookies
2. Используйте `/cookie youtube` для получения свежих cookies
3. Проверьте доступность видео

### Ошибки подключения к Firebase

**Причины:**
- Неверные учетные данные Firebase
- Неверные правила доступа к базе данных

**Решения:**
1. Проверьте проект Firebase и учетные данные
2. Убедитесь что правила Realtime Database разрешают чтение/запись
3. Проверьте подключение к сети

### Не переключается язык

**Решения:**
1. Проверьте наличие языкового файла в `CONFIG/LANGUAGES/`
2. Используйте `/lang` для сброса языка
3. Перезапустите бота если файлы были обновлены

---

# 👨‍💼 РАСШИРЕННАЯ ЧАСТЬ

---

## 🛠️ Установка

### 🚢 Docker (рекомендуется)

Это самый простой способ запуска бота: всё (бот + PO token provider + webserver для cookies) работает в Docker контейнерах.

**Требования:**
- **Docker** и **Docker Compose**
- Сервер или VPS с Linux (Ubuntu/Debian рекомендуем)

**Шаг 1 – Создать конфигурацию:**

```bash
git clone https://github.com/chelaxian/tg-ytdlp-bot.git
cd tg-ytdlp-bot
cp CONFIG/_config.py CONFIG/config.py
```

Отредактируйте `CONFIG/config.py` и заполните минимум:
- **BOT_NAME** – внутреннее имя бота
- **BOT_NAME_FOR_USERS** – имя в базе данных
- **ADMIN** – ваш Telegram user ID
- **ADMIN_USERNAME** – ваш username (например `"@"` или `"@username"`)
- **ADMIN_GROUP** – ID групп админов (опционально)
- **ALLOWED_GROUP** – ID разрешенных групп (опционально)
- **API_ID**, **API_HASH** – из [my.telegram.org](https://my.telegram.org)
- **BOT_TOKEN** – из [@BotFather](https://t.me/BotFather)
- **LOGS_*** – все лог-каналы
- **SUBSCRIBE_CHANNEL** и **SUBSCRIBE_CHANNEL_URL** – канал подписки

**Пример конфигурации:**

```python
#####################################################################
# ЗАПОЛНИТЕ ТОЛЬКО ЭТУ ЧАСТЬ !!!
#####################################################################

# Bot Configuration
BOT_NAME = "your_bot_name"                   # Имя бота
BOT_NAME_FOR_USERS = "tg-ytdlp-bot"          # Имя в базе данных
ADMIN = [123456789]                          # Список ID админов
ADMIN_USERNAME = "@"                         # Admin username
ADMIN_GROUP = [-1001234567890]               # ID групп админов
ALLOWED_GROUP = [-1001234567890]             # ID разрешенных групп
API_ID = 12345678                            # Ваш Telegram API ID
API_HASH = "your_api_hash_here"              # Ваш Telegram API Hash
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # Токен бота

# Channel Configuration (Multiple Log Channels)
LOGS_ID = -1001234567890                     # Основной лог-канал
LOGS_VIDEO_ID = -1001234567890               # Логи видео
LOGS_NSFW_ID = -1001234567890                # Логи NSFW
LOGS_IMG_ID = -1001234567890                 # Логи изображений
LOGS_PAID_ID = -1001234567890                # Логи платного контента
LOG_EXCEPTION = -1001234567890               # Логи ошибок
SUBSCRIBE_CHANNEL = -1000987654321           # Канал подписки
SUBSCRIBE_CHANNEL_URL = "https://t.me/your_channel"  # Ссылка на канал

#####################################################################
# ОСТАЛЬНОЕ ОСТАВЬТЕ БЕ ИЗМЕНЕНИЙ !!!
#####################################################################
```

**Шаг 2 – Файл окружения (.env):**

```bash
cp .env.example .env
```

Можно изменить:
- `COMPOSE_PROJECT_NAME` – префикс проекта для Docker
- `TZ` – ваш часовой пояс (например, `Europe/Moscow`)

**Шаг 3 – Запуск контейнеров:**

```bash
docker compose build warp
docker compose up -d --build
```

Контейнер бота будет собран из `Dockerfile`, и:
- `configuration-webserver` будет обслуживать cookie файлы по `http://configuration-webserver/cookies/<filename>`
- `bgutil-provider` будет доступен по `http://bgutil-provider:4416` для YouTube PO токенов
- **Dashboard панель** будет доступна по `http://localhost:5555` (или `http://<ваш-ip>:5555`)

**Шаг 4 – Доступ к Dashboard Panel:**

После запуска контейнеров веб-панель запустится на порту **5555** (настраивается через `DASHBOARD_PORT` в `CONFIG/config.py`):
- `http://localhost:5555` (если с той же машины)
- `http://<ваш-ip>:5555` (если удалённо)

**Учетные данные по умолчанию:**
- **Username:** `admin` (в `CONFIG/config.py` как `DASHBOARD_USERNAME`)
- **Password:** `admin123` (в `CONFIG/config.py` как `DASHBOARD_PASSWORD`)

**⚠️ Важно:** Смените пароль по умолчанию после первого входа!

P.S. не забудьте добавить бота в каналы с правами администратора
---

### Ручная установка (без Docker)

#### Предварительные требования

- **Python 3.10+**
- **Ubuntu/Debian** (рекомендуется) или другой Linux
- **Chromium** (опционально, для команды `/cookies_from_browser`)
- **Docker** (опционально, для PO Token Provider)
- **Telegram Bot Token** из [@BotFather](https://t.me/BotFather)
- **Telegram API Credentials** из [my.telegram.org](https://my.telegram.org)

#### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/chelaxian/tg-ytdlp-bot.git
cd tg-ytdlp-bot
chmod +x *.sh
```

#### Шаг 2: Установка зависимостей

```bash
# Обновление системных пакетов
sudo apt update
sudo apt install -y git python3.10 python3-pip python3.10-venv mediainfo rsync

# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate

# Установка Python пакетов
pip install --no-cache-dir -r requirements.txt
```

#### Шаг 3: Установка FFmpeg

```bash
# Установка FFmpeg (требуется для обработки видео)
sudo apt-get install -y ffmpeg

# Проверка установки
ffmpeg -version
```

#### Шаг 3.5: Установка Node.js и PhantomJS (рекомендуется)

Node.js необходим yt-dlp для выполнения JavaScript (YouTube и другие сайты).
PhantomJS необходим для некоторых сайтов, таких как PornHub.

```bash
# Установка Node.js (JS runtime для yt-dlp, нужен для YouTube)
sudo apt-get install -y nodejs

# Проверка Node.js
node --version  # Должно быть v18+ или v20+

```

> **Примечание:** Node.js уже включён в Docker-образ. Ручная установка нужна только для установки без Docker.
>
> ~~PhantomJS~~: больше не требуется. Ранее использовался для PornHub и подобных сайтов, но yt-dlp теперь использует другие методы извлечения.

#### Шаг 4: Настройка конфигурации

```bash
# Переход в директорию конфигурации
cd CONFIG

# Копирование шаблона конфигурации
cp _config.py config.py

# Редактирование конфигурации
nano config.py
```

#### Шаг 5: Запуск бота

```bash
# Активация виртуального окружения
source venv/bin/activate

# Запуск бота
python3 magic.py
```

---

## ⚙️ Конфигурация

### Обязательная конфигурация

Редактируйте `CONFIG/config.py` с вашими настройками:

```python
# Bot Configuration
BOT_NAME = "your_bot_name"                    # Имя бота
BOT_NAME_FOR_USERS = "tg-ytdlp-bot"          # Имя в базе данных
ADMIN = [123456789, 987654321]               # Список ID админов
ADMIN_USERNAME = "@"                          # Admin username
ADMIN_GROUP = [-1001234567890, -1001234567891]  # ID групп админов
ALLOWED_GROUP = [-1001234567890, -1001234567891]  # ID разрешенных групп
API_ID = 12345678                            # Ваш Telegram API ID
API_HASH = "your_api_hash_here"              # Ваш Telegram API Hash
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # Токен бота

# Channel Configuration (Multiple Log Channels)
LOGS_ID = -1001234567890                     # Основной лог-канал
LOGS_VIDEO_ID = -1001234567891               # Логи видео
LOGS_NSFW_ID = -1001234567892                # Логи NSFW
LOGS_IMG_ID = -1001234567893                 # Логи изображений
LOGS_PAID_ID = -1001234567894                # Логи платного контента
LOG_EXCEPTION = -1001234567895               # Логи ошибок
SUBSCRIBE_CHANNEL = -1001234567890           # Канал подписки
SUBSCRIBE_CHANNEL_URL = "https://t.me/your_channel"  # Ссылка на канал

# Cookie Configuration
COOKIE_URL = "https://your-domain.com/cookies/cookie.txt"  # Fallback cookie URL

# YouTube Cookie URLs (Multiple Sources)
YOUTUBE_COOKIE_URL = "https://your-domain.com/cookies/youtube/cookie1.txt"
YOUTUBE_COOKIE_URL_1 = "https://your-domain.com/cookies/youtube/cookie2.txt"
YOUTUBE_COOKIE_URL_2 = "https://your-domain.com/cookies/youtube/cookie3.txt"
# ... до YOUTUBE_COOKIE_URL_9

# Firebase Configuration
USE_FIREBASE = True

FIREBASE_USER = "your-email@gmail.com"
FIREBASE_PASSWORD = "your-firebase-password"
FIREBASE_CONF = {
    "apiKey": "your-api-key",
    "authDomain": "your-project.firebaseapp.com",
    "projectId": "your-project-id",
    "storageBucket": "your-project.appspot.com",
    "messagingSenderId": "123456789",
    "appId": "1:123456789:web:abcdef123456",
    "databaseURL": "https://your-project-default-rtdb.firebaseio.com"
}
```

### Получение API учетных данных

#### 1. Bot Token
1. Напишите [@BotFather](https://t.me/BotFather)
2. Создайте нового бота через `/newbot`
3. Скопируйте токен бота

#### 2. API ID & Hash
1. Посетите [my.telegram.org](https://my.telegram.org)
2. Войдите с номером телефона
3. Перейдите в "API development tools"
4. Создайте новое приложение
5. Скопируйте API ID и API Hash

#### 3. Channel IDs
1. Создайте каналы и добавьте бота как админа
2. Получите ID каналов используя [@userinfobot](https://t.me/userinfobot)
3. ID каналов начинаются с `-100`

#### 4. User ID
1. Напишите [@UserInfoToBot](https://t.me/UserInfoToBot)
2. Скопируйте ваш user ID
3. Добавьте в список `ADMIN` в config.py

#### 5. Group IDs (для ADMIN_GROUP и ALLOWED_GROUP)
1. Добавьте бота в группу как админа
2. Получите ID групп используя [@UserInfoToBot](https://t.me/UserInfoToBot) (перешлите сообщение из группы боту)
3. ID групп начинаются с `-100` (супергруппы) или отрицательные числа (обычные группы)
4. Добавьте ID групп в `ADMIN_GROUP` (группы без лимитов) или `ALLOWED_GROUP` (группы с увеличенными лимитами) в config.py

### Настройка Firebase

Подробные инструкции по настройке Firebase см. в разделе [Firebase Setup for Telegram Bot](#firebase-setup-for-telegram-bot) ниже.

**Быстрая настройка:**
1. Перейдите в [Firebase Console](https://console.firebase.google.com/)
2. Создайте новый проект
3. Включите Realtime Database и Authentication
4. Создайте пользователя с email/password
5. Получите конфигурацию из Project Settings
6. Обновите `FIREBASE_CONF` в config.py

---

### (Опционально) Установка дополнительных шрифтов

<details>
   <summary>Арабские и азиатские шрифты</summary>
   
   Если вам нужна поддержка дополнительных языков таких как арабский, китайский, японский, корейский - установите языковые пакеты:
   ```sh
   sudo apt update
   sudo add-apt-repository universe
   sudo apt update

   sudo apt install fonts-noto-core             # – Noto Sans, Noto Serif, … base fonts Google Noto
   sudo apt install fonts-noto-extra            # – extra fonts (включая арабский)
   sudo apt install fonts-kacst fonts-kacst-one # – KACST arabic fonts
   sudo apt install fonts-noto-cjk              # – Chinese-Japanese-Korean characters
   sudo apt install fonts-indic                 # – extra indian fonts

   sudo apt install fonts-noto-color-emoji fontconfig libass9
   ```

   Для Amiri arabic:
   ```sh
   git clone https://github.com/aliftype/amiri.git
   sudo mkdir -p /usr/share/fonts/truetype/amiri
   sudo cp amiri/fonts/*.ttf /usr/share/fonts/truetype/amiri/
   ```
   
   Обновите кэш шрифтов
   ```sh
   sudo fc-cache -fv
   fc-list | grep -i amiri
   ``` 
</details>

---

### (Опционально) Подготовка `yt-dlp` для `/cookies_from_browser`

<details>
   <summary>Подготовка yt-dlp</summary>

   Для использования команды `/cookies_from_browser` (которая извлекает cookies из установленных браузеров на вашем сервере), убедитесь что бинарник **yt-dlp** настроен правильно:
  
   1. **Скачайте `yt-dlp`**  
      Посетите [official `yt-dlp` releases page](https://github.com/yt-dlp/yt-dlp/releases) и скачайте бинарник для вашей архитектуры процессора (например, `yt-dlp_x86_64`, `yt-dlp_arm`, и т.д.).  
      Поместите исполняемый бинарник в папку проекта `tg-ytdlp-bot`.
 
  2. **Переименуйте и сделайте исполняемым**  
     ```bash
     mv yt-dlp_linux yt-dlp
     chmod +x yt-dlp
     ```

   3. **Создайте символическую ссылку**  
      Создайте symlink чтобы `yt-dlp` мог запускаться из любой директории (например, в `/usr/local/bin`):
      ```bash
      sudo ln -s /full/path/to/tg-ytdlp-bot/yt-dlp /usr/local/bin/yt-dlp
      ```
      Убедитесь что `/usr/local/bin` в вашем `PATH`. Теперь можно запускать `yt-dlp` напрямую.

   (Также в этом случае вам нужно установить рабочее окружение (GUI) и любой поддерживаемый `yt-dlp` браузер самостоятельно)

</details>

---

## ⏳ Лимиты и кулдауны (`CONFIG/limits.py`)

`CONFIG/limits.py` - это центральное место где все рабочие лимиты бота настроены. Перед деплоем, просмотрите этот файл и настройте значения для вашего железа и хостинга:

- **Загрузки и субтитры:** `MAX_FILE_SIZE_GB`, `MAX_VIDEO_DURATION`, и `MAX_SUB_*` предотвращают вход очень больших видео/субтитров в очередь. В группах применяется `GROUP_MULTIPLIER`.
- **Множественные URL:** `MAX_MULTI_URL_LIMIT` (по умолчанию: 10) контролирует сколько URL можно отправить в одном сообщении когда формат качества установлен. В группах это умножается на `GROUP_MULTIPLIER` (по умолчанию: 20). Админы без лимитов.
- **Изображения и live streams:** `MAX_IMG_*`, `ENABLE_LIVE_STREAM_BLOCKING`, и `MAX_LIVE_STREAM_DURATION` защищают от бесконечных альбом/live-stream загрузок. На медленных соединениях, увеличьте `MAX_IMG_TOTAL_WAIT_TIME`.
- **Cookie кэш:** `COOKIE_CACHE_DURATION`, `COOKIE_CACHE_MAX_LIFETIME`, и `YOUTUBE_COOKIE_RETRY_LIMIT_PER_HOUR` контролируют как агрессивно YouTube cookies используются повторно и сколько попыток повтора получает пользователь в час.
- **Rate limits:** `RATE_LIMIT_PER_MINUTE|HOUR|DAY` и соответствующие `RATE_LIMIT_COOLDOWN_*` значения реализуют anti‑spam. Когда пользователь превышает лимиты, он ставится на кулдаун на 5/60/1440 минут.
- **Команды:** `COMMAND_LIMIT_PER_MINUTE` и экспоненциальный `COMMAND_COOLDOWN_MULTIPLIER` защищают все команды (не только URL) от злоупотреблений.
- **NSFW монетизация:** `NSFW_STAR_COST` определяет цену Telegram Stars для платного NSFW контента и может быть изменена в любое время.

После изменения этого файла, перезапустите бота чтобы новые лимиты применились. Если вы запускаете несколько инстансов с разными лимитами, держите отдельные копии `CONFIG/limits.py` и монтируйте их через `systemd` или Docker volumes.

### 👑 Конфигурация лимитов админов

Бот поддерживает отключение всех лимитов и ограничений для администраторов и админских групп. Эта функция позволяет админам обходить лимиты размера файлов, длительности видео, количества плейлистов, rate limits, и ограничения платного NSFW контента.

**Конфигурация в `CONFIG/config.py`:**

```python
# Список ID админов пользователей
ADMIN = [123456789, 987654321]  # Ваши ID админов
ADMIN_USERNAME = "@"  # Admin username (например, "@" или "@your_username")

# Список ID админских групп (группы без лимитов)
ADMIN_GROUP = [-1001234567890, -1001234567891]  # ID админских групп

# Список разрешенных групп (группы с увеличенными лимитами через GROUP_MULTIPLIER)
ALLOWED_GROUP = [-1001234567890, -1001234567891]  # ID разрешенных групп
```

**Конфигурация в `CONFIG/limits.py`:**

```python
class LimitsConfig(object):
    # Включить/выключить лимиты для админов и админских групп
    TURN_OFF_LIMITS_FOR_ADMINS = True  # Установите в False чтобы применить лимиты к админам
```

**Как это работает:**

**Когда `TURN_OFF_LIMITS_FOR_ADMINS = True`:**

- **Индивидуальные Админы** (пользователи в списке `ADMIN`):
  - ✅ Нет лимитов размера файлов
  - ✅ Нет лимитов длительности видео
  - ✅ Нет лимитов количества плейлистов
  - ✅ Нет rate limits (URL в минуту/час/день)
  - ✅ Нет лимитов команд
  - ✅ Нет лимитов количества изображений
  - ✅ Нет лимитов длительности live stream
  - ✅ **NSFW контент бесплатен** (не требует Telegram Stars)
  - ✅ Меню Always Ask показывает **без иконок звёзд** для NSFW контента

- **Админские группы** (группы в списке `ADMIN_GROUP`):
  - ✅ Все те же преимущества что и у индивидуальных админов
  - ✅ Не применяется `GROUP_MULTIPLIER` (лимиты полностью отключены)
  - ✅ Проверка подписки отключена

**Когда `TURN_OFF_LIMITS_FOR_ADMINS = False`:**

- Админы и админские группы подчиняются тем же лимитам что и обычные пользователи
- `GROUP_MULTIPLIER` применяется к админским группам (то же что и к `ALLOWED_GROUP`)

**Админские группы против разрешенных групп:**

- **`ADMIN_GROUP`**: Группы которые обходят **все лимиты** когда `TURN_OFF_LIMITS_FOR_ADMINS = True`
- **`ALLOWED_GROUP`**: Группы с **увеличенными лимитами** через `GROUP_MULTIPLIER` (по умолчанию: 2x)
  - NSFW контент бесплатен в группах (всегда)
  - Лимиты умножаются на `GROUP_MULTIPLIER`
  - Проверка подписки отключена

**Примечание:** Если группа указана и в `ADMIN_GROUP` и в `ALLOWED_GROUP`, `ADMIN_GROUP` имеет приоритет (все лимиты отключены).

**Поведение NSFW контента:**

**Для админов (когда лимиты отключены):**
- NSFW контент отправляется как **обычное видео** (без Telegram Stars)
- Меню Always Ask показывает **без иконок звёзд** (⭐️)
- Контент всё равно логируется в каналы `LOGS_PAID_ID` и `LOGS_NSFW_ID` (то же что и для обычных пользователей)

**Для обычных пользователей:**
- NSFW контент требует Telegram Stars (платный контент)
- Меню Always Ask показывает иконки звёзд (⭐️) для NSFW контента
- Контент логируется в `LOGS_PAID_ID` (платная копия) и `LOGS_NSFW_ID` (открытая копия)

**Пример конфигурации:**

```python
# CONFIG/config.py
ADMIN = [123456789]  # Ваш user ID
ADMIN_USERNAME = "@"  # Admin username (например, "@" или "@your_username")
ADMIN_GROUP = [-1001234567890]  # Ваш ID админской группы
ALLOWED_GROUP = [-1001234567891]  # ID обычной разрешенной группы

# CONFIG/limits.py
TURN_OFF_LIMITS_FOR_ADMINS = True  # Включить неограниченный доступ для админов
GROUP_MULTIPLIER = 2  # 2x лимиты для ALLOWED_GROUP
```

**Результат:**
- Пользователь `123456789` без лимитов
- Группа `-1001234567890` без лимитов
- Группа `-1001234567891` с 2x лимитами (через `GROUP_MULTIPLIER`)

---

## 💬 Все команды пользователя

### Базовые команды

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/start` | Запустить бота | `/start` |
| `/help` | Показать справку | `/help` |
| `/settings` | Открыть меню настроек | `/settings` |
| `/usage` | Показать статистику использования | `/usage` |
| `/tags` | Получить все ваши теги | `/tags` |
| `/lang` | Изменить язык бота | `/lang ru` |

### Команды загрузки

| Команда | Описание | Пример |
|----------|-------------|---------|
| **Video URL** | Скачать видео (авто-определение) | `https://youtube.com/watch?v=...` |
| **Multiple URLs** | Скачать несколько видео в очереди (только в режиме качества) | Отправить до 10 URL (20 в группах) в одном сообщении |
| `/vid` | Скачать видео | `/vid https://youtube.com/watch?v=...` |
| `/audio` | Скачать только аудио | `/audio https://youtube.com/watch?v=...` |
| `/link` | Получить прямые ссылки на видео | `/link 720 https://youtube.com/watch?v=...` |
| `/img` | Скачать изображения | `/img https://instagram.com/p/...` |

### Команды формата и качества

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/format` | Выбрать формат/кодек видео | `/format 720` |
| `/split` | Установить размер разделения видео | `/split 500mb` |
| `/mediainfo` | Переключить отображение mediainfo | `/mediainfo on` |

### Команды субтитров

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/subs` | Настроить субтитры | `/subs en auto` |

**Интеллектуальная обработка субтитров:**
- **Container-Aware Embedding**:
  - **MKV**: Soft-muxing (субтитры как отдельная дорожка, без потери качества)
  - **MP4**: Hard-embedding (вшиты в видео для универсальной совместимости)
- **Language Detection**: Оптимизированный выбор yt-dlp клиента для более быстрого обнаружения субтитров
- **Auto Mode**: Автоматически выбирает авто-генерируемые или обычные титры в зависимости от предпочтения пользователя
- **Always Ask Mode**: Показывает все доступные языки субтитров для ручного выбора

**Использование:**
```bash
/subs off       # Отключить субтитры
/subs ru        # Установить язык субтитров на русский
/subs en        # Установить язык субтитров на английский
/subs en auto   # Установить язык на английский с AUTO/TRANS включённым
/subs fr auto   # Установить язык на французский с AUTO/TRANS включённым
```

### Команды cookies

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/cookie` | Скачать cookies | `/cookie youtube` |
| `/check_cookie` | Проверить cookies | `/check_cookie` |
| `/save_as_cookie` | Загрузить cookie файл | `/save_as_cookie` |
| `/cookies_from_browser` | Извлечь из браузера | `/cookies_from_browser` |

### Расширенные команды

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/args` | Настроить аргументы yt-dlp (группированное меню) | `/args` |
| `/list` | Показать доступные форматы для URL | `/list https://youtube.com/watch?v=...` |
| `/proxy` | Включить/выключить прокси | `/proxy on` |
| `/keyboard` | Управлять клавиатурой ответов | `/keyboard full` |
| `/search` | Помощник inline поиска | `/search` |
| `/clean` | Очистить файлы пользователя | `/clean args` |
| `/nsfw` | Настройки NSFW контента | `/nsfw on` |

### Аргументы команд

Многие команды поддерживают прямые аргументы для быстрой настройки:

```bash
# Формат с качеством
/format 720    # Установить на 720p или ниже
/format 4k     # Установить на 4K или ниже
/format best   # Установить на лучшее качество

# Раскладки клавиатуры
/keyboard off   # Скрыть клавиатуру
/keyboard 1x3   # Одна строка
/keyboard 2x3   # Двойная строка (по умолчанию)
/keyboard full  # Эмодзи клавиатура

# Размеры разделения
/split 100mb   # 100MB (минимум)
/split 500mb   # 500MB
/split 1gb     # 1GB
/split 2gb     # 2GB (максимум)

# Языки субтитров (см. раздел Команды субтитров для деталей)
/subs off       # Отключить субтитры
/subs ru        # Русские субтитры
/subs en auto   # Английские с автопереводом

# Сервисы cookies (см. раздел Расширенное управление cookies для деталей)
/cookie youtube        # Скачать YouTube cookies напрямую
/cookie youtube 1      # Использовать конкретный источник YouTube cookies по индексу (1-10)
/cookie tiktok         # Скачать TikTok cookies напрямую
/cookie x              # Скачать Twitter/X cookies напрямую (алиас)
/cookie twitter        # Скачать Twitter/X cookies напрямую
/check_cookie          # Проверить текущие YouTube cookies

# Настройки языка (см. раздел Поддержка мультиязычности для полного списка)
/lang en         # 🇺🇸 Set to English
/lang ru         # 🇷🇺 Set to Russian
# ... (см. раздел Команды языка для всех 25 языков)

# Очистить специфические настройки
/clean args      # Очистить аргументы yt-dlp
/clean nsfw      # Очистить настройки NSFW
/clean proxy     # Очистить настройки прокси
/clean flood_wait # Очистить настройки flood wait

# Формат с выбором ID
/format id 134   # Скачать конкретный формат ID (с аудио)
/format id 401   # Скачать конкретный формат ID (с аудио)

# Показать доступные форматы
/list https://youtube.com/watch?v=...  # Показать все доступные форматы
```

---

## 🎯 Расширенные функции

### 📦 Поддержка множественных URL

Загрузка нескольких видео в одном сообщении когда формат качества установлен:

- **Требуется режим качества**: Работает только когда вы установили формат качества через команду `/format` (не в режиме "Always Ask")
- **Обработка в очереди**: URL обрабатываются последовательно с обновлением прогресса в реальном времени
- **Лимиты**: 
  - Личные чаты: до **10 URL** на сообщение
  - Группы: до **20 URL** на сообщение (2x множитель)
  - Админы: без ограничений
- **Формат**: Каждый URL на новой строке или разделённый пробелами
- **Отображение статуса**: Показывает прогресс как при загрузке плейлиста: "URL: X / Y"

**Пример:**
```
https://youtube.com/watch?v=video1
https://youtube.com/watch?v=video2
https://youtube.com/watch?v=video3
```

**Примечание:** В режиме "Always Ask", обрабатывается только первый URL.

### 🎬 Меню Always Ask

Интерактивное меню выбора качества с расширенной фильтрацией и поддержкой кодеков.

**Функции:**
- **📼 CODEC Кнопка**: Доступ к расширенным фильтрам кодеков и контейнеров
  - AVC (H.264/AVC) - Традиционный, широко поддерживаемый
  - AV1 - Современный бесплатный от роялти кодек с ~25-40% лучшей эффективностью
  - VP9 - Google's VP9 codec
  - Выбор контейнера MP4/MKV
- **📹 DUBS Кнопка**: Выбор языка аудио с индикаторами флагов
  - Появляется только когда обнаружены несколько аудио языков
  - Поддержка пагинации для длинных списков языков
  - **ALL** кнопка: Автоматически выбрать все доступные аудио дорожки
  - **OFF** кнопка: Отключить все дополнительные аудио дорожки
- **💬 SUBS Кнопка**: Выбор языка субтитров с умным определением
  - Авто-генерируемые против обычных титров
  - Индикаторы перевода
  - Поддержка пагинации
  - **ALL DUBS** кнопка: Автоматически скачать субтитры для всех языков которые имеют озвученные аудио дорожки
  - **OFF** кнопка: Очистить все выбранные языки субтитров
- **✂️ TRIM Кнопка**: Обрезка видео до определённого временного диапазона
  - Формат ввода: `HH:MM:SS-HH:MM:SS` (например, `00:52:40-00:57:41`)
  - Frame-accurate обрезка с FFmpeg
  - Автоматический fallback к перекодированию если копирование потока не удается
  - Обрезанные видео не кэшируются (всегда свежая загрузка)
  - Работает со всеми выборами качества и кодеков
- **☑️ LINK Кнопка**: Переключить режим прямой ссылки
  - Когда включён (✅LINK), клик по кнопкам качества возвращает прямые ссылки вместо загрузки
  - Учитывает все выбранные фильтры (кодек, контейнер, язык аудио, субтитры)
  - Нет кэширования для прямых ссылок
  - Всегда доступен в главном меню (не только в фильтрах CODEC)
- **Динамическая фильтрация**: Фильтрация качества в реальном времени на основе выбранного кодека/контейнера
- **Умная логика субтитров**: Различает режим "Always Ask" и ручной выбор субтитров

### 🍪 Расширенное управление cookies

Бот поддерживает автоматическую загрузку и проверку YouTube cookies из множества источников с интеграцией браузера и поддержкой fallback.

**Функции:**
- **Множественные источники**: Настройка до 10 источников YouTube cookies
- **Автоматическая проверка**: Каждый cookie проверяется на работоспособность
- **Fallback система**: Автоматическое переключение между источниками если один не работает
- **Интеграция браузера**: Извлечение cookies из установленных браузеров
- **Progress в реальном времени**: Live обновления во время загрузки и проверки

**Конфигурация:**

**Для Docker установки:**
Сначала заполните файл `TXT/cookie.txt`. Этот cookie будет использоваться по умолчанию для всех пользователей. Вы также можете заполнить дополнительные cookie файлы для сервисов которые вам нужны (YouTube, TikTok, и т.д.) и поместить их в `docker/configuration-webserver/site/cookies/` перед запуском:
```
tg-ytdlp-bot/
├── TXT/
│   └── cookie.txt                    # Cookie по умолчанию для всех пользователей
└── docker/
    └── configuration-webserver/
        └── site/
            └── cookies/
                ├── cookie.txt
                ├── youtube.txt
                ├── youtube-1.txt
                ├── youtube-2.txt
                └── ... (до youtube-10.txt)
```

**Для ручной установки (в `CONFIG/config.py`):**
```python
# Cookie Configuration
COOKIE_URL = "https://your-domain.com/cookies/cookie.txt"  # Fallback cookie URL

# YouTube Cookie URLs (Multiple Sources)
YOUTUBE_COOKIE_URL = "https://your-domain.com/cookies/youtube/cookie1.txt"
YOUTUBE_COOKIE_URL_1 = "https://your-domain.com/cookies/youtube/cookie2.txt"
YOUTUBE_COOKIE_URL_2 = "https://your-domain.com/cookies/youtube/cookie3.txt"
# ... до YOUTUBE_COOKIE_URL_9
```

**Получение YouTube Cookies:**

YouTube часто вращает account cookies на открытых вкладках браузера YouTube как меру безопасности. Чтобы экспортировать cookies которые останутся рабочими с yt-dlp:

1. Откройте новое окно private browsing/incognito и войдите в YouTube
2. В том же окне и той же вкладке, перейдите на `https://www.youtube.com/robots.txt` (это должна быть единственная открытая вкладка private/incognito)
3. Экспортируйте youtube.com cookies из браузера используя [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) расширение
4. Закройте окно private browsing/incognito чтобы сессия никогда не открывалась в браузере снова

**Команды пользователя:**
- `/cookie` → YouTube: Загружает и проверяет cookies из множества источников
- `/cookie youtube <index>`: Выбор конкретного источника YouTube cookies по индексу (1-10)
- `/check_cookie`: Проверяет существующие cookies и проверяет работоспособность YouTube
- `/cookies_from_browser`: Извлекает cookies из установленных браузеров
- `/save_as_cookie`: Загружает пользовательский cookie файл

**Как это работает:**
1. Пользователь запускает `/cookie` и выбирает YouTube
2. Бот загружает cookies из первого доступного источника
3. Проверяет cookies тестируя их с YouTube видео
4. Если проверка не удается, автоматически пытает следующий источник
5. Продолжает пока рабочие cookies не найдены или все источники исчерпаны

**Процесс проверки cookies:**
1. **Загрузка**: Получает cookie файл из настроенного источника
2. **Проверка формата**: Проверяет формат Netscape cookie
3. **Проверка размера**: Убедится что размер файла под 100KB
4. **YouTube тест**: Проверяет cookies с коротким YouTube видео
5. **Анализ ошибок**: Различает между ошибками аутентификации и сетевыми ошибками
6. **Fallback**: Пытает следующий источник если текущий не работает

**Требования к файлу cookies:**
- **Формат**: Должен быть в формате Netscape cookie
- **Лимит размера**: Максимум 100KB на файл cookies
- **Доступ**: Cookie файлы должны быть доступны через HTTP/HTTPS URLs (для ручной установки)
- **Загрузка**: Используйте [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) расширение браузера для экспорта cookies

**Функции безопасности:**
- **Скрытие URL**: URL источников скрыты от пользователей в сообщениях об ошибках
- **Очистка ошибок**: Чувствительная информация удалена из логов
- **Временные файлы**: Cookie файлы очищаются после проверки
- **Контроль доступа**: Команды управления cookies должным образом ограничены

**Опыт пользователя:**
- Обновления прогресса: "🔄 Загрузка и проверка YouTube cookies... Попытка 1 из 4"
- Сообщение успеха: "✅ YouTube cookies успешно загружены и проверены! Использован источник 2 из 4"
- Сообщение неудачи: "❌ Все YouTube cookies устарели или недоступны! Свяжитесь с администратором бота для их замены."

### 🌐 Поддержка прокси

Глобальный контроль прокси для всех операций загрузки с настройками специфичными для пользователя.

**Конфигурация (в `CONFIG/config.py`):**
```python
# Proxy configuration (до 2 прокси)
PROXY_TYPE = "http"  # http, https, socks4, socks5, socks5h
PROXY_IP = "X.X.X.X"
PROXY_PORT = 3128
PROXY_USER = "username"
PROXY_PASSWORD = "password"

# Additional Proxy
PROXY_2_TYPE = "socks5"
PROXY_2_IP = "X.X.X.X"
PROXY_2_PORT = 3128
PROXY_2_USER = "username"
PROXY_2_PASSWORD = "password"

# Proxy selection method
PROXY_SELECT = "round_robin"  # random, round_robin
```

**Функции:**
- **Глобальный контроль**: Включить/выключить прокси для всех yt-dlp операций
- **Настройки специфичные для пользователя**: Каждый пользователь может независимо контролировать использование прокси через команду `/proxy`
- **Множественные прокси**: Поддержка до 2 прокси серверов с round-robin или случайным выбором
- **Автоматическая интеграция**: Когда включён, прокси автоматически применяется ко всем загрузкам
- **Поддержка cookies**: Работает с настройками cookies пользователя для доступа к приватному контенту
- **Постоянные настройки**: Предпочтение прокси сохраняется на пользователя в файле `proxy.txt`

**Использование:**
```bash
/proxy on                    # Включить прокси для всех загрузок
/proxy off                   # Выключить прокси для всех загрузок
/proxy                      # Показать меню управления прокси
```

**Как это работает:**
1. Пользователь запускает `/proxy on` чтобы включить прокси
2. Бот сохраняет предпочтение в `users/{user_id}/proxy.txt`
3. Все последующие yt-dlp операции автоматически используют настроенный прокси
4. Пользователь может выключить через `/proxy off` в любое время

### 🔗 Извлечение прямых ссылок

Получите прямые stream URLs для медиа проигрывателей с выбором качества и умным fallback.

**Функции:**
- **Выбор качества**: Укажите желаемое качество (например, `720`, `1080`, `4k`, `8k`)
- **Гибкий формат**: Поддержка как числовых (`720`) так и описательных (`720p`, `4k`, `8K`) спецификаций качества
- **Умный fallback**: Автоматически fallback к лучшему доступному качеству если указанное качество недоступно
- **Поддержка двойного потока**: Возвращает оба URL видео и аудио потока когда доступно
- **Поддержка прокси**: Работает с настроенными настройками прокси для ограниченных доменов
- **Интеграция cookies**: Использует настройки cookies пользователя для доступа к приватному контенту
- **Интеграция проигрывателя**: 🔗Link кнопка в меню Always Ask предоставляет прямые ссылки для медиа проигрывателей (VLC, MX Player, Infuse, IINA, nPlayer, MPV)

**Использование:**
```bash
/link https://youtube.com/watch?v=...          # Лучшее качество
/link 720 https://youtube.com/watch?v=...     # 720p или ниже
/link 720p https://youtube.com/watch?v=...    # То же что и выше
/link 4k https://youtube.com/watch?v=...      # 4K или ниже
/link 8k https://youtube.com/watch?v=...      # 8K или ниже
```

**Поддержка проигрывателей:**
- **🌐 Browser**: Прямой stream URL для веб-браузеров
- **🎬 VLC (iOS)**: iOS VLC проигрыватель с поддержкой x-callback
- **🎬 VLC (Android)**: Android VLC проигрыватель с поддержкой intent

### 🏷️ Система тегов

Добавьте теги к любой ссылке для организации. Для подробной информации см. раздел [Система тегов (Теги навигации)](#система-тегов-теги-навигации) ниже.

**Быстрое использование:**
```
https://youtube.com/watch?v=... #music #favorite #2024
```

Теги автоматически добавляются к описанию видео и сохраняются в вашем файле `tags.txt`.

### 🖼️ Поддержка загрузки изображений

Загрузка изображений из различных платформ:

- **Прямые URL**: Любая ссылка на изображение с обычными расширениями
- **Платформы**: Imgur, Flickr, DeviantArt, Pinterest, Instagram, Twitter/X, Reddit
- **Облачное хранилище**: Google Drive, Dropbox, Mega.nz
- **Диапазоны**: Загрузка конкретных диапазонов из альбомов/лент

### ⚙️ Пользовательские аргументы yt-dlp (`/args`)

Настройка расширенных параметров yt-dlp с группированным интерфейсом:

- **Boolean Options**: Включить/выключить функции (extract_flat, write_automatic_sub, и т.д.)
- **Text Parameters**: Пользовательский referer, user agent, output template
- **Numeric Settings**: Retries, timeout, fragment retries
- **JSON Headers**: Пользовательские HTTP headers для специфичных сайтов
- **Selection Options**: Качество аудио, качество видео, выбор формата

**Группированный интерфейс меню:**
- ✅/❌ **Boolean** - переключатели True/False
- 📋 **Select** - Выбор из опций
- 🔢 **Numeric** - ввод числа
- 📝🔧 **Text** - ввод текста/JSON

**Пример конфигурации:**
```
Referer: https://example.com
User Agent: Custom Bot 1.0
Custom HTTP Headers: {"X-API-Key": "your-key"}
Retries: 5
Timeout: 30
```

### 📋 Команда списка форматов (`/list`)

Просмотр всех доступных форматов для любого видео URL:

- **Полный список форматов**: Показывает все доступные форматы видео/аудио
- **Детали формата**: Разрешение, кодек, размер файла, информация о качестве
- **Подсказки по загрузке**: Инструкции как использовать команду `/format`
- **Экспорт файла**: Отправляет полный список форматов как загружаемый текстовый файл

**Использование:**
```bash
/list https://youtube.com/watch?v=dQw4w9WgXcQ
```

**Функции:**
- Показывает ID формата, разрешение, кодек, размер файла
- Включает инструкции по загрузке для команды `/format`
- Экспортирует полный список как текстовый файл
- Работает со всеми поддерживаемыми платформами

### 🚀 PO Token Provider (YouTube Bypass)

Автоматический обход YouTube ограничений:

- **"Sign in to confirm"** bypass сообщения
- **IP-based blocking** защита
- **Rate limiting** смягчение
- **Прозрачная работа**: Работает с существующими системами прокси и cookies
- **Автоматический fallback**: Falls back к стандартной извлечению если provider недоступен

**Настройка:**
```bash
# Установите Docker
sudo apt install -y docker.io

# Запустите PO Token Provider
docker run -d --name bgutil-provider -p 4416:4416 --init --restart unless-stopped brainicism/bgutil-ytdlp-pot-provider

# Установите yt-dlp plugin
python3 -m pip install -U bgutil-ytdlp-pot-provider
```

**Конфигурация:**
```python
# В CONFIG/config.py
YOUTUBE_POT_ENABLED = True
YOUTUBE_POT_BASE_URL = "http://127.0.0.1:4416"
YOUTUBE_POT_DISABLE_INNERTUBE = False
```

**Технические детали:**
- Использует правильный Python API формат для `extractor_args`: `dict -> dict -> list[str]`
- `disable_innertube` добавляется только когда включён (как `["1"]` string в list)
- Совместим с yt-dlp >= 2025.05.22
- Работает с HTTP и script-based providers
- **Автоматический fallback**: Если PO token provider недоступен, бот автоматически fallback к стандартной YouTube извлечению
- **Мониторинг здоровья**: Доступность provider кэшируется и проверяется каждые 30 секунд

**Требования:**
- Docker контейнер запускающий `brainicism/bgutil-ytdlp-pot-provider`
- yt-dlp plugin: `bgutil-ytdlp-pot-provider`

**Механизм fallback:**
- **Автоматическое определение**: Бот проверяет доступность provider перед каждым YouTube запросом
- **Кэшированные проверки здоровья**: Статус provider кэшируется на 30 секунд чтобы избежать избыточных запросов
- **Graceful degradation**: Если provider недоступен, бот автоматически fallback к стандартной YouTube извлечению
- **Без влияния на пользователя**: Fallback полностью прозрачен для пользователей
- **Мониторинг админа**: Здоровье provider автоматически мониторится и логируется

### 🎧 Многодорожечное аудио и субтитры (MKV)

Расширенная поддержка многодорожечности для встраивания нескольких аудио языков и субтитровых дорожек в MKV контейнеры.

**Функции:**
- **Множественные аудио дорожки**: Встраивает все выбранные аудио языки как отдельные дорожки в MKV
  - Оригинальная аудио дорожка всегда сохраняется и мапируется первой
  - Каждый дополнительный язык становится отдельной аудио дорожкой
  - Полное сохранение кодов языка (например, `zh-Hans`, `zh-Hant`, `en-US`, `en-GB`)
  - Автоматический выбор лучшего качества для каждого языка (OPUS > AAC > MP3)
  - Определение дублей и выбор на основе качества
- **Множественные субтитры дорожки**: Встраивает все выбранные языки субтитров как отдельные дорожки в MKV
  - Поддержка оригинальных, авто-генерируемых, и переведённых субтитров
  - Автоматическая конвертация формата (VTT, JSON3, SRV3, TTML → SRT)
  - Гарантия UTF-8 кодирования
  - Soft-muxing (без потери качества, субтитры как отдельные дорожки)
  - Обработка частичного успеха: если некоторые субтитры не удается скачать, успешно скачанные всё равно встраиваются
- **Поддержка VP9 кодека**: Полная поддержка VP9 видео кодека с многодорожечным аудио/субтитры встраиванием
- **Умное определение языка**: Улучшенное определение оригинального языка из метаданных видео
- **Надёжная загрузка**: Логика повтора с ротацией прокси для загрузки субтитров чтобы handle rate limiting
- **Визуальная обратная связь**: Выбранные языки отмечены ✅ в меню Always Ask

**Использование:**
1. Выберите контейнер **MKV** в меню CODEC
2. Выберите аудио языки через кнопку **DUBS** (или используйте **ALL** для всех дорожек)
3. Выберите языки субтитров через кнопку **SUBS** (или используйте **ALL DUBS** для языков озвучивания)
4. Выберите качество видео - все выбранные дорожки будут встроены автоматически

**Поддерживаемые форматы:**
- **Video**: VP9, AV1, H.264/AVC
- **Audio**: OPUS, AAC, MP3 (лучшее качество выбрано на язык)
- **Subtitles**: SRT (с автоматической конвертацией из VTT, JSON3, SRV3, TTML)

### Улучшенный выбор формата (`/format`)

Расширенный выбор формата с поддержкой кодеков, предпочтений контейнера, и выбора ID формата.

**Функции:**
- **Поддержка кодеков**: Выбор между H.264/AVC (avc1), AV1 (av01), и VP9 (vp9)
- **Переключатель контейнера**: Переключение между MP4 и MKV контейнерами
- **Умный выбор качества**: Приоритизирует точные совпадения высоты перед fallback к "меньше или равно"
- **Постоянные предпочтения**: Ваши выборы кодека и контейнера сохраняются на пользователя
- **Быстрая настройка качества**: Используйте аргументы чтобы установить качество напрямую (например, `/format 720`, `/format 4k`)
- **Поддержка ID формата**: Скачайте специфичные ID формата с автоматическим добавлением аудио
- **Умная обработка аудио**: Видео-only форматы автоматически получают лучшее аудио добавленным

**Использование:**
```bash
/format 720    # Установить качество на 720p или ниже
/format 4k     # Установить качество на 4K или ниже  
/format 8k     # Установить качество на 8K или ниже
/format best   # Установить на лучшее качество
/format ask    # Всегда спрашивать выбор качества
/format id 134 # Скачать конкретный формат ID (с аудио)
/format id 401 # Скачать конкретный формат ID (с аудио)
```

### Управление клавиатурой ответов

Бот поддерживает настраиваемые раскладки клавиатуры для быстрого доступа к командам. См. раздел [Аргументы команд](#аргументы-команд) выше для использования команды `/keyboard`.

**Режимы клавиатуры:**
- **OFF**: Полностью скрывает клавиатуру ответов
- **1x3**: Показывает одну строку с `/clean`, `/cookie`, `/settings`
- **2x3**: Показывает две строки с полным набором команд (режим по умолчанию)
- **FULL**: Показывает эмодзи клавиатуру с визуальным представлением команд

**Функции:**
- **Настраиваемая раскладка**: Выбор между 1x3 (одна строка), 2x3 (двойная строка), и FULL (эмодзи) раскладками клавиатуры
- **Умное отображение**: Клавиатура автоматически показывается/скрывается на основе предпочтений пользователя
- **Постоянные настройки**: Предпочтения клавиатуры пользователя сохраняются в файле `keyboard.txt`
- **Лёгкий переключатель**: Быстрый переключение между OFF, 1x3, 2x3, и FULL режимами через команду `/keyboard`

### 🔞 Управление NSFW контентом

Расширенная система определения и фильтрации NSFW контента с настраиваемыми списками доменов и ключевых слов.

**Функции:**
- **Автоматическое определение**: Сканирует заголовки видео, описания, и домены на взрослый контент
- **Умная тегировка**: Автоматически добавляет тег `#nsfw` к обнаруженному контенту
- **Защита спойлером**: Скрывает NSFW контент под тегами спойлера в Telegram
- **Контроль пользователя**: Переключить настройки NSFW blur через `/nsfw on/off`
- **Управление админа**: Обновить и управлять списками определения porn
- **Множественное определение**: Домен-based и ключевые-слова based фильтрация
- **Настраиваемые списки**: Настраиваемые porn домены и ключевые слова

**Команды пользователя:**
```bash
/nsfw on          # Включить NSFW blur
/nsfw off         # Выключить NSFW blur
/nsfw             # Показать меню настроек NSFW
```

**Команды админа:**
```bash
/update_porn      # Обновить списки определения porn из внешних источников
/reload_porn      # Перезагрузить кэш определения porn без рестарта
/check_porn       # Проверить URL на NSFW контент с детальным объяснением
```

**Структура файла:**
```
TXT/
├── porn_domains.txt      # Список porn доменов (по одному на строку)
├── porn_keywords.txt     # Список porn ключевых слов (по одному на строку)
└── supported_sites.txt   # Список поддерживаемых видео сайтов

script.sh                 # Скрипт обновления (настраиваемый через CONFIG/domains.py)
```

**Система фильтрации доменов:**
Бот использует трёхуровневую систему фильтрации доменов:

1. **WHITELIST** (`CONFIG/domains.py`): Домены полностью исключённые из porn определения
   - Эти домены и их поддомены никогда не проверяются на porn контент
   - Пример: `youtube.com`, `bilibili.com`, `dailymotion.com`

2. **GREYLIST** (`CONFIG/domains.py`): Домены исключённые только из проверки списка доменов
   - Эти домены всё ещё проверяются на porn ключевые слова в заголовках/описаниях
   - Но они исключены из проверки файла `porn_domains.txt`
   - Полезно для сайтов которые могут иметь взрослый контент но не являются porn сайтами

3. **BLACKLIST** (`CONFIG/domains.py`): Домены явно заблокированные
   - Пусто по умолчанию, можно использовать чтобы заблокировать специфичные домены

**Конфигурация в `CONFIG/domains.py`:**
```python
# Whitelist - полностью исключённые из porn определения
WHITELIST = [
    'bilibili.com', 'dailymotion.com', 'youtube.com', 'youtu.be',
    'twitch.tv', 'vimeo.com', 'facebook.com', 'tiktok.com'
]

# Greylist - исключённые из списка доменов но ещё проверяемые на ключевые слова
GREYLIST = [
    'example.com', 'test.com'
    # Добавьте домены сюда которые должны быть исключены из проверки porn_domains.txt
    # но ещё проверяемые против porn_keywords.txt
]

# Update script path
UPDATE_PORN_SCRIPT_PATH = "./script.sh"  # Настраиваемый путь скрипта
```

Для более подробной информации по управлению определением porn, см. раздел [Porn Detection Management](#porn-detection-management).

### ⏱️ Защита от Flood Wait

Умное ограничение скорости и обработка flood wait:

- **Автоматическое определение**: Определяет лимиты скорости Telegram API
- **Уведомление пользователя**: Информирует пользователей о периодах flood wait
- **Сохранение настроек**: Сохраняет настройки flood wait на пользователя
- **Умное восстановление**: Автоматически обрабатывает восстановление от rate limit
- **Мониторинг админа**: Отслеживает события flood wait в логах

**Функции Flood Wait:**
- Автоматическое определение и обработка flood wait
- Уведомление пользователя с оценочным временем ожидания
- Сохранение настроек через рестарты бота
- Интеграция со всеми командами бота
- Мониторинг и логирование админа

### Улучшенная обработка ошибок
- **Повторы загрузки**: Умная логика повтора для неудачных загрузок с fallback в режим документа
- **Динамическое дисковое пространство**: Интеллектуальная оценка места на основе размера видео
- **Graceful degradation**: Лучшая обработка недоступности формата и сетевых проблем
- **Восстановление от Flood Wait**: Автоматическая обработка rate limits Telegram API

---

## 💳 Платные посты (Telegram Stars) и групповой режим

- **Платные посты (Stars)**: Бот может отправлять платные посты через Telegram Stars для NSFW контента в личных чатах.
  - Обложка подготавливается автоматически (320×320 с отступами) чтобы соответствовать требованиям Telegram.
  - Цена настраивается в `CONFIG/limits.py` через `NSFW_STAR_COST`.
  - Для каналов/групп, поддерживается relay (когда бот добавлен как админ); платный контент кэшируется должным образом.

- **Добавление бота в группу**: Добавьте бота как админа в вашу группу/супергруппу чтобы использовать команды внутри чата.
  - **Типы групп:**
    - **ADMIN_GROUP**: Группы перечисленные в `ADMIN_GROUP` обходят все лимиты (когда `TURN_OFF_LIMITS_FOR_ADMINS = True` в `CONFIG/limits.py`)
    - **ALLOWED_GROUP**: Группы перечисленные в `ALLOWED_GROUP` имеют увеличенные лимиты через `GROUP_MULTIPLIER` (по умолчанию: 2x)
    - **Обычные группы**: Лимиты умножаются на `GROUP_MULTIPLIER` (по умолчанию: 2x), уменьшая fallbacks к режиму документа для больших файлов
  - Все другие функции (форматы, прокси, cookies, прямые ссылки) работают так же как в личных чатах.
  - NSFW контент бесплатен в группах (всегда бесплатен в группах)

**Конфигурация:**
- Добавьте ID групп в `ADMIN_GROUP` или `ALLOWED_GROUP` в `CONFIG/config.py` (см. раздел [Getting API Credentials](#получение-api-учетных-данных) для как получить ID групп)
- Настройте `GROUP_MULTIPLIER` и `TURN_OFF_LIMITS_FOR_ADMINS` в `CONFIG/limits.py` (см. раздел [Admin Limits Configuration](#-конфигурация-лимитов-админов))

Примечание: Вы можете настроить точные значения лимитов и поведение в `CONFIG/limits.py` и `CONFIG/config.py` согласно вашему хостингу и потребностям.

---

## 🧑 Команды администратора

### Управление пользователями

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/block_user` | Заблокировать пользователя | `/block_user 123456789` |
| `/unblock_user` | Разблокировать пользователя | `/unblock_user 123456789` |
| `/all_users` | Получить всех пользователей | `/all_users` |
| `/all_blocked` | Получить заблокированных пользователей | `/all_blocked` |
| `/all_unblocked` | Получить разблокированных пользователей | `/all_unblocked` |

### Управление системой

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/run_time` | Показать время работы бота | `/run_time` |
| `/log` | Получить логи пользователя | `/log 123456789` |
| `/broadcast` | Рассылка сообщения | `/broadcast` (ответ на сообщение) |
| `/reload_cache` | Перезагрузить кэш Firebase | `/reload_cache` |
| `/auto_cache` | Управление авто кэшом | `/auto_cache 24` |

### Управление контентом

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/update_porn` | Обновить списки определения porn | `/update_porn` |
| `/reload_porn` | Перезагрузить кэш определения porn | `/reload_porn` |
| `/check_porn` | Проверить URL на NSFW контент с детальным объяснением | `/check_porn https://example.com/video` |
| `/uncache` | Очистить кэш субтитров | `/uncache` |

### Управление языком

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/lang` | 🌍 Показать меню выбора языка | `/lang` |
| `/lang <code>` | 🌍 Установить язык бота | `/lang ru` |

### Мониторинг системы

| Команда | Описание | Пример |
|----------|-------------|---------|
| `/nsfw` | Настройки NSFW контента | `/nsfw on` |

---

## 📊 Управление контентом

### Auto cache – как это работает (on/off/N)

Бот поддерживает локальный JSON кэш (dump) данных Firebase. Фоновый релоадер может периодически обновлять этот кэш сначала скачивая свежий dump и затем перезагружая его в память.

- Цикл обновления:
  - Скачать dump через REST (`download_firebase.py` logic)
  - Перезагрузить локальный JSON в память
- Выравнивание интервала: следующий запуск выравнивается к шагам от полуночи (00:00) с вашим шагом интервала (N часов).
- Примеры логов которые вы увидите:
  - `🔄 Загрузка и перезагрузка dump Firebase кэша...`
  - `✅ Firebase кэш успешно обновлён!`

### Использование команды
- `/auto_cache on` – включить фоновый авто-обновление
- `/auto_cache off` – выключить фоновый авто-обновление
- `/auto_cache N` – установить интервал обновления на N часов (1..168)
  - Это немедленно обновляет настройки runtime
  - Значение также сохраняется в `CONFIG/config.py` обновляя `RELOAD_CACHE_EVERY = N`
  - Фоновый поток безопасно перезапускается чтобы новый интервал вступил в силу немедленно

Ваш текущий интервал по умолчанию из `CONFIG/config.py`:
```python
RELOAD_CACHE_EVERY = 24  # в часах
```

---

## 🔞 Управление определением porn

Этот раздел предоставляет дополнительные детали для админов управляющих списками определения porn. Для общих функций управления NSFW контентом, см. раздел [NSFW Content Management](#-nsfw-управление-контентом) в Расширенных функциях.

### Детали команд админа

#### `/update_porn`
Запускает внешний скрипт чтобы обновить porn домены и ключевые слова из внешних источников.

**Функции:**
- Запускает настраиваемый скрипт (по умолчанию: `./script.sh`)
- Показывает вывод скрипта в реальном времени и статус выполнения
- Комплексная обработка ошибок и логирование
- Путь скрипта настраиваем через `CONFIG/domains.py`

#### `/reload_porn`
Перезагружает кэш определения porn без рестарта бота.

**Функции:**
- Горячая перезагрузка porn доменов из `TXT/porn_domains.txt`
- Горячая перезагрузка porn ключевых слов из `TXT/porn_keywords.txt`
- Горячая перезагрузка поддерживаемых сайтов из `TXT/supported_sites.txt`
- Показывает текущую статистику кэша
- Немедленный эффект - нет рестарта бота требуется

### Интеграция
Эти команды интегрируются с существующей системой определения porn:
- **Domain Detection**: Проверяет URL видео против списков porn доменов
- **Keyword Detection**: Сканирует заголовки видео, описания, и подписи
- **Auto-tagging**: Автоматически добавляет тег `#nsfw` к обнаруженному контенту
- **Защита спойлером**: Скрывает porn контент под тегами спойлера в Telegram

### Безопасность
- Обе команды только для админов с должным контролем доступа
- Выполнение скрипта логируется для аудита
- Скрипт запускается из корневой папки бота
- Вывод скрипта захвачен и отображается админу

---

## 🔄 Обновление бота (скрипты обновления)

Вы можете обновить код из ветки `newdesign2` (или `main` ветка) `chelaxian/tg-ytdlp-bot` используя предоставленные скрипты. Апдейтер будет:
- Клонировать репозиторий во временную директорию
- Обновить Python файлы (`.py`), shell скрипты (`.sh`), Docker файлы (`Dockerfile`, `docker-compose.yml`, `.dockerignore`), и документацию (`.md`)
- Сохранить ваш `CONFIG/config.py`, `.env`, и другие исключённые файлы/директории с чувствительными данными
- Сделать бекапы изменённых файлов с суффиксом `.backup_YYYYMMDD_HHMM` и переместить их в `_backup/` (оригинальная структура сохранена)
- Попросить подтверждения перед применением изменений

### Файлы которые будут обновлены:
- ✅ Все Python файлы (`.py`)
- ✅ Shell скрипты (`.sh`) - включая `UPDATE_DOCKER.sh`, `UPDATE.sh`, `engines_updater.sh`, `update_bgutil_provider.sh`, `warp/entrypoint.sh`, и т.д. (кроме `script.sh` который исключён)
- ✅ Docker файлы - `Dockerfile`, `docker-compose.yml`, `.dockerignore`, `docker-entrypoint.sh`, `warp/Dockerfile`, `warp/entrypoint.sh`
- ✅ Документация - `README.md`, `CONTRIBUTING.md`, `LICENSE`
- ✅ Шаблоны конфигурации - `requirements.txt`, `CONFIG/LANGUAGES/`, `web/` директория

### Файлы которые НЕ будут обновлены (сохранены):
- ❌ `CONFIG/config.py` - ваша личная конфигурация
- ❌ `CONFIG/domains.py` - ваши настройки доменов
- ❌ `.env` - переменные окружения
- ❌ `script.sh` - ваш пользовательский скрипт обновления для списков porn.
- ❌ `TXT/` директория - ваши cookie файлы и списки
- ❌ `users/`, `cookies/`, `_backup/` директории
- ❌ Session файлы, логи, и runtime данные

### Обновление локальной установки (без Docker)

#### Одно-командное обновление (рекомендуется)
```bash
./UPDATE.sh
```
- Скрипт проверяет предпосылки и запускает Python апдейтер.
- После успешного обновления, перезапустите сервис бота (если используете systemd):
```bash
systemctl restart tg-ytdlp-bot
journalctl -u tg-ytdlp-bot -f
```

#### Ручное обновление через Python
```bash
python3 update_from_repo.py --show-excluded   # показать исключённые файлы/папки
python3 update_from_repo.py                   # интерактивное обновление (прошит подтверждение)
```

### Обновление Docker установки

#### Быстрое обновление (рекомендуется)
Используйте скрипт `UPDATE_DOCKER.sh` для автоматического обновления Docker окружения:

```bash
# Сделать скрипт исполняемым (только в первый раз)
chmod +x UPDATE_DOCKER.sh

# Полное обновление: остановить контейнеры -> обновить код -> пересобрать -> перезапустить
./UPDATE_DOCKER.sh

# Пропустить обновление кода, только пересобрать и перезапустить контейнеры
./UPDATE_DOCKER.sh --skip-update

# Полное обновление с чистой сборкой (без кэша)
./UPDATE_DOCKER.sh --no-cache

# Показать помощь
./UPDATE_DOCKER.sh --help
```

**Что `UPDATE_DOCKER.sh` делает:**
1. ✅ Останавливает и удаляет все Docker контейнеры
2. ✅ Обновляет код из репозитория (если не пропущено)
3. ✅ Пересобирает Docker образы
4. ✅ Запускает все контейнеры

**Опции:**
- `--skip-update` - Пропустить обновление кода, только пересобрать и перезапустить контейнеры
- `--no-cache` - Собрать образы без использования кэша (чистая сборка)
- `--remove-volumes` - Удалить volumes при остановке (⚠️ **ПРЕДУПРЕЖДЕНИЕ**: Это удалит volume `warp-data` с WireGuard конфигурацией!)

#### Очистить неиспользуемое Docker пространство
Для очистки неиспользуемого Docker пространства используйте следующую команду:
```bash
docker system prune -a --volumes
```

#### Ручное Docker обновление

Если предпочитаете обновлять вручную:

```bash
# 1. Обновить код
./UPDATE.sh

# 2. Остановить контейнеры
docker compose down

# 3. Пересобрать образы
docker compose build

# 4. Запустить контейнеры
docker compose up -d

# 5. Проверить статус
docker compose ps
docker compose logs -f
```

#### Обновление специфичных сервисов

Чтобы обновить только специфичные сервисы без полной пересборки:

```bash
# Пересобрать и перезапустить только бот и dashboard
docker compose up -d --build bot dashboard

# Пересобрать только warp сервис
docker compose build warp
docker compose up -d warp

# Скачать последний bgutil-provider образ
docker compose pull bgutil-provider
docker compose up -d bgutil-provider
```

#### После обновления

После обновления, проверьте что всё работает:

```bash
# Проверить статус контейнеров
docker compose ps

# Просмотреть логи
docker compose logs -f bot
docker compose logs -f dashboard
docker compose logs -f warp

# Проверить dashboard
curl http://localhost:5555/health
```

---

### (Опционально) Удалить все контейнеры и образы проекта

```bash
docker stop tg-ytdlp-warp
docker stop tg-ytdlp-dashboard
docker stop tg-ytdlp-bot
docker stop tg-ytdlp-bgutil-provider

docker rm tg-ytdlp-warp
docker rm tg-ytdlp-dashboard
docker rm tg-ytdlp-bot
docker rm tg-ytdlp-bgutil-provider

docker rmi tg-ytdlp-bot-bot
docker rmi tg-ytdlp-bot-dashboard
docker rmi tg-ytdlp-bot-warp
docker rmi brainicism/bgutil-ytdlp-pot-provider

docker system prune -a --volumes
```

---

## 🔄 Восстановление из бекапов

Когда апдейтер изменяет файлы, он создаёт бекапы и перемещает их в папку `_backup/`, сохраняя оригинальную структуру директории. Имена бекап файлов имеют суффикс `.backup_YYYYMMDD_HHMM` (уровень минут). Инструмент восстановления позволяет вам вернуться к выбранному индексу бекапа.

### Интерактивное восстановление (рекомендуется)
```bash
python3 restore_from_backup.py
```
- Используйте клавиши Arrow (или j/k) чтобы навигировать, PgUp/PgDn для пагинации, Enter чтобы выбрать, q чтобы выйти.
- Список показывает сгруппированные бекапы по минуте: `[YYYY-MM-DD HH:MM:SS] files: N (id: YYYYMMDD_HHMM)`.
- После подтверждения, все файлы из того бекапа восстанавливаются в корень проекта, с суффиксом `.backup_YYYYMMDD_HHMM` удалённым.

### Список доступных бекапов
```bash
python3 restore_from_backup.py --list
```
Выводит доступные ID бекапов (сначала новейшие) с количеством файлов.

### Не-интерактивное восстановление по ID
```bash
python3 restore_from_backup.py --timestamp YYYYMMDD_HHMM
```
Восстанавливает все файлы для указанного ID бекапа.

### После восстановления
Если вы запускаете бота как сервис, перезапустите его:
```bash
systemctl restart tg-ytdlp-bot
journalctl -u tg-ytdlp-bot -f
```

---

## 🔗 Спецификация шаблона команды link

- **`https://example.com`** \
  Скачать видео с его оригинальным именем. \
  Если это плейлист, только первое видео скачивается. 

- **`https://example.com*1*3`**  \
  Скачать указанный диапазон видео из плейлиста с их оригинальными именами. 

- **`https://example.com*1*3*name`**  \
  Скачать указанный диапазон видео из плейлиста с пользовательским именем. \
  Видео будут названы как: 
  - `name - Part 1` 
  - `name - Part 2` 

---

## 🏷️ Система тегов (Теги навигации)

Вы можете добавить теги к любой ссылке (видео, плейлист, аудио) напрямую в вашем сообщении:

- Формат: `https://site.com/link#tag1#tag2#my_tag`
- Теги должны начинаться с `#` и содержать только буквы, цифры, и подчёркивание (`_`).
- Теги автоматически добавляются к описанию видео/аудио, разделённые пробелами.
- Все уникальные теги которые вы отправляете сохраняются в файле `tags.txt` в папке пользователя.

### Пример использования тегов:
```
https://youtu.be/STeeOaX2FBs?si=5rz1QhvuiauZ7A4d#youtube#mytag#tag123
```
Описание видео будет включать:
```
#youtube #mytag #tag123
```

---

### /tags Команда

Команда `/tags` позволяет вам получить список всех ваших уникальных тегов (по одному на строку). Если список длинный, бот отправит несколько сообщений.

**Пример:**
```
/tags
```
Ответ:
```
#youtube
#mytag
#tag123
...
```

---

## 🧹 Авто-очистка пользовательских директорий с Crontab

Чтобы предотвратить заполнение вашего сервера скачанными файлами, вы можете настроить задачу crontab которая запускается каждые 24 часа и удаляет все файлы в пользовательских директориях (кроме `cookie.txt` и `logs.txt`).

Например, добавьте следующую строку в ваш crontab:

```bash
0 0 * * * /usr/bin/find /root/Telegram/tg-ytdlp-bot/users -type f ! -name "cookie.txt" ! -name "logs.txt" -delete
```

**Объяснение:**
- `0 0 * * *` – Выполняет команду каждый день в полночь.
- `/usr/bin/find /CHANGE/ME/TO/REAL/PATH/TO/tg-ytdlp-bot/users -type f` – Ищет все файлы под директорией users.
- `! -name "cookie.txt" ! -name "logs.txt"` – Исключает файлы `cookie.txt` и `logs.txt` из удаления.
- `-delete` – Удаляет найденные файлы.

---

## 🔥 Настройка Firebase для Telegram Bot

Этот раздел описывает как создать Firebase проект, настроить Realtime Database с аутентификацией, создать тестового пользователя, и интегрировать Firebase в ваш Telegram бот.

### 1. Создать Firebase проект

1. Перейдите в [Firebase Console](https://console.firebase.google.com/) и кликните **Add Project** (или выберите существующий проект).
2. Следуйте мастеру настройки чтобы создать ваш новый проект.
3. После создания проекта, перейдите в **Project Settings** и скопируйте ваши параметры конфигурации (такие как `apiKey`, `authDomain`, `databaseURL`, `projectId`, и т.д.). Эти значения требуются для настройки соединения в вашем боте.

### 2. Создать Realtime Database

1. В Firebase Console, выберите **Realtime Database**.
2. Кликните **Create Database**.
3. Выберите локацию вашей базы данных и установите режим. Для начального тестирования, вы можете выбрать **Test Mode** (имейте в виду что тестовый режим не принуждает аутентификацию).
4. Однажды база данных создана, обновите её правила безопасности как описано в шаге 4.

### 3. Включить Authentication

1. В левом меню Firebase Console, выберите **Authentication**.
2. Кликните **Get Started**.
3. Перейдите на вкладку **Sign-in Method** и включите желаемого провайдера. Для базовой настройки, включите **Email/Password**:
   - Кликните на **Email/Password**.
   - Переключите переключатель на **Enable**.
4. После включения метода входа, создайте тестового пользователя вручную во вкладке **Users**, или реализуйте регистрацию пользователя в вашем приложении.

### 4. Обновить правила безопасности Realtime Database

Чтобы ограничить доступ к вашей базе данных только аутентифицированным пользователям, обновите ваши правила безопасности следующим образом:

```json
{
  "rules": {
    // Разрешить доступ только аутентифицированному пользователю с определённым email
    ".read":  "auth != null && auth.token.email === 'YOUREMAIL@gmail.com'",
    ".write": "auth != null && auth.token.email === 'YOUREMAIL@gmail.com'"
  }
}
```

Эти правила разрешают операции чтения и записи только если запрос содержит валидный `idToken`—означает что пользователь аутентифицирован.

### 5. Автостарт сервиса

Чтобы создать сервис автозапуска для этого бота - скопируйте текст из этого файла https://github.com/chelaxian/tg-ytdlp-bot/blob/main/etc/systemd/system/tg-ytdlp-bot.service и вставьте его в
```bash
/etc/systemd/system/tg-ytdlp-bot.service
```
не забудьте изменить путь в сервисе на ваш реальный путь

перезагрузите systemctl и включить/запустить сервис
```bash
systemctl daemon-reexec
systemctl daemon-reload
systemctl enable tg-ytdlp-bot.service
systemctl restart tg-ytdlp-bot.service
journalctl -u tg-ytdlp-bot -f
```

### Автостарт сервиса dashboard

Чтобы автозапустить FastAPI dashboard, скопируйте шаблон `_etc/systemd/system/tg-ytdlp-dashboard.service` в:
```bash
/etc/systemd/system/tg-ytdlp-dashboard.service
```
отредактируйте `WorkingDirectory`, `ExecStart`, и порт согласно вашей настройке.

Перезагрузите systemd и включите unit:
```bash
systemctl daemon-reexec
systemctl daemon-reload
systemctl enable tg-ytdlp-dashboard.service
systemctl restart tg-ytdlp-dashboard.service
journalctl -u tg-ytdlp-dashboard -f
```

Команда по умолчанию запускает `uvicorn web.dashboard_app:app --host 0.0.0.0 --port 5555`; добавьте `--reload` или измените порт если требуется.

---

### /vid range shortcut
- Используйте диапазон перед URL и он будет трансформирован в индексы плейлиста:
  - `/vid 3-7 https://youtube.com/playlist?list=...` → `/vid https://youtube.com/playlist?list=...*3*7`

---

## 🔍 Помощник inline поиска (/search)

Используйте эту команду чтобы быстро активировать inline поиск через `@vid`.

- 📱 Mobile: коснитесь кнопку показанную `/search`. Она открывает ваш чат с пре-заполненым `@vid` и ноль-ширинным пробелом. Добавьте ваш запрос после `@vid`.
- 💻 PC/Desktop: inline deep-linking не может пре-заполнить надёжно. Введите вручную в любом чате:
  - `@vid Ваш_Поисковый_Запрос`

Примечания:
- Desktop Telegram не всегда отправляет `/start` payloads от ссылок повторно; избегайте полагаться на `https://t.me/<bot>?start=...` для inline пре-заполнения.
- Команда `/search` бота показывает только работающие опции и краткую подсказку руководства.

---

## 🚀 Панель статистики (порт 5555)

Мы предоставляем отдельный FastAPI сервис с мульти-табличным UI и REST API который показывает ключевые метрики бота в реальном времени без постоянного попадания в Firebase.

### Как запустить

```bash
pip install -r requirements.txt           # убедитесь что fastapi/uvicorn установлены
./venv/bin/python -m uvicorn web.dashboard_app:app --host 0.0.0.0 --port 5555 --reload
```

После запуска, откройте `http://<your-host>:5555`. Dashboard не запускается автоматически с ботом, поэтому вы можете обернуть эту команду в специализированный systemd unit или Docker сервис.

### Что он показывает

- Active users "right now" (на основе `Config.STATS_ACTIVE_TIMEOUT`), их ссылки, и быстрая блокировка через кнопку ❌.
- Top загрузки по дню/неделе/месяцу/всё время, top страны, пол и возрастные группы (эвристики на основе данных Telegram).
- Популярные домены, NSFW источники, любители плейлистов, и тяжёлые потребители NSFW.
- "Persistent" пользователи которые отправляют ≥10 URL в день в течение 7 дней подряд.
- Лог join/leave канала за последние 48 часов и список заблокированных пользователей с кнопкой ✅ разблокировки.

На каждой вкладке с длинными списками, top‑10 элементов отображаются с кнопкой "Show all".

### Откуда данные берутся

- Базовый снимок читается из локального `dump.json`, который уже обновляется `DATABASE/download_firebase.py`.
- Хуки в `DATABASE/firebase_init.py` и `HELPERS/logger.py`, плюс `StatsAwareDBAdapter` proxy, перехватывают все DB записи и обновляют in‑memory кэш без дополнительных REST вызов.
- Информация о пользователе обогащается через Telegram Bot API (`getChat`) с локальным кэшем, и мгновенные данные берутся напрямую из входящих `message` объектов.

### REST API

UI использует простые JSON endpoints (`/api/active-users`, `/api/top-downloaders`, `/api/block-user`, `/api/channel-events`, и т.д.), поэтому вы можете повторно использовать ту же статистику в внешних инструментах мониторинга, оповещениях, или ботах без рендеринга HTML.

### Конфигурация и использование dashboard

1. **Обновите конфиг.** В `CONFIG/config.py`, установите `DASHBOARD_PORT`, `DASHBOARD_USERNAME`, и `DASHBOARD_PASSWORD`. В Docker вы можете также переопределить их через переменные окружения. Значения читаются при runtime, но обычно вы пересобираете/перезапускаете контейнер или сервис один раз после изменений.
2. **Запустите сервис.** На bare‑metal используйте `./venv/bin/python -m uvicorn web.dashboard_app:app --host 0.0.0.0 --port $DASHBOARD_PORT`. В Docker добавьте отдельный сервис или подключите dashboard в существующий compose файл.
3. **Защитите доступ.** Поставьте dashboard за HTTPS (Nginx/Traefik) и IP allowlist если он открыт в интернет. Для local‑only использования, предпочитайте SSH port forwarding вместо публичного открытия.
4. **Работа в UI.**
   - Вкладка **Active Users** показывает live сессии; кнопка ❌ мгновенно блокирует пользователя.  
   - **Top Downloads / Domains** помогает вам заметить паттерны злоупотреблений.  
   - **Channel Events / Blocked Users** позволяет вам управлять подписками и списком блокировок не касаясь базы данных напрямую.
5. **Отладка.** Если dashboard перестаёт отвечать, проверьте `journalctl -u tg-ytdlp-dashboard -f` (или Docker логи) и убедитесь что `DATABASE/download_firebase.py` всё ещё обновляет `dump.json`.

Добавьте специализированный systemd unit (см. `etc/systemd/system/tg-ytdlp-bot.service` как референс) или Docker healthcheck чтобы dashboard автоматически перезапускался после перезапуска хоста или контейнера.

---

## 🤝 Разработка

Мы приветствуем вклад! Пожалуйста см. наши [Руководства по вкладу](CONTRIBUTING.md) для деталей.

### Настройка разработки

```bash
# Fork и клонировать репозиторий
git clone https://github.com/your-username/tg-ytdlp-bot.git
cd tg-ytdlp-bot

# Создать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Сделать ваши изменения и протестировать
python3 magic.py
```

### Процесс Pull Request

1. Fork репозитория
2. Создайте feature ветку (`git checkout -b feature/amazing-feature`)
3. Commit ваши изменения (`git commit -m 'Add amazing feature'`)
4. Push к ветке (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

---

## 📄 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.

---

## 🙏 Благодарности

- **Оригинальный автор**: [upekshaip](https://github.com/upekshaip)
- **Главный разработчик и участник проекта**: [chelaxian](https://github.com/chelaxian)
- **Администратор Telegram-бота**: [@IIlIlIlIIIlllIIlIIlIllIIllIlIIIl](https://t.me/IIlIlIlIIIlllIIlIIlIllIIllIlIIIl)
- **yt-dlp**: [yt-dlp](https://github.com/yt-dlp/yt-dlp) для извлечения видео
- **gallery-dl**: [gallery-dl](https://github.com/mikf/gallery-dl) для извлечения изображений
- **PyroTGFork**: [PyroTGFork](https://telegramplayground.github.io/pyrogram/) для Telegram API

---

## 💖 Поддержка

Если вы находите этот проект полезным, пожалуйста рассмотрите возможность:

- ⭐ **Поставить звезду** репозиторию
- 🍕 **Купить кофе** для разработчика через [Tribute](https://t.me/tribute/app?startapp=dmPO)
- 🐛 **Сообщить о багах** и предложить новые функции
- 📢 **Поделиться** с другими которые могут найти это полезным

---

**Создано с ❤️ сообществом tg-ytdlp-bot**