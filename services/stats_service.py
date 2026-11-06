"""Statistics for the dashboard: a thin, cached facade over StatsCollector.

Every result is cached for a few seconds (per arguments), so many browser tabs or
fast polling never recompute the same aggregate twice. Computations are local and
in-memory: Telegram profiles are filled in by a background worker (see
stats_collector.enable_background_profiles), never during a request.
"""

from __future__ import annotations

import threading
import time
from typing import Any, Callable, Dict, List, Tuple

from CONFIG.config import Config
from DATABASE.firebase_init import db
from HELPERS.channel_guard import get_channel_guard
from HELPERS.logger import logger
from services.stats_collector import get_stats_collector

_cache: Dict[Tuple, Tuple[float, Any]] = {}
_cache_lock = threading.Lock()
_key_locks: Dict[Tuple, threading.Lock] = {}

TTL_DEFAULT = 15
TTL_LIVE = 3
TTL_SLOW = 300   # countries (reads users/*/lang.txt), format users (scans users/*)


def _cached(key: Tuple, ttl: float, compute: Callable[[], Any]) -> Any:
    now = time.time()
    with _cache_lock:
        hit = _cache.get(key)
        if hit and now - hit[0] < ttl:
            return hit[1]
        lock = _key_locks.setdefault(key, threading.Lock())
    with lock:  # one computation per key at a time; others wait and reuse it
        with _cache_lock:
            hit = _cache.get(key)
            if hit and time.time() - hit[0] < ttl:
                return hit[1]
        value = compute()
        with _cache_lock:
            _cache[key] = (time.time(), value)
            if len(_cache) > 2000:
                for old in sorted(_cache, key=lambda k: _cache[k][0])[:500]:
                    _cache.pop(old, None)
        return value


def invalidate() -> None:
    with _cache_lock:
        _cache.clear()


def _c():
    return get_stats_collector()


def fetch_active_users(limit: int = 10, minutes: int | None = None) -> Dict[str, Any]:
    return _cached(("active", limit, minutes), TTL_LIVE, lambda: _c().get_active_users(limit=limit, minutes=minutes))


def fetch_top_downloaders(period: str, limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("top", period, limit), TTL_DEFAULT, lambda: _c().get_top_downloaders(period, limit))


def fetch_top_domains(period: str, limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("domains", period, limit), TTL_DEFAULT, lambda: _c().get_top_domains(period, limit))


def fetch_top_countries(period: str, limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("countries", period, limit), TTL_SLOW, lambda: _c().get_top_countries(period, limit))


def fetch_gender_stats(period: str) -> List[Dict[str, Any]]:
    return _cached(("gender", period), TTL_DEFAULT, lambda: _c().get_gender_stats(period))


def fetch_age_stats(period: str) -> List[Dict[str, Any]]:
    return _cached(("age", period), TTL_DEFAULT, lambda: _c().get_age_stats(period))


def fetch_channel_join_stats(period: str) -> List[Dict[str, Any]]:
    return _cached(("joins", period), TTL_DEFAULT, lambda: _c().get_channel_join_stats(period))


def fetch_top_nsfw_users(limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("nsfw_users", limit), TTL_DEFAULT, lambda: _c().get_top_nsfw_users(limit))


def fetch_top_nsfw_domains(limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("nsfw_domains", limit), TTL_DEFAULT, lambda: _c().get_top_nsfw_domains(limit))


def fetch_top_playlist_users(limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("playlist", limit), TTL_DEFAULT, lambda: _c().get_top_playlist_users(limit))


def fetch_power_users(min_urls: int = 10, days: int = 7, limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("power", min_urls, days, limit), TTL_DEFAULT,
                   lambda: _c().get_power_users(min_urls=min_urls, days=days, limit=limit))


def fetch_top_multi_url_users(period: str, limit: int = 10) -> List[Dict[str, Any]]:
    return _cached(("multi", period, limit), TTL_DEFAULT, lambda: _c().get_top_multi_url_users(period, limit))


