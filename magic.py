# Version 4.0.0 # split monolith code into multiple modules
###########################################################
#        GLOBAL IMPORTS
###########################################################

# ГЛОБАЛЬНЫЙ ПАТЧ ДЛЯ ПРЕДОТВРАЩЕНИЯ ОШИБКИ 'name messages is not defined'
try:
    from PATCH.GLOBAL_MESSAGES_PATCH import apply_global_messages_patch
    apply_global_messages_patch()
except Exception as e:
    print(f"⚠️  Global messages patch failed: {e}")
    # Минимальная защита уже встроена в safe_get_messages функции

# ПАТЧ NONE ОТКЛЮЧЕН - ОШИБКА УЖЕ ИСПРАВЛЕНА В КОДЕ
# try:
#     from PATCH.FIX_NONE_COMPARISONS_PATCH import apply_patch
#     apply_patch()
# except Exception as e:
#     print(f"⚠️  None comparisons patch failed: {e}")

# DEBUG ПАТЧИ ОТКЛЮЧЕНЫ - ОШИБКА NONE ИСПРАВЛЕНА
# try:
#     from PATCH.DEBUG_NONE_COMPARISON import apply_debug_none_comparison
#     apply_debug_none_comparison()
# except Exception as e:
#     print(f"⚠️  Debug None comparison failed: {e}")
import glob
try:
    from sdnotify import SystemdNotifier  # optional, used for watchdog
except Exception:
    SystemdNotifier = None
from datetime import datetime, timedelta
import hashlib
import io
import json
import logging
import math
import os
import re
import requests
import shutil
import subprocess
import random
import sys
import threading
import time
import signal
import atexit
from datetime import datetime
from PIL import Image
from types import SimpleNamespace
from typing import Tuple
from urllib.parse import urlparse, parse_qs, urlunparse, unquote, urlencode
import traceback
# removed pyrebase (migrated to firebase_admin)
import tldextract
# from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pyrogram import Client, filters, idle
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup
)
from yt_dlp import YoutubeDL
import yt_dlp

# Config is now imported from CONFIG.config

import chardet
###########################################################
#        MODULE IMPORTS
###########################################################
# CONFIG
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
# from test_config import Config

# HELPERS (только те, что не содержат обработчики)
from HELPERS.app_instance import set_app
from HELPERS.download_status import *
from HELPERS.channel_guard import start_channel_guard, stop_channel_guard
from HELPERS.filesystem_hlp import *
from HELPERS.limitter import *
from HELPERS.limitter import ensure_group_admin
from HELPERS.logger import *
from HELPERS.porn import *
from HELPERS.qualifier import *
from HELPERS.safe_messeger import *

###########################################################
#        APP INITIALIZATION
###########################################################
# Pyrogram App Initialization
app = Client(
    "magic",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Set global app instance BEFORE importing handlers
set_app(app)

# Кэш для username бота (будет заполнен после старта)
_bot_username_cache = None

def _get_bot_username():
    """Получить username текущего бота (с кэшированием)"""
    global _bot_username_cache
    if _bot_username_cache is None:
        try:
            bot_info = app.get_me()
            _bot_username_cache = bot_info.username.lower() if bot_info.username else None
        except Exception:
            # Fallback на Config.BOT_NAME если не удалось получить через API
            bot_name = getattr(Config, 'BOT_NAME', '').strip()
            _bot_username_cache = bot_name.lower().replace('@', '') if bot_name else None
    return _bot_username_cache

def _should_handle_group_command(app, message):
    """
    Проверяет, должен ли бот обрабатывать команду в группе.
    
    Правила:
    - В личных чатах: всегда обрабатывать
    - В группах:
      - Если команда содержит @mention СЛИТНО с командой (например /vid@bot_name) и это не имя текущего бота - НЕ обрабатывать
      - Если команда содержит @mention СЛИТНО с командой и это имя текущего бота - обрабатывать
      - Если команда НЕ содержит @mention СЛИТНО с командой - обрабатывать (любой бот может ответить)
    
    Returns:
        bool: True если команда должна быть обработана, False иначе
    """
    # В личных чатах всегда обрабатываем
    if message.chat.type in (enums.ChatType.PRIVATE, enums.ChatType.BOT):
        return True
    
    # В группах проверяем @mention только для формата /команда@bot_name (слитно)
    if message.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL):
        text = (message.text or "").strip()
        
        # Проверяем наличие @mention СЛИТНО с командой (формат: /vid@bot_name)
        # Используем паттерн, который ищет @mention сразу после команды без пробела
        # Это исключает упоминания в URL (например, https://www.tiktok.com/@user)
        command_mention_pattern = r'^/(\w+)@(\w+)'
        match = re.match(command_mention_pattern, text)
        
        if match:
            # Найдено упоминание слитно с командой
            mentioned_bot = match.group(2).lower()
            bot_username = _get_bot_username()
            
            if bot_username:
                # Проверяем, соответствует ли упоминание текущему боту
                if mentioned_bot == bot_username.lower():
                    # Упоминание текущего бота - обрабатываем
                    return True
                else:
                    # Упоминание другого бота - не обрабатываем
                    return False
            else:
                # Не удалось получить username бота - обрабатываем для совместимости
                return True
        
        # Нет упоминания слитно с командой - любой бот может обработать
        return True
    
    # Для других типов чатов обрабатываем
    return True

