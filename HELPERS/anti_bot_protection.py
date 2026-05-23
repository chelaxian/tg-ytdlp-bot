"""
Anti-bot protection — zero-contention, per-user isolation.

Architecture
~~~~~~~~~~~~
* **Per-user locks** — each user's state is protected by its own
  ``threading.Lock``.  Checks for user A never block user B.
* **Background persistence** — a daemon thread writes snapshots to
  disk every ~60 s.  Handler threads never touch the filesystem.
* **Double-checked registry** — user lookup is a plain ``dict.get()``
  on the fast path; a global lock is taken only when a new
  ``_UserData`` must be created.
* **Offloaded bans** — ``block_user``, Telegram API calls and admin
  notifications run in a dedicated ``ThreadPoolExecutor`` so that
  message handlers return immediately.
"""

import time
import threading
import json
import os
import string
from typing import Optional, Tuple, Dict, List
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from CONFIG.limits import LimitsConfig
from CONFIG.config import Config
from HELPERS.logger import logger
from HELPERS.safe_messeger import safe_send_message
from services.stats_service import block_user
from HELPERS.app_instance import get_app


# ── Constants ────────────────────────────────────────────────────────────

_ANTI_BOT_DATA_FILE = "CONFIG/.anti_bot_data.json"
_SAVE_INTERVAL = 60
_BAN_POOL_SIZE = 4


# ── Per-user state ───────────────────────────────────────────────────────

class _UserData:
    """All anti-bot tracking data for a single user, guarded by its own lock."""
    __slots__ = (
        'lock',
        'url_history',
        'command_history',
        'message_history',
        'message_timestamps',
        'activity_hours',
    )

    def __init__(self):
        self.lock = threading.Lock()
        self.url_history: List[Tuple[str, float]] = []
        self.command_history: List[Tuple[str, float]] = []
        self.message_history: List[Tuple[str, float]] = []
        self.message_timestamps: List[float] = []
        self.activity_hours: Dict[int, float] = {}


# ── Global registry (lock-free fast path) ────────────────────────────────

_registry: Dict[int, _UserData] = {}
_registry_lock = threading.Lock()
_bot_start_time: float = time.time()


def _get_user(user_id: int) -> _UserData:
    """Return (or atomically create) the ``_UserData`` for *user_id*."""
    ud = _registry.get(user_id)
    if ud is not None:
        return ud
    with _registry_lock:
        ud = _registry.get(user_id)
        if ud is None:
            ud = _UserData()
            _registry[user_id] = ud
        return ud


# ── Background persistence ───────────────────────────────────────────────

_dirty = threading.Event()
_save_stop = threading.Event()


def _save_worker():
    """Daemon thread: snapshots all user data to disk every _SAVE_INTERVAL seconds."""
    while not _save_stop.is_set():
        _dirty.wait(timeout=_SAVE_INTERVAL)
        _dirty.clear()
        if _save_stop.is_set():
            return
        try:
            _do_save()
        except Exception as exc:
            logger.error(f"Anti-bot save failed: {exc}")


def _do_save():
    """Collect a snapshot of every user and write atomically."""
    with _registry_lock:
        snapshot = dict(_registry)

    url_h: Dict = {}
    cmd_h: Dict = {}
    msg_h: Dict = {}
    msg_ts: Dict = {}
    act_h: Dict = {}

    for uid, ud in snapshot.items():
        with ud.lock:
            if ud.url_history:
                url_h[str(uid)] = list(ud.url_history)
            if ud.command_history:
                cmd_h[str(uid)] = list(ud.command_history)
            if ud.message_history:
                msg_h[str(uid)] = list(ud.message_history)
            if ud.message_timestamps:
                msg_ts[str(uid)] = list(ud.message_timestamps)
            if ud.activity_hours:
                act_h[str(uid)] = {str(h): ts for h, ts in ud.activity_hours.items()}

    data = {
        'bot_start_time': _bot_start_time,
        'url_history': url_h,
        'command_history': cmd_h,
        'message_history': msg_h,
        'message_timestamps': msg_ts,
        'activity_hours': act_h,
        'message_intervals': {},
    }

    tmp = _ANTI_BOT_DATA_FILE + '.tmp'
    try:
        os.makedirs(os.path.dirname(_ANTI_BOT_DATA_FILE) or '.', exist_ok=True)
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        if os.path.exists(_ANTI_BOT_DATA_FILE):
            os.replace(tmp, _ANTI_BOT_DATA_FILE)
        else:
            os.rename(tmp, _ANTI_BOT_DATA_FILE)
    except Exception:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except OSError:
            pass
        raise


