# ####################################################################################
# Args Command - Interactive yt-dlp parameters configuration
# ####################################################################################

from HELPERS.safe_messeger import safe_callback_answer
import os
import html
import json
import re
import threading
import time
from typing import Dict, Any, Optional
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums

from HELPERS.app_instance import get_app
from HELPERS.logger import logger, send_to_user, send_error_to_user
from HELPERS.limitter import check_user, is_user_in_channel
from HELPERS.safe_messeger import safe_send_message
from HELPERS.decorators import background_handler, light_only
from CONFIG.config import Config
from CONFIG.messages import get_messages_instance, safe_get_messages
from CONFIG.logger_msg import LoggerMsg

# Initialize messages for global use (will be overridden in functions)
# Note: This will be overridden in each function with proper user_id

# Get app instance
app = get_app()

def get_param_description(param_config, param_name, messages):
    """Get parameter description from messages using description_key"""
    description_key = param_config.get('description_key', f'ARGS_{param_name.upper()}_DESC_MSG')
    return getattr(messages, description_key, f'{param_name} description')

# Global dictionaries to track user input states
# - For private chats: keyed by user_id (backward compatibility)
# - For groups with topics: keyed by (chat_id, thread_id)
user_input_states_dm = {}  # {user_id: {"param": param_name, "type": param_type}}
user_input_states_topic = {}  # {(chat_id, thread_id): {"param": param_name, "type": param_type}}
# Backward-compatibility alias for modules importing user_input_states (used in private chat flow)
user_input_states = user_input_states_dm

# Timers for auto-closing input states after 5 minutes
input_state_timers_dm = {}  # {user_id: timer_thread}
input_state_timers_topic = {}  # {(chat_id, thread_id): timer_thread}
# Flags to prevent duplicate timeout messages
timeout_sent_dm = set()  # {user_id}
timeout_sent_topic = set()  # {(chat_id, thread_id)}

# File to store user args settings
ARGS_FILE = "args.txt"

def clear_input_state_timer(user_id: int, thread_id: int = None):
    messages = get_messages_instance(user_id)
    """Clear input state and its timer"""
    if thread_id:
        # Clear topic state
        user_input_states_topic.pop((user_id, thread_id), None)
        timer = input_state_timers_topic.pop((user_id, thread_id), None)
        if timer:
            try:
                timer.cancel()
            except Exception:
                pass
        # Clear timeout flag
        timeout_sent_topic.discard((user_id, thread_id))
    else:
        # Clear DM state
        user_input_states_dm.pop(user_id, None)
        timer = input_state_timers_dm.pop(user_id, None)
        if timer:
            try:
                timer.cancel()
            except Exception:
                pass
        # Clear timeout flag
        timeout_sent_dm.discard(user_id)

def start_input_state_timer(user_id: int, thread_id: int = None):
    messages = get_messages_instance(user_id)
    """Start a 5-minute timer to auto-close input state"""
    def auto_close():
        messages = get_messages_instance(user_id)
        # Check if timer still exists (not cancelled)
        if thread_id:
            if (user_id, thread_id) not in input_state_timers_topic:
                return
            # Check if timeout message already sent
            if (user_id, thread_id) in timeout_sent_topic:
                return
            timeout_sent_topic.add((user_id, thread_id))
        else:
            if user_id not in input_state_timers_dm:
                return
            # Check if timeout message already sent
            if user_id in timeout_sent_dm:
                return
            timeout_sent_dm.add(user_id)
        
        clear_input_state_timer(user_id, thread_id)
        # Send notification to user only once
        try:
            messages = get_messages_instance(user_id)
            safe_send_message(
                user_id,
                messages.ARGS_INPUT_TIMEOUT_MSG
            )
        except Exception as e:
            messages = get_messages_instance(user_id)
            logger.error(messages.ARGS_ERROR_SENDING_TIMEOUT_MSG.format(error=e))
    
    # Cancel existing timer if any
    if thread_id:
        existing_timer = input_state_timers_topic.get((user_id, thread_id))
        if existing_timer:
            existing_timer.cancel()
        timer = threading.Timer(300, auto_close)  # 5 minutes = 300 seconds
        input_state_timers_topic[(user_id, thread_id)] = timer
    else:
        existing_timer = input_state_timers_dm.get(user_id)
        if existing_timer:
            existing_timer.cancel()
        timer = threading.Timer(300, auto_close)  # 5 minutes = 300 seconds
        input_state_timers_dm[user_id] = timer
    
    timer.start()

# Available yt-dlp parameters with their types and options
# Note: descriptions will be loaded dynamically in functions
YTDLP_PARAMS = {
    "impersonate": {
        "type": "select",
        "description_key": "ARGS_IMPERSONATE_DESC_MSG",
        "options": ["chrome", "firefox", "safari", "edge", "opera"],
        "default": "chrome"
    },
    "referer": {
        "type": "text",
        "description_key": "ARGS_REFERER_DESC_MSG",
        "placeholder": "https://example.com",
        "default": "",
        "validation": "url"
    },
    "user_agent": {
        "type": "text", 
        "description_key": "ARGS_USER_AGENT_DESC_MSG",
        "placeholder": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "default": "",
        "validation": "text"
    },
    "geo_bypass": {
        "type": "boolean",
        "description_key": "ARGS_GEO_BYPASS_DESC_MSG",
        "default": True
    },
    "check_certificate": {
        "type": "boolean", 
        "description_key": "ARGS_CHECK_CERTIFICATE_DESC_MSG",
        "default": True
    },
    "live_from_start": {
        "type": "boolean",
        "description_key": "ARGS_LIVE_FROM_START_DESC_MSG",
        "default": True
    },
    "no_live_from_start": {
        "type": "boolean",
        "description_key": "ARGS_NO_LIVE_FROM_START_DESC_MSG",
        "default": False
    },
    "hls_use_mpegts": {
        "type": "boolean",
        "description_key": "ARGS_HLS_USE_MPEGTS_DESC_MSG",
        "default": True
    },
    "no_playlist": {
        "type": "boolean",
        "description_key": "ARGS_NO_PLAYLIST_DESC_MSG",
        "default": False
    },
    "no_part": {
        "type": "boolean",
        "description_key": "ARGS_NO_PART_DESC_MSG",
        "default": False
    },
    "no_continue": {
        "type": "boolean",
        "description_key": "ARGS_NO_CONTINUE_DESC_MSG",
        "default": False
    },
    "audio_format": {
        "type": "select",
        "description_key": "ARGS_AUDIO_FORMAT_DESC_MSG",
        "options": ["best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", "wav", "alac", "ac3"],
        "default": "best"
    },
    "embed_metadata": {
        "type": "boolean",
        "description_key": "ARGS_EMBED_METADATA_DESC_MSG",
        "default": False
    },
    "embed_thumbnail": {
        "type": "boolean",
        "description_key": "ARGS_EMBED_THUMBNAIL_DESC_MSG",
        "default": True
    },
    "write_thumbnail": {
        "type": "boolean",
        "description_key": "ARGS_WRITE_THUMBNAIL_DESC_MSG",
        "default": True
    },
    "concurrent_fragments": {
        "type": "number",
        "description_key": "ARGS_CONCURRENT_FRAGMENTS_DESC_MSG",
        "placeholder": "1",
        "default": 1,
        "min": 1,
        "max": 16
    },
    "force_ipv4": {
        "type": "boolean",
        "description_key": "ARGS_FORCE_IPV4_DESC_MSG",
        "default": False
    },
    "force_ipv6": {
        "type": "boolean",
        "description_key": "ARGS_FORCE_IPV6_DESC_MSG",
        "default": False
    },
    "xff": {
        "type": "text",
        "description_key": "ARGS_XFF_DESC_MSG",
        "placeholder": "default, never, US, GB, DE, 192.168.1.0/24",
        "default": "default",
        "validation": "xff"
    },
    "http_chunk_size": {
        "type": "number",
        "description_key": "ARGS_HTTP_CHUNK_SIZE_DESC_MSG",
        "placeholder": "10485760",
        "default": 0,
        "min": 0,
        "max": 104857600
    },
    "sleep_subtitles": {
        "type": "number",
        "description_key": "ARGS_SLEEP_SUBTITLES_DESC_MSG",
        "placeholder": "0",
        "default": 0,
        "min": 0,
        "max": 60
    },
    "legacy_server_connect": {
        "type": "boolean",
        "description_key": "ARGS_LEGACY_SERVER_CONNECT_DESC_MSG",
        "default": False
    },
    "no_check_certificates": {
        "type": "boolean",
        "description_key": "ARGS_NO_CHECK_CERTIFICATES_DESC_MSG",
        "default": False
    },
    "username": {
        "type": "text",
        "description_key": "ARGS_USERNAME_DESC_MSG",
        "placeholder": "your_username",
        "default": "",
        "validation": "text"
    },
    "password": {
        "type": "text",
        "description_key": "ARGS_PASSWORD_DESC_MSG",
        "placeholder": "your_password",
        "default": "",
        "validation": "text"
    },
    "twofactor": {
        "type": "text",
        "description_key": "ARGS_TWOFACTOR_DESC_MSG",
        "placeholder": "123456",
        "default": "",
        "validation": "text"
    },
    "ignore_errors": {
        "type": "boolean",
        "description_key": "ARGS_IGNORE_ERRORS_DESC_MSG",
        "default": False
    },
    "min_filesize": {
        "type": "number",
        "description_key": "ARGS_MIN_FILESIZE_DESC_MSG",
        "placeholder": "0",
        "default": 0,
        "min": 0,
        "max": 10000
    },
    "max_filesize": {
        "type": "number",
        "description_key": "ARGS_MAX_FILESIZE_DESC_MSG",
        "placeholder": "0",
        "default": 0,
        "min": 0,
        "max": 10000
    },
    "playlist_items": {
        "type": "text",
        "description_key": "ARGS_PLAYLIST_ITEMS_DESC_MSG",
        "placeholder": "1,3,5",
        "default": "",
        "validation": "playlist_items"
    },
    "date": {
        "type": "text",
        "description_key": "ARGS_DATE_DESC_MSG",
        "placeholder": "20230930",
        "default": "",
        "validation": "date"
    },
    "datebefore": {
        "type": "text",
        "description_key": "ARGS_DATEBEFORE_DESC_MSG",
        "placeholder": "20230930",
        "default": "",
        "validation": "date"
    },
    "dateafter": {
        "type": "text",
        "description_key": "ARGS_DATEAFTER_DESC_MSG",
        "placeholder": "20230930",
        "default": "",
        "validation": "date"
    },
    "http_headers": {
        "type": "json",
        "description_key": "ARGS_HTTP_HEADERS_DESC_MSG",
        "placeholder": '{"Authorization": "Bearer token", "X-API-Key": "key123"}',
        "default": "{}",
        "validation": "json"
    },
    "sleep_interval": {
        "type": "number",
        "description_key": "ARGS_SLEEP_INTERVAL_DESC_MSG",
        "placeholder": "1",
        "default": 1,
        "min": 0,
        "max": 60
    },
    "max_sleep_interval": {
        "type": "number", 
        "description_key": "ARGS_MAX_SLEEP_INTERVAL_DESC_MSG",
        "placeholder": "5",
        "default": 5,
        "min": 0,
        "max": 300
    },
    "retries": {
        "type": "number",
        "description_key": "ARGS_RETRIES_DESC_MSG",
        "placeholder": "10",
        "default": 10,
        "min": 0,
        "max": 50
    },
    "video_format": {
        "type": "select",
        "description_key": "ARGS_VIDEO_FORMAT_DESC_MSG",
        "options": ["mp4", "webm", "mkv", "avi", "mov", "flv", "3gp", "ogv", "m4v", "wmv", "asf"],
        "default": "mp4"
    },
    "merge_output_format": {
        "type": "select",
        "description_key": "ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG",
        "options": ["mp4", "webm", "mkv", "avi", "mov", "flv", "3gp", "ogv", "m4v", "wmv", "asf"],
        "default": "mp4"
    },
    "send_as_file": {
        "type": "boolean",
        "description_key": "ARGS_SEND_AS_FILE_DESC_MSG",
        "default": False
    }
}

