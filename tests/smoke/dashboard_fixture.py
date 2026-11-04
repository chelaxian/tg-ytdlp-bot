"""Offline harness for the dashboard: stubs the bot modules, uses a temp CONFIG dir.

Used by tests/smoke/test_m_dashboard.py and by
  python tests/smoke/dashboard_fixture.py --serve 8765
for a local visual check with demo data (login demo / demo-password-123).
"""

from __future__ import annotations

import os
import random
import sys
import tempfile
import time
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

TMP = Path(tempfile.mkdtemp(prefix="tgdash-"))
DEMO_USER = "demo"
DEMO_PASSWORD = "demo-password-123"


def _module(name: str, **attrs):
    mod = types.ModuleType(name)
    mod.__dict__.update(attrs)
    sys.modules[name] = mod
    return mod


class Config:
    BOT_NAME_FOR_USERS = "tgytdlp_demo_bot"
    DASHBOARD_USERNAME = DEMO_USER
    DASHBOARD_PASSWORD = DEMO_PASSWORD
    PORN_DOMAINS_FILE = "TXT/porn_domains.txt"
    PORN_KEYWORDS_FILE = "TXT/porn_keywords.txt"
    SUPPORTED_SITES_FILE = "TXT/supported_sites.txt"
    PROXY_TYPE = "http"; PROXY_IP = ""; PROXY_PORT = 3128; PROXY_USER = "u"; PROXY_PASSWORD = "secret-proxy-pass"
    PROXY_2_TYPE = "socks5"; PROXY_2_IP = ""; PROXY_2_PORT = 1080; PROXY_2_USER = ""; PROXY_2_PASSWORD = ""
    PROXY_SELECT = "round_robin"
    COOKIE_URL = "http://localhost/cookies/cookie.txt"; YOUTUBE_COOKIE_URL = "http://localhost/cookies/youtube.txt"
    YOUTUBE_COOKIE_ORDER = "round_robin"; YOUTUBE_COOKIE_TEST_URL = "https://www.youtube.com/watch?v=_GuOjXYl5ew"
    YOUTUBE_POT_BASE_URL = "http://localhost:4416"
    LOGS_ID = -1001; LOGS_VIDEO_ID = -1002; LOGS_NSFW_ID = -1003; LOGS_IMG_ID = -1004; LOGS_PAID_ID = -1005
    LOG_EXCEPTION = -1006; SUBSCRIBE_CHANNEL = -1007; SUBSCRIBE_CHANNEL_URL = "https://t.me/+demo"
    MINIAPP_URL = "https://t.me/demo_bot/?startapp"; ALLOWED_GROUP = [-100123, -100456]
    ADMIN = [1]
    BOT_TOKEN = "123:SECRET-TOKEN"
    RELOAD_CACHE_EVERY = 4


NAMES = ["Анна", "Дмитрий", "Lena", "Ахмед", "Maria", "Игорь", "Sam", "Ольга", "Ravi", "Кирилл", "<script>x</script>", "Zoë"]
DOMAINS = ["youtube.com", "tiktok.com", "instagram.com", "vk.com", "x.com", "reddit.com", "rutube.ru", "twitch.tv"]


def _user(i: int, **extra):
    u = {"user_id": 100000 + i, "name": NAMES[i % len(NAMES)], "username": f"user{i}" if i % 3 else None,
         "flag": random.choice(["🇷🇺", "🇺🇸", "🇮🇳", "🇩🇪", "🏳"]), "country_code": random.choice(["RU", "US", "IN", "DE"]),
         "gender": random.choice(["male", "female", "unknown"]), "age": None}
    u.update(extra)
    return u