# DATABASE (без обработчиков)
from DATABASE.cache_db import *
from DATABASE.download_firebase import *
from DATABASE.firebase_init import *

# URL_PARSERS (без обработчиков)
from URL_PARSERS.embedder import *
from URL_PARSERS.nocookie import *
from URL_PARSERS.normalizer import *
from URL_PARSERS.tags import *
from URL_PARSERS.tiktok import *
from URL_PARSERS.url_extractor import *
from URL_PARSERS.video_extractor import *
from URL_PARSERS.youtube import *

# DOWN_AND_UP (без обработчиков)
from DOWN_AND_UP.down_and_audio import *
from DOWN_AND_UP.down_and_up import *
from DOWN_AND_UP.ffmpeg import *
from DOWN_AND_UP.sender import *
from DOWN_AND_UP.yt_dlp_hook import *

# HELPERS (с обработчиками - импортируем после установки app)
from HELPERS.caption import *

# COMMANDS (импортируем после установки app)
from COMMANDS.admin_cmd import *
from COMMANDS.clean_cmd import *
from COMMANDS.cookies_cmd import *
from COMMANDS.format_cmd import *
from COMMANDS.link_cmd import *
from COMMANDS.mediainfo_cmd import *
from COMMANDS.other_handlers import *
from COMMANDS.proxy_cmd import *
from COMMANDS.settings_cmd import *
from COMMANDS.split_sizer import *
from COMMANDS.subtitles_cmd import *
from COMMANDS.tag_cmd import *
# Register handlers via their own modules' decorators only (avoid global catch-all)
from COMMANDS.proxy_cmd import proxy_command
from COMMANDS.cookies_cmd import download_cookie

# DOWN_AND_UP (с обработчиками - импортируем после установки app)
from DOWN_AND_UP.always_ask_menu import *

# Инициализируем глобальную переменную messages
messages = safe_get_messages(None)

print(messages.MAGIC_ALL_MODULES_LOADED_MSG)

###########################################################
#        BOT KEYBOARD
###########################################################
# Import decorators from HELPERS
from HELPERS.decorators import reply_with_keyboard, get_main_reply_keyboard, send_reply_keyboard_always

###########################################################
#        GROUP HANDLERS FOR ALLOWED GROUPS
###########################################################
from COMMANDS.image_cmd import image_command
from COMMANDS.mediainfo_cmd import mediainfo_command
from COMMANDS.nsfw_cmd import nsfw_command
from COMMANDS.settings_cmd import settings_command
from COMMANDS.format_cmd import set_format
from COMMANDS.split_sizer import split_command
from COMMANDS.other_handlers import link_command_handler
from COMMANDS.other_handlers import audio_command_handler, playlist_command
from COMMANDS.tag_cmd import tags_command
from URL_PARSERS.url_extractor import url_distractor
from COMMANDS.subtitles_cmd import subs_command
from COMMANDS import args_cmd
from COMMANDS.list_cmd import list_command
from COMMANDS.cookies_cmd import cookies_from_browser

def _wrap_group(fn):
    def _inner(app, message):
        if not ensure_group_admin(app, message):
            return
        return fn(app, message)
    return _inner

# Register group equivalents where applicable
_allowed_groups = tuple(getattr(Config, 'ALLOWED_GROUP', []))

def _is_allowed_group(message):
    messages = safe_get_messages(None)
    try:
        gid = int(getattr(message.chat, 'id', 0))
        allowed = gid in _allowed_groups
        try:
            # Explicit log once per check
            from HELPERS.logger import logger
            logger.info(messages.MAGIC_ALLOWED_GROUP_CHECK_LOG_MSG.format(chat_id=gid, allowed=allowed, list=list(_allowed_groups)))
        except Exception:
            pass
        return allowed
    except Exception:
        return False

