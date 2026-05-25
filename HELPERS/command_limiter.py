"""
Command rate limiter with exponential backoff — zero-contention design.

Per-user locks ensure that checking limits for user A never blocks user B.
A background daemon thread handles disk persistence; handler threads never
touch the filesystem.

Bug fix (from original): the old code used a non-reentrant ``threading.Lock``
and acquired it recursively (check_command_limit → _set_cooldown → same lock),
causing a guaranteed deadlock when a user exceeded the command limit.
This rewrite collapses all state into a single per-user lock so no recursive
acquisition is possible.
"""

import time
import os
import json
import threading
from typing import Optional, Tuple, Dict, List

from CONFIG.limits import LimitsConfig
from HELPERS.logger import logger

# ── Constants ────────────────────────────────────────────────────────────

_COMMAND_LIMITS_FILE = "CONFIG/.command_limits.json"
_COMMAND_COOLDOWNS_FILE = "CONFIG/.command_cooldowns.json"
_SAVE_INTERVAL = 30


# ── Per-user state ───────────────────────────────────────────────────────

class _UserData:
    """Command-limit state for a single user."""
    __slots__ = ('lock', 'commands', 'violations', 'cooldown')

    def __init__(self):
        self.lock = threading.Lock()
        self.commands: List[float] = []
        self.violations: int = 0
        self.cooldown: Optional[Dict] = None  # {'until': float, 'duration': float}


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
            logger.error(f"Command-limiter save failed: {exc}")


def _do_save():
    with _registry_lock:
        snapshot = dict(_registry)

    limits_data: Dict = {}
    cooldowns_data: Dict = {}
    for uid, ud in snapshot.items():
        with ud.lock:
            has_limits = ud.commands or ud.violations > 0
            if has_limits:
                limits_data[str(uid)] = {
                    'commands': list(ud.commands),
                    'violations': ud.violations,
                }
            if ud.cooldown is not None:
                cooldowns_data[str(uid)] = dict(ud.cooldown)

    try:
        os.makedirs(os.path.dirname(_COMMAND_LIMITS_FILE) or '.', exist_ok=True)

        tmp = _COMMAND_LIMITS_FILE + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(limits_data, f, indent=2)
        if os.path.exists(_COMMAND_LIMITS_FILE):
            os.replace(tmp, _COMMAND_LIMITS_FILE)
        else:
            os.rename(tmp, _COMMAND_LIMITS_FILE)

        tmp = _COMMAND_COOLDOWNS_FILE + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(cooldowns_data, f, indent=2)
        if os.path.exists(_COMMAND_COOLDOWNS_FILE):
            os.replace(tmp, _COMMAND_COOLDOWNS_FILE)
        else:
            os.rename(tmp, _COMMAND_COOLDOWNS_FILE)
    except Exception:
        for path in (_COMMAND_LIMITS_FILE + '.tmp', _COMMAND_COOLDOWNS_FILE + '.tmp'):
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                pass
        raise


def _load_from_disk():
    global _registry

    registry: Dict[int, _UserData] = {}

    if os.path.exists(_COMMAND_LIMITS_FILE):
        try:
            with open(_COMMAND_LIMITS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for uid_str, user_data in data.items():
                uid = int(uid_str)
                ud = _UserData()
                ud.commands = [float(ts) for ts in user_data.get('commands', [])]
                ud.violations = int(user_data.get('violations', 0))
                registry[uid] = ud
        except Exception as exc:
            logger.error(f"Failed to load command limits: {exc}")

    if os.path.exists(_COMMAND_COOLDOWNS_FILE):
        try:
            with open(_COMMAND_COOLDOWNS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for uid_str, cd_data in data.items():
                uid = int(uid_str)
                if uid not in registry:
                    registry[uid] = _UserData()
                registry[uid].cooldown = {
                    'until': float(cd_data.get('until', 0)),
                    'duration': float(cd_data.get('duration', 0)),
                }
                if 'violations' in cd_data:
                    registry[uid].violations = int(cd_data['violations'])
        except Exception as exc:
            logger.error(f"Failed to load command cooldowns: {exc}")

    _registry = registry


# ── Public API ───────────────────────────────────────────────────────────

def check_command_limit(user_id: int, is_admin: bool = False) -> Tuple[bool, Optional[str]]:
    """
    Check if user can send another command.
    Returns ``(allowed, message)``.  When *allowed* is False, *message*
    contains the cooldown info.
    """
    if is_admin and LimitsConfig.TURN_OFF_LIMITS_FOR_ADMINS:
        return (True, None)

    now = time.time()
    ud = _get_user(user_id)

    with ud.lock:
        # ── Check cooldown ───────────────────────────────────────────
        if ud.cooldown is not None:
            if now < ud.cooldown['until']:
                remaining = ud.cooldown['until'] - now
                minutes = int(remaining // 60)
                seconds = int(remaining % 60)
                if minutes > 0:
                    msg = f"Too many commands. Cooldown: {minutes}m {seconds}s remaining"
                else:
                    msg = f"Too many commands. Cooldown: {seconds}s remaining"
                return (False, msg)
            ud.cooldown = None

        # ── Cleanup old commands ──────────────────────────────────────
        cut = now - 60
        i = 0
        while i < len(ud.commands) and ud.commands[i] < cut:
            i += 1
        if i:
            del ud.commands[:i]

        # ── Check limit ───────────────────────────────────────────────
        if len(ud.commands) >= LimitsConfig.COMMAND_LIMIT_PER_MINUTE:
            ud.violations += 1
            violations = ud.violations
            duration = LimitsConfig.COMMAND_COOLDOWN_INITIAL * (
                LimitsConfig.COMMAND_COOLDOWN_MULTIPLIER ** violations
            )
            ud.cooldown = {'until': now + duration, 'duration': duration}
            ud.commands.clear()

            minutes = int(duration // 60)
            seconds = int(duration % 60)
            _dirty.set()
            logger.warning(
                f"Command spam detected for user {user_id}. "
                f"Cooldown: {duration}s (violations: {violations})"
            )
            if minutes > 0:
                return (False, f"Too many commands (max {LimitsConfig.COMMAND_LIMIT_PER_MINUTE}/minute). Cooldown: {minutes}m {seconds}s")
            return (False, f"Too many commands (max {LimitsConfig.COMMAND_LIMIT_PER_MINUTE}/minute). Cooldown: {seconds}s")

        # ── Record command ────────────────────────────────────────────
        ud.commands.append(now)
        if ud.violations > 0 and len(ud.commands) == 0:
            ud.violations = 0

    _dirty.set()
    return (True, None)


# ── Module initialization ────────────────────────────────────────────────

_load_from_disk()

_save_thread = threading.Thread(target=_save_worker, name="cmdlimit-save", daemon=True)
_save_thread.start()