class FakeCollector:
    def __init__(self):
        import threading
        self._lock = threading.RLock()
        self._blocked_users = {7: 1}
        self._last_reload_ts = time.time() - 40
        now = time.time()
        self.downloads = [types.SimpleNamespace(user_id=100000 + random.randint(0, 40), timestamp=now - random.randint(0, 9 * 86400))
                          for _ in range(800)]

    def _filter_downloads(self, period):
        span = {"today": 86400, "week": 7 * 86400, "month": 30 * 86400}.get(period)
        now = time.time()
        return [d for d in self.downloads if span is None or d.timestamp >= now - span]

    def get_active_users(self, limit=10, minutes=None):
        now = time.time()
        items = []
        for i in range(12):
            live = i < 3
            items.append(_user(i, last_event_ts=now - (5 if live else i * 70), url=f"https://{DOMAINS[i % 8]}/watch?v={i}",
                               title=f"Видео номер {i} — очень длинное название ролика, чтобы проверить обрезку текста",
                               progress=(35 + i * 20) if live else None,
                               metadata={"resolution": "1080p", "speed": "4.2 MiB/s", "eta": "00:41", "size": "312 MiB"} if live else {},
                               first_seen_ts=now - 86400 * 30))
        return {"total": len(items), "items": items[:limit]}

    def get_top_downloaders(self, period, limit=10):
        return [_user(i, count=300 - i * 7) for i in range(min(limit, 40))]

    def get_suspicious_users(self, period, limit=20):
        return [_user(i, max_gap_seconds=600 + i * 300, downloads=80 - i, last_event_ts=time.time() - 300) for i in range(min(limit, 6))]

    def get_top_domains(self, period, limit=10):
        return [{"domain": d, "count": 900 // (i + 1)} for i, d in enumerate(DOMAINS)][:limit]

    def get_top_countries(self, period, limit=10):
        return [{"flag": f, "country_code": c, "count": n} for f, c, n in [("🇷🇺", "RU", 812), ("🇺🇸", "US", 233), ("🇮🇳", "IN", 120), ("🇩🇪", "DE", 41)]]

    def get_gender_stats(self, period):
        return [{"gender": "male", "count": 620}, {"gender": "female", "count": 310}, {"gender": "unknown", "count": 270}]

    def get_age_stats(self, period):
        return [{"age_group": g, "count": n} for g, n in [("< 1 года", 80), ("1–3 года", 230), ("3–5 лет", 410), ("> 5 лет", 520)]]

    def get_channel_join_stats(self, period):
        return [{"join_date": f"2026-11-0{d}", "count": 10 + d * 3} for d in range(1, 5)]

    def get_top_nsfw_users(self, limit=10):
        return [_user(i, count=40 - i) for i in range(5)]

    def get_top_nsfw_domains(self, limit=10):
        return [{"domain": "example-nsfw.com", "count": 55}, {"domain": "other.xxx", "count": 12}]

    def get_top_playlist_users(self, limit=10):
        return [_user(i, count=12 - i) for i in range(4)]

    def get_top_multi_url_users(self, period, limit=10):
        return [_user(i, messages=8, total_urls=40 - i, avg_urls=5.0, last_event_ts=time.time()) for i in range(3)]

    def get_format_users(self, limit=20):
        return [_user(i, format="bv*[height<=1080]+ba/b", updated_ts=time.time() - i * 3600) for i in range(4)]

    def get_power_users(self, min_urls=10, days=7, limit=10):
        return [_user(i, streak=days) for i in range(3)]

    def get_blocked_users(self, limit=50):
        return [_user(i, reason="auto_bot_protection: flood" if i % 2 else "manual", timestamp=time.time() - i * 5000) for i in range(30)][:limit]

    def get_user_history(self, user_id, period="all", limit=100):
        now = time.time()
        return [{"timestamp": now - i * 3000, "url": f"https://{DOMAINS[i % 8]}/v/{i}", "title": f"<b>Ролик</b> {i}",
                 "domain": DOMAINS[i % 8], "is_nsfw": i % 11 == 0, "is_playlist": i % 7 == 0} for i in range(min(limit, 260))]

    def get_recent_channel_events(self, hours=48, limit=100):
        now = time.time()
        return [{"type": "join" if i % 3 else "leave", "timestamp": now - i * 4000, "user_id": 200000 + i,
                 "name": NAMES[i % len(NAMES)], "username": None, "description": ""} for i in range(10)]

    def block_user_local(self, user_id, reason="manual"):
        self._blocked_users[user_id] = reason

    def unblock_user_local(self, user_id):
        self._blocked_users.pop(user_id, None)


class _Node:
    writes = []

    def __init__(self, path=""):
        self.path = path

    def child(self, name):
        return _Node(f"{self.path}/{name}".strip("/"))

    def set(self, value):
        _Node.writes.append(("set", self.path, value))

    def remove(self):
        _Node.writes.append(("remove", self.path, None))


def install_stubs():
    os.environ["TG_DASHBOARD_READ_ONLY"] = "0"  # exercise write handlers against fixtures only
    import logging
    collector = FakeCollector()
    _module("CONFIG.config", Config=Config)
    _module("DATABASE.firebase_init", db=_Node())
    from datetime import datetime, timedelta
    _module("DATABASE.cache_db", get_next_reload_time=lambda hours: datetime.now() + timedelta(hours=1))
    _module("HELPERS.logger", logger=logging.getLogger("stub"))
    _module("HELPERS.channel_guard", get_channel_guard=lambda: None)
    _module("services.stats_collector", get_stats_collector=lambda: collector, enable_background_profiles=lambda: None)

    from CONFIG import overrides
    overrides.OVERRIDES_FILE = TMP / ".dashboard_overrides.json"
    from HELPERS import runtime_status
    runtime_status.RUNTIME_FILE = TMP / ".bot_runtime.json"
    import json
    (TMP / ".bot_runtime.json").write_text(json.dumps({"pid": 4242, "started_at": int(time.time()) - 7200,
                                                       "ts": int(time.time()) + 10 ** 6, "running": 2, "queued": 1,
                                                       "warp_tunnels": 2}))
    from services import lists_service
    domains = TMP / "domains.py"
    domains.write_text((ROOT / "CONFIG" / "domains.py").read_text(encoding="utf-8"), encoding="utf-8")
    lists_service.DOMAINS_FILE = domains
    lists_service.BASE_DIR = TMP
    (TMP / "CONFIG").mkdir(exist_ok=True)
    (TMP / "TXT").mkdir(exist_ok=True)
    for name in ("porn_domains.txt", "porn_keywords.txt", "supported_sites.txt"):
        (TMP / "TXT" / name).write_text("\n".join(f"line{i}" for i in range(25)), encoding="utf-8")

    from web import security
    security.sessions = security.SessionStore(TMP / ".dashboard_sessions.json")
    security.throttle = security.LoginThrottle()
    from web import dashboard_app
    dashboard_app.AUDIT_FILE = TMP / ".dashboard_audit.log"
    return dashboard_app.app, collector


if __name__ == "__main__":
    import uvicorn
    port = int(sys.argv[sys.argv.index("--serve") + 1]) if "--serve" in sys.argv else 8765
    app, _ = install_stubs()
    print(f"demo dashboard on http://127.0.0.1:{port}  login {DEMO_USER} / {DEMO_PASSWORD}")
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")