_CONTROL_CHARS_RE = re.compile(r'[\x00-\x1f\x7f]')
_PLAYLIST_ITEMS_RE = re.compile(r'^\s*-?\d*(?:\s*[-:]\s*-?\d*){0,2}(?:\s*,\s*-?\d*(?:\s*[-:]\s*-?\d*){0,2})*\s*$')
# Values that are credentials: never shown back, exported or logged in clear
SECRET_PARAMS = frozenset({"password", "twofactor"})
SECRET_MASK = "••••••"


def _parse_yyyymmdd(value: str):
    from datetime import datetime
    try:
        return datetime.strptime(value, "%Y%m%d")
    except ValueError:
        return None


def validate_input(value: str, param_name: str, user_id: int = None) -> tuple[bool, str]:
    """
    Validate a text/JSON value for an /args parameter.
    Returns (is_valid, error_message).

    Values are stored as JSON and handed to yt-dlp as Python options (no shell,
    no SQL), so quotes and semicolons are legitimate (User-Agent strings and
    JSON headers need them). What is rejected: control characters (they would
    end up in HTTP headers), oversized input and values yt-dlp cannot use.
    """
    messages = get_messages_instance(user_id)
    param_config = YTDLP_PARAMS.get(param_name, {})
    validation_type = param_config.get("validation", "text")

    if len(value) > 1000:
        return False, messages.ARGS_INPUT_TOO_LONG_MSG

    if validation_type != "json" and _CONTROL_CHARS_RE.search(value):
        return False, messages.ARGS_INPUT_DANGEROUS_MSG.format(pattern="control characters")

    if validation_type == "url":
        if value and not re.match(r'^https?://[^\s]+$', value, re.IGNORECASE):
            return False, messages.ARGS_INVALID_URL_MSG

    elif validation_type == "json":
        if value:
            try:
                parsed = json.loads(value)
            except (json.JSONDecodeError, ValueError):
                return False, messages.ARGS_INVALID_JSON_MSG
            if not isinstance(parsed, dict):
                return False, messages.ARGS_JSON_MUST_BE_OBJECT_MSG
            for key, val in parsed.items():
                if (not isinstance(val, str) or not key or _CONTROL_CHARS_RE.search(key)
                        or _CONTROL_CHARS_RE.search(val)):
                    return False, getattr(messages, 'ARGS_HEADERS_STRINGS_ONLY_MSG',
                                          "❌ Header names and values must be single-line strings")

    elif validation_type == "number":
        try:
            num = float(value)
        except ValueError:
            return False, messages.ARGS_INVALID_NUMBER_MSG
        min_val = param_config.get("min", 0)
        max_val = param_config.get("max", 999999)
        if num < min_val or num > max_val:
            return False, messages.ARGS_NUMBER_RANGE_MSG.format(min_val=min_val, max_val=max_val)

    elif validation_type == "date":
        if value:
            if not re.match(r'^\d{8}$', value):
                return False, messages.ARGS_DATE_FORMAT_MSG
            parsed = _parse_yyyymmdd(value)
            if parsed is None:
                return False, messages.ARGS_INVALID_DATE_MSG
            if parsed.year < 1900 or parsed.year > 2100:
                return False, messages.ARGS_YEAR_RANGE_MSG

    elif validation_type == "xff":
        if value and _xff_to_ytdlp(value) is None:
            return False, messages.ARGS_INVALID_XFF_MSG

    elif validation_type == "playlist_items":
        if value and (not _PLAYLIST_ITEMS_RE.match(value) or not re.search(r'\d', value)):
            return False, getattr(messages, 'ARGS_INVALID_PLAYLIST_ITEMS_MSG',
                                  "❌ Use item numbers and ranges, e.g. 1,3,5-7 or 2:10")

    return True, ""


def _xff_to_ytdlp(value: str):
    """Map the /args xff value to yt-dlp's Python options (None = invalid)."""
    import ipaddress
    value = (value or "").strip()
    if not value or value.lower() == "default":
        return {}
    if value.lower() == "never":
        return {"geo_bypass": False}
    if re.fullmatch(r'[A-Za-z]{2}', value):
        return {"geo_bypass": True, "geo_bypass_country": value.upper()}
    try:
        network = ipaddress.ip_network(value, strict=False)
    except ValueError:
        return None
    return {"geo_bypass": True, "geo_bypass_ip_block": str(network)}


