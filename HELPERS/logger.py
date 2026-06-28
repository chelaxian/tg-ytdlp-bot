# ############################################################################################
import logging
import time
import threading
try:
    from sdnotify import SystemdNotifier
    SDNOTIFY_AVAILABLE = True
except ImportError:
    SDNOTIFY_AVAILABLE = False
    SystemdNotifier = None
try:
    from pyrogram import enums
except Exception:
    enums = None
import re
from CONFIG.config import Config
from services.stats_events import capture_message_context


def safe_send_message(*args, **kwargs):
    """Lazy wrapper around HELPERS.safe_messeger.safe_send_message.

    Defers the pyrogram import so that standalone scripts (e.g.
    DATABASE/download_firebase.py) can import this module without pulling
    in the full pyrogram dependency chain.
    """
    from HELPERS.safe_messeger import safe_send_message as _real
    return _real(*args, **kwargs)


def _html_parse_mode():
    """Return pyrogram HTML parse mode, or None when pyrogram is unavailable."""
    if enums is not None:
        return enums.ParseMode.HTML
    return None

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('bot.log', mode='a', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

def close_logger():
    """Close all logging handlers to prevent file descriptor leaks"""
    try:
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)
        logger.info("Logger handlers closed successfully")
    except Exception as e:
        logger.error(f"Error closing logger handlers: {e}")

# WatchDog
if SDNOTIFY_AVAILABLE:
    notifier = SystemdNotifier()
    
    def watchdog_loop():
        while True:
            notifier.notify("WATCHDOG=1")
            logger.info("[Watchdog] Sent WATCHDOG=1")
            time.sleep(30)  # Frequency is less than WatchdogSec

    # Start watchdog thread
    threading.Thread(target=watchdog_loop, daemon=True).start()

    # At the beginning of initialization
    notifier.notify("READY=1")
    logger.info("[Watchdog] Sent READY=1")
else:
    logger.info("[Watchdog] SystemdNotifier not available - watchdog disabled")
# Utility: pick proper log channel per kind

def get_log_channel(kind: str = "general", nsfw: bool = False, paid: bool = False) -> int:
    """Returns the appropriate Telegram chat ID for logs.

    kind: "general" | "video" | "image"
    nsfw: if True and kind is media, route to NSFW channel
    paid: if True, route to paid media channel
    """
    try:
        kind_normalized = (kind or "general").strip().lower()
        if paid:
            # For paid media never fallback to general LOGS_ID
            return getattr(Config, "LOGS_PAID_ID", 0) or getattr(Config, "LOG_EXCEPTION", 0)
        if nsfw and kind_normalized in ("video", "image"):
            # For NSFW media never fallback to general LOGS_ID
            return getattr(Config, "LOGS_NSFW_ID", 0) or getattr(Config, "LOG_EXCEPTION", 0)
        if kind_normalized == "video":
            # For video never fallback to general LOGS_ID
            return getattr(Config, "LOGS_VIDEO_ID", 0) or getattr(Config, "LOG_EXCEPTION", 0)
        if kind_normalized == "image":
            # For image never fallback to general LOGS_ID
            return getattr(Config, "LOGS_IMG_ID", 0) or getattr(Config, "LOG_EXCEPTION", 0)
        # General messages and other kinds use LOGS_ID
        return getattr(Config, "LOGS_ID", 0)
    except Exception:
        # In case of unexpected errors avoid misrouting media to LOGS_ID
        if kind in ("video", "image") or nsfw or paid:
            return getattr(Config, "LOG_EXCEPTION", 0)
        return getattr(Config, "LOG_EXCEPTION", getattr(Config, "LOGS_ID", 0))

# Send Message to Logger

def send_to_logger(message, msg):
    capture_message_context(message)
    user_id = message.chat.id
    msg_with_id = f"{message.chat.first_name} - {user_id}\n \n{msg}"
    # Print (user_id, "-", msg)
    safe_send_message(get_log_channel("general"), msg_with_id,
                     parse_mode=_html_parse_mode())

# Send Message to User Only

def send_to_user(message, msg):
    capture_message_context(message)
    user_id = message.chat.id
    # Маскируем секретные данные перед отправкой пользователю
    sanitized_msg = sanitize_error_message(str(msg))
    safe_send_message(user_id, sanitized_msg, parse_mode=_html_parse_mode(), message=message)

