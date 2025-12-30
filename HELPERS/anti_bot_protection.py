"""
Anti-bot protection module for detecting and blocking malicious bots.
Detects patterns like:
- Repeated identical URLs/links
- Repeated identical commands
- 24/7 activity (no sleep pattern)
"""
import time
import threading
import json
import os
from typing import Optional, Tuple, Dict, List
from collections import defaultdict
from datetime import datetime, timedelta

from CONFIG.limits import LimitsConfig
from CONFIG.config import Config
from HELPERS.logger import logger
from HELPERS.safe_messeger import safe_send_message
from services.stats_service import block_user
from HELPERS.app_instance import get_app


# In-memory storage for tracking user activity
_user_url_history: Dict[int, List[Tuple[str, float]]] = defaultdict(list)  # {user_id: [(url, timestamp), ...]}
_user_command_history: Dict[int, List[Tuple[str, float]]] = defaultdict(list)  # {user_id: [(command, timestamp), ...]}
_user_activity_hours: Dict[int, Dict[int, float]] = defaultdict(dict)  # {user_id: {hour: last_timestamp}}
_user_message_history: Dict[int, List[Tuple[str, float]]] = defaultdict(list)  # {user_id: [(message, timestamp), ...]}
_user_message_timestamps: Dict[int, List[float]] = defaultdict(list)  # {user_id: [timestamps, ...]} for flood detection
_user_message_intervals: Dict[int, List[float]] = defaultdict(list)  # {user_id: [intervals, ...]} for timer detection
_lock = threading.Lock()

# File for persistence
_ANTI_BOT_DATA_FILE = "CONFIG/.anti_bot_data.json"