def get_user_args(user_id: int) -> Dict[str, Any]:
    """Get user's saved args settings"""
    user_dir = os.path.join("users", str(user_id))
    args_file = os.path.join(user_dir, ARGS_FILE)
    
    if not os.path.exists(args_file):
        return {}
    
    try:
        with open(args_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(LoggerMsg.ARGS_ERROR_READING_USER_ARGS_LOG_MSG.format(user_id=user_id, error=e))
        return {}

def save_user_args(user_id: int, args: Dict[str, Any]) -> bool:
    """Save user's args settings"""
    try:
        user_dir = os.path.join("users", str(user_id))
        os.makedirs(user_dir, exist_ok=True)
        
        args_file = os.path.join(user_dir, ARGS_FILE)
        with open(args_file, 'w', encoding='utf-8') as f:
            json.dump(args, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logger.error(LoggerMsg.ARGS_ERROR_SAVING_USER_ARGS_LOG_MSG.format(user_id=user_id, error=e))
        return False

def get_args_menu_keyboard(user_id: int) -> InlineKeyboardMarkup:
    """Generate main args menu keyboard with grouped parameters"""
    messages = get_messages_instance(user_id)
    user_args = get_user_args(user_id)
    
    # Short descriptions for better UI
    short_descriptions = {
        "impersonate": messages.ARGS_IMPERSONATE_SHORT_MSG,
        "referer": messages.ARGS_REFERER_SHORT_MSG,
        "geo_bypass": messages.ARGS_GEO_BYPASS_SHORT_MSG,
        "check_certificate": messages.ARGS_CHECK_CERTIFICATE_SHORT_MSG,
        "live_from_start": messages.ARGS_LIVE_FROM_START_SHORT_MSG,
        "no_live_from_start": messages.ARGS_NO_LIVE_FROM_START_SHORT_MSG,
        "user_agent": messages.ARGS_USER_AGENT_SHORT_MSG,
        "hls_use_mpegts": messages.ARGS_HLS_USE_MPEGTS_SHORT_MSG,
        "no_playlist": messages.ARGS_NO_PLAYLIST_SHORT_MSG,
        "no_part": messages.ARGS_NO_PART_SHORT_MSG,
        "no_continue": messages.ARGS_NO_CONTINUE_SHORT_MSG,
        "audio_format": messages.ARGS_AUDIO_FORMAT_SHORT_MSG,
        "embed_metadata": messages.ARGS_EMBED_METADATA_SHORT_MSG,
        "embed_thumbnail": messages.ARGS_EMBED_THUMBNAIL_SHORT_MSG,
        "write_thumbnail": messages.ARGS_WRITE_THUMBNAIL_SHORT_MSG,
        "concurrent_fragments": messages.ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG,
        "force_ipv4": messages.ARGS_FORCE_IPV4_SHORT_MSG,
        "force_ipv6": messages.ARGS_FORCE_IPV6_SHORT_MSG,
        "xff": messages.ARGS_XFF_SHORT_MSG,
        "http_chunk_size": messages.ARGS_HTTP_CHUNK_SIZE_SHORT_MSG,
        "sleep_subtitles": messages.ARGS_SLEEP_SUBTITLES_SHORT_MSG,
        "legacy_server_connect": messages.ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG,
        "no_check_certificates": messages.ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG,
        "username": messages.ARGS_USERNAME_SHORT_MSG,
        "password": messages.ARGS_PASSWORD_SHORT_MSG,
        "twofactor": messages.ARGS_TWOFACTOR_SHORT_MSG,
        "ignore_errors": messages.ARGS_IGNORE_ERRORS_SHORT_MSG,
        "min_filesize": messages.ARGS_MIN_FILESIZE_SHORT_MSG,
        "max_filesize": messages.ARGS_MAX_FILESIZE_SHORT_MSG,
        "playlist_items": messages.ARGS_PLAYLIST_ITEMS_SHORT_MSG,
        "date": messages.ARGS_DATE_SHORT_MSG,
        "datebefore": messages.ARGS_DATEBEFORE_SHORT_MSG,
        "dateafter": messages.ARGS_DATEAFTER_SHORT_MSG,
        "http_headers": messages.ARGS_HTTP_HEADERS_SHORT_MSG,
        "sleep_interval": messages.ARGS_SLEEP_INTERVAL_SHORT_MSG,
        "max_sleep_interval": messages.ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG,
        "video_format": messages.ARGS_VIDEO_FORMAT_SHORT_MSG,
        "merge_output_format": messages.ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG,
        "send_as_file": messages.ARGS_SEND_AS_FILE_SHORT_MSG
    }
    
    buttons = []
    
    # Group 1: Boolean parameters (True/False)
    boolean_params = []
    def _append_boolean_button(pname: str):
        messages = get_messages_instance(None)
        pconfig = YTDLP_PARAMS.get(pname)
        if not pconfig or pconfig.get("type") != "boolean":
            return
        current_value = user_args.get(pname, pconfig.get("default", False))
        status = messages.ARGS_STATUS_TRUE_MSG if current_value else messages.ARGS_STATUS_FALSE_MSG
        # Get description from messages using the key
        description_key = pconfig.get('description_key', f'ARGS_{pname.upper()}_DESC_MSG')
        description = getattr(messages, description_key, f'{pname} description')
        short_desc = short_descriptions.get(pname, description[:15])
        btn_text = f"{status} {short_desc}"
        if len(btn_text) > 30:
            btn_text = f"{status} {short_desc[:25]}..."
        boolean_params.append(InlineKeyboardButton(btn_text, callback_data=f"args_set_{pname}"))

    # Ensure paired items stay together
    preferred_order = ["check_certificate", "no_check_certificates", "live_from_start", "no_live_from_start", "force_ipv4", "force_ipv6"]
    for pname in preferred_order:
        _append_boolean_button(pname)
    # Append the rest
    for pname, pconfig in YTDLP_PARAMS.items():
        if pconfig["type"] == "boolean" and pname not in preferred_order:
            _append_boolean_button(pname)
    
    # Add boolean parameters in rows of 2
    for i in range(0, len(boolean_params), 2):
        row = boolean_params[i:i+2]
        if len(row) == 1:
            row.append(InlineKeyboardButton("", callback_data="args_empty"))  # Empty button for alignment
        buttons.append(row)
    
    # Add separator
    buttons.append([InlineKeyboardButton("━━━━━━━━━━━━━━━━━━━━", callback_data="args_empty")])
    
    # Group 2: Select parameters (dropdown choices)
    select_params = []
    for param_name, param_config in YTDLP_PARAMS.items():
        if param_config["type"] == "select":
            current_value = user_args.get(param_name, param_config.get("default", ""))
            status = f"📋 {current_value}"
            description = get_param_description(param_config, param_name, messages)
            short_desc = short_descriptions.get(param_name, description[:15])
            button_text = f"{status} {short_desc}"
            if len(button_text) > 30:
                button_text = f"{status} {short_desc[:25]}..."
            
            select_params.append(InlineKeyboardButton(
                button_text,
                callback_data=f"args_set_{param_name}"
            ))
    
    # Add select parameters in rows of 2
    for i in range(0, len(select_params), 2):
        row = select_params[i:i+2]
        if len(row) == 1:
            row.append(InlineKeyboardButton("", callback_data="args_empty"))  # Empty button for alignment
        buttons.append(row)
    
    # Add separator
    buttons.append([InlineKeyboardButton("━━━━━━━━━━━━━━━━━━━━", callback_data="args_empty")])
    
    # Group 3: Numeric input parameters (require number input)
    numeric_params = []
    date_like_params = {"date", "datebefore", "dateafter"}
    for param_name, param_config in YTDLP_PARAMS.items():
        if param_config["type"] == "number" or param_name in date_like_params:
            current_value = user_args.get(param_name, param_config.get("default", ""))
            
            # Special handling for send_as_file parameter
            if param_name == "send_as_file":
                # Convert boolean to True/False display
                if isinstance(current_value, bool):
                    display_value = "True" if current_value else "False"
                else:
                    display_value = str(current_value)
                status = messages.ARGS_STATUS_TRUE_MSG if current_value else messages.ARGS_STATUS_FALSE_MSG
            else:
                status = f"🔢 {current_value}"
                display_value = str(current_value)
            
            description = get_param_description(param_config, param_name, messages)
            short_desc = short_descriptions.get(param_name, description[:15])
            button_text = f"{status} {short_desc}"
            if len(button_text) > 30:
                button_text = f"{status} {short_desc[:25]}..."
            
            numeric_params.append(InlineKeyboardButton(
                button_text,
                callback_data=f"args_set_{param_name}"
            ))
    
    # Add numeric parameters in rows of 2
    for i in range(0, len(numeric_params), 2):
        row = numeric_params[i:i+2]
        if len(row) == 1:
            row.append(InlineKeyboardButton("", callback_data="args_empty"))  # Empty button for alignment
        buttons.append(row)
    
    # Add separator
    buttons.append([InlineKeyboardButton("━━━━━━━━━━━━━━━━━━━━", callback_data="args_empty")])
    
    # Group 4: Text input parameters (require text/JSON input)
    text_params = []
    for param_name, param_config in YTDLP_PARAMS.items():
        if param_config["type"] in ["text", "json"] and param_name not in date_like_params:
            current_value = user_args.get(param_name, param_config.get("default", ""))
            if param_config["type"] == "text":
                status = "📝" if current_value else "📝"
            elif param_config["type"] == "json":
                status = "🔧" if current_value and current_value != "{}" else "🔧"
            
            description = get_param_description(param_config, param_name, messages)
            short_desc = short_descriptions.get(param_name, description[:15])
            button_text = f"{status} {short_desc}"
            if len(button_text) > 30:
                button_text = f"{status} {short_desc[:25]}..."
            
            text_params.append(InlineKeyboardButton(
                button_text,
                callback_data=f"args_set_{param_name}"
            ))
    
    # Add text parameters in rows of 2
    for i in range(0, len(text_params), 2):
        row = text_params[i:i+2]
        if len(row) == 1:
            row.append(InlineKeyboardButton("", callback_data="args_empty"))  # Empty button for alignment
        buttons.append(row)
    
    # Add separator
    buttons.append([InlineKeyboardButton("━━━━━━━━━━━━━━━━━━━━", callback_data="args_empty")])
    
    # Control buttons
    buttons.append([
        InlineKeyboardButton(messages.ARGS_RESET_ALL_BUTTON_MSG, callback_data="args_reset_all"),
        InlineKeyboardButton(messages.ARGS_VIEW_CURRENT_BUTTON_MSG, callback_data="args_view_current")
    ])
    buttons.append([InlineKeyboardButton(messages.ARGS_CLOSE_BUTTON_MSG, callback_data="args_close")])
    
    return InlineKeyboardMarkup(buttons)

def get_boolean_menu_keyboard(param_name: str, current_value: bool, user_id: int = None) -> InlineKeyboardMarkup:
    """Generate boolean parameter menu keyboard"""
    messages = get_messages_instance(user_id)
    buttons = [
        [InlineKeyboardButton(
            messages.ARGS_TRUE_BUTTON_MSG,
            callback_data=f"args_bool_{param_name}_true"
        )],
        [InlineKeyboardButton(
            messages.ARGS_FALSE_BUTTON_MSG, 
            callback_data=f"args_bool_{param_name}_false"
        )],
        [InlineKeyboardButton(messages.ARGS_BACK_BUTTON_MSG, callback_data="args_back")]
    ]
    return InlineKeyboardMarkup(buttons)

def get_select_menu_keyboard(param_name: str, current_value: str, user_id: int = None) -> InlineKeyboardMarkup:
    """Generate select parameter menu keyboard"""
    messages = get_messages_instance(user_id)
    param_config = YTDLP_PARAMS[param_name]
    options = param_config["options"]
    
    buttons = []
    for option in options:
        status = messages.ARGS_STATUS_SELECTED_MSG if option == current_value else messages.ARGS_STATUS_UNSELECTED_MSG
        buttons.append([InlineKeyboardButton(
            f"{status} {option}",
            callback_data=f"args_select_{param_name}_{option}"
        )])
    
    buttons.append([InlineKeyboardButton(messages.ARGS_BACK_BUTTON_MSG, callback_data="args_back")])
    return InlineKeyboardMarkup(buttons)

def get_text_input_message(param_name: str, current_value: str, user_id: int = None) -> str:
    """Generate text input message"""
    messages = get_messages_instance(user_id)
    param_config = YTDLP_PARAMS[param_name]
    placeholder = param_config.get("placeholder", "")
    
    description = get_param_description(param_config, param_name, messages)
    message = messages.ARGS_PARAM_DESCRIPTION_MSG.format(description=description)
    if current_value:
        message += messages.ARGS_CURRENT_VALUE_MSG.format(current_value=_display_value(param_name, current_value))
    
    if param_name == "xff":
        message += messages.ARGS_XFF_EXAMPLES_MSG
        message += messages.ARGS_XFF_NOTE_MSG
    elif placeholder:
        message += messages.ARGS_EXAMPLE_MSG.format(placeholder=placeholder)
    
    message += messages.ARGS_SEND_VALUE_MSG
    
    return message

def get_number_input_message(param_name: str, current_value: Any, user_id: int = None) -> str:
    """Generate number input message"""
    messages = get_messages_instance(user_id)
    param_config = YTDLP_PARAMS[param_name]
    
    # Special handling for send_as_file parameter
    if param_name == "send_as_file":
        description = get_param_description(param_config, param_name, messages)
        message = f"<b>⚙️ {description}</b>\n\n"
        if current_value is not None:
            display_value = "True" if current_value else "False"
            message += f"Current value: <code>{display_value}</code>\n\n"
        message += messages.ARGS_BOOL_VALUE_REQUEST_MSG
        return message
    
    min_val = param_config.get("min", 0)
    max_val = param_config.get("max", 999999)
    
    description = get_param_description(param_config, param_name, messages)
    message = messages.ARGS_NUMBER_PARAM_MSG.format(description=description)
    if current_value is not None:
        message += messages.ARGS_CURRENT_VALUE_MSG.format(current_value=current_value)
    message += messages.ARGS_RANGE_MSG.format(min_val=min_val, max_val=max_val)
    message += messages.ARGS_SEND_NUMBER_MSG
    
    return message

def get_json_input_message(param_name: str, current_value: str, user_id: int = None) -> str:
    """Generate JSON input message"""
    messages = get_messages_instance(user_id)
    param_config = YTDLP_PARAMS[param_name]
    placeholder = param_config.get("placeholder", "{}")
    
    description = get_param_description(param_config, param_name, messages)
    message = messages.ARGS_JSON_PARAM_MSG.format(description=description)
    if current_value and current_value != "{}":
        message += messages.ARGS_CURRENT_VALUE_MSG.format(current_value=html.escape(str(current_value)))
    
    if param_name == "http_headers":
        message += messages.ARGS_HTTP_HEADERS_EXAMPLES_MSG.format(placeholder=placeholder)
        message += messages.ARGS_HTTP_HEADERS_NOTE_MSG
    else:
        message += messages.ARGS_EXAMPLE_MSG.format(placeholder=placeholder)
    
    message += messages.ARGS_JSON_VALUE_REQUEST_MSG
    
    return message

def _display_value(param_name: str, value: Any) -> str:
    """Human-readable, HTML-safe value; credentials are never echoed back."""
    if isinstance(value, bool):
        return "✅ True" if value else "❌ False"
    if isinstance(value, (int, float)):
        return str(value)
    if param_name in SECRET_PARAMS and value:
        return SECRET_MASK
    return html.escape(str(value)) if value else "Not set"


def mask_args_for_log(args: Dict[str, Any]) -> Dict[str, Any]:
    """Copy of /args (or yt-dlp options) safe to write to the journal."""
    masked = {}
    for key, value in (args or {}).items():
        if key in SECRET_PARAMS and value:
            masked[key] = SECRET_MASK
        elif key == "http_headers" and value:
            if isinstance(value, dict):
                masked[key] = {k: SECRET_MASK for k in value}
            else:
                try:
                    masked[key] = {k: SECRET_MASK for k in json.loads(value)}
                except Exception:
                    masked[key] = SECRET_MASK
        else:
            masked[key] = value
    return masked


def format_current_args(user_args: Dict[str, Any], user_id: int = None) -> str:
    """Format current args for display with localized names"""
    messages = get_messages_instance(user_id)
    if not user_args:
        return messages.ARGS_NO_CUSTOM_MSG
    
    message = messages.ARGS_CURRENT_ARGS_MSG
    
    # Get localized parameter names based on user language
    display_names = get_localized_display_names(user_id)
    
    for param_name, value in user_args.items():
        display_name = html.escape(str(display_names.get(param_name, param_name)))
        display_value = _display_value(param_name, value)
        message += f"<b>{display_name}:</b> <code>{display_value}</code>\n"
    
    return message

def get_localized_display_names(user_id: int = None) -> Dict[str, str]:
    """Get localized parameter names for display based on user language"""
    messages = get_messages_instance(user_id)
    
    # Get language-specific parameter names
    if hasattr(messages, 'ARGS_PARAM_NAMES'):
        return messages.ARGS_PARAM_NAMES
    
    # Fallback to English if no localized names available
    return get_export_display_names()

def get_export_display_names() -> Dict[str, str]:
    """Get English parameter names for export (human-readable names)"""
    return {
        "force_ipv6": "Force IPv6 connections",
        "force_ipv4": "Force IPv4 connections", 
        "no_live_from_start": "Do not download live streams from start",
        "live_from_start": "Download live streams from start",
        "no_check_certificates": "Suppress HTTPS certificate validation",
        "check_certificate": "Check SSL certificate",
        "no_playlist": "Download only single video, not playlist",
        "embed_metadata": "Embed metadata in video file",
        "embed_thumbnail": "Embed thumbnail in video file",
        "write_thumbnail": "Write thumbnail to file",
        "ignore_errors": "Ignore download errors and continue",
        "legacy_server_connect": "Allow legacy server connections",
        "concurrent_fragments": "Number of concurrent fragments to download",
        "xff": "X-Forwarded-For header strategy",
        "user_agent": "User-Agent header",
        "impersonate": "Browser impersonation",
        "referer": "Referer header",
        "geo_bypass": "Bypass geographic restrictions",
        "hls_use_mpegts": "Use MPEG-TS for HLS",
        "no_part": "Do not use .part files",
        "no_continue": "Do not resume partial downloads",
        "audio_format": "Audio format",
        "video_format": "Video format",
        "merge_output_format": "Merge output format",
        "send_as_file": "Send as file",
        "username": "Username",
        "password": "Password",
        "twofactor": "Two-factor authentication code",
        "min_filesize": "Minimum file size (MB)",
        "max_filesize": "Maximum file size (MB)",
        "playlist_items": "Playlist items",
        "date": "Date",
        "datebefore": "Date before",
        "dateafter": "Date after",
        "http_headers": "HTTP headers",
        "sleep_interval": "Sleep interval",
        "max_sleep_interval": "Maximum sleep interval",
        "retries": "Number of retries",
        "http_chunk_size": "HTTP chunk size",
        "sleep_subtitles": "Sleep for subtitles"
    }

def get_localized_to_english_mapping() -> Dict[str, str]:
    """Get mapping from localized parameter names to English parameter names"""
    return {
        # New English mappings (from get_export_display_names)
        "Force IPv6 connections": "force_ipv6",
        "Force IPv4 connections": "force_ipv4",
        "Do not download live streams from start": "no_live_from_start",
        "Download live streams from start": "live_from_start",
        "Suppress HTTPS certificate validation": "no_check_certificates",
        "Check SSL certificate": "check_certificate",
        "Download only single video, not playlist": "no_playlist",
        "Embed metadata in video file": "embed_metadata",
        "Embed thumbnail in video file": "embed_thumbnail",
        "Write thumbnail to file": "write_thumbnail",
        "Ignore download errors and continue": "ignore_errors",
        "Allow legacy server connections": "legacy_server_connect",
        "Number of concurrent fragments to download": "concurrent_fragments",
        "X-Forwarded-For header strategy": "xff",
        "User-Agent header": "user_agent",
        "Browser impersonation": "impersonate",
        "Referer header": "referer",
        "Bypass geographic restrictions": "geo_bypass",
        "Use MPEG-TS for HLS": "hls_use_mpegts",
        "Do not use .part files": "no_part",
        "Do not resume partial downloads": "no_continue",
        "Audio format": "audio_format",
        "Video format": "video_format",
        "Merge output format": "merge_output_format",
        "Send as file": "send_as_file",
        "Username": "username",
        "Password": "password",
        "Two-factor authentication code": "twofactor",
        "Minimum file size (MB)": "min_filesize",
        "Maximum file size (MB)": "max_filesize",
        "Playlist items": "playlist_items",
        "Date": "date",
        "Date before": "datebefore",
        "Date after": "dateafter",
        "HTTP headers": "http_headers",
        "Sleep interval": "sleep_interval",
        "Maximum sleep interval": "max_sleep_interval",
        "Number of retries": "retries",
        "HTTP chunk size": "http_chunk_size",
        "Sleep for subtitles": "sleep_subtitles",
        
        # Old English mappings (for backward compatibility) - removed duplicates
        
        # Russian mappings (if any)
        "Разрешить устаревшие подключения к серверу": "legacy_server_connect",
        "Имитация браузера": "impersonate",
        "Проверить SSL сертификат": "check_certificate",
        "Не загружать прямые трансляции с начала": "no_live_from_start",
        "Загружать прямые трансляции с начала": "live_from_start",
        "Загружать только одно видео, не плейлист": "no_playlist",
        "Встроить метаданные в видеофайл": "embed_metadata",
        "Встроить миниатюру в видеофайл": "embed_thumbnail",
        "Принудительные IPv4 подключения": "force_ipv4",
        "Принудительные IPv6 подключения": "force_ipv6",
        "Игнорировать ошибки загрузки и продолжать": "ignore_errors",
        "Количество одновременных фрагментов для загрузки": "concurrent_fragments",
        "Подавить проверку HTTPS сертификата": "no_check_certificates",
        "Заголовок User-Agent": "user_agent",
        "Записать миниатюру в файл": "write_thumbnail",
        "Стратегия заголовка X-Forwarded-For": "xff",
        
        # Add more mappings as needed for other languages
    }

def create_export_message(user_args: Dict[str, Any], user_id: int = None) -> str:
    """Create export message for forwarding to favorites - always in English"""
    if not user_args:
        return "📋 Current yt-dlp Arguments:\n\nNo custom settings configured.\n\n---\n\n<i>Forward this message to your favorites to save these settings as a template.</i> \n\n<i>Forward this message back here to apply these settings.</i>"
    
    # Always use English header
    message = "📋 Current yt-dlp Arguments:\n\n"
    
    # Get English parameter names
    display_names = get_export_display_names()
    
    # Sort parameters for consistent display
    sorted_params = sorted(user_args.items(), key=lambda x: display_names.get(x[0], x[0]))
    
    for param_name, value in sorted_params:
        display_name = display_names.get(param_name, param_name)
        # Credentials are not exported: the template is meant to be forwarded
        status = _display_value(param_name, value)

        # Make parameter names bold and values monospace
        message += f"<b>{display_name}:</b> <code>{status}</code>\n"
    
    # Always use English footer
    message += "\n---\n\n<i>Forward this message to your favorites to save these settings as a template.</i> \n\n<i>Forward this message back here to apply these settings.</i>"
    
    return message

def parse_import_message(text: str, user_id: int = None) -> Dict[str, Any]:
    """Parse settings from imported message text"""
    messages = get_messages_instance(user_id)
    
    if not text:
        logger.info(f"parse_import_message: No text provided")
        return {}
    
    # Check for args header in any supported language
    args_headers = [
        "📋 Current yt-dlp Arguments:",  # English
        "📋 Текущие аргументы yt-dlp:",  # Russian
        "📋 वर्तमान yt-dlp तर्क:",  # Hindi
        "📋 وسائط yt-dlp الحالية:",  # Arabic
    ]
    
    has_args_header = any(header in text for header in args_headers)
    
    if not has_args_header:
        logger.info(f"parse_import_message: No header found in text. Text: {text[:200] if text else 'None'}")
        return {}
    
    # For forwarded messages, try to extract the actual content
    # Look for the start of the settings section
    settings_start = -1
    for header in args_headers:
        if header in text:
            settings_start = text.find(header)
            break
    
    if settings_start == -1:
        logger.info(f"parse_import_message: Could not find settings start position")
        return {}
    
    # Extract the settings part, skipping any forwarded message metadata
    settings_text = text[settings_start:]
    
    # Remove any potential forwarded message metadata that might appear at the beginning
    lines = settings_text.split('\n')
    clean_lines = []
    in_settings = False
    
    for line in lines:
        line = line.strip()
        # Start processing when we find the header
        if any(header in line for header in args_headers):
            in_settings = True
            clean_lines.append(line)
        elif in_settings:
            # Stop if we hit a separator or instruction line
            if (line.startswith('---') or 
                'Forward this message' in line or 
                'Перешлите это сообщение' in line):
                break
            clean_lines.append(line)
    
    # Reconstruct the clean text
    clean_text = '\n'.join(clean_lines)
    logger.info(f"parse_import_message: Cleaned text length: {len(clean_text)}")
    logger.info(f"parse_import_message: Cleaned text preview: {clean_text[:200]}...")
    
    # Use the cleaned text for parsing
    text = clean_text
    
    # Get valid parameter names from YTDLP_PARAMS
    valid_params = set(YTDLP_PARAMS.keys())
    
    # Get mapping from localized names to English parameter names
    localized_mapping = get_localized_to_english_mapping()
    
    parsed_args = {}
    lines = text.split('\n')
    
    logger.info(f"parse_import_message: Processing {len(lines)} lines")
    
    for line in lines:
        line = line.strip()
        # Skip empty lines, headers, separators, and HTML tags
        if (not line or line.startswith('📋') or line.startswith('---') or 
            line.startswith('<i>') or line.startswith('Forward this message') or
            line.startswith('Перешлите это сообщение')):
            continue
            
        # Parse format: "Display Name: Value"
        if ':' in line:
            parts = line.split(':', 1)
            if len(parts) == 2:
                param_name = parts[0].strip()
                value_str = parts[1].strip()
                
                # Clean param name from potential HTML tags and extra whitespace
                import re
                param_name = re.sub(r'<[^>]+>', '', param_name).strip()
                # Remove any potential emoji or special characters that might interfere
                param_name = re.sub(r'^[^\w\s]+', '', param_name).strip()
                # Remove any potential forwarded message indicators
                param_name = re.sub(r'^[^\w\s]*', '', param_name).strip()
                # Clean value string as well
                value_str = re.sub(r'<[^>]+>', '', value_str).strip()
                
                logger.info(f"parse_import_message: Found param_name='{param_name}'")
                
                # Try to map localized name to English parameter name
                english_param_name = None
                if param_name in valid_params:
                    # Direct match with English parameter name
                    english_param_name = param_name
                    logger.info(f"parse_import_message: Direct match found: {param_name}")
                elif param_name in localized_mapping:
                    # Mapped from localized name
                    english_param_name = localized_mapping[param_name]
                    logger.info(f"parse_import_message: Mapped '{param_name}' -> '{english_param_name}'")
                else:
                    logger.info(f"parse_import_message: Unknown parameter '{param_name}', skipping")
                    continue
                
                # Check if the mapped parameter exists in YTDLP_PARAMS
                if english_param_name in valid_params:
                    param_config = YTDLP_PARAMS[english_param_name]
                    param_type = param_config.get("type", "text")
                    
                    # Clean value string from potential HTML tags
                    value_str = re.sub(r'<[^>]+>', '', value_str).strip()
                    
                    # Parse value based on type
                    if param_type == "boolean":
                        if value_str in ["✅ True", "True", "true", "1", "yes", "on", "✅"]:
                            parsed_args[english_param_name] = True
                            logger.info(f"parse_import_message: Set {english_param_name} = True")
                        elif value_str in ["❌ False", "False", "false", "0", "no", "off", "❌"]:
                            parsed_args[english_param_name] = False
                            logger.info(f"parse_import_message: Set {english_param_name} = False")
                    elif param_type == "number":
                        numbers = re.findall(r'\d+', value_str)
                        if numbers:
                            num_value = int(numbers[0])
                            min_val = param_config.get("min", 0)
                            max_val = param_config.get("max", 999999)
                            if min_val <= num_value <= max_val:
                                parsed_args[english_param_name] = num_value
                                logger.info(f"parse_import_message: Set {english_param_name} = {num_value}")
                    elif param_type in ["text", "json"]:
                        value_str = html.unescape(value_str)
                        if (value_str and value_str != "Not set" and value_str != SECRET_MASK
                                and validate_input(value_str, english_param_name, user_id)[0]):
                            parsed_args[english_param_name] = value_str
                            logger.info(f"parse_import_message: Set {english_param_name}")
                    elif param_type == "select":
                        if value_str and value_str != "Not set":
                            # Validate that the value is in the allowed options
                            options = param_config.get("options", [])
                            if value_str in options:
                                parsed_args[english_param_name] = value_str
                                logger.info(f"parse_import_message: Set {english_param_name} = '{value_str}'")
                else:
                    logger.info(f"parse_import_message: Mapped parameter '{english_param_name}' not found in YTDLP_PARAMS")
    
    logger.info(f"parse_import_message: Parsed {len(parsed_args)} arguments: {list(parsed_args.keys())}")
    return parsed_args

@app.on_message(filters.command("args"))
@background_handler(label="args_command", heavy_if=light_only)
def args_command(app, message):
    messages = get_messages_instance(message.chat.id)
    """Handle /args command"""
    chat_id = message.chat.id
    invoker_id = getattr(message, 'from_user', None).id if getattr(message, 'from_user', None) else chat_id
    
    # Subscription check for non-admins
    if int(invoker_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return  # is_user_in_channel already sends subscription message
    
    # Create user directory after subscription check
    user_dir = os.path.join("users", str(invoker_id))
    if not os.path.exists(user_dir):
        os.makedirs(user_dir, exist_ok=True)
    
    keyboard = get_args_menu_keyboard(invoker_id)
    
    safe_send_message(
        chat_id,
        messages.ARGS_CONFIG_TITLE_MSG.format(groups_msg=messages.ARGS_MENU_DESCRIPTION_MSG),
        reply_markup=keyboard,
        message=message
    )

@app.on_callback_query(filters.regex("^args_"))
def args_callback_handler(app, callback_query):
    messages = get_messages_instance(callback_query.message.chat.id)
    """Handle args menu callbacks"""
    user_id = callback_query.from_user.id
    data = callback_query.data
    
    try:
        if data == "args_close":
            callback_query.message.delete()
            safe_callback_answer(callback_query, messages.ARGS_CLOSED_MSG)
            return
        
        elif data == "args_empty":
            # Ignore separator buttons
            safe_callback_answer(callback_query)
            return
        
        elif data == "args_back":
            # Clear state and convert submenu back to main menu (edit current message)
            try:
                chat_id = callback_query.message.chat.id
                thread_id = getattr(callback_query.message, 'message_thread_id', None) or 0
                if thread_id:
                    clear_input_state_timer(chat_id, thread_id)
                else:
                    clear_input_state_timer(callback_query.from_user.id)
            except Exception:
                pass
            keyboard = get_args_menu_keyboard(user_id)
            try:
                callback_query.edit_message_text(
                    messages.ARGS_CONFIG_TITLE_MSG.format(groups_msg=messages.ARGS_MENU_DESCRIPTION_MSG),
                    reply_markup=keyboard
                )
            except Exception:
                # If editing failed (deleted/invalid) — just ignore
                pass
            try:
                safe_callback_answer(callback_query)
            except Exception:
                pass
            return
        
        elif data == "args_view_current":
            user_args = get_user_args(user_id)
            message = format_current_args(user_args, user_id)
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(messages.ARGS_EXPORT_SETTINGS_BUTTON_MSG, callback_data="args_export")],
                [InlineKeyboardButton(messages.ARGS_BACK_BUTTON_MSG, callback_data="args_back")]
            ])
            callback_query.edit_message_text(message, reply_markup=keyboard)
            safe_callback_answer(callback_query)
            return
        
        elif data == "args_export":
            user_args = get_user_args(user_id)
            export_message = create_export_message(user_args, user_id)
            keyboard = InlineKeyboardMarkup([[
                InlineKeyboardButton(messages.ARGS_BACK_BUTTON_MSG, callback_data="args_view_current")
            ]])
            callback_query.edit_message_text(export_message, reply_markup=keyboard)
            safe_callback_answer(callback_query, messages.ARGS_SETTINGS_READY_MSG)
            return
        
        elif data == "args_reset_all":
            if save_user_args(user_id, {}):
                keyboard = get_args_menu_keyboard(user_id)
                callback_query.edit_message_text(
                    messages.ARGS_CONFIG_TITLE_MSG.format(groups_msg=messages.ARGS_MENU_DESCRIPTION_MSG) + "\n\n" + messages.ARGS_RESET_SUCCESS_MSG,
                    reply_markup=keyboard
                )
                safe_callback_answer(callback_query, messages.ARGS_ALL_RESET_MSG)
            else:
                safe_callback_answer(callback_query, messages.ARGS_RESET_ERROR_MSG, show_alert=True)
            return
        
        elif data.startswith("args_set_"):
            param_name = data.replace("args_set_", "")
            if not param_name or param_name not in YTDLP_PARAMS:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_PARAM_MSG, show_alert=True)
                return
            
            param_config = YTDLP_PARAMS[param_name]
            user_args = get_user_args(user_id)
            current_value = user_args.get(param_name, param_config.get("default", ""))
            
            if param_config["type"] == "boolean":
                keyboard = get_boolean_menu_keyboard(param_name, current_value, user_id)
                display_value = messages.ARGS_STATUS_TRUE_DISPLAY_MSG if current_value else messages.ARGS_STATUS_FALSE_DISPLAY_MSG
                callback_query.edit_message_text(
                    f"<b>⚙️ {get_param_description(param_config, param_name, messages)}</b>\n\n"
                    f"{messages.ARGS_CURRENT_VALUE_MSG.format(current_value=display_value)}",
                    reply_markup=keyboard
                )
            
            elif param_config["type"] == "select":
                keyboard = get_select_menu_keyboard(param_name, current_value, user_id)
                callback_query.edit_message_text(
                    f"<b>⚙️ {get_param_description(param_config, param_name, messages)}</b>\n\n"
                    f"{messages.ARGS_CURRENT_VALUE_MSG.format(current_value=html.escape(str(current_value)))}",
                    reply_markup=keyboard
                )
            
            elif param_config["type"] in ["text", "json", "number"]:
                # Set user input state keyed by chat/topic (or DM by user_id)
                chat_id = callback_query.message.chat.id
                thread_id = getattr(callback_query.message, 'message_thread_id', None) or 0
                # owner: only the user who opened the prompt may answer it
                state = {"param": param_name, "type": param_config["type"],
                         "owner": callback_query.from_user.id}
                if thread_id:
                    user_input_states_topic[(chat_id, thread_id)] = state
                    start_input_state_timer(chat_id, thread_id)
                else:
                    user_input_states_dm[callback_query.from_user.id] = state
                    start_input_state_timer(callback_query.from_user.id)
                
                if param_config["type"] == "text":
                    message = get_text_input_message(param_name, current_value, user_id)
                elif param_config["type"] == "json":
                    message = get_json_input_message(param_name, current_value, user_id)
                else:  # number
                    message = get_number_input_message(param_name, current_value, user_id)
                
                keyboard = InlineKeyboardMarkup([[
                    InlineKeyboardButton(messages.ARGS_BACK_BUTTON_MSG, callback_data="args_back")
                ]])
                # For text/numeric/JSON parameters, replace current message with input prompt,
                # to avoid duplicating main menu.
                try:
                    callback_query.edit_message_text(
                        message,
                        reply_markup=keyboard
                    )
                except Exception:
                    # Fallback: if editing failed — send as reply in the same topic
                    safe_send_message(chat_id, message, reply_markup=keyboard, message=callback_query.message)
            
            return
        
        elif data.startswith("args_bool_"):
            # Parse: args_bool_{param_name}_{true/false}
            remaining = data.replace("args_bool_", "")
            if not remaining:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_BOOL_MSG, show_alert=True)
                return
                
            value = None  # Initialize value
            if remaining.endswith("_true"):
                param_name = remaining[:-5]  # Remove "_true"
                value = True
            elif remaining.endswith("_false"):
                param_name = remaining[:-6]  # Remove "_false"
                value = False
            else:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_BOOL_MSG, show_alert=True)
                return
            
            # Validate param_name exists in YTDLP_PARAMS
            if param_name not in YTDLP_PARAMS:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_PARAM_MSG, show_alert=True)
                return
            
            # Ensure value is defined
            if value is None:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_BOOL_MSG, show_alert=True)
                return
            
            user_args = get_user_args(user_id)
            current_value = user_args.get(param_name, YTDLP_PARAMS[param_name].get("default", False))
            
            # Save value and enforce mutual exclusivity for paired booleans
            user_args[param_name] = value
            # Enforce pairs: check_certificate vs no_check_certificates
            try:
                if param_name in ("check_certificate", "no_check_certificates"):
                    opposite = "no_check_certificates" if param_name == "check_certificate" else "check_certificate"
                    user_args[opposite] = (not value)
            except Exception:
                pass
            # Enforce pairs: live_from_start vs no_live_from_start
            try:
                if param_name in ("live_from_start", "no_live_from_start"):
                    opposite = "no_live_from_start" if param_name == "live_from_start" else "live_from_start"
                    user_args[opposite] = (not value)
            except Exception:
                pass
            # force_ipv4 / force_ipv6: at most one of them, but turning one off
            # must not force the other protocol on
            try:
                if param_name in ("force_ipv4", "force_ipv6") and value:
                    opposite = "force_ipv6" if param_name == "force_ipv4" else "force_ipv4"
                    user_args[opposite] = False
            except Exception:
                pass
            save_user_args(user_id, user_args)
            
            # Only update message if value actually changed
            if current_value != value:
                # Rebuild main menu to reflect paired toggles instantly
                keyboard = get_args_menu_keyboard(user_id)
                callback_query.edit_message_text(
                    messages.ARGS_CONFIG_TITLE_MSG.format(groups_msg=messages.ARGS_MENU_DESCRIPTION_MSG),
                    reply_markup=keyboard
                )
                try:
                    safe_callback_answer(callback_query, messages.ARGS_BOOL_SET_MSG.format(value='True' if value else 'False'))
                except Exception:
                    pass
            else:
                # Value is the same, just acknowledge
                try:
                    safe_callback_answer(callback_query, messages.ARGS_BOOL_ALREADY_SET_MSG.format(value='True' if value else 'False'))
                except Exception:
                    pass
            return
        
        elif data.startswith("args_select_"):
            # Parse: args_select_{param_name}_{value}
            remaining = data.replace("args_select_", "")
            if not remaining:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_SELECT_MSG, show_alert=True)
                return
                
            # Find the last underscore to separate param_name and value
            last_underscore = remaining.rfind("_")
            if last_underscore == -1:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_SELECT_MSG, show_alert=True)
                return
            param_name = remaining[:last_underscore]
            value = remaining[last_underscore + 1:]
            
            if not param_name or not value:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_SELECT_MSG, show_alert=True)
                return
            
            # Validate param_name exists in YTDLP_PARAMS and the value is one of its options
            if param_name not in YTDLP_PARAMS:
                safe_callback_answer(callback_query, messages.ARGS_INVALID_PARAM_MSG, show_alert=True)
                return
            if value not in YTDLP_PARAMS[param_name].get("options", []):
                safe_callback_answer(callback_query, messages.ARGS_INVALID_SELECT_MSG, show_alert=True)
                return

            user_args = get_user_args(user_id)
            current_value = user_args.get(param_name, YTDLP_PARAMS[param_name].get("default", ""))

            # Always save the value (even if it's the same)
            user_args[param_name] = value
            save_user_args(user_id, user_args)
            
            # Only update message if value actually changed
            if current_value != value:
                keyboard = get_select_menu_keyboard(param_name, value, user_id)
                # If we changed impersonate, it may affect headers; but keep same screen
                callback_query.edit_message_text(
                    f"<b>⚙️ {get_param_description(YTDLP_PARAMS[param_name], param_name, messages)}</b>\n\n"
                    f"{messages.ARGS_CURRENT_VALUE_MSG.format(current_value=value)}",
                    reply_markup=keyboard
                )
                try:
                    safe_callback_answer(callback_query, messages.ARGS_VALUE_SET_MSG.format(value=value))
                except Exception:
                    pass
            else:
                # Value is the same, just acknowledge
                try:
                    safe_callback_answer(callback_query, messages.ARGS_VALUE_ALREADY_SET_MSG.format(value=value))
                except Exception:
                    pass
            return
        
        else:
            # Unknown callback_data
            logger.warning(f"Unknown args callback_data: {data}")
            safe_callback_answer(callback_query, messages.ERROR_OCCURRED_SHORT_MSG, show_alert=False)
            return
        
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        logger.error(f"Error in args callback handler: {e}")
        logger.error(f"Callback data: {data}")
        logger.error(f"Traceback:\n{error_trace}")
        try:
            safe_callback_answer(callback_query, messages.ERROR_OCCURRED_SHORT_MSG, show_alert=False)
        except Exception:
            pass
        # Clear any input states to prevent further errors
        try:
            user_id = callback_query.from_user.id
            chat_id = callback_query.message.chat.id
            thread_id = getattr(callback_query.message, 'message_thread_id', None) or 0
            if thread_id:
                clear_input_state_timer(chat_id, thread_id)
            else:
                clear_input_state_timer(user_id)
        except Exception:
            pass