def _load_from_disk():
    """Load anti-bot data from disk on startup (backward-compatible format)."""
    global _bot_start_time, _registry

    if not os.path.exists(_ANTI_BOT_DATA_FILE):
        logger.info(
            f"Initialized new anti-bot data file, bot_start_time: "
            f"{datetime.fromtimestamp(_bot_start_time).strftime('%Y-%m-%d %H:%M:%S')}"
        )
        return

    try:
        with open(_ANTI_BOT_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        _bot_start_time = float(data.get('bot_start_time', time.time()))

        all_uids: set = set()
        for key in ('url_history', 'command_history', 'message_history',
                     'message_timestamps', 'activity_hours'):
            for uid_str in data.get(key, {}):
                all_uids.add(int(uid_str))

        registry: Dict[int, _UserData] = {}
        for uid in all_uids:
            uid_s = str(uid)
            ud = _UserData()
            ud.url_history = [
                (str(x[0]), float(x[1]))
                for x in data.get('url_history', {}).get(uid_s, [])
            ]
            ud.command_history = [
                (str(x[0]), float(x[1]))
                for x in data.get('command_history', {}).get(uid_s, [])
            ]
            ud.message_history = [
                (str(x[0]), float(x[1]))
                for x in data.get('message_history', {}).get(uid_s, [])
            ]
            ud.message_timestamps = [
                float(ts) for ts in data.get('message_timestamps', {}).get(uid_s, [])
            ]
            ud.activity_hours = {
                int(h): float(ts)
                for h, ts in data.get('activity_hours', {}).get(uid_s, {}).items()
            }
            registry[uid] = ud

        _registry = registry
        logger.info(
            f"Loaded anti-bot data: {len(_registry)} users, "
            f"bot_start_time: "
            f"{datetime.fromtimestamp(_bot_start_time).strftime('%Y-%m-%d %H:%M:%S')}"
        )
    except Exception as exc:
        logger.error(f"Failed to load anti-bot data: {exc}")


# ── Background ban executor ──────────────────────────────────────────────

_ban_pool = ThreadPoolExecutor(max_workers=_BAN_POOL_SIZE, thread_name_prefix="antiban")


def _do_ban_async(user_id: int, reason: str):
    """Submit all ban side-effects to a background thread pool."""
    def _task():
        try:
            block_user(user_id, reason=f"auto_bot_protection: {reason}")
            logger.warning(f"User {user_id} banned by anti-bot: {reason}")
        except Exception as exc:
            logger.error(f"Failed to block user {user_id}: {exc}")

        try:
            use_firebase = getattr(Config, 'USE_FIREBASE', True)
            if not use_firebase:
                from DATABASE.cache_db import firebase_cache, _sync_local_cache_to_file
                if "bot" not in firebase_cache:
                    firebase_cache["bot"] = {}
                bn = Config.BOT_NAME_FOR_USERS
                if bn not in firebase_cache["bot"]:
                    firebase_cache["bot"][bn] = {}
                if "blocked_users" not in firebase_cache["bot"][bn]:
                    firebase_cache["bot"][bn]["blocked_users"] = {}
                firebase_cache["bot"][bn]["blocked_users"][str(user_id)] = {
                    "ID": str(user_id),
                    "timestamp": str(int(time.time())),
                    "blocked_reason": f"auto_bot_protection: {reason}",
                }
                if "unblocked_users" in firebase_cache["bot"][bn]:
                    firebase_cache["bot"][bn]["unblocked_users"].pop(str(user_id), None)
                _sync_local_cache_to_file()
                logger.info(f"Local cache updated: user {user_id} added to blocked_users")
        except Exception as exc:
            logger.error(f"Failed to update local cache after ban: {exc}")

        try:
            ban_user_from_channel(user_id, reason)
        except Exception as exc:
            logger.error(f"Failed to ban {user_id} from channel: {exc}")

        try:
            _notify_admins(user_id, reason)
        except Exception as exc:
            logger.error(f"Failed to notify admins about {user_id}: {exc}")

    _ban_pool.submit(_task)


# ── Lazy cleanup helpers ─────────────────────────────────────────────────

def _prune_tuples(lst: List, now: float, window: float):
    """Remove (.., ts) entries whose timestamp < now - window.  In-place, O(k)."""
    cut = now - window
    i = 0
    while i < len(lst) and lst[i][1] < cut:
        i += 1
    if i:
        del lst[:i]


def _prune_floats(lst: List[float], now: float, window: float):
    """Remove raw floats older than now - window.  In-place, O(k)."""
    cut = now - window
    i = 0
    while i < len(lst) and lst[i] < cut:
        i += 1
    if i:
        del lst[:i]


def _prune_hours(d: Dict, now: float, window: float):
    """Remove hour entries whose timestamp < now - window."""
    cut = now - window
    stale = [k for k, v in d.items() if v < cut]
    for k in stale:
        del d[k]


def _cleanup_user(ud: _UserData, now: float):
    """Prune all stale data for one user.  Caller must hold ``ud.lock``."""
    _prune_tuples(ud.url_history, now, LimitsConfig.ANTI_BOT_DUPLICATE_URL_WINDOW)
    _prune_tuples(ud.command_history, now, LimitsConfig.ANTI_BOT_DUPLICATE_COMMAND_WINDOW)
    _prune_tuples(ud.message_history, now, LimitsConfig.ANTI_BOT_DUPLICATE_MESSAGE_WINDOW)
    _prune_floats(ud.message_timestamps, now, LimitsConfig.ANTI_BOT_FLOOD_WINDOW)
    _prune_hours(ud.activity_hours, now, LimitsConfig.ANTI_BOT_24H_WINDOW)


# ── Detection functions (operate on _UserData under its lock) ────────────

def _check_flood(ud: _UserData, now: float) -> Optional[str]:
    """Flood: >= max_per_second messages in EVERY second of the window."""
    window = LimitsConfig.ANTI_BOT_FLOOD_WINDOW
    max_ps = LimitsConfig.ANTI_BOT_FLOOD_MESSAGES_PER_SECOND
    ts = ud.message_timestamps

    if len(ts) < max_ps * window:
        return None

    buckets: Dict[int, int] = {}
    for t in ts:
        s = int(t)
        buckets[s] = buckets.get(s, 0) + 1

    cur_sec = int(now)
    for offset in range(window):
        if buckets.get(cur_sec - offset, 0) < max_ps:
            return None

    return (
        f"Обнаружен флуд: в каждую секунду в течение {window} секунд "
        f"отправлялось {max_ps} и более сообщений в секунду"
    )


def _check_suspicious_patterns(text: str) -> Optional[str]:
    """Pure function — no state access."""
    if len(text) < LimitsConfig.ANTI_BOT_PATTERN_MIN_LENGTH:
        return None
    stripped = text.strip()
    if LimitsConfig.ANTI_BOT_BLOCK_NUMBERS_ONLY and stripped.isdigit():
        return "Подозрительный паттерн: сообщение состоит только из цифр"
    if LimitsConfig.ANTI_BOT_BLOCK_SPECIAL_ONLY and stripped and all(
        c in string.punctuation + string.whitespace for c in stripped
    ):
        return "Подозрительный паттерн: сообщение состоит только из спецсимволов"
    return None


def _check_duplicate_messages(ud: _UserData, text: str, now: float) -> Optional[str]:
    """Read-only check against existing message_history (written by record_user_activity)."""
    window = LimitsConfig.ANTI_BOT_DUPLICATE_MESSAGE_WINDOW
    limit = LimitsConfig.ANTI_BOT_DUPLICATE_MESSAGE_LIMIT
    cut = now - window
    count = sum(1 for msg, ts in ud.message_history if ts >= cut and msg == text)
    if count >= limit:
        return (
            f"Превышен лимит повторяющихся сообщений: "
            f"{count} одинаковых сообщений в течение {window // 60} минут"
        )
    return None


def _check_timer_interval(ud: _UserData, now: float) -> Optional[str]:
    """Detect messages sent at identical intervals (timer pattern)."""
    window = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_WINDOW
    tolerance = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_TOLERANCE
    min_count = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_MIN_COUNT
    min_interval = LimitsConfig.ANTI_BOT_TIMER_INTERVAL_MIN_INTERVAL

    cut = now - window
    timestamps = sorted(ts for _, ts in ud.message_history if ts >= cut)

    if len(timestamps) < min_count + 1:
        return None

    intervals = [
        timestamps[i + 1] - timestamps[i]
        for i in range(len(timestamps) - 1)
        if timestamps[i + 1] - timestamps[i] >= min_interval
    ]

    if len(intervals) < min_count:
        return None

    groups: Dict[float, List[float]] = {}
    for iv in intervals:
        matched = False
        for key in groups:
            if abs(iv - key) <= tolerance:
                groups[key].append(iv)
                matched = True
                break
        if not matched:
            groups[iv] = [iv]

    for key, members in groups.items():
        if len(members) >= min_count:
            return (
                f"Обнаружена отправка по таймеру: "
                f"одинаковый интервал ~{key:.1f} секунд обнаружен {len(members)} раз "
                f"в течение {window // 60} минут"
            )
    return None


def _check_duplicate_urls(ud: _UserData, url: str, now: float) -> Optional[str]:
    """Check and record URL.  Returns reason if limit exceeded."""
    window = LimitsConfig.ANTI_BOT_DUPLICATE_URL_WINDOW
    limit = LimitsConfig.ANTI_BOT_DUPLICATE_URL_LIMIT
    cut = now - window
    count = sum(1 for u, ts in ud.url_history if ts >= cut and u == url)
    if count >= limit:
        return (
            f"Превышен лимит повторяющихся ссылок: "
            f"{count} одинаковых ссылок в течение {window // 60} минут"
        )
    ud.url_history.append((url, now))
    return None


def _check_duplicate_commands(ud: _UserData, cmd: str, now: float) -> Optional[str]:
    """Check and record command.  Returns reason if limit exceeded."""
    window = LimitsConfig.ANTI_BOT_DUPLICATE_COMMAND_WINDOW
    limit = LimitsConfig.ANTI_BOT_DUPLICATE_COMMAND_LIMIT
    cut = now - window
    count = sum(1 for c, ts in ud.command_history if ts >= cut and c == cmd)
    if count >= limit:
        return (
            f"Превышен лимит повторяющихся команд: "
            f"{count} одинаковых команд в течение {window // 60} минут"
        )
    ud.command_history.append((cmd, now))
    return None


def _check_24h_activity(ud: _UserData, now: float) -> Optional[str]:
    """Detect 24/7 activity (no sleep pattern).  Read-only on activity_hours."""
    window_s = LimitsConfig.ANTI_BOT_24H_WINDOW
    frequency = LimitsConfig.ANTI_BOT_24H_ACTIVITY_FREQUENCY
    window_h = window_s / 3600.0

    if window_h < 2:
        return None

    hours_since_start = (now - _bot_start_time) / 3600.0
    if hours_since_start < window_h:
        return None

    if _bot_start_time > now:
        return None

    all_ts = list(ud.activity_hours.values())
    hours_in_window = int(window_h)

    if len(all_ts) < frequency:
        return None

    active_hours: List[int] = []
    hour_activity_counts: Dict[int, int] = {}

    for offset in range(1, hours_in_window + 1):
        h_start = now - offset * 3600
        h_end = h_start + 3600
        in_hour = [t for t in all_ts if h_start <= t < h_end]
        if in_hour:
            active_hours.append(offset)
            hour_activity_counts[offset] = len(in_hour)

    if frequency <= hours_in_window:
        required_hours = frequency
        if len(active_hours) >= required_hours:
            return (
                f"Обнаружена активность 24/7 (подозрение на бота): "
                f"активность в {len(active_hours)} из {hours_in_window} часов "
                f"в течение последних {hours_in_window} часов "
                f"(требуется: {required_hours} активных часов из {hours_in_window})"
            )
    else:
        req_per_hour = frequency // hours_in_window
        sufficient = sum(1 for c in hour_activity_counts.values() if c >= req_per_hour)
        if sufficient >= hours_in_window:
            return (
                f"Обнаружена активность 24/7 (подозрение на бота): "
                f"в каждом из {hours_in_window} часов минимум {req_per_hour} активностей "
                f"в течение последних {hours_in_window} часов"
            )
    return None


# ── Channel ban (blocking — for admin commands & background bans) ────────

def ban_user_from_channel(user_id: int, reason: str = "manual"):
    """Ban user from subscribe channel if bot is admin."""
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

        try:
            from pyrogram.enums import ChatMemberStatus
            bot_member = app.get_chat_member(subscribe_channel, "me")
            logger.info(f"[CHANNEL_BAN] Bot status in channel: {bot_member.status}")

            if bot_member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                logger.warning(
                    f"[CHANNEL_BAN] Bot is not admin in channel {subscribe_channel} "
                    f"(status: {bot_member.status}), cannot ban user {user_id}"
                )
                return

            if hasattr(bot_member, 'privileges') and bot_member.privileges:
                if not bot_member.privileges.can_restrict_members:
                    logger.warning(
                        f"[CHANNEL_BAN] Bot does not have 'can_restrict_members' permission "
                        f"in channel {subscribe_channel}, cannot ban user {user_id}"
                    )
                    return
        except Exception as check_error:
            logger.error(f"[CHANNEL_BAN] Failed to check bot permissions in channel: {check_error}")

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

        try:
            logger.info(f"[CHANNEL_BAN] Calling ban_chat_member for user {user_id} in channel {subscribe_channel}")
            result = app.ban_chat_member(
                chat_id=subscribe_channel,
                user_id=user_id,
                until_date=0,
            )
            logger.info(f"[CHANNEL_BAN] Successfully banned user {user_id} from channel {subscribe_channel} due to: {reason}")
            logger.debug(f"[CHANNEL_BAN] ban_chat_member result: {result}")
        except Exception as e:
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


# ── Admin notification ───────────────────────────────────────────────────

def _notify_admins(user_id: int, reason: str):
    """Send notification to all admins about banned user."""
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
                from pyrogram import enums as pyro_enums
                safe_send_message(
                    admin_id,
                    message,
                    parse_mode=pyro_enums.ParseMode.HTML,
                )
                logger.info(f"Notification sent to admin {admin_id} about banned user {user_id}")
            except Exception as e:
                logger.error(f"Failed to notify admin {admin_id}: {e}")
    except Exception as e:
        logger.error(f"Failed to notify admins: {e}")


# ── Public API ───────────────────────────────────────────────────────────

def record_user_activity(user_id: int, is_admin: bool = False, message_text: Optional[str] = None):
    """
    Record user activity.  Called for every incoming message.

    Fast path: acquires only the per-user lock, no I/O.
    """
    if is_admin and LimitsConfig.TURN_OFF_LIMITS_FOR_ADMINS:
        return
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return

    now = time.time()
    ud = _get_user(user_id)

    with ud.lock:
        if message_text is not None:
            ud.message_history.append((message_text, now))
        ud.message_timestamps.append(now)
        hour_idx = int((now - _bot_start_time) / 3600)
        ud.activity_hours[hour_idx] = now

    _dirty.set()


def check_and_ban_user(
    user_id: int,
    content: str,
    is_command: bool = False,
    is_admin: bool = False,
    full_message_text: Optional[str] = None,
) -> Tuple[bool, Optional[str]]:
    """
    Run all anti-bot checks for this user + content.

    Returns ``(should_ban, reason)``.  Ban side-effects are submitted
    to a background pool so this function returns immediately.
    """
    if is_admin and LimitsConfig.TURN_OFF_LIMITS_FOR_ADMINS:
        return (False, None)
    if not LimitsConfig.ANTI_BOT_PROTECTION_ENABLED:
        return (False, None)

    now = time.time()
    ud = _get_user(user_id)

    with ud.lock:
        _cleanup_user(ud, now)

        reason = _check_flood(ud, now)
        if reason:
            _do_ban_async(user_id, reason)
            return (True, reason)

        if full_message_text:
            reason = _check_suspicious_patterns(full_message_text)
            if reason:
                _do_ban_async(user_id, reason)
                return (True, reason)

            reason = _check_duplicate_messages(ud, full_message_text, now)
            if reason:
                _do_ban_async(user_id, reason)
                return (True, reason)

            reason = _check_timer_interval(ud, now)
            if reason:
                _do_ban_async(user_id, reason)
                return (True, reason)

        if is_command:
            reason = _check_duplicate_commands(ud, content, now)
        else:
            reason = _check_duplicate_urls(ud, content, now)
        if reason:
            _do_ban_async(user_id, reason)
            return (True, reason)

        reason = _check_24h_activity(ud, now)
        if reason:
            _do_ban_async(user_id, reason)
            return (True, reason)

    _dirty.set()
    return (False, None)


# ── Module initialization ────────────────────────────────────────────────

_load_from_disk()

_save_thread = threading.Thread(target=_save_worker, name="antibot-save", daemon=True)
_save_thread.start()
