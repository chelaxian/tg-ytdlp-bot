"""Settings changed from the web dashboard, kept apart from CONFIG/config.py.

The dashboard never writes Python. It stores a whitelisted, typed set of values
in CONFIG/.dashboard_overrides.json; the bot (magic.py) and the dashboard apply
them onto Config at startup with setattr(). Every value is validated again when
it is applied, so a damaged or hand-edited file can never crash the bot or run
code: invalid entries are skipped and logged.

Keys that grant privileges (ADMIN) or hold Telegram credentials are not editable.
"""

from __future__ import annotations

import ipaddress
import json
import logging
import os
import re
import tempfile
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

OVERRIDES_FILE = Path(os.environ.get("TG_DASHBOARD_PROJECT_DIR", str(Path(__file__).resolve().parent.parent))) / "CONFIG" / ".dashboard_overrides.json"
_LOCK = threading.Lock()

_CONTROL = re.compile(r"[\x00-\x1f\x7f]")
_HOST = re.compile(r"^(?=.{1,253}$)[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*$")


@dataclass(frozen=True)
class Field:
    kind: str                     # text | secret | url | host | port | tg_id | id_list | enum
    section: str
    choices: Tuple[str, ...] = ()
    allow_empty: bool = True


_PROXY_TYPES = ("http", "https", "socks4", "socks5", "socks5h")

SCHEMA: Dict[str, Field] = {
    # proxies
    "PROXY_TYPE": Field("enum", "proxy", _PROXY_TYPES),
    "PROXY_IP": Field("host", "proxy"),
    "PROXY_PORT": Field("port", "proxy"),
    "PROXY_USER": Field("text", "proxy"),
    "PROXY_PASSWORD": Field("secret", "proxy"),
    "PROXY_2_TYPE": Field("enum", "proxy", _PROXY_TYPES),
    "PROXY_2_IP": Field("host", "proxy"),
    "PROXY_2_PORT": Field("port", "proxy"),
    "PROXY_2_USER": Field("text", "proxy"),
    "PROXY_2_PASSWORD": Field("secret", "proxy"),
    "PROXY_SELECT": Field("enum", "proxy", ("round_robin", "random"), allow_empty=False),
    # cookies
    "COOKIE_URL": Field("url", "cookies"),
    "YOUTUBE_COOKIE_URL": Field("url", "cookies"),
    **{f"YOUTUBE_COOKIE_URL_{i}": Field("url", "cookies") for i in range(1, 11)},
    "YOUTUBE_COOKIE_ORDER": Field("enum", "cookies", ("round_robin", "random"), allow_empty=False),
    "YOUTUBE_COOKIE_TEST_URL": Field("url", "cookies"),
    "YOUTUBE_POT_BASE_URL": Field("url", "cookies"),
    "INSTAGRAM_COOKIE_URL": Field("url", "cookies"),
    "TIKTOK_COOKIE_URL": Field("url", "cookies"),
    "FACEBOOK_COOKIE_URL": Field("url", "cookies"),
    "TWITTER_COOKIE_URL": Field("url", "cookies"),
    "VK_COOKIE_URL": Field("url", "cookies"),
    # Telegram channels and links
    "LOGS_ID": Field("tg_id", "channels"),
    "LOGS_VIDEO_ID": Field("tg_id", "channels"),
    "LOGS_NSFW_ID": Field("tg_id", "channels"),
    "LOGS_IMG_ID": Field("tg_id", "channels"),
    "LOGS_PAID_ID": Field("tg_id", "channels"),
    "LOG_EXCEPTION": Field("tg_id", "channels"),
    "SUBSCRIBE_CHANNEL": Field("tg_id", "channels"),
    "SUBSCRIBE_CHANNEL_URL": Field("url", "channels"),
    "MINIAPP_URL": Field("url", "channels"),
    "ALLOWED_GROUP": Field("id_list", "channels"),
}

SECTIONS = ("proxy", "cookies", "channels")


class ValidationError(ValueError):
    pass


def validate(key: str, value: Any) -> Any:
    """Return the normalised value for `key`, or raise ValidationError."""
    field = SCHEMA.get(key)
    if field is None:
        raise ValidationError("unknown setting")
    kind = field.kind

    if kind == "id_list":
        if isinstance(value, str):
            value = [v for v in re.split(r"[\s,;]+", value.strip()) if v]
        if not isinstance(value, (list, tuple)) or len(value) > 500:
            raise ValidationError("expected a list of chat ids")
        out = []
        for item in value:
            out.append(_tg_id(item))
        return out

    if kind in ("tg_id", "port"):
        if value in ("", None):
            if not field.allow_empty:
                raise ValidationError("value required")
            return 0 if kind == "port" else 0
        if kind == "port":
            try:
                port = int(str(value).strip())
            except (TypeError, ValueError):
                raise ValidationError("port must be a number") from None
            if not 1 <= port <= 65535:
                raise ValidationError("port must be 1-65535")
            return port
        return _tg_id(value)

    if not isinstance(value, str):
        raise ValidationError("expected text")
    value = value.strip()
    if _CONTROL.search(value):
        raise ValidationError("control characters are not allowed")
    if value == "":
        if not field.allow_empty:
            raise ValidationError("value required")
        return ""
    if len(value) > 500:
        raise ValidationError("too long")

    if kind == "enum":
        if value not in field.choices:
            raise ValidationError("unsupported value")
        return value
    if kind == "host":
        if _HOST.match(value):
            return value
        try:
            return str(ipaddress.ip_address(value.strip("[]")))
        except ValueError:
            raise ValidationError("expected a host name or IP address") from None
    if kind == "url":
        parsed = urlparse(value)
        if parsed.scheme not in ("http", "https") or not parsed.netloc or " " in value:
            raise ValidationError("expected an http(s):// URL")
        return value
    if kind in ("text", "secret"):
        if len(value) > 200:
            raise ValidationError("too long")
        return value
    raise ValidationError("unsupported setting type")