def handle_args_text_input(app, message):
    messages = get_messages_instance(message.chat.id)
    """Handle text input for args parameters"""
    user_id = message.chat.id  # where to reply
    owner_id = getattr(message, 'from_user', None).id if getattr(message, 'from_user', None) else user_id  # whose settings to change
    text = message.text.strip()
    thread_id = getattr(message, 'message_thread_id', None) or 0
    # Try topic state first, then DM state
    state = None
    if thread_id and (user_id, thread_id) in user_input_states_topic:
        state = user_input_states_topic[(user_id, thread_id)]
        state_key = user_id
    elif not thread_id and owner_id in user_input_states_dm:
        state = user_input_states_dm[owner_id]
        state_key = owner_id  # DM state is keyed by the user, also inside groups
    else:
        return
    if state.get("owner") not in (None, owner_id):
        return  # someone else in the topic: their message is not the answer
    param_name = state["param"]
    param_type = state["type"]

    def _done():
        clear_input_state_timer(state_key, thread_id)

    def _invalid(error_msg):
        safe_send_message(user_id, error_msg, message=message)
        
    try:
        # Validate and process input based on type
        if param_type == "text":
            # Basic validation for text input
            if len(text) > 500:
                error_msg = messages.ARGS_TEXT_TOO_LONG_MSG
                safe_send_message(user_id, error_msg, message=message)
                from HELPERS.logger import log_error_to_channel
                log_error_to_channel(message, error_msg)
                return
            
            ok, error_msg = validate_input(text, param_name, owner_id)
            if not ok:
                _invalid(error_msg)
                return

            # Save the value
            user_args = get_user_args(owner_id)
            user_args[param_name] = text
            save_user_args(owner_id, user_args)

            # Clear state and show success
            _done()
            safe_send_message(
                user_id,
                    messages.ARGS_PARAM_SET_TO_MSG.format(description=get_param_description(YTDLP_PARAMS[param_name], param_name, messages), value=_display_value(param_name, text)),
                parse_mode=enums.ParseMode.HTML,
                message=message
            )
            
        elif param_type == "json":
            # Validate JSON input
            try:
                import json
                parsed_json = json.loads(text)
                if not isinstance(parsed_json, dict):
                    _invalid(messages.ARGS_JSON_MUST_BE_OBJECT_MSG)
                    return
                ok, error_msg = validate_input(text, param_name, owner_id)
                if not ok:
                    _invalid(error_msg)
                    return

                # Save the value
                user_args = get_user_args(owner_id)
                user_args[param_name] = text
                save_user_args(owner_id, user_args)

                # Clear state and show success (header values may be tokens: names only)
                _done()
                shown = ", ".join(parsed_json.keys()) or "{}"
                safe_send_message(
                    user_id,
                    messages.ARGS_PARAM_SET_TO_MSG.format(description=get_param_description(YTDLP_PARAMS[param_name], param_name, messages), value=html.escape(shown)),
                    parse_mode=enums.ParseMode.HTML,
                    message=message
                )
                
            except json.JSONDecodeError:
                error_msg = messages.ARGS_INVALID_JSON_FORMAT_MSG
                safe_send_message(user_id, error_msg, message=message)
                from HELPERS.logger import log_error_to_channel
                log_error_to_channel(message, error_msg)
                return
                
        elif param_type == "number":
            # Special handling for send_as_file parameter
            if param_name == "send_as_file":
                # Handle True/False input for send_as_file
                text_lower = text.lower().strip()
                if text_lower in ["true", "1", "yes", "on"]:
                    value = True
                elif text_lower in ["false", "0", "no", "off"]:
                    value = False
                else:
                    error_msg = messages.ARGS_BOOL_INPUT_MSG
                    safe_send_message(user_id, error_msg, message=message)
                    from HELPERS.logger import log_error_to_channel
                    log_error_to_channel(message, error_msg)
                    return
                
                # Save the value
                user_args = get_user_args(owner_id)
                user_args[param_name] = value
                save_user_args(owner_id, user_args)
                
                # Clear state and show success
                _done()
                safe_send_message(
                    user_id,
                    messages.ARGS_PARAM_SET_TO_MSG.format(description=get_param_description(YTDLP_PARAMS[param_name], param_name, messages), value='True' if value else 'False'),
                    parse_mode=enums.ParseMode.HTML,
                    message=message
                )
            else:
                # Validate number input for other parameters
                try:
                    value = int(text)
                    param_config = YTDLP_PARAMS[param_name]
                    min_val = param_config.get("min", 0)
                    max_val = param_config.get("max", 999999)
                    
                    if value < min_val or value > max_val:
                        safe_send_message(
                            user_id,
                            messages.ARGS_VALUE_MUST_BE_BETWEEN_MSG.format(min_val=min_val, max_val=max_val),
                            message=message
                        )
                        return
                    
                    # Save the value
                    user_args = get_user_args(owner_id)
                    user_args[param_name] = value
                    save_user_args(owner_id, user_args)
                    
                    # Clear state and show success
                    _done()
                    safe_send_message(
                        user_id,
                        messages.ARGS_PARAM_SET_TO_MSG.format(description=get_param_description(YTDLP_PARAMS[param_name], param_name, messages), value=value),
                        parse_mode=enums.ParseMode.HTML,
                        message=message
                    )
                    
                except ValueError:
                    error_msg = messages.ARGS_INVALID_NUMBER_INPUT_MSG
                    safe_send_message(user_id, error_msg, message=message)
                    from HELPERS.logger import log_error_to_channel
                    log_error_to_channel(message, error_msg)
                    return
                
    except Exception as e:
        logger.error(LoggerMsg.ARGS_ERROR_HANDLING_TEXT_INPUT_LOG_MSG.format(error=e))
        error_msg = messages.ARGS_ERROR_PROCESSING_MSG
        safe_send_message(user_id, error_msg, message=message)
        from HELPERS.logger import log_error_to_channel
        log_error_to_channel(message, error_msg)
        # Clear state on error
        _done()

