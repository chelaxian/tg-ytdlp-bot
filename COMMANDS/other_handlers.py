# #############################################################################################################################

import os
import re
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyParameters
from HELPERS.safe_messeger import safe_send_message

from HELPERS.app_instance import get_app
from HELPERS.decorators import background_handler
from HELPERS.logger import send_to_logger, send_to_user
from HELPERS.limitter import is_user_in_channel, check_user, check_playlist_range_limits
from HELPERS.download_status import get_active_download, can_start_download
from HELPERS.filesystem_hlp import create_directory

from CONFIG.config import Config
from CONFIG.messages import safe_get_messages

from URL_PARSERS.tags import extract_url_range_tags, save_user_tags

from DOWN_AND_UP.down_and_audio import down_and_audio
from COMMANDS.link_cmd import link_command
from COMMANDS.proxy_cmd import proxy_command

# Get app instance for decorators
app = get_app()


def _check_access(message, *, require_channel: bool = True) -> bool:
    """Common access check for private-chat command handlers.
    
    Returns True if the user is allowed to proceed, False if a guard
    already sent a response or the user should be silently dropped.
    """
    user_id = message.chat.id
    is_admin = int(user_id) in Config.ADMIN
    text = getattr(message, 'text', '').strip() if hasattr(message, 'text') else ''
    is_ignore_command = text.startswith(Config.IGNORE_USER_COMMAND) or text.startswith(Config.UNIGNORE_USER_COMMAND)

    if not is_ignore_command:
        from DATABASE.firebase_init import is_user_ignored
        if is_user_ignored(message):
            return False

    if not is_admin:
        from DATABASE.firebase_init import is_user_blocked
        if is_user_blocked(message):
            return False

    if require_channel and not is_admin and not is_user_in_channel(app, message):
        return False

    return True


def _close_callback(callback_query, answer_msg_key: str, log_msg_key: str) -> None:
    """Handle a generic 'close' callback: delete message (or clear markup), answer, and log."""
    user_id = callback_query.from_user.id
    _messages = safe_get_messages(user_id)
    try:
        callback_query.message.delete()
    except Exception:
        callback_query.edit_message_reply_markup(reply_markup=None)
    callback_query.answer(getattr(_messages, answer_msg_key, ""))
    send_to_logger(callback_query.message, getattr(_messages, log_msg_key, ""))


# Keep only the callback handler for help close button
@app.on_callback_query(filters.regex(r"^help_msg\|"))
def help_msg_callback(app, callback_query):
    data = callback_query.data.split("|")[1]
    if data == "close":
        _close_callback(callback_query, "OTHER_HELP_CLOSED_MSG", "HELP_MESSAGE_CLOSED_LOG_MSG")


#############################################################################################################################

