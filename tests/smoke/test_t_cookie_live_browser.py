"""Smoke test: /cookies_from_browser and the /cookie service buttons take cookies from the live browser.

The handler module needs a running Pyrogram client, so the helper
`_save_live_browser_cookies` is lifted out of COMMANDS/cookies_cmd.py with ast and run
against fakes. Also checks the wiring (call sites) in the source.

Run: python tests/smoke/test_t_cookie_live_browser.py   (offline)
"""
import ast
import logging
import os
import sys
import tempfile
from types import SimpleNamespace

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

from HELPERS import browser_session as bs  # noqa: E402
from HELPERS.cookie_file import validate_cookie_bytes, write_cookie_file  # noqa: E402

SRC = open(os.path.join(ROOT, "COMMANDS", "cookies_cmd.py"), encoding="utf-8").read()
tree = ast.parse(SRC)
fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_save_live_browser_cookies_impl")
code = ast.get_source_segment(SRC, fn)

ok = fail = 0


def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} {info}")


class Msgs:
    COOKIES_LIVE_BROWSER_SAVED_MSG = "saved {service} {count}"
    COOKIES_LIVE_BROWSER_LOG_MSG = "log {user_id} {service} {count}"
    COOKIES_LIVE_BROWSER_EMPTY_MSG = "empty {service}"


sent, logged = [], []
tmp = tempfile.mkdtemp(prefix="cc_")
os.chdir(tmp)


def make_ns(config, jar):
    state = {"running": True, "jar": jar}

    class FakeBS:
        BrowserError = bs.BrowserError
        COOKIE_SERVICES = bs.COOKIE_SERVICES
        SERVICE_DOMAINS = bs.SERVICE_DOMAINS

        @staticmethod
        def enabled():
            return config.BROWSER_SESSION_ENABLED

        @staticmethod
        def is_running():
            return state["running"]

        @staticmethod
        def export_netscape(services=None, domains=None):
            chosen = bs.filter_cookies(state["jar"], services, domains)
            if not chosen:
                return None, 0, []
            return bs.to_netscape(chosen).encode(), len(chosen), sorted({c["domain"].lstrip(".") for c in chosen})

    ns = {
        "os": os, "logger": logging.getLogger("t"), "Config": config, "validate_cookie_bytes": validate_cookie_bytes,
        "write_cookie_file": write_cookie_file, "create_directory": lambda p: os.makedirs(p, exist_ok=True),
        "safe_get_messages": lambda uid: Msgs, "send_to_user": lambda m, t: sent.append(t),
        "send_to_logger": lambda m, t: logged.append(t),
    }
    import HELPERS
    HELPERS.browser_session = FakeBS  # the helper does `from HELPERS import browser_session`
    exec(code, ns)
    return ns["_save_live_browser_cookies_impl"], state


JAR = [
    {"name": "auth_token", "value": "T", "domain": ".x.com", "path": "/", "secure": True, "httpOnly": True, "expires": 2000000000},
    {"name": "sessionid", "value": "I", "domain": ".instagram.com", "path": "/", "secure": True, "expires": 2000000000},
    {"name": "bank", "value": "B", "domain": "bank.example.org", "path": "/", "secure": True, "expires": 2000000000},
    {"name": "c_user", "value": "F", "domain": ".facebook.com", "path": "/", "secure": True, "expires": 2000000000},
]
cfg = SimpleNamespace(BROWSER_SESSION_ENABLED=True, BROWSER_COOKIES_ADMIN_ONLY=False, ADMIN=[1], COOKIE_FILE_PATH="./cookie.txt")
save, state = make_ns(cfg, JAR)
path = os.path.join(".", "users", "42", "cookie.txt")

check("all services (/cookies_from_browser)", save(None, 42) == "saved")
body = open(path, "rb").read().decode()
check("file has the cookies of the five services", "auth_token" in body and "sessionid" in body)
check("cookies of other sites never leave the browser", "bank" not in body and "c_user" not in body)
check("file is valid for yt-dlp loader", validate_cookie_bytes(body.encode())[0])
check("user is told service and count only, no domains",
      sent[-1] == "saved YouTube, X, Instagram, VK, TikTok 2", sent[-1])
check("log has no cookie values", logged and "T" not in logged[-1].split()[-1] and "auth_token" not in logged[-1])

sent.clear()
check("service button: twitter", save(None, 42, ["twitter"]) == "saved")
body = open(path, "rb").read().decode()
check("only that service's cookies are written", "auth_token" in body and "sessionid" not in body)

sent.clear()
check("service without cookies -> empty (caller falls back to the static URL)", save(None, 42, ["vk"]) == "empty")
check("button says that it uses the backup source", sent == ["empty vk"], sent)
sent.clear()
saved_jar, state["jar"] = state["jar"], []
check("all services without any cookie stays silent (the menu follows)", save(None, 42) == "empty" and sent == [], sent)
state["jar"] = saved_jar
check("empty result leaves the previous file alone", "auth_token" in open(path).read())

state["running"] = False
check("browser stopped -> unavailable", save(None, 42) == "unavailable")
state["running"] = True
cfg.BROWSER_SESSION_ENABLED = False
check("feature off -> unavailable", save(None, 42) == "unavailable")
cfg.BROWSER_SESSION_ENABLED = True
cfg.BROWSER_COOKIES_ADMIN_ONLY = True
check("admin-only: regular user refused", save(None, 42) == "unavailable")
check("admin-only: admin served", save(None, 1) == "saved")

# wiring in the handlers
check("/cookies_from_browser tries the live session first",
      '_save_live_browser_cookies(message, user_id) == "saved"' in SRC)
for svc in ("instagram", "twitter", "tiktok", "vk"):
    check(f"button {svc}: live first, static URL fallback",
          f'_save_live_browser_cookies(callback_query.message, user_id, ["{svc}"]) != "saved"' in SRC
          and f'Config.{svc.upper()}_COOKIE_URL, "{svc}")' in SRC)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