async def _has_args_state(flt, client, message) -> bool:
    # async: a sync filter runs in Client.executor and stalls when handlers saturate it
    try:
        chat_id = message.chat.id
        thread_id = getattr(message, 'message_thread_id', None) or 0
        uid = getattr(message, 'from_user', None).id if getattr(message, 'from_user', None) else chat_id
        if thread_id:
            state = user_input_states_topic.get((chat_id, thread_id))
            return state is not None and state.get("owner") in (None, uid)
        return uid in user_input_states_dm
    except Exception:
        return False

@app.on_message(filters.text & ~filters.regex(r'^/') & filters.create(_has_args_state))
@background_handler(label="args_text_handler", heavy_if=light_only)
def args_text_handler(app, message):
    """Handle text input for args configuration in same chat/topic using stored state"""
    try:
        handle_args_text_input(app, message)
    except Exception as e:
        logger.error(LoggerMsg.ARGS_CRITICAL_ERROR_LOG_MSG.format(error=e))

def args_import_handler(app, message):
    messages = get_messages_instance(message.chat.id)
    """Handle import of settings from forwarded message"""
    try:
        # Check if this is a forwarded message with settings template
        # Check for headers in all supported languages
        args_headers = [
            "📋 Current yt-dlp Arguments:",  # English
            "📋 Текущие аргументы yt-dlp:",  # Russian
            "📋 वर्तमान yt-dlp तर्क:",  # Hindi
            "📋 وسائط yt-dlp الحالية:",  # Arabic
        ]
        
        has_args_header = any(header in message.text for header in args_headers) if message.text else False
        
        if not message.text or not has_args_header:
            logger.info(f"args_import_handler: No text or header not found. Text: {message.text[:100] if message.text else 'None'}")
            return
        
        # Log that we're attempting to import settings
        logger.info(f"{LoggerMsg.ARGS_ATTEMPTING_IMPORT_SETTINGS_LOG_MSG}")
        
        user_id = message.chat.id
        invoker_id = getattr(message, 'from_user', None).id if getattr(message, 'from_user', None) else user_id
        
        logger.info(f"args_import_handler: user_id={user_id}, invoker_id={invoker_id}")
        
        # Subscription check for non-admins
        if int(invoker_id) not in Config.ADMIN and not is_user_in_channel(app, message):
            logger.info(f"args_import_handler: User {invoker_id} not subscribed, skipping import")
            return  # is_user_in_channel already sends subscription message
        
        # Parse settings from message
        parsed_args = parse_import_message(message.text, invoker_id)
        logger.info(f"{LoggerMsg.ARGS_PARSED_SETTINGS_LOG_MSG}")
        logger.info(f"args_import_handler: Parsed {len(parsed_args)} settings: {list(parsed_args.keys())}")
        
        if not parsed_args:
            logger.info(f"args_import_handler: No settings parsed, sending failure message")
            safe_send_message(
                user_id,
                messages.ARGS_FAILED_RECOGNIZE_MSG,
                message=message
            )
            return
        
        # Apply mutual exclusivity for paired booleans
        if "check_certificate" in parsed_args and parsed_args["check_certificate"]:
            parsed_args["no_check_certificates"] = False
        elif "no_check_certificates" in parsed_args and parsed_args["no_check_certificates"]:
            parsed_args["check_certificate"] = False
            
        if "live_from_start" in parsed_args and parsed_args["live_from_start"]:
            parsed_args["no_live_from_start"] = False
        elif "no_live_from_start" in parsed_args and parsed_args["no_live_from_start"]:
            parsed_args["live_from_start"] = False
            
        if "force_ipv4" in parsed_args and parsed_args["force_ipv4"]:
            parsed_args["force_ipv6"] = False
        elif "force_ipv6" in parsed_args and parsed_args["force_ipv6"]:
            parsed_args["force_ipv4"] = False
        
        # Save imported settings
        if save_user_args(invoker_id, parsed_args):
            # Show success message with applied settings count
            applied_count = len(parsed_args)
            success_message = f"{messages.ARGS_SUCCESSFULLY_IMPORTED_MSG.format(applied_count=applied_count)}\n\n"
            
            # Show ALL settings that were applied (no truncation)
            all_settings = []
            for param_name, value in parsed_args.items():
                param_config = YTDLP_PARAMS.get(param_name, {})
                description = param_config.get("description", param_name)
                if isinstance(value, bool):
                    display_value = "✅" if value else "❌"
                else:
                    display_value = _display_value(param_name, value)
                all_settings.append(f"• {html.escape(str(description))}: {display_value}")
            
            if all_settings:
                success_message += messages.ARGS_KEY_SETTINGS_MSG + "\n".join(all_settings)
            
            safe_send_message(
                user_id,
                success_message,
                message=message
            )
        else:
            safe_send_message(
                user_id,
                messages.ARGS_ERROR_SAVING_MSG,
                message=message
            )
            
    except Exception as e:
        logger.error(f"Error in args_import_handler: {e}")
        safe_send_message(
            message.chat.id,
            messages.ARGS_ERROR_IMPORTING_MSG,
            message=message
        )

