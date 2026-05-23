"""
Rate limiter for URL requests per user — zero-contention design.

Per-user locks ensure that checking limits for user A never blocks user B.
A background daemon thread handles disk persistence; handler threads never
touch the filesystem.
"""

import time
import os
import json
import threading
from typing import Optional, Tuple, Dict, List

from CONFIG.config import Config
from CONFIG.limits import LimitsConfig
from HELPERS.logger import logger

# ── Constants ────────────────────────────────────────────────────────────

_RATE_LIMITS_FILE = "CONFIG/.rate_limits.json"
_COOLDOWNS_FILE = "CONFIG/.cooldowns.json"
_SAVE_INTERVAL = 30


# ── Per-user state ───────────────────────────────────────────────────────

class _UserData:
    """Rate-limit state for a single user."""
    __slots__ = ('lock', 'minute', 'hour', 'day', 'cooldown')

    def __init__(self):
        self.lock = threading.Lock()
        self.minute: List[float] = []
        self.hour: List[float] = []
        self.day: List[float] = []
        self.cooldown: Optional[Dict] = None  # {'period': str, 'until': float}


# ── Global registry (lock-free fast path) ────────────────────────────────

_registry: Dict[int, _UserData] = {}
_registry_lock = threading.Lock()


def _get_user(user_id: int) -> _UserData:
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
    while not _save_stop.is_set():
        _dirty.wait(timeout=_SAVE_INTERVAL)
        _dirty.clear()
        if _save_stop.is_set():
            return
        try:
            _do_save()
        except Exception as exc:
            logger.error(f"Rate-limiter save failed: {exc}")


def _do_save():
    with _registry_lock:
        snapshot = dict(_registry)

    limits_data: Dict = {}
    cooldowns_data: Dict = {}
    for uid, ud in snapshot.items():
        with ud.lock:
            has_limits = ud.minute or ud.hour or ud.day
            if has_limits:
                limits_data[str(uid)] = {
                    'minute': list(ud.minute),
                    'hour': list(ud.hour),
                    'day': list(ud.day),
                }
            if ud.cooldown is not None:
                cooldowns_data[str(uid)] = dict(ud.cooldown)

    try:
        os.makedirs(os.path.dirname(_RATE_LIMITS_FILE) or '.', exist_ok=True)

        tmp = _RATE_LIMITS_FILE + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(limits_data, f, indent=2)
        if os.path.exists(_RATE_LIMITS_FILE):
            os.replace(tmp, _RATE_LIMITS_FILE)
        else:
            os.rename(tmp, _RATE_LIMITS_FILE)

        tmp = _COOLDOWNS_FILE + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(cooldowns_data, f, indent=2)
        if os.path.exists(_COOLDOWNS_FILE):
            os.replace(tmp, _COOLDOWNS_FILE)
        else:
            os.rename(tmp, _COOLDOWNS_FILE)
    except Exception:
        for path in (_RATE_LIMITS_FILE + '.tmp', _COOLDOWNS_FILE + '.tmp'):
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                pass
        raise


