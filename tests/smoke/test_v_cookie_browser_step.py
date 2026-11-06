"""Smoke test: the live dashboard browser is a step of the cookie cascade (offline).

cookies_cmd.py pulls in Pyrogram, so the helpers are cut out by AST and run against a fake
HELPERS.browser_session; the placement of the steps is checked on the AST.
Run: python tests/smoke/test_v_cookie_browser_step.py
"""
import ast
import contextlib
import logging
import os
import sys
import tempfile
import types

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)
SRC_PATH = os.path.join(ROOT, "COMMANDS", "cookies_cmd.py")

import HELPERS  # noqa: E402
from HELPERS.cookie_file import validate_cookie_bytes, write_cookie_file  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


text = open(SRC_PATH, encoding="utf-8").read()
tree = ast.parse(text)
funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
seg = lambda name: ast.get_source_segment(text, funcs[name])  # noqa: E731

GOOD = (b"# Netscape HTTP Cookie File\n"
        b".x.com\tTRUE\t/\tTRUE\t1790000000\tauth_token\tabc123secret\n")


class FakeSession(types.ModuleType):
    def __init__(self):
        super().__init__("HELPERS.browser_session")
        self.on = True
        self.running = True
        self.payload = (GOOD, 1, [".x.com"])
        self.asked = []

    class BrowserError(Exception):
        pass

    def enabled(self):
        return self.on

    def is_running(self):
        return self.running

    def export_netscape(self, services=None):
        self.asked.append(list(services or []))
        if isinstance(self.payload, Exception):
            raise self.payload
        return self.payload


fake = FakeSession()
sys.modules["HELPERS.browser_session"] = fake
HELPERS.browser_session = fake


class Cfg:
    ADMIN = [1]
    COOKIE_FILE_PATH = "TXT/cookie.txt"


def build():
    ns = {"os": os, "contextlib": contextlib, "Config": Cfg, "logger": logging.getLogger("t"),
          "validate_cookie_bytes": validate_cookie_bytes, "write_cookie_file": write_cookie_file,
          "create_directory": lambda d: os.makedirs(d, exist_ok=True)}
    exec(text.split("_BROWSER_STEP_SERVICES = ", 1)[1].split("\n", 1)[0].join(["_BROWSER_STEP_SERVICES = ", "\n"]), ns)
    exec(seg("_export_live_browser_cookies"), ns)
    # ast.get_source_segment drops decorators, put the contextmanager one back
    exec("import contextlib\n@contextlib.contextmanager\n" + seg("_live_browser_cookie_file"), ns)
    return ns


work = tempfile.mkdtemp()
os.chdir(work)
ns = build()
export, live = ns["_export_live_browser_cookies"], ns["_live_browser_cookie_file"]

# --- helper behaviour
path = export(7, "twitter")
check("happy path: temp file inside users/<uid>/", bool(path) and path.startswith(os.path.join("users", "7"))
      and os.path.exists(path))
check("temp file holds valid Netscape cookies", validate_cookie_bytes(open(path, "rb").read())[0])
check("only the requested service is exported", fake.asked[-1] == ["twitter"])
check("user's own cookie.txt untouched", not os.path.exists(os.path.join("users", "7", "cookie.txt")))
os.remove(path)

with live(7, "instagram") as p:
    inside = bool(p) and os.path.exists(p)
check("context manager yields a file and removes it on exit", inside and not os.path.exists(p))

try:
    with live(7, "instagram") as p:
        raise RuntimeError("download failed")
except RuntimeError:
    pass
check("file removed even when the attempt raises", not os.path.exists(p))

check("unknown service -> None, browser not asked", export(7, "facebook") is None and fake.asked[-1] == ["instagram"])
fake.on = False
check("feature off -> None", export(7, "twitter") is None)
fake.on, fake.running = True, False
check("browser not running -> None", export(7, "twitter") is None)
fake.running = True
fake.payload = (None, 0, [])
check("nothing logged in -> None", export(7, "twitter") is None)
fake.payload = (b"<html>nope</html>", 3, [".x.com"])
check("invalid export is rejected", export(7, "twitter") is None)
fake.payload = fake.BrowserError("browser is not running")
check("BrowserError is swallowed", export(7, "twitter") is None)
fake.payload = OSError("boom")
check("any other error is swallowed", export(7, "twitter") is None)
fake.payload = (GOOD, 1, [".x.com"])
Cfg.BROWSER_COOKIES_ADMIN_ONLY = True
check("admin-only switch: regular user gets nothing", export(7, "twitter") is None)
p_admin = export(1, "twitter")
check("admin-only switch: admin still gets cookies", bool(p_admin))
if p_admin:
    os.remove(p_admin)
del Cfg.BROWSER_COOKIES_ADMIN_ONLY
left = [f for f in os.listdir(os.path.join("users", "7")) if f.startswith("temp_browser_")]
check("no temp files left behind", not left)

# --- service detection (vk.ru / vkvideo.ru count as VK)
sns = {}
exec(seg("get_service_name_from_url"), sns)
detect = sns["get_service_name_from_url"]
check("x.com -> twitter", detect("https://x.com/a/status/1") == "twitter")
check("vkvideo.ru -> vk", detect("https://vkvideo.ru/video-1_2") == "vk")
check("m.vk.ru -> vk", detect("https://m.vk.ru/video-1_2") == "vk")
check("vk.com -> vk", detect("https://vk.com/video-1_2") == "vk")
check("evilvk.ru is not vk", detect("https://evilvk.ru/x") is None)


# --- placement of the steps
def lines_of(func_name, pred):
    return [n.lineno for n in ast.walk(funcs[func_name]) if pred(n)]


is_call = lambda name: (lambda n: isinstance(n, ast.Call)  # noqa: E731
                        and getattr(n.func, "id", getattr(n.func, "attr", None)) == name)

yt_browser = lines_of("retry_download_with_different_cookies", is_call("_live_browser_cookie_file"))
yt_limit = lines_of("retry_download_with_different_cookies", is_call("check_youtube_cookie_retry_limit"))
yt_static = lines_of("retry_download_with_different_cookies", is_call("get_unchecked_cookie_sources"))
check("YouTube cascade has one browser step", len(yt_browser) == 1)
check("YouTube browser step precedes the rotation limit and the static sources",
      yt_browser and yt_limit and yt_static and yt_browser[0] < yt_limit[0] < min(yt_static))
guard = [n for n in ast.walk(funcs["retry_download_with_different_cookies"]) if isinstance(n, ast.If)
         and isinstance(n.test, ast.UnaryOp) and isinstance(n.test.operand, ast.Name)
         and n.test.operand.id == "proxy_enabled"]
check("YouTube browser step skipped when the user has an own proxy",
      any(yt_browser and g.lineno < yt_browser[0] <= g.end_lineno for g in guard))

nyt = funcs["try_non_youtube_cookie_fallback"]
b_line = lines_of("try_non_youtube_cookie_fallback", is_call("_live_browser_cookie_file"))
svc_line = lines_of("try_non_youtube_cookie_fallback", is_call("get_service_cookie_url"))
user_line = lines_of("try_non_youtube_cookie_fallback", is_call("ensure_valid_cookie_file"))
check("non-YouTube cascade: user cookies -> browser -> static service link",
      len(b_line) == 1 and user_line and svc_line and user_line[0] < b_line[0] < svc_line[0])

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