def _load_from_disk():
    """Load anti-bot data from disk"""
    global _user_url_history, _user_command_history, _user_activity_hours
    
    if os.path.exists(_ANTI_BOT_DATA_FILE):
        try:
            with open(_ANTI_BOT_DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Load URL history
                _user_url_history = {
                    int(k): [(url, ts) for url, ts in v]
                    for k, v in data.get('url_history', {}).items()
                }
                
                # Load command history
                _user_command_history = {
                    int(k): [(cmd, ts) for cmd, ts in v]
                    for k, v in data.get('command_history', {}).items()
                }
                
                # Load activity hours
                _user_activity_hours = {
                    int(k): {int(h): ts for h, ts in v.items()}
                    for k, v in data.get('activity_hours', {}).items()
                }
                
                # Load message history
                _user_message_history = {
                    int(k): [(msg, ts) for msg, ts in v]
                    for k, v in data.get('message_history', {}).items()
                }
                
                # Load message intervals (not critical, can be empty on load)
                # Intervals will be recalculated as messages come in
        except Exception as e:
            logger.error(f"Failed to load anti-bot data: {e}")
            _user_url_history = defaultdict(list)
            _user_command_history = defaultdict(list)
            _user_activity_hours = defaultdict(dict)
    else:
        _user_url_history = defaultdict(list)
        _user_command_history = defaultdict(list)
        _user_activity_hours = defaultdict(dict)
        _user_message_history = defaultdict(list)
        _user_message_history = defaultdict(list)


def _save_to_disk():
    """Save anti-bot data to disk"""
    try:
        os.makedirs(os.path.dirname(_ANTI_BOT_DATA_FILE), exist_ok=True)
        
        with _lock:
            data = {
                'url_history': {
                    str(k): v for k, v in _user_url_history.items()
                },
                'command_history': {
                    str(k): v for k, v in _user_command_history.items()
                },
                'activity_hours': {
                    str(k): {str(h): ts for h, ts in v.items()}
                    for k, v in _user_activity_hours.items()
                },
                'message_history': {
                    str(k): v for k, v in _user_message_history.items()
                }
            }
        
        with open(_ANTI_BOT_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save anti-bot data: {e}")


def _cleanup_old_data(user_id: int, current_time: float):
    """Remove old entries outside time windows"""
    with _lock:
        # Clean URL history
        if user_id in _user_url_history:
            window = LimitsConfig.ANTI_BOT_DUPLICATE_URL_WINDOW
            _user_url_history[user_id] = [
                (url, ts) for url, ts in _user_url_history[user_id]
                if current_time - ts < window
            ]
        
        # Clean command history
        if user_id in _user_command_history:
            window = LimitsConfig.ANTI_BOT_DUPLICATE_COMMAND_WINDOW
            _user_command_history[user_id] = [
                (cmd, ts) for cmd, ts in _user_command_history[user_id]
                if current_time - ts < window
            ]
        
        # Clean message history
        if user_id in _user_message_history:
            window = LimitsConfig.ANTI_BOT_DUPLICATE_MESSAGE_WINDOW
            _user_message_history[user_id] = [
                (msg, ts) for msg, ts in _user_message_history[user_id]
                if current_time - ts < window
            ]
        
        # Clean activity hours (keep only last 24 hours)
        if user_id in _user_activity_hours:
            window = LimitsConfig.ANTI_BOT_24H_WINDOW
            _user_activity_hours[user_id] = {
                hour: ts for hour, ts in _user_activity_hours[user_id].items()
                if current_time - ts < window
            }


def _check_duplicate_urls(user_id: int, url: str, current_time: float) -> Optional[str]:
    """Check if user is sending duplicate URLs too frequently. Returns ban reason if detected."""
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return None
    
    _cleanup_old_data(user_id, current_time)
    
    with _lock:
        if user_id not in _user_url_history:
            _user_url_history[user_id] = []
        
        history = _user_url_history[user_id]
        
        # Find all occurrences of this URL in the window
        window = LimitsConfig.ANTI_BOT_DUPLICATE_URL_WINDOW
        url_occurrences = [
            ts for u, ts in history
            if u == url and current_time - ts < window
        ]
        
        # Check if exceeds limit
        if len(url_occurrences) >= LimitsConfig.ANTI_BOT_DUPLICATE_URL_LIMIT:
            reason = (
                f"Превышен лимит повторяющихся ссылок: "
                f"{len(url_occurrences)} одинаковых ссылок в течение {window // 60} минут"
            )
            return reason
        
        # Add current URL to history
        _user_url_history[user_id].append((url, current_time))
    
    _save_to_disk()
    return None


def _check_timer_interval(user_id: int, current_time: float) -> Optional[str]:
    """Check if user is sending messages with identical intervals (timer pattern). Returns ban reason if detected."""
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return None
    
    with _lock:
        if user_id not in _user_message_history:
            _user_message_history[user_id] = []
        
        history = _user_message_history[user_id]
        window = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_WINDOW
        tolerance = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_TOLERANCE
        min_count = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_MIN_COUNT
        
        # Get recent messages within window
        recent_messages = [
            ts for _, ts in history
            if current_time - ts < window
        ]
        
        # Need at least min_count + 1 messages to have min_count intervals
        if len(recent_messages) < min_count + 1:
            return None
        
        # Sort timestamps
        recent_messages.sort()
        
        # Calculate intervals between consecutive messages
        # Only consider intervals that are at least the minimum interval
        min_interval = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_MIN_INTERVAL
        intervals = []
        for i in range(len(recent_messages) - 1):
            interval = recent_messages[i + 1] - recent_messages[i]
            # Only track intervals that are at least the minimum (to avoid false positives on fast command spam)
            if interval >= min_interval:
                intervals.append(interval)
        
        if len(intervals) < min_count:
            return None
        
        # Group intervals by similarity (within tolerance)
        interval_groups = {}
        
        for interval in intervals:
            # Find similar interval group
            found_group = False
            for group_interval in interval_groups.keys():
                if abs(interval - group_interval) <= tolerance:
                    interval_groups[group_interval].append(interval)
                    found_group = True
                    break
            
            if not found_group:
                interval_groups[interval] = [interval]
        
        # Check if any group has enough occurrences
        for group_interval, group_intervals in interval_groups.items():
            if len(group_intervals) >= min_count:
                reason = (
                    f"Обнаружена отправка по таймеру: "
                    f"одинаковый интервал ~{group_interval:.1f} секунд обнаружен {len(group_intervals)} раз "
                    f"в течение {window // 60} минут"
                )
                return reason
    
    return None


def _check_duplicate_commands(user_id: int, command: str, current_time: float) -> Optional[str]:
    """Check if user is sending duplicate commands too frequently. Returns ban reason if detected."""
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return None
    
    _cleanup_old_data(user_id, current_time)
    
    with _lock:
        if user_id not in _user_command_history:
            _user_command_history[user_id] = []
        
        history = _user_command_history[user_id]
        
        # Find all occurrences of this command in the window
        window = LimitsConfig.ANTI_BOT_DUPLICATE_COMMAND_WINDOW
        cmd_occurrences = [
            ts for c, ts in history
            if c == command and current_time - ts < window
        ]
        
        # Check if exceeds limit
        if len(cmd_occurrences) >= LimitsConfig.ANTI_BOT_DUPLICATE_COMMAND_LIMIT:
            reason = (
                f"Превышен лимит повторяющихся команд: "
                f"{len(cmd_occurrences)} одинаковых команд в течение {window // 60} минут"
            )
            return reason
        
        # Add current command to history
        _user_command_history[user_id].append((command, current_time))
    
    _save_to_disk()
    return None


def _check_flood(user_id: int, current_time: float) -> Optional[str]:
    """Check if user is flooding messages. Returns ban reason if detected.
    Checks if every second within the window has 5+ messages per second."""
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return None
    
    with _lock:
        if user_id not in _user_message_timestamps:
            _user_message_timestamps[user_id] = []
        
        timestamps = _user_message_timestamps[user_id]
        window = LimitsConfig.ANTI_BOT_FLOOD_WINDOW
        max_per_second = LimitsConfig.ANTI_BOT_FLOOD_MESSAGES_PER_SECOND
        
        # Clean old timestamps (keep only within window)
        timestamps[:] = [ts for ts in timestamps if current_time - ts <= window]
        
        # Add current timestamp
        timestamps.append(current_time)
        
        # Check each second in the window
        # We need to verify that for each second in the last 'window' seconds,
        # there were at least 'max_per_second' messages
        violations = 0
        for second_offset in range(window):
            # Check second from (current_time - second_offset - 1) to (current_time - second_offset)
            second_start = current_time - second_offset - 1
            second_end = current_time - second_offset
            
            # Count messages in this second (inclusive of second_end, exclusive of second_start)
            messages_in_second = sum(
                1 for ts in timestamps
                if second_start < ts <= second_end
            )
            
            if messages_in_second >= max_per_second:
                violations += 1
        
        # If every second in the window has violations, it's a flood
        if violations >= window:
            reason = (
                f"Обнаружен флуд: в каждую секунду в течение {window} секунд "
                f"отправлялось {max_per_second} и более сообщений в секунду"
            )
            return reason
    
    return None


def _check_duplicate_messages(user_id: int, message_text: str, current_time: float) -> Optional[str]:
    """Check if user is sending duplicate messages too frequently. Returns ban reason if detected."""
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return None
    
    _cleanup_old_data(user_id, current_time)
    
    with _lock:
        if user_id not in _user_message_history:
            _user_message_history[user_id] = []
        
        history = _user_message_history[user_id]
        
        # Find all occurrences of this message in the window
        window = LimitsConfig.ANTI_BOT_DUPLICATE_MESSAGE_WINDOW
        msg_occurrences = [
            ts for msg, ts in history
            if msg == message_text and current_time - ts < window
        ]
        
        # Check if exceeds limit (no minimum interval check - just count occurrences)
        if len(msg_occurrences) >= LimitsConfig.ANTI_BOT_DUPLICATE_MESSAGE_LIMIT:
            reason = (
                f"Превышен лимит повторяющихся сообщений: "
                f"{len(msg_occurrences)} одинаковых сообщений в течение {window // 60} минут"
            )
            return reason
        
        # Add current message to history
        _user_message_history[user_id].append((message_text, current_time))
    
    _save_to_disk()
    return None


def _check_suspicious_patterns(message_text: str) -> Optional[str]:
    """Check if message matches suspicious bot patterns. Returns ban reason if detected."""
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return None
    
    if len(message_text) < LimitsConfig.ANTI_BOT_PATTERN_MIN_LENGTH:
        return None
    
    # Check if message is only numbers
    if LimitsConfig.ANTI_BOT_BLOCK_NUMBERS_ONLY:
        if message_text.strip().isdigit():
            reason = "Подозрительный паттерн: сообщение состоит только из цифр"
            return reason
    
    # Check if message is only special characters
    if LimitsConfig.ANTI_BOT_BLOCK_SPECIAL_ONLY:
        import string
        if message_text.strip() and all(c in string.punctuation + string.whitespace for c in message_text.strip()):
            reason = "Подозрительный паттерн: сообщение состоит только из спецсимволов"
            return reason
    
    return None


def _check_24h_activity(user_id: int, current_time: float) -> Optional[str]:
    """Check if user is active 24/7 (no sleep pattern). Returns ban reason if detected."""
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return None
    
    _cleanup_old_data(user_id, current_time)
    
    with _lock:
        if user_id not in _user_activity_hours:
            _user_activity_hours[user_id] = {}
        
        # Get current hour (0-23)
        current_hour = datetime.fromtimestamp(current_time).hour
        
        # Update activity for current hour
        _user_activity_hours[user_id][current_hour] = current_time
        
        # Check how many different hours user was active in last 24 hours
        window = LimitsConfig.ANTI_BOT_24H_WINDOW
        active_hours = {
            hour for hour, ts in _user_activity_hours[user_id].items()
            if current_time - ts < window
        }
        
        if len(active_hours) >= LimitsConfig.ANTI_BOT_24H_ACTIVITY_LIMIT:
            reason = (
                f"Обнаружена активность 24/7 (подозрение на бота): "
                f"активность в {len(active_hours)} разных часах в течение 24 часов"
            )
            return reason
    
    _save_to_disk()
    return None


def ban_user_from_channel(user_id: int, reason: str = "manual"):
    """Ban user from subscribe channel if bot is admin.
    
    Args:
        user_id: User ID to ban from channel
        reason: Reason for ban (for logging)
    """
    logger.info(f"[CHANNEL_BAN] Attempting to ban user {user_id} from channel, reason: {reason}")
    
    try:
        app = get_app()
        if app is None:
            logger.error("[CHANNEL_BAN] Cannot ban user from channel: app instance not available")
            return
        
        subscribe_channel = getattr(Config, 'SUBSCRIBE_CHANNEL', None)
        if not subscribe_channel:
            logger.warning("[CHANNEL_BAN] SUBSCRIBE_CHANNEL not configured, skipping channel ban")
            return
        
        logger.info(f"[CHANNEL_BAN] Channel ID: {subscribe_channel}, User ID: {user_id}")
        
        # First, check if bot is admin in the channel
        try:
            from pyrogram.enums import ChatMemberStatus
            from pyrogram import enums
            bot_member = app.get_chat_member(subscribe_channel, "me")
            logger.info(f"[CHANNEL_BAN] Bot status in channel: {bot_member.status}")
            
            if bot_member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                logger.warning(f"[CHANNEL_BAN] Bot is not admin in channel {subscribe_channel} (status: {bot_member.status}), cannot ban user {user_id}")
                return
            
            # Check if bot has ban_users permission
            if hasattr(bot_member, 'privileges') and bot_member.privileges:
                if not bot_member.privileges.can_restrict_members:
                    logger.warning(f"[CHANNEL_BAN] Bot does not have 'can_restrict_members' permission in channel {subscribe_channel}, cannot ban user {user_id}")
                    return
        except Exception as check_error:
            logger.error(f"[CHANNEL_BAN] Failed to check bot permissions in channel: {check_error}")
            # Continue anyway, let ban_chat_member fail with proper error
        
        # Check if user is a member of the channel
        try:
            user_member = app.get_chat_member(subscribe_channel, user_id)
            logger.info(f"[CHANNEL_BAN] User {user_id} status in channel: {user_member.status}")
            
            if user_member.status == ChatMemberStatus.BANNED:
                logger.info(f"[CHANNEL_BAN] User {user_id} is already banned from channel {subscribe_channel}")
                return
        except Exception as check_error:
            error_msg = str(check_error)
            if "USER_NOT_PARTICIPANT" in error_msg or "user not found" in error_msg.lower():
                logger.info(f"[CHANNEL_BAN] User {user_id} is not a member of channel {subscribe_channel}, skipping ban")
                return
            else:
                logger.warning(f"[CHANNEL_BAN] Could not check user membership: {check_error}, proceeding with ban attempt")
        
        # Ban user from channel (permanently)
        try:
            logger.info(f"[CHANNEL_BAN] Calling ban_chat_member for user {user_id} in channel {subscribe_channel}")
            result = app.ban_chat_member(
                chat_id=subscribe_channel,
                user_id=user_id,
                until_date=0  # 0 means permanent ban
            )
            logger.info(f"[CHANNEL_BAN] Successfully banned user {user_id} from channel {subscribe_channel} due to: {reason}")
            logger.debug(f"[CHANNEL_BAN] ban_chat_member result: {result}")
        except Exception as e:
            # Log error but don't fail the ban process
            error_msg = str(e)
            error_type = type(e).__name__
            logger.error(f"[CHANNEL_BAN] Exception type: {error_type}, message: {error_msg}")
            
            if "CHAT_ADMIN_REQUIRED" in error_msg or "not enough rights" in error_msg.lower() or "ADMIN_RIGHTS_REQUIRED" in error_msg:
                logger.warning(f"[CHANNEL_BAN] Bot is not admin or lacks permissions in channel {subscribe_channel}, cannot ban user {user_id}")
            elif "USER_NOT_PARTICIPANT" in error_msg or "user not found" in error_msg.lower():
                logger.info(f"[CHANNEL_BAN] User {user_id} is not a member of channel {subscribe_channel}, skipping ban")
            elif "USER_ADMIN_INVALID" in error_msg or "can't remove chat owner" in error_msg.lower():
                logger.warning(f"[CHANNEL_BAN] Cannot ban user {user_id} - user is admin or owner of channel {subscribe_channel}")
            else:
                logger.error(f"[CHANNEL_BAN] Failed to ban user {user_id} from channel {subscribe_channel}: {error_type}: {error_msg}")
                import traceback
                logger.error(f"[CHANNEL_BAN] Traceback: {traceback.format_exc()}")
    except Exception as e:
        logger.error(f"[CHANNEL_BAN] Unexpected error while banning user {user_id} from channel: {type(e).__name__}: {e}")
        import traceback
        logger.error(f"[CHANNEL_BAN] Traceback: {traceback.format_exc()}")


def _ban_user_from_channel(user_id: int, reason: str):
    """Internal alias for ban_user_from_channel (for backward compatibility)"""
    ban_user_from_channel(user_id, reason)


def _notify_admins(user_id: int, reason: str):
    """Send notification to all admins about banned user"""
    try:
        app = get_app()
        if app is None:
            logger.error("Cannot notify admins: app instance not available")
            return
        
        message = (
            f"🚫 <b>Автоматический бан пользователя</b>\n\n"
            f"👤 <b>Пользователь:</b> <code>{user_id}</code>\n"
            f"📋 <b>Причина:</b> {reason}\n"
            f"⏰ <b>Время:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        
        for admin_id in Config.ADMIN:
            try:
                # Use enums.ParseMode.HTML and ensure it's passed correctly
                from pyrogram import enums as pyro_enums
                safe_send_message(
                    admin_id,
                    message,
                    parse_mode=pyro_enums.ParseMode.HTML
                )
                logger.info(f"Notification sent to admin {admin_id} about banned user {user_id}")
            except Exception as e:
                logger.error(f"Failed to notify admin {admin_id}: {e}")
    except Exception as e:
        logger.error(f"Failed to notify admins: {e}")


def check_and_ban_user(user_id: int, content: str, is_command: bool = False, is_admin: bool = False, full_message_text: Optional[str] = None) -> Tuple[bool, Optional[str]]:
    """
    Check if user should be banned based on anti-bot patterns.
    
    Args:
        user_id: User ID to check
        content: URL or command text
        is_command: True if content is a command, False if URL
        is_admin: True if user is admin (admins are not checked)
        full_message_text: Full message text for duplicate message and pattern checks
    
    Returns:
        (should_ban: bool, reason: Optional[str])
    """
    # Skip check for admins if limits are turned off
    if is_admin and LimitsConfig.TURN_OFF_LIMITS_FOR_ADMINS:
        return (False, None)
    
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return (False, None)
    
    current_time = time.time()
    ban_reason = None
    
    # Check flood first (fastest check)
    ban_reason = _check_flood(user_id, current_time)
    if ban_reason:
        # Ban immediately for flood
        try:
            block_user(user_id, reason=f"auto_bot_protection: {ban_reason}")
            logger.warning(f"User {user_id} banned by anti-bot protection: {ban_reason}")
            ban_user_from_channel(user_id, ban_reason)
            _notify_admins(user_id, ban_reason)
            return (True, ban_reason)
        except Exception as e:
            logger.error(f"Failed to ban user {user_id}: {e}")
            return (False, None)
    
    # Check suspicious patterns if full message text is provided
    if full_message_text:
        ban_reason = _check_suspicious_patterns(full_message_text)
        if ban_reason:
            try:
                block_user(user_id, reason=f"auto_bot_protection: {ban_reason}")
                logger.warning(f"User {user_id} banned by anti-bot protection: {ban_reason}")
                ban_user_from_channel(user_id, ban_reason)
                _notify_admins(user_id, ban_reason)
                return (True, ban_reason)
            except Exception as e:
                logger.error(f"Failed to ban user {user_id}: {e}")
                return (False, None)
        
        # Check for duplicate messages
        ban_reason = _check_duplicate_messages(user_id, full_message_text, current_time)
        if ban_reason:
            try:
                block_user(user_id, reason=f"auto_bot_protection: {ban_reason}")
                logger.warning(f"User {user_id} banned by anti-bot protection: {ban_reason}")
                ban_user_from_channel(user_id, ban_reason)
                _notify_admins(user_id, ban_reason)
                return (True, ban_reason)
            except Exception as e:
                logger.error(f"Failed to ban user {user_id}: {e}")
                return (False, None)
        
        # Check for timer interval pattern (for all messages, not just URLs/commands)
        ban_reason = _check_timer_interval(user_id, current_time)
        if ban_reason:
            try:
                block_user(user_id, reason=f"auto_bot_protection: {ban_reason}")
                logger.warning(f"User {user_id} banned by anti-bot protection: {ban_reason}")
                ban_user_from_channel(user_id, ban_reason)
                _notify_admins(user_id, ban_reason)
                return (True, ban_reason)
            except Exception as e:
                logger.error(f"Failed to ban user {user_id}: {e}")
                return (False, None)
    
    if is_command:
        # Check for duplicate commands
        ban_reason = _check_duplicate_commands(user_id, content, current_time)
    else:
        # Check for duplicate URLs
        ban_reason = _check_duplicate_urls(user_id, content, current_time)
    
    # Always check 24/7 activity
    if not ban_reason:
        ban_reason = _check_24h_activity(user_id, current_time)
    
    if ban_reason:
        # Ban the user
        try:
            block_user(user_id, reason=f"auto_bot_protection: {ban_reason}")
            logger.warning(f"User {user_id} banned by anti-bot protection: {ban_reason}")
            
            # Update local cache immediately if not using Firebase
            use_firebase = getattr(Config, 'USE_FIREBASE', True)
            if not use_firebase:
                try:
                    from DATABASE.cache_db import firebase_cache, _sync_local_cache_to_file
                    # Ensure blocked_users path exists
                    if "bot" not in firebase_cache:
                        firebase_cache["bot"] = {}
                    if Config.BOT_NAME_FOR_USERS not in firebase_cache["bot"]:
                        firebase_cache["bot"][Config.BOT_NAME_FOR_USERS] = {}
                    if "blocked_users" not in firebase_cache["bot"][Config.BOT_NAME_FOR_USERS]:
                        firebase_cache["bot"][Config.BOT_NAME_FOR_USERS]["blocked_users"] = {}
                    
                    # Add user to blocked list
                    firebase_cache["bot"][Config.BOT_NAME_FOR_USERS]["blocked_users"][str(user_id)] = {
                        "ID": str(user_id),
                        "timestamp": str(int(time.time())),
                        "blocked_reason": f"auto_bot_protection: {ban_reason}"
                    }
                    
                    # Remove from unblocked_users if exists
                    if "unblocked_users" in firebase_cache["bot"][Config.BOT_NAME_FOR_USERS]:
                        firebase_cache["bot"][Config.BOT_NAME_FOR_USERS]["unblocked_users"].pop(str(user_id), None)
                    
                    # Sync to file
                    _sync_local_cache_to_file()
                    logger.info(f"Local cache updated: user {user_id} added to blocked_users")
                except Exception as cache_error:
                    logger.error(f"Failed to update local cache after ban: {cache_error}")
            
            # Ban user from subscribe channel
            ban_user_from_channel(user_id, ban_reason)
            
            # Notify admins
            _notify_admins(user_id, ban_reason)
            
            return (True, ban_reason)
        except Exception as e:
            logger.error(f"Failed to ban user {user_id}: {e}")
            return (False, None)
    
    return (False, None)


def record_user_activity(user_id: int, is_admin: bool = False, message_text: Optional[str] = None):
    """
    Record user activity for 24/7 detection and timer interval detection.
    Should be called for any user activity (not just URLs/commands).
    
    Args:
        user_id: User ID
        is_admin: True if user is admin
        message_text: Optional message text for tracking
    """
    if is_admin and LimitsConfig.TURN_OFF_LIMITS_FOR_ADMINS:
        return
    
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return
    
    current_time = time.time()
    
    # Record message for timer interval detection and flood detection
    with _lock:
        if message_text is not None:
            if user_id not in _user_message_history:
                _user_message_history[user_id] = []
            _user_message_history[user_id].append((message_text, current_time))
        
        # Record timestamp for flood detection
        if user_id not in _user_message_timestamps:
            _user_message_timestamps[user_id] = []
        _user_message_timestamps[user_id].append(current_time)
    
    _check_24h_activity(user_id, current_time)


# Load data on module import
_load_from_disk()