if _allowed_groups:
    app.on_message(filters.group & filters.command("img"))(_wrap_group(lambda a, m: image_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("mediainfo"))(_wrap_group(lambda a, m: mediainfo_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("nsfw"))(_wrap_group(lambda a, m: nsfw_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("proxy"))(_wrap_group(lambda a, m: proxy_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("settings"))(_wrap_group(lambda a, m: settings_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("format"))(_wrap_group(lambda a, m: set_format(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("split"))(_wrap_group(lambda a, m: split_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("link"))(_wrap_group(lambda a, m: link_command_handler(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("tags"))(_wrap_group(lambda a, m: tags_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("audio"))(_wrap_group(lambda a, m: audio_command_handler(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("playlist"))(_wrap_group(lambda a, m: playlist_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("subs"))(_wrap_group(lambda a, m: subs_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("args"))(_wrap_group(lambda a, m: args_cmd.args_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("list"))(_wrap_group(lambda a, m: list_command(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))
    app.on_message(filters.group & filters.command("cookies_from_browser"))(_wrap_group(lambda a, m: cookies_from_browser(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))

    # Text/url handler in allowed groups (topic-aware)
    # Text/url handler in allowed groups (topic-aware) including mentions
    def _guarded_text(a, m):
        if not _is_allowed_group(m):
            return None
        
        # Проверяем, является ли сообщение командой
        text = (m.text or "").strip()
        is_command = text.startswith('/') or text in [
            "🧹", "🍪", "⚙️", "🔍", "🌐", "🔗", "📼", "📊", "✂️", "🎧", "💬", 
            "#️⃣", "🆘", "📃", "⏯️", "🎹", "🌎", "✅", "🖼", "🧰", "🔞", "🧾"
        ]
        
        # Для команд проверяем @mention, для обычных текстов - всегда обрабатываем
        if is_command:
            if not _should_handle_group_command(a, m):
                return None
        
        return url_distractor(a, m)
    app.on_message(filters.group & filters.text)(_wrap_group(_guarded_text))

    # Map basic commands to url_distractor to mimic private behavior
    for _cmd in ("start", "help", "keyboard", "clean", "search", "usage", "check_cookie", "save_as_cookie"):
        app.on_message(filters.group & filters.command(_cmd))(_wrap_group(lambda a, m, __c=_cmd: url_distractor(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))

###########################################################
#        /vid command (private and groups)
###########################################################
def _vid_handler(app, message):
    messages = safe_get_messages(message.chat.id)
    # Transform "/vid [url]" into plain URL text for url_distractor
    try:
        txt = (message.text or "").strip()
        parts = txt.split()
        url = ""
        # Support syntax: /vid 1-10 https://...  -> append *1*10 to URL (поддерживаем отрицательные числа)
        # Если первое число с минусом, то добавляем минус и ко второму числу: /vid -1-7 URL -> URL*-1*-7
        if len(parts) >= 3 and re.match(r"^-?\d+-\d*$", parts[1]):
            rng = parts[1]
            url = " ".join(parts[2:])
            # Парсим диапазон: если начинается с минуса, оба числа отрицательные
            if rng.startswith("-"):
                # Формат: -1-7 -> *-1*-7
                # Находим второе число после первого минуса
                match = re.match(r"^-(\d+)-(\d*)$", rng)
                if match:
                    first_num = f"-{match.group(1)}"
                    second_num = f"-{match.group(2)}" if match.group(2) else None
                    if url:
                        if second_num:
                            url = f"{url}*{first_num}*{second_num}"
                        else:
                            url = f"{url}*{first_num}*"
                else:
                    # Fallback: обычный парсинг
                    a, b = rng.split("-", 1)
                    if b != "":
                        b = f"-{b}"
                    if url:
                        url = f"{url}*{a}*{b}" if b else f"{url}*{a}*"
            else:
                # Обычный формат: 1-7 -> *1*7
                a, b = rng.split("-", 1)
                b = b if b != "" else None
                if url:
                    url = f"{url}*{a}*{b}" if b is not None else f"{url}*{a}*"
            if url:
                logger.info(f"🔍 [DEBUG] Преобразовано /vid команда: '{message.text}' -> '{url}'")
        else:
            # Fallback: /vid URL
            url = parts[1] if len(parts) > 1 else ""
        # Remove @bot mention if present in command
        if url.startswith("@"):  # case of "/vid @bot url"
            url = " ".join(url.split()[1:])
        if url:
            # Reuse original message for thread/reply context
            message.text = url
            return url_distractor(app, message)
        else:
            from HELPERS.safe_messeger import safe_send_message
            from pyrogram import enums
            from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
            kb = InlineKeyboardMarkup([[InlineKeyboardButton(messages.URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG, callback_data="vid_help|close")]])
            help_text = (
                messages.MAGIC_VID_HELP_TITLE_MSG +
                messages.MAGIC_VID_HELP_USAGE_MSG +
                messages.MAGIC_VID_HELP_EXAMPLES_MSG +
                messages.MAGIC_VID_HELP_EXAMPLE_1_MSG +
                messages.MAGIC_VID_HELP_EXAMPLE_2_MSG +
                messages.MAGIC_VID_HELP_EXAMPLE_3_MSG +
                messages.MAGIC_VID_HELP_ALSO_SEE_MSG
            )
            safe_send_message(message.chat.id, help_text, parse_mode=enums.ParseMode.HTML, reply_markup=kb, message=message)
    except Exception:
        from HELPERS.safe_messeger import safe_send_message
        from pyrogram import enums
        from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
        kb = InlineKeyboardMarkup([[InlineKeyboardButton(messages.URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG, callback_data="vid_help|close")]])
        help_text = (
            messages.MAGIC_VID_HELP_TITLE_MSG +
            messages.MAGIC_VID_HELP_USAGE_MSG +
            messages.MAGIC_VID_HELP_EXAMPLES_MSG +
            messages.MAGIC_VID_HELP_EXAMPLE_1_MSG +
            messages.MAGIC_VID_HELP_EXAMPLE_2_MSG +
            messages.MAGIC_VID_HELP_EXAMPLE_3_MSG +
            messages.MAGIC_VID_HELP_ALSO_SEE_MSG
        )
        safe_send_message(message.chat.id, help_text, parse_mode=enums.ParseMode.HTML, reply_markup=kb, message=message)

# Register /vid in private and allowed groups
app.on_message(filters.command("vid") & filters.private)(_vid_handler)
if _allowed_groups:
    app.on_message(filters.group & filters.command("vid"))(_wrap_group(lambda a, m: _vid_handler(a, m) if _is_allowed_group(m) and _should_handle_group_command(a, m) else None))

# Help close handler for /vid
@app.on_callback_query(filters.regex(r"^vid_help\|"))
def vid_help_callback(app, callback_query):
    messages = safe_get_messages(None)
    data = callback_query.data.split("|")[1]
    if data == "close":
        try:
            callback_query.message.delete()
        except Exception:
            try:
                callback_query.edit_message_reply_markup(reply_markup=None)
            except Exception:
                pass
        try:
            callback_query.answer(messages.MAGIC_HELP_CLOSED_MSG)
        except Exception:
            pass
        return

###########################################################
#        APP STARTS
###########################################################
# ###############################################################################################
# Global starting point list (do not modify)
starting_point = []

# ###############################################################################################

# Run the automatic loading of the Firebase cache (only if Firebase is enabled)
use_firebase = getattr(Config, 'USE_FIREBASE', True)
if use_firebase:
    start_auto_cache_reloader()
else:
    print("ℹ️ Автоматическая перезагрузка кэша отключена (локальный режим)")

def cleanup_on_exit():
    messages = safe_get_messages(None)
    """Cleanup function to close Firebase connections, HTTP sessions and logger on exit"""
    try:
        # Close all HTTP sessions first
        try:
            from HELPERS.http_manager import close_all_sessions
            close_all_sessions()
            print("✅ HTTP sessions closed")
        except Exception as e:
            print(f"⚠️ Error closing HTTP sessions: {e}")
        
        # Close Firebase connections
        from DATABASE.cache_db import close_all_firebase_connections
        close_all_firebase_connections()
        
        # Close logger handlers
        try:
            from HELPERS.logger import close_logger
            close_logger()
        except Exception as e:
            print(messages.MAGIC_ERROR_CLOSING_LOGGER_MSG.format(error=e))
        
        print(messages.MAGIC_CLEANUP_COMPLETED_MSG)
    except Exception as e:
        print(messages.MAGIC_ERROR_DURING_CLEANUP_MSG.format(error=e))

# Register cleanup function 
atexit.register(cleanup_on_exit)

# Register signal handlers for graceful shutdown
def signal_handler(sig, frame):
    messages = safe_get_messages(None)
    """Handle shutdown signals gracefully"""
    print(messages.MAGIC_SIGNAL_RECEIVED_MSG.format(signal=sig))
    cleanup_on_exit()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def _is_running_in_docker():
    """Проверяет, запущен ли текущий процесс внутри Docker контейнера."""
    from pathlib import Path
    # Проверяем наличие .dockerenv файла
    if Path("/.dockerenv").exists():
        return True
    # Проверяем cgroup (более надежный способ)
    try:
        with open("/proc/self/cgroup", "r") as f:
            content = f.read()
            # Если находимся в Docker, в cgroup будет упоминание docker
            if "docker" in content or "/docker/" in content:
                return True
    except Exception:
        pass
    return False

def run_with_auto_reconnect():
    """
    Запускает бота с автоматическим переподключением при сетевых ошибках.
    Используется только в Docker для обработки перезапуска сетевого стека (warp).
    """
    from HELPERS.logger import logger
    import time
    import threading
    
    max_reconnect_attempts = 50  # Больше попыток для Docker
    reconnect_delay = 3  # секунд между попытками
    connection_check_interval = 30  # Проверяем соединение каждые 30 секунд
    
    attempt = 0
    _should_reconnect = False
    _reconnect_lock = threading.Lock()
    
    def check_connection_periodically():
        """Периодически проверяет соединение и устанавливает флаг переподключения при проблемах"""
        nonlocal _should_reconnect
        while True:
            time.sleep(connection_check_interval)
            try:
                # Проверяем, что клиент запущен и соединение активно
                if app.is_connected:
                    try:
                        # Простая проверка - пытаемся получить информацию о себе
                        app.get_me()
                    except Exception as e:
                        error_str = str(e).lower()
                        if any(keyword in error_str for keyword in ['timeout', 'connection', 'network', 'disconnected', 'unable to connect']):
                            logger.warning(f"Connection check failed: {e}")
                            with _reconnect_lock:
                                _should_reconnect = True
                else:
                    logger.warning("Client is not connected")
                    with _reconnect_lock:
                        _should_reconnect = True
            except Exception as e:
                logger.warning(f"Error during connection check: {e}")
                with _reconnect_lock:
                    _should_reconnect = True
    
    while attempt < max_reconnect_attempts:
        try:
            with _reconnect_lock:
                _should_reconnect = False
            
            logger.info(f"Starting bot (attempt {attempt + 1}/{max_reconnect_attempts})...")
            app.start()
            start_channel_guard(app)
            logger.info("Bot started successfully, entering idle mode...")
            
            # Запускаем поток для периодической проверки соединения
            check_thread = threading.Thread(target=check_connection_periodically, daemon=True)
            check_thread.start()
            
            # Запускаем idle - он будет работать до KeyboardInterrupt
            try:
                idle()
            except KeyboardInterrupt:
                logger.info("Received KeyboardInterrupt, shutting down...")
                break
            
            # Проверяем, нужен ли переподключение
            with _reconnect_lock:
                if _should_reconnect:
                    logger.warning("Reconnection needed, stopping current session...")
                    attempt += 1
                    
                    # Останавливаем клиент перед переподключением
                    try:
                        app.loop.run_until_complete(stop_channel_guard())
                    except Exception:
                        pass
                    try:
                        app.stop()
                    except Exception:
                        pass
                    
                    logger.info(f"Waiting {reconnect_delay} seconds before reconnecting...")
                    time.sleep(reconnect_delay)
                    continue
            
            # Если idle завершился нормально (не из-за переподключения)
            break
            
        except KeyboardInterrupt:
            logger.info("Received KeyboardInterrupt, shutting down...")
            break
        except Exception as e:
            error_str = str(e).lower()
            if any(keyword in error_str for keyword in ['timeout', 'connection', 'network', 'disconnected', 'unable to connect']):
                logger.warning(f"Network error detected: {e}")
                attempt += 1
                if attempt < max_reconnect_attempts:
                    logger.info(f"Attempting to reconnect in {reconnect_delay} seconds...")
                    try:
                        app.loop.run_until_complete(stop_channel_guard())
                    except Exception:
                        pass
                    try:
                        app.stop()
                    except Exception:
                        pass
                    time.sleep(reconnect_delay)
                    continue
                else:
                    logger.error("Max reconnect attempts reached, exiting...")
                    raise
            else:
                # Не сетевая ошибка - пробрасываем дальше
                logger.error(f"Unexpected error: {e}")
                raise
        finally:
            try:
                app.loop.run_until_complete(stop_channel_guard())
            except Exception:
                pass
            try:
                app.stop()
            except Exception:
                pass

if __name__ == "__main__":
    # В Docker используем автоматическое переподключение, локально - обычный запуск
    if _is_running_in_docker():
        run_with_auto_reconnect()
    else:
        app.start()
        start_channel_guard(app)
        idle()
        try:
            app.loop.run_until_complete(stop_channel_guard())
        except Exception:
            pass
        app.stop()
