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
from pyrogram import enums
import re
from CONFIG.config import Config
from HELPERS.safe_messeger import safe_send_message
from services.stats_events import capture_message_context

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
                     parse_mode=enums.ParseMode.HTML)

# Send Message to User Only

def send_to_user(message, msg):
    capture_message_context(message)
    user_id = message.chat.id
    # Маскируем секретные данные перед отправкой пользователю
    sanitized_msg = sanitize_error_message(str(msg))
    safe_send_message(user_id, sanitized_msg, parse_mode=enums.ParseMode.HTML, message=message)

# Send Message to All ...

def send_to_all(message, msg, parse_mode=None):
    capture_message_context(message)
    user_id = message.chat.id
    msg_with_id = f"{message.chat.first_name} - {user_id}\n \n{msg}"
    safe_send_message(get_log_channel("general"), msg_with_id, parse_mode=enums.ParseMode.HTML)
    safe_send_message(user_id, msg, parse_mode=parse_mode or enums.ParseMode.HTML, message=message)

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

def sanitize_error_message(error_text: str) -> str:
    """
    Маскирует секретные данные в тексте ошибки перед отправкой пользователю.
    Маскирует:
    - Прокси с логином/паролем: http://user:pass@host:port -> http://***:***@host:port
    - Прокси в разных форматах (http, https, socks4, socks5, socks5h)
    - Пароли в других местах
    """
    if not error_text:
        return error_text
    
    try:
        # Маскируем прокси с логином/паролем в формате protocol://user:pass@host:port
        # Паттерн: protocol://user:pass@host:port или protocol://user:pass@host
        # Поддерживаемые протоколы: http, https, socks4, socks5, socks5h
        proxy_pattern = r'((?:http|https|socks4|socks5|socks5h)://)([^:@\s]+):([^@\s]+)@([^\s\'"\),]+)'
        
        def mask_proxy(match):
            protocol = match.group(1)
            user = match.group(2)
            password = match.group(3)
            host_port = match.group(4)
            # Маскируем логин и пароль, оставляем протокол и хост:порт
            return f"{protocol}***:***@{host_port}"
        
        sanitized = re.sub(proxy_pattern, mask_proxy, error_text, flags=re.IGNORECASE)
        
        # Также маскируем прокси в одинарных/двойных кавычках (для командных строк)
        # Паттерн: '--proxy', 'http://user:pass@host:port'
        proxy_in_quotes_pattern = r"(['\"])((?:http|https|socks4|socks5|socks5h)://)([^:@\s]+):([^@\s]+)@([^\s\'"\)]+)\1"
        
        def mask_proxy_in_quotes(match):
            quote = match.group(1)
            protocol = match.group(2)
            user = match.group(3)
            password = match.group(4)
            host_port = match.group(5)
            return f"{quote}{protocol}***:***@{host_port}{quote}"
        
        sanitized = re.sub(proxy_in_quotes_pattern, mask_proxy_in_quotes, sanitized, flags=re.IGNORECASE)
        
        # Маскируем прокси в квадратных скобках (для списков/массивов)
        proxy_in_brackets_pattern = r"(\['--proxy',\s*['\"])((?:http|https|socks4|socks5|socks5h)://)([^:@\s]+):([^@\s]+)@([^\s\'"\)]+)(['\"])"
        
        def mask_proxy_in_brackets(match):
            prefix = match.group(1)
            protocol = match.group(2)
            user = match.group(3)
            password = match.group(4)
            host_port = match.group(5)
            quote = match.group(6)
            return f"{prefix}{protocol}***:***@{host_port}{quote}"
        
        sanitized = re.sub(proxy_in_brackets_pattern, mask_proxy_in_brackets, sanitized, flags=re.IGNORECASE)
        
        return sanitized
    except Exception as e:
        # Если что-то пошло не так с маскировкой, возвращаем оригинал
        # но логируем ошибку
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
    
    # Маскируем секретные данные в сообщении для пользователя
    sanitized_msg = sanitize_error_message(str(msg))
    
    if url_str:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \nURL: {url_str}\n\n{sanitized_msg}"
    else:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \n{sanitized_msg}"
    # Send to LOG_EXCEPTION channel for error tracking (полная версия для админов)
    safe_send_message(Config.LOG_EXCEPTION, msg_with_id, parse_mode=enums.ParseMode.HTML)
    # Send to user (маскированная версия)
    safe_send_message(user_id, sanitized_msg, parse_mode=enums.ParseMode.HTML, message=message)

# Log error message to LOG_EXCEPTION channel (without sending to user)
def log_error_to_channel(message, msg, url: str = None):
    capture_message_context(message)
    """Log error message to LOG_EXCEPTION channel only.

    url: optional explicit URL that caused the error; if not provided, will be
         extracted from the user's message text/caption when possible.
    """
    user_id = message.chat.id
    url_str = (url or _extract_url_from_message(message) or "").strip()
    if url_str:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \nURL: {url_str}\n\n{msg}"
    else:
        msg_with_id = f"{message.chat.first_name} - {user_id}\n \n{msg}"
    # Send to LOG_EXCEPTION channel for error tracking
    safe_send_message(Config.LOG_EXCEPTION, msg_with_id, parse_mode=enums.ParseMode.HTML)