def _load_from_disk():
    global _registry

    registry: Dict[int, _UserData] = {}

    if os.path.exists(_RATE_LIMITS_FILE):
        try:
            with open(_RATE_LIMITS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for uid_str, user_data in data.items():
                uid = int(uid_str)
                ud = _UserData()
                ud.minute = [float(ts) for ts in user_data.get('minute', [])]
                ud.hour = [float(ts) for ts in user_data.get('hour', [])]
                ud.day = [float(ts) for ts in user_data.get('day', [])]
                registry[uid] = ud
        except Exception as exc:
            logger.error(f"Failed to load rate limits: {exc}")

    if os.path.exists(_COOLDOWNS_FILE):
        try:
            with open(_COOLDOWNS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for uid_str, cd_data in data.items():
                uid = int(uid_str)
                if uid not in registry:
                    registry[uid] = _UserData()
                registry[uid].cooldown = {
                    'period': cd_data.get('period', 'minute'),
                    'until': float(cd_data.get('until', 0)),
                }
        except Exception as exc:
            logger.error(f"Failed to load cooldowns: {exc}")

    _registry = registry


# ── Lazy cleanup ─────────────────────────────────────────────────────────

def _cleanup_user(ud: _UserData, now: float):
    """Prune stale timestamps. Caller must hold ud.lock."""
    cut_60 = now - 60
    cut_3600 = now - 3600
    cut_86400 = now - 86400

    i = 0
    while i < len(ud.minute) and ud.minute[i] < cut_60:
        i += 1
    if i:
        del ud.minute[:i]

    i = 0
    while i < len(ud.hour) and ud.hour[i] < cut_3600:
        i += 1
    if i:
        del ud.hour[:i]

    i = 0
    while i < len(ud.day) and ud.day[i] < cut_86400:
        i += 1
    if i:
        del ud.day[:i]


# ── Public API ───────────────────────────────────────────────────────────

def check_rate_limit(user_id: int, is_admin: bool = False) -> Tuple[bool, Optional[str]]:
    """
    Check if user can send another URL.
    Returns ``(allowed, message)``.  When *allowed* is False, *message*
    contains the cooldown info.
    """
    if is_admin and LimitsConfig.TURN_OFF_LIMITS_FOR_ADMINS:
        return (True, None)

    now = time.time()
    ud = _get_user(user_id)

    with ud.lock:
        if ud.cooldown is not None:
            if now < ud.cooldown['until']:
                period = ud.cooldown.get('period', 'unknown')
                remaining = ud.cooldown['until'] - now
                hours = int(remaining // 3600)
                minutes = int((remaining % 3600) // 60)
                seconds = int(remaining % 60)

                if period == 'day':
                    msg = f"Rate limit exceeded. Cooldown: {hours}h {minutes}m {seconds}s remaining"
                elif period == 'hour':
                    msg = f"Rate limit exceeded. Cooldown: {minutes}m {seconds}s remaining"
                else:
                    msg = f"Rate limit exceeded. Cooldown: {seconds}s remaining"
                return (False, msg)
            ud.cooldown = None

        _cleanup_user(ud, now)

        if len(ud.minute) >= LimitsConfig.RATE_LIMIT_PER_MINUTE:
            duration = LimitsConfig.RATE_LIMIT_COOLDOWN_MINUTE
            ud.cooldown = {'period': 'minute', 'until': now + duration}
            minutes = int(duration // 60)
            _dirty.set()
            return (False, f"Rate limit exceeded (max {LimitsConfig.RATE_LIMIT_PER_MINUTE} URLs/minute). Cooldown: {minutes}m remaining")

        if len(ud.hour) >= LimitsConfig.RATE_LIMIT_PER_HOUR:
            duration = LimitsConfig.RATE_LIMIT_COOLDOWN_HOUR
            ud.cooldown = {'period': 'hour', 'until': now + duration}
            hours = int(duration // 3600)
            _dirty.set()
            return (False, f"Rate limit exceeded (max {LimitsConfig.RATE_LIMIT_PER_HOUR} URLs/hour). Cooldown: {hours}h remaining")

        if len(ud.day) >= LimitsConfig.RATE_LIMIT_PER_DAY:
            duration = LimitsConfig.RATE_LIMIT_COOLDOWN_DAY
            ud.cooldown = {'period': 'day', 'until': now + duration}
            hours = int(duration // 3600)
            _dirty.set()
            return (False, f"Rate limit exceeded (max {LimitsConfig.RATE_LIMIT_PER_DAY} URLs/day). Cooldown: {hours}h remaining")

        ud.minute.append(now)
        ud.hour.append(now)
        ud.day.append(now)

    _dirty.set()
    return (True, None)


# ── Module initialization ────────────────────────────────────────────────

_load_from_disk()

_save_thread = threading.Thread(target=_save_worker, name="ratelimit-save", daemon=True)
_save_thread.start()
