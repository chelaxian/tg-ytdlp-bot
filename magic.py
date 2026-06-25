# Version 4.0.1 # refactored magic.py: eliminated wildcard imports, DRY group handlers,
#   extracted _send_vid_help, simplified _should_handle_group_command, removed dead imports
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

try:
    from sdnotify import SystemdNotifier  # optional, used for watchdog
except Exception:
    SystemdNotifier = None
from datetime import datetime, timedelta
import logging
import os
import re
import sys
import signal
import atexit
import time
import threading

from pyrogram import Client, filters, idle
from pyrogram import enums
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

###########################################################
#        MODULE IMPORTS
###########################################################
# CONFIG
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages

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
            bot_name = getattr(Config, 'BOT_NAME', '').strip()
            _bot_username_cache = bot_name.lower().replace('@', '') if bot_name else None
    return _bot_username_cache


def _should_handle_group_command(message):
    """
    Проверяет, должен ли бот обрабатывать команду в группе.

    В личных чатах всегда True. В группах — проверяет @mention слитно
    с командой: если упомянут другой бот, возвращает False.
    """
    if message.chat.type in (enums.ChatType.PRIVATE, enums.ChatType.BOT):
        return True

    text = (message.text or "").strip()
    match = re.match(r'^/(\w+)@(\w+)', text)
    if not match:
        return True

    mentioned_bot = match.group(2).lower()
    bot_username = _get_bot_username()
    if not bot_username:
        return True

    return mentioned_bot == bot_username.lower()


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
from COMMANDS.dubs_cmd import *
from COMMANDS.tag_cmd import *
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
from HELPERS.decorators import reply_with_keyboard, get_main_reply_keyboard

###########################################################
#        GROUP HANDLERS FOR ALLOWED GROUPS
###########################################################
from COMMANDS.image_cmd import image_command
from COMMANDS.mediainfo_cmd import mediainfo_command
from COMMANDS.nsfw_cmd import nsfw_command
from COMMANDS.settings_cmd import settings_command
from COMMANDS.format_cmd import set_format
from COMMANDS.split_sizer import split_command
from COMMANDS.other_handlers import link_command_handler, audio_command_handler, playlist_command
from COMMANDS.tag_cmd import tags_command
from URL_PARSERS.url_extractor import url_distractor
from COMMANDS.subtitles_cmd import subs_command
from COMMANDS.dubs_cmd import dubs_command
from COMMANDS import args_cmd
from COMMANDS.list_cmd import list_command
from COMMANDS.cookies_cmd import cookies_from_browser


def _wrap_group(fn):
    """Обёртка для групповых обработчиков: проверяет права админа бота."""
    def _inner(app, message):
        if not ensure_group_admin(app, message):
            return
        return fn(app, message)
    return _inner


# Register group equivalents where applicable
_allowed_groups = tuple(getattr(Config, 'ALLOWED_GROUP', []))


def _is_allowed_group(message):
    """Проверяет, входит ли chat_id сообщения в список разрешённых групп."""
    _messages = safe_get_messages(None)
    try:
        gid = int(getattr(message.chat, 'id', 0))
        allowed = gid in _allowed_groups
        try:
            from HELPERS.logger import logger
            logger.info(_messages.MAGIC_ALLOWED_GROUP_CHECK_LOG_MSG.format(
                chat_id=gid, allowed=allowed, list=list(_allowed_groups)))
        except Exception:
            pass
        return allowed
    except Exception:
        return False


def _register_group_command(command_name, handler_fn):
    """Регистрирует обработчик команды для групп с проверкой разрешённых групп и @mention."""
    app.on_message(filters.group & filters.command(command_name))(
        _wrap_group(lambda a, m: handler_fn(a, m)
                     if _is_allowed_group(m) and _should_handle_group_command(m)
                     else None)
    )


if _allowed_groups:
    # Маппинг команд -> обработчиков для групп
    _group_command_map = {
        "img": image_command,
        "mediainfo": mediainfo_command,
        "nsfw": nsfw_command,
        "proxy": proxy_command,
        "settings": settings_command,
        "format": set_format,
        "split": split_command,
        "link": link_command_handler,
        "tags": tags_command,
        "audio": audio_command_handler,
        "playlist": playlist_command,
        "subs": subs_command,
        "dubs": dubs_command,
        "args": args_cmd.args_command,
        "list": list_command,
        "cookies_from_browser": cookies_from_browser,
    }

    for _cmd_name, _handler in _group_command_map.items():
        _register_group_command(_cmd_name, _handler)

    # Text/url handler in allowed groups (topic-aware) including mentions
    def _guarded_text(a, m):
        if not _is_allowed_group(m):
            return None

        text = (m.text or "").strip()
        _emoji_commands = {
            "🧹", "🍪", "⚙️", "🔍", "🌐", "🔗", "📼", "📊", "✂️", "🎧", "💬",
            "#️⃣", "🆘", "📃", "⏯️", "🎹", "🌎", "✅", "🖼", "🧰", "🔞", "🧾",
        }
        is_command = text.startswith('/') or text in _emoji_commands

        if is_command and not _should_handle_group_command(m):
            return None

        return url_distractor(a, m)

    app.on_message(filters.group & filters.text)(_wrap_group(_guarded_text))

    # Map basic commands to url_distractor to mimic private behavior
    for _cmd in ("start", "help", "keyboard", "clean", "search", "usage", "check_cookie", "save_as_cookie"):
        _register_group_command(_cmd, url_distractor)