# Send Message to All ...

def send_to_all(message, msg, parse_mode=None):
    capture_message_context(message)
    user_id = message.chat.id
    msg_with_id = f"{message.chat.first_name} - {user_id}\n \n{msg}"
    safe_send_message(get_log_channel("general"), msg_with_id, parse_mode=_html_parse_mode())
    safe_send_message(user_id, msg, parse_mode=parse_mode or _html_parse_mode(), message=message)

# --- Error log throttle/dedup to prevent spam ----------------------------------

_error_throttle_lock = threading.Lock()
_error_throttle_cache: dict[str, float] = {}
_ERROR_THROTTLE_SECONDS = 120


def _should_send_error(msg: str, url: str = "") -> bool:
    key = f"{msg}|{url}"
    now = time.time()
    with _error_throttle_lock:
        last_sent = _error_throttle_cache.get(key)
        if last_sent and (now - last_sent) < _ERROR_THROTTLE_SECONDS:
            return False
        _error_throttle_cache[key] = now
        if len(_error_throttle_cache) > 500:
            cutoff = now - _ERROR_THROTTLE_SECONDS
            _error_throttle_cache.update(
                {k: v for k, v in list(_error_throttle_cache.items()) if v > cutoff}
            )
        return True

# --- Helpers for error logging -------------------------------------------------

def _extract_url_from_message(message) -> str:
    """Best-effort extraction of the first URL from user message text/caption."""
    try:
        text = getattr(message, "text", None) or getattr(message, "caption", None) or ""
        if not text:
            return ""
        match = re.search(r"https?://\S+", text)
        return match.group(0) if match else ""
    except Exception:
        return ""

_PROXY_CREDS_PATTERN = re.compile(
    r'((?:http|https|socks4|socks5|socks5h)://)([^:@\s]+):([^@\s]+)@([^\s\'"\),]+)',
    flags=re.IGNORECASE,
)


def sanitize_error_message(error_text: str) -> str:
    """
    Masks proxy credentials (user:pass@host) in error text before sending to user.
    All proxy types: http, https, socks4, socks5, socks5h.
    """
    if not error_text:
        return error_text
    try:
        return _PROXY_CREDS_PATTERN.sub(r'\1***:***@\4', error_text)
    except Exception as e:
        logger.error(f"Error sanitizing error message: {e}")
        return error_text

# Send Error Message to User and LOG_EXCEPTION channel
def send_error_to_user(message, msg, url: str = None):
    capture_message_context(message)
    """Send error message to user and log it to LOG_EXCEPTION channel.

    url: optional explicit URL that caused the error; if not provided, will be
         extracted from the user's message text/caption when possible.
    """
    user_id = message.chat.id
    url_str = (url or _extract_url_from_message(message) or "").strip()

    sanitized_msg = sanitize_error_message(str(msg))

    if not _should_send_error(sanitized_msg, url_str):
        logger.debug(f"Suppressed duplicate error to LOG_EXCEPTION (throttle): {sanitized_msg[:100]}")
        safe_send_message(user_id, sanitized_msg, parse_mode=_html_parse_mode(), message=message)
        return

    if url_str:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \nURL: {url_str}\n\n{sanitized_msg}"
    else:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \n{sanitized_msg}"
    safe_send_message(Config.LOG_EXCEPTION, msg_with_id, parse_mode=_html_parse_mode())
    safe_send_message(user_id, sanitized_msg, parse_mode=_html_parse_mode(), message=message)

# Log error message to LOG_EXCEPTION channel (without sending to user)
def log_error_to_channel(message, msg, url: str = None):
    capture_message_context(message)
    """Log error message to LOG_EXCEPTION channel only.

    url: optional explicit URL that caused the error; if not provided, will be
         extracted from the user's message text/caption when possible.
    """
    url_str = (url or _extract_url_from_message(message) or "").strip()

    if not _should_send_error(msg, url_str):
        logger.debug(f"Suppressed duplicate error to LOG_EXCEPTION (throttle): {msg[:100]}")
        return

    user_id = message.chat.id
    if url_str:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \nURL: {url_str}\n\n{msg}"
    else:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \n{msg}"
    safe_send_message(Config.LOG_EXCEPTION, msg_with_id, parse_mode=_html_parse_mode())