def _int_arg(value, default=None):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def get_user_ytdlp_args(user_id: int, url: str = None) -> Dict[str, Any]:
    """Translate the user's /args settings into yt-dlp Python API options.

    Only real YoutubeDL parameter names are produced (the CLI-style names used in
    the menu, such as force_ipv4, xff, datebefore or no_continue, are silently
    ignored by yt-dlp). A few bot-side keys are passed along for the download
    code: embed_thumbnail, embed_metadata, audio_format, video_format,
    send_as_file (yt-dlp ignores unknown keys).
    """
    user_args = get_user_args(user_id)
    if user_args:
        logger.info(f"User {user_id} args loaded: {mask_args_for_log(user_args)}")

    ytdlp_args: Dict[str, Any] = {}

    # Thumbnails are on unless the user switched them off
    ytdlp_args["writethumbnail"] = bool(user_args.get("write_thumbnail", True))
    ytdlp_args["embed_thumbnail"] = bool(user_args.get("embed_thumbnail", True))

    if not user_args:
        return ytdlp_args

    # Certificate verification: yt-dlp verifies unless nocheckcertificate is set.
    # The two menu switches are kept opposite; either one disables verification.
    if user_args.get("no_check_certificates") is True or user_args.get("check_certificate") is False:
        ytdlp_args["nocheckcertificate"] = True

    # IPv4 / IPv6 (yt-dlp: source_address)
    if user_args.get("force_ipv6") is True:
        ytdlp_args["source_address"] = "::"
    elif user_args.get("force_ipv4") is True:
        ytdlp_args["source_address"] = "0.0.0.0"

    # Live streams
    if "live_from_start" in user_args or "no_live_from_start" in user_args:
        ytdlp_args["live_from_start"] = bool(user_args.get("live_from_start", True)) and not user_args.get("no_live_from_start", False)

    # Upload date filter (yt-dlp: daterange)
    def _date(name):
        value = str(user_args.get(name) or "")
        return value if re.fullmatch(r"\d{8}", value) and _parse_yyyymmdd(value) else None

    date_on, date_after, date_before = _date("date"), _date("dateafter"), _date("datebefore")
    if date_on or date_after or date_before:
        try:
            from yt_dlp.utils import DateRange
            ytdlp_args["daterange"] = DateRange.day(date_on) if date_on else DateRange(date_after, date_before)
        except Exception as e:
            logger.warning(f"User {user_id}: ignoring date filter: {e}")

    # X-Forwarded-For / geo bypass
    xff = _xff_to_ytdlp(str(user_args.get("xff") or ""))
    if xff:
        ytdlp_args.update(xff)

    # Video container preference
    video_format = user_args.get("video_format")
    if video_format and video_format != "mp4":
        ytdlp_args["video_format"] = video_format
        if video_format == "webm":
            # For webm, use best available format and let FFmpeg convert to webm
            ytdlp_args["format"] = "best"
        else:
            ytdlp_args["format"] = f"best[ext={video_format}]/best[ext=mp4]/best"
        logger.info(f"User {user_id} selected video_format={video_format}, using format={ytdlp_args['format']}")

    headers: Dict[str, str] = {}
    for param_name, value in user_args.items():
        if param_name == "impersonate":
            if value in YTDLP_PARAMS["impersonate"]["options"]:
                ytdlp_args["extractor_args"] = {"generic": {"impersonate": [value]}}

        elif param_name == "referer":
            if value:
                headers["Referer"] = str(value)
                ytdlp_args["referer"] = value

        elif param_name == "user_agent":
            if value:
                headers["User-Agent"] = str(value)

        elif param_name == "http_headers":
            if value and value != "{}":
                try:
                    custom_headers = json.loads(value) if isinstance(value, str) else value
                except (json.JSONDecodeError, ValueError):
                    custom_headers = None
                if isinstance(custom_headers, dict):
                    headers.update({str(k): v for k, v in custom_headers.items()
                                    if isinstance(v, str) and not _CONTROL_CHARS_RE.search(str(k) + v)})

        elif param_name in ("geo_bypass", "hls_use_mpegts"):
            if "geo_bypass" not in ytdlp_args or param_name != "geo_bypass":
                ytdlp_args[param_name] = bool(value)

        elif param_name == "legacy_server_connect":
            ytdlp_args["legacyserverconnect"] = bool(value)

        elif param_name == "ignore_errors":
            ytdlp_args["ignoreerrors"] = bool(value)

        elif param_name == "no_playlist":
            ytdlp_args["noplaylist"] = bool(value)

        elif param_name == "no_part":
            ytdlp_args["nopart"] = bool(value)

        elif param_name == "no_continue":
            ytdlp_args["continuedl"] = not value

        elif param_name in ("embed_metadata", "send_as_file"):
            # handled by the bot (postprocessors / sender), not by yt-dlp
            ytdlp_args[param_name] = bool(value)

        elif param_name == "audio_format":
            if value and value != "best":
                ytdlp_args["audio_format"] = value

        elif param_name == "merge_output_format":
            if value and value != "mp4":
                ytdlp_args["merge_output_format"] = value
                logger.info(f"{LoggerMsg.ARGS_USER_SELECTED_MERGE_OUTPUT_FORMAT_LOG_MSG}")

        elif param_name == "format":
            # legacy key; video_format wins
            if value and "format" not in ytdlp_args:
                ytdlp_args["format"] = value

        elif param_name == "concurrent_fragments":
            number = _int_arg(value)
            if number is not None and number >= 1:
                ytdlp_args["concurrent_fragment_downloads"] = min(number, 16)

        elif param_name in ("sleep_interval", "max_sleep_interval", "retries", "http_chunk_size"):
            number = _int_arg(value)
            if number is not None and number >= 0:
                ytdlp_args[param_name] = number

        elif param_name == "sleep_subtitles":
            number = _int_arg(value)
            if number:
                ytdlp_args["sleep_interval_subtitles"] = number

        elif param_name in ("username", "password", "twofactor"):
            if value:
                ytdlp_args[param_name] = value

        elif param_name in ("min_filesize", "max_filesize"):
            number = _int_arg(value, 0)
            if number > 0:
                # Megabytes in the menu, bytes for yt-dlp
                ytdlp_args[param_name] = number * 1024 * 1024

        elif param_name == "playlist_items":
            if value:
                ytdlp_args["playlist_items"] = value

    if headers:
        ytdlp_args["http_headers"] = headers

    # yt-dlp sleeps a random time in [sleep_interval, max_sleep_interval]
    if ytdlp_args.get("max_sleep_interval") is not None and \
            ytdlp_args.get("max_sleep_interval", 0) < ytdlp_args.get("sleep_interval", 0):
        ytdlp_args.pop("max_sleep_interval")

    logger.info(f"User {user_id} final ytdlp_args: {mask_args_for_log(ytdlp_args)}")
    return ytdlp_args


