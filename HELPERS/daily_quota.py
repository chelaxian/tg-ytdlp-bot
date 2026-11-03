"""Per-user daily quotas: videos and images delivered per calendar day.

Counts successfully delivered items (downloads and, with DAILY_QUOTA_COUNT_CACHED,
reposts from the cache). The counters live in CONFIG/.daily_quota.json so a
restart does not reset them; all of them start from zero at 00:00 server local
time. Admins (TURN_OFF_LIMITS_FOR_ADMINS) and groups are exempt.
"""
import datetime
import json
import os
import threading

from CONFIG.limits import LimitsConfig
from HELPERS.logger import logger

VIDEO = "video"
IMAGE = "image"

_PATH = os.path.join("CONFIG", ".daily_quota.json")
_LOCK = threading.Lock()
_STATE = None  # {"date": "YYYY-MM-DD", "users": {"<chat_id>": {"video": n, "image": m}}}

_TEXT = {
    "en": ("⏳ <b>Daily limit reached</b>\n\n"
           "You have already received <b>{used}/{limit}</b> {kind} today.\n"
           "New downloads will be available in <b>{wait}</b> (at 00:00 server time).\n\n"
           "The limit resets every day at midnight.",
           {VIDEO: "videos", IMAGE: "images"}, "{h} h {m} min", "{m} min"),
    "ru": ("⏳ <b>Достигнут дневной лимит</b>\n\n"
           "Сегодня вы уже получили <b>{used}/{limit}</b> {kind}.\n"
           "Новые загрузки будут доступны через <b>{wait}</b> (в 00:00 по времени сервера).\n\n"
           "Лимит обнуляется каждый день в полночь.",
           {VIDEO: "видео", IMAGE: "изображений"}, "{h} ч {m} мин", "{m} мин"),
}


def _limit(kind):
    name = "DAILY_VIDEO_LIMIT" if kind == VIDEO else "DAILY_IMAGE_LIMIT"
    return int(getattr(LimitsConfig, name, 0) or 0)


def _today():
    return datetime.datetime.now().date().isoformat()


def seconds_until_reset(now=None):
    now = now or datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time())
    return max(1, int((midnight - now).total_seconds()))


def _state():
    """Loaded state for today (caller holds _LOCK)."""
    global _STATE
    if _STATE is None:
        try:
            with open(_PATH, "r", encoding="utf-8") as f:
                _STATE = json.load(f)
        except FileNotFoundError:
            _STATE = {}
        except Exception as e:
            logger.warning(f"[QUOTA] cannot read {_PATH}: {e}; starting empty")
            _STATE = {}
    if _STATE.get("date") != _today():
        _STATE = {"date": _today(), "users": {}}
    _STATE.setdefault("users", {})
    return _STATE


def _save(state):
    from HELPERS.atomic_io import atomic_write_json
    try:
        atomic_write_json(_PATH, state)
    except Exception as e:
        logger.warning(f"[QUOTA] cannot save {_PATH}: {e}")


def _chat_id(target):
    if isinstance(target, int):
        return target
    chat = getattr(target, "chat", None)
    chat_id = getattr(chat, "id", None)
    return int(chat_id) if chat_id is not None else None


def is_exempt(target) -> bool:
    chat_id = _chat_id(target)
    if chat_id is None or chat_id < 0:
        return True  # groups and channels
    try:
        from HELPERS.limitter import should_apply_limits_to_admin
        return not should_apply_limits_to_admin(user_id=chat_id)
    except Exception:
        return False


def used(target, kind) -> int:
    chat_id = _chat_id(target)
    with _LOCK:
        return int(_state()["users"].get(str(chat_id), {}).get(kind, 0))


def remaining(target, kind):
    """Items still allowed today; None when there is no quota for this chat."""
    limit = _limit(kind)
    if limit <= 0 or is_exempt(target):
        return None
    return max(0, limit - used(target, kind))


def record(target, kind, count=1, cached=False):
    """Count `count` delivered items; never raises."""
    try:
        if count <= 0 or _limit(kind) <= 0 or is_exempt(target):
            return
        if cached and not getattr(LimitsConfig, "DAILY_QUOTA_COUNT_CACHED", True):
            return
        chat_id = _chat_id(target)
        with _LOCK:
            state = _state()
            user = state["users"].setdefault(str(chat_id), {})
            user[kind] = int(user.get(kind, 0)) + int(count)
            _save(state)
    except Exception as e:
        logger.warning(f"[QUOTA] record failed: {e}")


def _wait_text(lang, seconds):
    _, _, hm, m_only = _TEXT.get(lang, _TEXT["en"])
    hours, minutes = divmod(max(1, (seconds + 59) // 60), 60)
    return hm.format(h=hours, m=minutes) if hours else m_only.format(m=minutes)


def limit_message(target, kind, lang=None):
    if lang is None:
        try:
            from CONFIG.LANGUAGES.language_router import language_router
            lang = (language_router.get_user_language(_chat_id(target)) or "en").lower()[:2]
        except Exception:
            lang = "en"
    template, kinds, _, _ = _TEXT.get(lang, _TEXT["en"])
    limit = _limit(kind)
    return template.format(used=min(used(target, kind), limit), limit=limit, kind=kinds[kind],
                           wait=_wait_text(lang if lang in _TEXT else "en", seconds_until_reset()))


def deny_if_exhausted(message, kind) -> bool:
    """True (and a fresh message with the time left) when today's quota is used up."""
    left = remaining(message, kind)
    if left is None or left > 0:
        return False
    chat_id = _chat_id(message)
    logger.info(f"[QUOTA] {kind} quota exhausted for {chat_id} ({used(message, kind)}/{_limit(kind)})")
    try:
        from HELPERS.safe_messeger import safe_send_message
        safe_send_message(chat_id, limit_message(message, kind), message=message)
    except Exception as e:
        logger.warning(f"[QUOTA] cannot notify {chat_id}: {e}")
    return True
