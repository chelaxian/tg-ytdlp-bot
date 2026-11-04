"""Dashboard authentication: password hashing, sessions, login throttling, CSRF.

* Passwords are PBKDF2-SHA256 (600k iterations, random salt per hash). The hash
  set from the dashboard lives in CONFIG/.dashboard_overrides.json and takes
  precedence over DASHBOARD_USERNAME / DASHBOARD_PASSWORD in config.py.
* A default or short config password still logs in, but only into the forced
  "set a new password" screen.
* Session tokens are random 256-bit values. Only their SHA-256 is kept (in memory
  and in CONFIG/.dashboard_sessions.json, written on login/logout only).
* Each session has its own CSRF token; every POST must echo it in X-CSRF-Token
  and come from the dashboard's own origin.
* Failed logins are throttled per IP and per username with a capped backoff.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import secrets
import tempfile
import threading
import time
from collections import OrderedDict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

from CONFIG import overrides
from CONFIG.config import Config

SESSIONS_FILE = Path(os.environ.get("TG_DASHBOARD_PROJECT_DIR", str(Path(__file__).resolve().parent.parent))) / "CONFIG" / ".dashboard_sessions.json"
SESSION_COOKIE = "tgdash_session"
CSRF_HEADER = "x-csrf-token"

IDLE_TTL = int(getattr(Config, "DASHBOARD_SESSION_IDLE", 30 * 60))
ABSOLUTE_TTL = int(getattr(Config, "DASHBOARD_SESSION_MAX", 12 * 3600))
PBKDF2_ITERATIONS = 600_000
MIN_PASSWORD_LENGTH = 10
_WEAK_DEFAULTS = {"admin123", "admin", "password", "changeme"}

FREE_ATTEMPTS = 5
MAX_LOCK_SECONDS = 15 * 60


# --------------------------------------------------------------------------------------
# Passwords
# --------------------------------------------------------------------------------------

def hash_password(password: str, *, iterations: int = PBKDF2_ITERATIONS) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return "pbkdf2_sha256${}${}${}".format(
        iterations,
        base64.b64encode(salt).decode("ascii"),
        base64.b64encode(digest).decode("ascii"),
    )


def verify_password(password: str, encoded: str) -> bool:
    try:
        algo, iterations, salt_b64, digest_b64 = encoded.split("$")
        if algo != "pbkdf2_sha256":
            return False
        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(digest_b64)
        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, int(iterations))
    except Exception:
        return False
    return hmac.compare_digest(actual, expected)


def password_problem(password: str) -> Optional[str]:
    """None when acceptable, else an error code for the UI."""
    if len(password) < MIN_PASSWORD_LENGTH:
        return "too_short"
    if len(password) > 256:
        return "too_long"
    if password.lower() in _WEAK_DEFAULTS:
        return "too_weak"
    return None


def _same(a: str, b: str) -> bool:
    return hmac.compare_digest(hashlib.sha256(a.encode("utf-8")).digest(),
                               hashlib.sha256(b.encode("utf-8")).digest())


def check_credentials(username: str, password: str) -> Tuple[bool, bool]:
    """Returns (valid, must_change_password)."""
    stored = overrides.get_auth()
    if stored.get("password_hash"):
        ok_user = _same(username, str(stored.get("username") or ""))
        ok_pass = verify_password(password, stored["password_hash"])
        return ok_user and ok_pass, False
    cfg_user = str(getattr(Config, "DASHBOARD_USERNAME", "admin") or "admin")
    cfg_pass = str(getattr(Config, "DASHBOARD_PASSWORD", "") or "")
    # keep the cost of a check constant whether or not a hash is configured
    hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), b"tgdash-constant", 50_000)
    if not cfg_pass:
        return False, True
    ok = _same(username, cfg_user) and _same(password, cfg_pass)
    return ok, password_problem(cfg_pass) is not None


def current_username() -> str:
    stored = overrides.get_auth()
    if stored.get("username"):
        return str(stored["username"])
    return str(getattr(Config, "DASHBOARD_USERNAME", "admin") or "admin")


def set_password(username: str, new_password: str) -> None:
    overrides.set_auth(username, hash_password(new_password))


# --------------------------------------------------------------------------------------
# Sessions
# --------------------------------------------------------------------------------------

@dataclass
class Session:
    user: str
    created: float
    last_seen: float
    ip: str
    csrf: str
    must_change: bool = False


def _token_key(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


class SessionStore:
    def __init__(self, path: Path = SESSIONS_FILE):
        self._path = path
        self._lock = threading.Lock()
        self._sessions: Dict[str, Session] = {}
        self._load()

    def _load(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as fh:
                raw = json.load(fh)
        except Exception:
            return
        now = time.time()
        if not isinstance(raw, dict):
            return
        for key, item in raw.items():
            try:
                session = Session(**item)
            except Exception:
                continue
            if self._alive(session, now):
                self._sessions[key] = session

    def _persist_locked(self) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            fd, tmp = tempfile.mkstemp(prefix=".sessions.", dir=str(self._path.parent))
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump({k: asdict(v) for k, v in self._sessions.items()}, fh)
            os.chmod(tmp, 0o600)
            os.replace(tmp, self._path)
        except OSError:
            pass

    @staticmethod
    def _alive(session: Session, now: float) -> bool:
        return (now - session.last_seen) < IDLE_TTL and (now - session.created) < ABSOLUTE_TTL

    def create(self, user: str, ip: str, must_change: bool) -> Tuple[str, Session]:
        token = secrets.token_urlsafe(32)
        now = time.time()
        session = Session(user=user, created=now, last_seen=now, ip=ip,
                          csrf=secrets.token_urlsafe(24), must_change=must_change)
        with self._lock:
            self._sessions = {k: v for k, v in self._sessions.items() if self._alive(v, now)}
            self._sessions[_token_key(token)] = session
            self._persist_locked()
        return token, session

    def get(self, token: Optional[str]) -> Optional[Session]:
        if not token or len(token) > 128:
            return None
        key = _token_key(token)
        now = time.time()
        with self._lock:
            session = self._sessions.get(key)
            if session is None:
                return None
            if not self._alive(session, now):
                self._sessions.pop(key, None)
                self._persist_locked()
                return None
            session.last_seen = now  # in memory only; the file keeps the login time
            return session

    def drop(self, token: Optional[str]) -> None:
        if not token:
            return
        with self._lock:
            if self._sessions.pop(_token_key(token), None) is not None:
                self._persist_locked()

    def drop_all(self) -> None:
        with self._lock:
            self._sessions.clear()
            self._persist_locked()

    def clear_must_change(self, token: str) -> None:
        with self._lock:
            session = self._sessions.get(_token_key(token))
            if session:
                session.must_change = False
                self._persist_locked()


# --------------------------------------------------------------------------------------
# Login throttling
# --------------------------------------------------------------------------------------

class LoginThrottle:
    """Per-key failure counter: FREE_ATTEMPTS tries, then 30 s doubling up to 15 min."""

    def __init__(self, capacity: int = 5000):
        self._lock = threading.Lock()
        self._data: "OrderedDict[str, Tuple[int, float]]" = OrderedDict()
        self._capacity = capacity

    def retry_after(self, *keys: str) -> int:
        now = time.time()
        wait = 0.0
        with self._lock:
            for key in keys:
                fails, until = self._data.get(key, (0, 0.0))
                if until > now:
                    wait = max(wait, until - now)
        return int(wait + 0.999)

    def fail(self, *keys: str) -> None:
        now = time.time()
        with self._lock:
            for key in keys:
                fails, _ = self._data.pop(key, (0, 0.0))
                fails += 1
                until = 0.0
                if fails >= FREE_ATTEMPTS:
                    until = now + min(MAX_LOCK_SECONDS, 30 * 2 ** min(6, fails - FREE_ATTEMPTS))
                self._data[key] = (fails, until)
            while len(self._data) > self._capacity:
                self._data.popitem(last=False)

    def success(self, *keys: str) -> None:
        with self._lock:
            for key in keys:
                self._data.pop(key, None)


# --------------------------------------------------------------------------------------
# Request helpers
# --------------------------------------------------------------------------------------

def _trusted_proxies() -> set:
    value = getattr(Config, "DASHBOARD_TRUSTED_PROXIES", ()) or ()
    if isinstance(value, str):
        value = [v.strip() for v in value.split(",")]
    return {str(v) for v in value if v}


def client_ip(request) -> str:
    peer = request.client.host if request.client else "unknown"
    if peer in _trusted_proxies():
        forwarded = request.headers.get("x-forwarded-for", "")
        if forwarded:
            return forwarded.split(",")[0].strip()[:64] or peer
    return peer


def is_https(request) -> bool:
    if request.url.scheme == "https":
        return True
    if (request.client and request.client.host in _trusted_proxies()
            and request.headers.get("x-forwarded-proto", "").lower() == "https"):
        return True
    return False


def same_origin(request) -> bool:
    """POSTs must come from the page itself (Origin, else Referer, must match Host)."""
    host = request.headers.get("host", "")
    source = request.headers.get("origin") or request.headers.get("referer") or ""
    if not source or not host:
        return False
    try:
        from urllib.parse import urlparse
        parsed = urlparse(source)
        scheme = "https" if is_https(request) else request.url.scheme
        return parsed.scheme == scheme and parsed.netloc == host
    except Exception:
        return False


sessions = SessionStore()
throttle = LoginThrottle()