def merge_user_ytdlp_args(opts: Dict[str, Any], user_args: Dict[str, Any], skip=()) -> Dict[str, Any]:
    """Apply get_user_ytdlp_args() output to yt-dlp options in place.

    Unlike dict.update(), the nested extractor_args / http_headers are merged,
    so e.g. a chosen impersonate target does not wipe the youtube / youtubetab /
    youtubepot extractor arguments the bot set up.
    """
    for key, value in (user_args or {}).items():
        if key in skip:
            continue
        current = opts.get(key)
        if key == "extractor_args" and isinstance(value, dict) and isinstance(current, dict):
            merged = dict(current)
            for ie_key, ie_args in value.items():
                if isinstance(ie_args, dict) and isinstance(merged.get(ie_key), dict):
                    merged[ie_key] = {**merged[ie_key], **ie_args}
                else:
                    merged[ie_key] = ie_args
            opts[key] = merged
        elif key == "http_headers" and isinstance(value, dict) and isinstance(current, dict):
            opts[key] = {**current, **value}
        else:
            opts[key] = value
    return opts

def log_ytdlp_options(user_id: int, ytdlp_opts: dict, operation: str = "download"):
    messages = get_messages_instance(user_id)
    """Log the final yt-dlp options for debugging.

    Only logs when Config.VERBOSE_LOGGING is True (issue #57).
    Sensitive data is always redacted:
    - cookiefile → '[SET]' or '[NOT_SET]'
    - proxy URL → scheme://host:port (credentials stripped)
    """
    try:
        verbose = getattr(Config, 'VERBOSE_LOGGING', False)
        if not verbose:
            return

        # Create a copy to avoid modifying the original
        opts_copy = ytdlp_opts.copy()

        # Redact sensitive information
        if 'cookiefile' in opts_copy:
            cookie_path = opts_copy['cookiefile']
            opts_copy['cookiefile'] = '[SET: cookie.txt present]' if cookie_path else '[NOT_SET]'

        # Redact proxy credentials — keep host:port for debugging
        if 'proxy' in opts_copy and opts_copy['proxy']:
            proxy_val = str(opts_copy['proxy'])
            try:
                from urllib.parse import urlparse
                parsed = urlparse(proxy_val)
                if parsed.hostname:
                    redacted = f"{parsed.scheme or 'proxy'}://{parsed.hostname}"
                    if parsed.port:
                        redacted += f":{parsed.port}"
                    opts_copy['proxy'] = redacted
                else:
                    opts_copy['proxy'] = '[REDACTED]'
            except Exception:
                opts_copy['proxy'] = '[REDACTED]'
        
        # Recursive sanitization for JSON: functions/objects -> string
        def _sanitize(value):
            try:
                if isinstance(value, dict):
                    return {k: _sanitize(v) for k, v in value.items()}
                if isinstance(value, (list, tuple, set)):
                    return [ _sanitize(v) for v in value ]
                if callable(value):
                    return str(value)
                # Convert match_filter and similar objects to string
                value_str = str(value)
                # Keep simple types as is
                if isinstance(value, (str, int, float, bool)) or value is None:
                    return value
                # Replace unsupported types with string representation
                return value_str
            except Exception:
                try:
                    return str(value)
                except Exception:
                    return "<unserializable>"

        # Sanitize copy before JSON
        opts_sanitized = _sanitize(opts_copy)

        # Format the options nicely
        import json
        opts_str = json.dumps(opts_sanitized, indent=2, ensure_ascii=False)
        logger.info(LoggerMsg.ARGS_FINAL_YTDLP_OPTIONS_LOG_MSG.format(user_id=user_id, operation=operation, opts_str=opts_str))
        
    except Exception as e:
        logger.error(LoggerMsg.COOKIES_ERROR_LOGGING_LOG_MSG.format(e=e))
