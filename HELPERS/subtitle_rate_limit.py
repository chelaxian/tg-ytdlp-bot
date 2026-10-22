"""Отрицательный кэш HTTP 429 субтитров, независимый от кэша меню (#355)."""
import threading
import time

_TTL = 3600
_MAX_ENTRIES = 2000
_blocked = {}
_lock = threading.Lock()


def subtitles_rate_limited(url, user_id):
    key = (str(user_id), url)
    with _lock:
        deadline = _blocked.get(key)
        if deadline is None:
            return False
        if time.monotonic() < deadline:
            return True
        _blocked.pop(key, None)
        return False


def block_subtitles(url, user_id):
    """Не повторять запросы субтитров этой ссылки час после HTTP 429."""
    key = (str(user_id), url)
    now = time.monotonic()
    with _lock:
        for expired in [k for k, deadline in _blocked.items() if deadline <= now]:
            _blocked.pop(expired, None)
        if key not in _blocked and len(_blocked) >= _MAX_ENTRIES:
            _blocked.pop(next(iter(_blocked)))
        _blocked[key] = now + _TTL