###########################################################
#        /vid command (private and groups)
###########################################################

def _send_vid_help(chat_id, vid_messages, message=None):
    """Отправляет help-сообщение для команды /vid."""
    from HELPERS.safe_messeger import safe_send_message
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            vid_messages.URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG,
            callback_data="vid_help|close"
        )
    ]])
    help_text = (
        vid_messages.MAGIC_VID_HELP_TITLE_MSG
        + vid_messages.MAGIC_VID_HELP_USAGE_MSG
        + vid_messages.MAGIC_VID_HELP_EXAMPLES_MSG
        + vid_messages.MAGIC_VID_HELP_EXAMPLE_1_MSG
        + vid_messages.MAGIC_VID_HELP_EXAMPLE_2_MSG
        + vid_messages.MAGIC_VID_HELP_EXAMPLE_3_MSG
        + vid_messages.MAGIC_VID_HELP_ALSO_SEE_MSG
    )
    safe_send_message(
        chat_id, help_text,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=kb,
        message=message,
    )


def _vid_handler(app, message):
    """Обработчик команды /vid: преобразует '/vid [диапазон] URL' и передаёт в url_distractor."""
    _messages = safe_get_messages(message.chat.id)
    try:
        txt = (message.text or "").strip()
        parts = txt.split()
        url = ""

        # /vid 1-10 https://... -> URL*1*10  (поддерживаем отрицательные числа)
        if len(parts) >= 3 and re.match(r"^-?\d+-\d*$", parts[1]):
            rng = parts[1]
            url = " ".join(parts[2:])

            if rng.startswith("-"):
                match = re.match(r"^-(\d+)-(\d*)$", rng)
                if match:
                    first_num = f"-{match.group(1)}"
                    second_num = f"-{match.group(2)}" if match.group(2) else None
                    if url:
                        url = f"{url}*{first_num}*{second_num}" if second_num else f"{url}*{first_num}*"
                else:
                    a, b = rng.split("-", 1)
                    if b:
                        b = f"-{b}"
                    if url:
                        url = f"{url}*{a}*{b}" if b else f"{url}*{a}*"
            else:
                a, b = rng.split("-", 1)
                b = b if b else None
                if url:
                    url = f"{url}*{a}*{b}" if b is not None else f"{url}*{a}*"

            if url:
                logger.info(f"🔍 [DEBUG] Преобразовано /vid команда: '{message.text}' -> '{url}'")
        else:
            url = parts[1] if len(parts) > 1 else ""

        # Remove @bot mention if present in command (/vid @bot url)
        if url.startswith("@"):
            url = " ".join(url.split()[1:])

        if url:
            message.text = url
            return url_distractor(app, message)

        _send_vid_help(message.chat.id, _messages, message=message)

    except Exception:
        _send_vid_help(message.chat.id, _messages, message=message)


# Register /vid in private and allowed groups
app.on_message(filters.command("vid") & filters.private)(_vid_handler)
if _allowed_groups:
    _register_group_command("vid", _vid_handler)

# Help close handler for /vid
@app.on_callback_query(filters.regex(r"^vid_help\|"))
def vid_help_callback(app, callback_query):
    _messages = safe_get_messages(None)
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
            callback_query.answer(_messages.MAGIC_HELP_CLOSED_MSG)
        except Exception:
            pass
        return

###########################################################
#        APP STARTS
###########################################################
# Global starting point list (do not modify)
starting_point = []

# Run the automatic loading of the Firebase cache (only if Firebase is enabled)
use_firebase = getattr(Config, 'USE_FIREBASE', True)
if use_firebase:
    start_auto_cache_reloader()
else:
    print("ℹ️ Автоматическая перезагрузка кэша отключена (локальный режим)")


def cleanup_on_exit():
    """Cleanup function to close Firebase connections, HTTP sessions and logger on exit"""
    _messages = safe_get_messages(None)
    try:
        try:
            from HELPERS.http_manager import close_all_sessions
            close_all_sessions()
            print("✅ HTTP sessions closed")
        except Exception as e:
            print(f"⚠️ Error closing HTTP sessions: {e}")

        from DATABASE.cache_db import close_all_firebase_connections
        close_all_firebase_connections()

        try:
            from HELPERS.logger import close_logger
            close_logger()
        except Exception as e:
            print(_messages.MAGIC_ERROR_CLOSING_LOGGER_MSG.format(error=e))

        print(_messages.MAGIC_CLEANUP_COMPLETED_MSG)
    except Exception as e:
        print(_messages.MAGIC_ERROR_DURING_CLEANUP_MSG.format(error=e))


# Register cleanup function
atexit.register(cleanup_on_exit)

# Register signal handlers for graceful shutdown
def signal_handler(sig, frame):
    """Handle shutdown signals gracefully"""
    _messages = safe_get_messages(None)
    print(_messages.MAGIC_SIGNAL_RECEIVED_MSG.format(signal=sig))
    cleanup_on_exit()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    app.start()
    start_channel_guard(app)
    idle()
    try:
        app.loop.run_until_complete(stop_channel_guard())
    except Exception:
        pass
    app.stop()
