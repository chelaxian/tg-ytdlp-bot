"""Which database engine the bot runs on.

Config (CONFIG/config.py):
    USE_FIREBASE = True               -> Google Firebase Realtime Database
    USE_FIREBASE = False + DB_ENGINE  -> "json" (dump.json file, legacy local mode)
                                         "sqlite" (local SQLite file)
                                         "postgres" (local or remote PostgreSQL over TLS)

A missing DB_ENGINE keeps the old behaviour of USE_FIREBASE = False (json).
"""
from CONFIG.config import Config

FIREBASE = "firebase"
JSON = "json"
SQLITE = "sqlite"
POSTGRES = "postgres"

_ALIASES = {
    "json": JSON, "dump": JSON, "file": JSON,
    "sqlite": SQLITE, "sqlite3": SQLITE,
    "postgres": POSTGRES, "postgresql": POSTGRES, "pg": POSTGRES,
}

_active = None  # set when the firebase engine falls back to json at runtime


def configured_engine() -> str:
    if getattr(Config, "USE_FIREBASE", True):
        return FIREBASE
    name = str(getattr(Config, "DB_ENGINE", JSON) or JSON).strip().lower()
    try:
        return _ALIASES[name]
    except KeyError:
        raise RuntimeError(f"Unknown DB_ENGINE {name!r}: use json, sqlite or postgres") from None


def active_engine() -> str:
    return _active or configured_engine()


def set_active_engine(engine: str) -> None:
    global _active
    _active = engine


def is_firebase() -> bool:
    return active_engine() == FIREBASE


def is_json() -> bool:
    """dump.json is the store itself: the in-memory mirror must be kept in sync."""
    return active_engine() == JSON


def is_sql() -> bool:
    return active_engine() in (SQLITE, POSTGRES)