def _tg_id(value: Any) -> int:
    try:
        number = int(str(value).strip())
    except (TypeError, ValueError):
        raise ValidationError("chat id must be a number") from None
    if abs(number) > 10 ** 16:
        raise ValidationError("chat id out of range")
    return number


# --------------------------------------------------------------------------------------
# Storage
# --------------------------------------------------------------------------------------

def _empty() -> Dict[str, Any]:
    return {"version": 1, "values": {}, "dashboard_auth": {}, "updated_at": 0}


def load(path: Optional[Path] = None) -> Dict[str, Any]:
    path = path or OVERRIDES_FILE
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        return _empty()
    except Exception as exc:
        logger.error("[overrides] %s is unreadable (%s); ignoring it", path, type(exc).__name__)
        return _empty()
    if not isinstance(data, dict):
        return _empty()
    base = _empty()
    if isinstance(data.get("values"), dict):
        base["values"] = data["values"]
    if isinstance(data.get("dashboard_auth"), dict):
        base["dashboard_auth"] = data["dashboard_auth"]
    base["updated_at"] = data.get("updated_at") or 0
    return base


def _write(data: Dict[str, Any], path: Optional[Path] = None) -> None:
    path = path or OVERRIDES_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        try:
            backup = path.with_suffix(path.suffix + ".bak")
            with open(path, "rb") as src, open(backup, "wb") as dst:
                dst.write(src.read())
            os.chmod(backup, 0o600)
        except OSError:
            pass
    fd, tmp = tempfile.mkstemp(prefix=".overrides.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=1, sort_keys=True)
            fh.flush()
            os.fsync(fh.fileno())
        os.chmod(tmp, 0o600)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def save_values(changes: Dict[str, Any], path: Optional[Path] = None) -> Tuple[Dict[str, Any], Dict[str, str]]:
    """Validate and store `changes`. Returns (stored values, {key: error}).

    Nothing is written when any value is invalid. A secret sent as None/"" with
    the special marker {"keep": true} is left unchanged.
    """
    path = path or OVERRIDES_FILE
    errors: Dict[str, str] = {}
    clean: Dict[str, Any] = {}
    for key, value in changes.items():
        if key in SCHEMA and SCHEMA[key].kind == "secret" and isinstance(value, dict) and value.get("keep"):
            continue
        try:
            clean[key] = validate(key, value)
        except ValidationError as exc:
            errors[key] = str(exc)
    if errors:
        return {}, errors
    with _LOCK:
        data = load(path)
        data["values"].update(clean)
        data["updated_at"] = int(time.time())
        _write(data, path)
    return clean, {}


def reset_keys(keys: Iterable[str], path: Optional[Path] = None) -> List[str]:
    path = path or OVERRIDES_FILE
    removed = []
    with _LOCK:
        data = load(path)
        for key in keys:
            if key in data["values"]:
                data["values"].pop(key)
                removed.append(key)
        if removed:
            data["updated_at"] = int(time.time())
            _write(data, path)
    return removed


def get_auth(path: Optional[Path] = None) -> Dict[str, Any]:
    path = path or OVERRIDES_FILE
    return dict(load(path).get("dashboard_auth") or {})


def set_auth(username: str, password_hash: str, path: Optional[Path] = None) -> None:
    path = path or OVERRIDES_FILE
    with _LOCK:
        data = load(path)
        data["dashboard_auth"] = {"username": username, "password_hash": password_hash,
                                  "changed_at": int(time.time())}
        data["updated_at"] = int(time.time())
        _write(data, path)


# --------------------------------------------------------------------------------------
# Applying
# --------------------------------------------------------------------------------------

_BASE: Dict[str, Any] = {}
_APPLIED: Dict[str, Any] = {}


def apply(config_cls, path: Optional[Path] = None) -> Dict[str, Any]:
    """Apply stored overrides onto `config_cls`. Never raises."""
    path = path or OVERRIDES_FILE
    try:
        if not _BASE:
            for key in SCHEMA:
                _BASE[key] = getattr(config_cls, key, None)
        values = load(path).get("values") or {}
        applied = {}
        for key, raw in values.items():
            if key not in SCHEMA:
                logger.warning("[overrides] unknown key %s ignored", key)
                continue
            try:
                value = validate(key, raw)
            except ValidationError as exc:
                logger.warning("[overrides] %s ignored: %s", key, exc)
                continue
            setattr(config_cls, key, value)
            applied[key] = value
        # keys removed from the file since the last apply go back to config.py
        for key in set(_APPLIED) - set(applied):
            setattr(config_cls, key, _BASE.get(key))
        _APPLIED.clear()
        _APPLIED.update(applied)
        if applied:
            logger.info("[overrides] applied %d dashboard setting(s): %s", len(applied), ", ".join(sorted(applied)))
        return applied
    except Exception as exc:  # pragma: no cover - must never break startup
        logger.error("[overrides] could not apply dashboard settings: %s", type(exc).__name__)
        return {}


def base_value(key: str, config_cls=None) -> Any:
    if key in _BASE:
        return _BASE[key]
    return getattr(config_cls, key, None) if config_cls is not None else None


def overridden_keys() -> List[str]:
    return sorted(_APPLIED)