def fetch_format_users(limit: int = 20) -> List[Dict[str, Any]]:
    return _cached(("formats", limit), TTL_SLOW, lambda: _c().get_format_users(limit))


def fetch_blocked_users(limit: int = 50) -> List[Dict[str, Any]]:
    return _cached(("blocked", limit), TTL_DEFAULT, lambda: _c().get_blocked_users(limit))


def fetch_user_history(user_id: int, period: str = "all", limit: int = 100) -> List[Dict[str, Any]]:
    return _cached(("history", user_id, period, limit), TTL_DEFAULT,
                   lambda: _c().get_user_history(user_id, period, limit))


def fetch_suspicious_users(period: str, limit: int = 20) -> List[Dict[str, Any]]:
    return _cached(("suspicious", period, limit), TTL_DEFAULT, lambda: _c().get_suspicious_users(period, limit))


def fetch_overview() -> Dict[str, Any]:
    """Headline numbers for the overview screen."""
    def compute():
        collector = _c()
        day = collector._filter_downloads("today")
        week = collector._filter_downloads("week")
        with collector._lock:
            blocked = len(collector._blocked_users)
            last_reload = collector._last_reload_ts
        active = collector.get_active_users(limit=0, minutes=15)
        return {
            "downloads_today": len(day),
            "users_today": len({r.user_id for r in day}),
            "downloads_week": len(week),
            "users_week": len({r.user_id for r in week}),
            "active_15m": int(active.get("total") or 0),
            "blocked_total": blocked,
            "data_loaded_at": int(last_reload or 0),
        }
    return _cached(("overview",), TTL_LIVE, compute)


def _is_guard_ready(guard) -> bool:
    return bool(
        guard
        and getattr(guard, "_running", False)
        and getattr(guard, "_loop", None)
    )


def fetch_recent_channel_events(hours: int = 48, limit: int = 100) -> List[Dict[str, Any]]:
    def compute():
        guard = get_channel_guard()
        if _is_guard_ready(guard) and guard.can_read_admin_log():
            try:
                return guard.export_recent_activity(hours=hours, limit=limit)
            except Exception as exc:
                logger.debug(f"[stats-service] channel guard export failed: {exc}")
        return _c().get_recent_channel_events(hours=hours, limit=limit)
    return _cached(("channel_events", hours, limit), TTL_DEFAULT, compute)


def _db_node(suffix: str):
    base = getattr(Config, "BOT_DB_PATH", f"bot/{getattr(Config, 'BOT_NAME_FOR_USERS', 'tgytdlp_bot')}")
    base = base.rstrip("/")
    suffix = suffix.lstrip("/")
    path = f"{base}/{suffix}" if suffix else base
    return db.child(path)


def block_user(user_id: int, reason: str = "manual") -> None:
    ts = str(int(time.time()))
    payload = {"ID": str(user_id), "timestamp": ts, "blocked_reason": reason}
    _db_node("blocked_users").child(str(user_id)).set(payload)
    # Удаляем пользователя из списка разблокированных и игнорируемых при блокировке
    _db_node("unblocked_users").child(str(user_id)).remove()
    _db_node("ignored_users").child(str(user_id)).remove()
    _c().block_user_local(user_id, reason=reason)
    guard = get_channel_guard()
    if guard:
        guard.mark_user_blocked(user_id, reason)
    invalidate()


def unblock_user(user_id: int) -> None:
    ts = str(int(time.time()))
    payload = {"ID": str(user_id), "timestamp": ts}
    _db_node("unblocked_users").child(str(user_id)).set(payload)
    _db_node("blocked_users").child(str(user_id)).remove()
    _c().unblock_user_local(user_id)
    _reset_antibot_state(user_id)
    guard = get_channel_guard()
    if guard:
        guard.record_manual_unblock(user_id)
    invalidate()


def _reset_antibot_state(user_id) -> None:
    """Drop stale anti-bot history so an unblocked user is not banned again at once."""
    try:
        from HELPERS.anti_bot_protection import reset_user_state
        reset_user_state(int(user_id))
    except Exception:
        pass