# Command to Download Audio from a Video url
@app.on_message(filters.command("audio") & filters.private)
@background_handler(label="audio_command")
def audio_command_handler(app, message):
    user_id = message.chat.id
    is_admin = int(user_id) in Config.ADMIN

    if not _check_access(message):
        return

    if not can_start_download(user_id):
        safe_send_message(user_id, safe_get_messages(user_id).AUDIO_WAIT_MSG, reply_parameters=ReplyParameters(message_id=message.id))
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    text = message.text
    # Нормализация синтаксиса диапазона: 
    # поддержка «/audio 1-10 URL» → преобразуем во «/audio URL*1*10» для единого пайплайна
    try:
        parts = (text or '').split()
        if len(parts) >= 3 and parts[0].lower().startswith('/audio'):
            if re.match(r"^\d+-\d*$", parts[1]):
                rng = parts[1]
                start_str, end_str = rng.split('-')
                start_val = int(start_str)
                end_val = int(end_str) if end_str != '' else None
                if start_val and start_val >= 1:
                    url_candidate = ' '.join(parts[2:]).strip()
                    if end_val is not None:
                        text = f"/audio {url_candidate}*{start_val}*{end_val}"
                    else:
                        text = f"/audio {url_candidate}*{start_val}*"
    except Exception:
        pass
    url, _, _, _, tags, tags_text, tag_error = extract_url_range_tags(text)
    if tag_error:
        wrong, example = tag_error
        error_msg = safe_get_messages(user_id).OTHER_TAG_ERROR_MSG.format(wrong=wrong, example=example)
        safe_send_message(user_id, error_msg, reply_parameters=ReplyParameters(message_id=message.id))
        from HELPERS.logger import log_error_to_channel
        log_error_to_channel(message, error_msg)
        return
    if not url:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(safe_get_messages(user_id).OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG, callback_data="audio_hint|close")]
        ])
        safe_send_message(
            user_id,
            safe_get_messages(user_id).AUDIO_HELP_MSG,
            parse_mode=enums.ParseMode.HTML,
            reply_parameters=ReplyParameters(message_id=message.id),
            reply_markup=keyboard
        )
        send_to_logger(message, safe_get_messages(user_id).AUDIO_HELP_SHOWN_LOG_MSG)
        return
    save_user_tags(user_id, tags)
    
    # Extract playlist parameters from the message
    full_string = text or message.caption or ""
    _, video_start_with, video_end_with, playlist_name, _, _, tag_error = extract_url_range_tags(full_string)
    # Правильное вычисление video_count для отрицательных индексов
    if video_start_with < 0 and video_end_with < 0:
        video_count = abs(video_end_with) - abs(video_start_with) + 1
    elif video_start_with > video_end_with:
        video_count = abs(video_start_with - video_end_with) + 1
    else:
        video_count = video_end_with - video_start_with + 1
    
    # Checking the range limit
    if not check_playlist_range_limits(url, video_start_with, video_end_with, app, message):
        return
    
    # Note: cached_video_info=None for direct calls (no optimization available)
    down_and_audio(app, message, url, tags, quality_key="mp3", playlist_name=playlist_name, video_count=video_count, video_start_with=video_start_with, format_override="ba", cached_video_info=None)


# /Link Command
@app.on_message(filters.command("link") & filters.private)
@background_handler(label="link_command")
def link_command_handler(app, message):
    if not _check_access(message):
        return
    link_command(app, message)

# /Proxy Command
@app.on_message(filters.command("proxy") & filters.private)
@background_handler(label="proxy_command")
def proxy_command_handler(app, message):
    if not _check_access(message, require_channel=False):
        return
    proxy_command(app, message)


# /Playlist Command
@app.on_message(filters.command("playlist") & filters.private)
@background_handler(label="playlist_command")
def playlist_command(app, message):
    user_id = message.chat.id

    if not _check_access(message):
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(safe_get_messages(user_id).OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG, callback_data="playlist_help|close")]
    ])
    safe_send_message(user_id, safe_get_messages(user_id).PLAYLIST_HELP_MSG, parse_mode=enums.ParseMode.HTML, reply_markup=keyboard, message=message)
    send_to_logger(message, safe_get_messages(user_id).PLAYLIST_HELP_REQUESTED_LOG_MSG)

@app.on_callback_query(filters.regex(r"^playlist_help\|"))
def playlist_help_callback(app, callback_query):
    data = callback_query.data.split("|")[1]
    if data == "close":
        _close_callback(callback_query, "PLAYLIST_HELP_CLOSED_MSG", "PLAYLIST_HELP_CLOSED_LOG_MSG")

@app.on_callback_query(filters.regex(r"^userlogs_close\|"))
def userlogs_close_callback(app, callback_query):
    data = callback_query.data.split("|")[1]
    if data == "close":
        _close_callback(callback_query, "OTHER_LOGS_MESSAGE_CLOSED_MSG", "USERLOGS_CLOSED_MSG")

@app.on_callback_query(filters.regex(r"^audio_hint\|"))
def audio_hint_callback(app, callback_query):
    data = callback_query.data.split("|")[1]
    if data == "close":
        _close_callback(callback_query, "AUDIO_HELP_CLOSED_MSG", "AUDIO_HINT_CLOSED_LOG_MSG")




