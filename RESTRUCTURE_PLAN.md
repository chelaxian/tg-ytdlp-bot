# 🏗️ Code Restructuring Plan

## ✅ Completed Modules

### 📁 magic/utils/
- ✅ `formatters.py` - Функции форматирования (humanbytes, TimeFormatter, truncate_caption, sanitize_filename)
- ✅ `filesystem.py` - Работа с файловой системой (create_directory, cleanup, remove_media, active downloads tracking)

### 📁 magic/database/
- ✅ `firebase.py` - Работа с Firebase (AuthedDB, token_refresher, user checking, logging)

### 📁 magic/processing/
- ✅ `tags.py` - Система тегов (extract_url_range_tags, auto-tagging, porn detection)

### 📁 magic/download/
- ✅ `cache.py` - Система кэширования (video/playlist cache, normalize URLs)

### 📁 magic/user/
- ✅ `settings.py` - Пользовательские настройки (quality, split size, mediainfo, etc.)

## 🔄 Remaining Modules to Create

### 📁 magic/processing/
- ⏳ `url_parser.py` - URL processing functions:
  - `extract_real_url_if_google()`
  - `is_youtube_url()`, `youtube_to_short_url()`, `youtube_to_long_url()`
  - `strip_range_from_url()`
  - `get_domain_from_url()`

- ⏳ `video.py` - Video processing:
  - `split_video_2()`
  - `get_duration_thumb()`
  - `get_video_resolution()`

### 📁 magic/download/
- ⏳ `core.py` - Main download functions:
  - `down_and_up()` - основная функция загрузки
  - `down_and_audio()` - загрузка аудио
  - `send_videos()` - отправка видео

- ⏳ `quality.py` - Quality management:
  - `get_quality_from_info()`
  - `ceil_to_popular()`
  - Quality mapping functions

### 📁 magic/handlers/
- ⏳ `commands.py` - Command handlers:
  - `/start`, `/help`, `/settings`, `/playlist_help`
  - `/save_as_cookie`, `/remove`
  - `/stats`, `/clear_cache`

- ⏳ `messages.py` - Message handlers:
  - URL message processing
  - Error handling
  - Progress updates

- ⏳ `callbacks.py` - Callback query handlers:
  - Quality selection callbacks
  - Settings callbacks
  - Navigation callbacks

### 📁 magic/user/
- ⏳ `management.py` - User management:
  - User blocking/unblocking
  - Admin functions
  - User statistics

## 🔧 Main magic.py Structure

После реструктуризации главный файл `magic.py` будет содержать только:

```python
# Imports
import pyrogram
from pyrogram import Client, filters
from config import Config
from magic.database.firebase import *
from magic.handlers.commands import *
from magic.handlers.messages import *
from magic.handlers.callbacks import *

# Bot initialization
app = Client(...)
db = ...

# Pyrogram handlers registration
@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Import and call from handlers.commands
    pass

@app.on_message(filters.text & ~filters.command(...))
async def handle_url_message(client, message):
    # Import and call from handlers.messages
    pass

# Main run
if __name__ == "__main__":
    app.run()
```

## 📋 Migration Steps

### 1. Create URL Parser Module
```bash
# Move URL processing functions to magic/processing/url_parser.py
```

### 2. Create Video Processing Module
```bash
# Move video processing functions to magic/processing/video.py
```

### 3. Create Download Core Module
```bash
# Move main download functions to magic/download/core.py
```

### 4. Create Quality Management Module
```bash
# Move quality functions to magic/download/quality.py
```

### 5. Create Handler Modules
```bash
# Move Pyrogram handlers to magic/handlers/
```

### 6. Update Imports
```bash
# Update all imports in remaining code
```

### 7. Refactor main magic.py
```bash
# Keep only bot initialization and handler registration
```

## 🔗 Import Structure

### Example imports after restructuring:
```python
# In magic.py
from magic.database.firebase import AuthedDB, check_user, is_user_blocked
from magic.download.core import down_and_up, down_and_audio
from magic.download.cache import get_cached_message_ids, save_to_video_cache
from magic.processing.tags import extract_url_range_tags, generate_final_tags
from magic.processing.url_parser import is_youtube_url, extract_real_url_if_google
from magic.user.settings import get_user_quality, format_settings_text
from magic.utils.formatters import humanbytes, TimeFormatter
from magic.utils.filesystem import create_directory, cleanup_temp_files
```

## 💡 Benefits After Restructuring

- ✅ **Модульность** - код разделен по логическим группам
- ✅ **Читаемость** - легче найти нужную функцию
- ✅ **Поддержка** - проще исправлять и добавлять новые функции
- ✅ **Тестирование** - можно тестировать модули отдельно
- ✅ **Масштабируемость** - легче добавлять новые платформы
- ✅ **Производительность** - загружаются только нужные модули

## 🚀 Next Steps

1. Создать оставшиеся модули из списка выше
2. Перенести функции из magic.py в соответствующие модули
3. Обновить все импорты
4. Протестировать каждый модуль
5. Рефакторить главный magic.py файл

## ⚠️ Important Notes

- Сохранить обратную совместимость
- Тщательно протестировать каждый перенесенный модуль
- Обновить документацию и комментарии
- Убедиться что все импорты работают корректно 