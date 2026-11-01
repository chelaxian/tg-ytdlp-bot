"""Offline smoke tests for agent C fixes (#468 #478 #316 #487 #464 #463 #326 #372 #465 #460/#385).

No network: requests calls are mocked; heavy modules (pyrogram/yt-dlp/firebase)
are not imported - their helpers are extracted via AST or stubbed.
Run: python test_c.py [repo_root]
"""
import ast
import asyncio
import concurrent.futures
import io
import json
import logging
import os
import sys
import tempfile
import threading
import time
import types
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

REPO = sys.argv[1] if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
sys.path.insert(0, REPO)
WORK = tempfile.mkdtemp(prefix="test_c_")
os.chdir(WORK)  # HELPERS.logger writes bot.log into cwd
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(name)s: %(message)s")

PASSED = []


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    PASSED.append(name)
    print(f"ok  {name}")


class LogCapture(logging.Handler):
    def __init__(self):
        super().__init__(logging.DEBUG)
        self.records = []

    def emit(self, record):
        self.records.append(record)

    def at(self, level):
        return [r.getMessage() for r in self.records if r.levelno == level]


def extract(path, names, extra_globals):
    """Exec only the named top-level functions/assignments of a module."""
    src = open(os.path.join(REPO, path), encoding="utf-8").read()
    tree = ast.parse(src)
    body = [n for n in tree.body
            if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names)
            or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in names for t in n.targets))]
    mod = ast.Module(body=body, type_ignores=[])
    g = dict(extra_globals)
    exec(compile(mod, path, "exec"), g)
    return g


# ------------------------------------------------------------------ atomic_io (#316)
from HELPERS import atomic_io

p = os.path.join(WORK, "a.json")
atomic_io.atomic_write_json(p, {"x": 1})
check("atomic_json_written", json.load(open(p, encoding="utf-8")) == {"x": 1})
try:
    atomic_io.atomic_write_json(p, {"bad": object()})
except TypeError:
    pass
check("atomic_json_nonserializable_keeps_old", json.load(open(p, encoding="utf-8")) == {"x": 1})
with mock.patch("os.replace", side_effect=OSError(122, "Disk quota exceeded")):
    try:
        atomic_io.atomic_write_json(p, {"x": 2})
    except OSError:
        pass
check("atomic_json_quota_keeps_old", json.load(open(p, encoding="utf-8")) == {"x": 1})
check("atomic_no_tmp_left", [f for f in os.listdir(WORK) if f.endswith(".tmp")] == [])

# ------------------------------------------------------------------ cookie_file (#478)
from HELPERS import cookie_file as cf

GOOD = b"# Netscape HTTP Cookie File\n.youtube.com\tTRUE\t/\tTRUE\t0\tSID\tabc\n"
check("cookie_valid", cf.validate_cookie_bytes(GOOD)[0])
check("cookie_empty", cf.validate_cookie_bytes(b"") == (False, "empty file"))
check("cookie_html", "HTML" in cf.validate_cookie_bytes(b"<html>login</html>")[1])
check("cookie_json", "JSON" in cf.validate_cookie_bytes(b'[{"name": "a"}]')[1])
check("cookie_header_not_first_line", not cf.validate_cookie_bytes(b"\n# Netscape HTTP Cookie File\n")[0])
check("cookie_header_only_ok_for_file_check", cf.validate_cookie_bytes(b"# HTTP Cookie File\n", require_entries=False)[0])
check("cookie_no_entries_rejected_for_download", not cf.validate_cookie_bytes(b"# Netscape HTTP Cookie File\n")[0])

cdir = os.path.join(WORK, "users", "1")
os.makedirs(cdir)
cpath = os.path.join(cdir, "cookie.txt")
open(cpath, "wb").write(b"")  # truncated by Errno 122
check("ensure_valid_quarantines_broken", cf.ensure_valid_cookie_file(cpath) is None
      and not os.path.exists(cpath) and os.path.exists(cpath + ".invalid"))
check("ensure_valid_missing_none", cf.ensure_valid_cookie_file(cpath) is None)
cf.write_cookie_file(cpath, GOOD)
check("ensure_valid_good_path", cf.ensure_valid_cookie_file(cpath) == cpath)
with mock.patch("os.replace", side_effect=OSError(122, "Disk quota exceeded")):
    try:
        cf.write_cookie_file(cpath, b"# Netscape HTTP Cookie File\n.x\tTRUE\t/\tTRUE\t0\tA\tB\n")
        raised = False
    except OSError:
        raised = True
check("cookie_write_quota_keeps_previous", raised and open(cpath, "rb").read() == GOOD)

# ------------------------------------------------------------------ cookies_cmd helpers (#468)
import HELPERS.ytdlp_errors as ye
g = extract("COMMANDS/cookies_cmd.py", {"_call_with_cookie_override", "_is_local_cookie_failure"},
            {"is_local_file_error": ye.is_local_file_error, "is_missing_local_file": ye.is_missing_local_file, "ensure_valid_cookie_file": lambda p: p})
seen = {}


def fake_download(*a, **k):
    seen["override"] = getattr(threading.current_thread(), "cookiefile_override", "UNSET")
    return "ok"


r = g["_call_with_cookie_override"]("users/1/cookie.txt", fake_download, 1, x=2)
check("override_applied_during_call", r == "ok" and seen["override"] == "users/1/cookie.txt")
check("override_removed_after_call", not hasattr(threading.current_thread(), "cookiefile_override"))
threading.current_thread().cookiefile_override = None
g["_call_with_cookie_override"]("p", fake_download)
check("override_previous_restored", threading.current_thread().cookiefile_override is None)
del threading.current_thread().cookiefile_override
loc = g["_is_local_cookie_failure"]
check("local_failure_enoent", loc(FileNotFoundError(2, "No such file or directory")))
check("local_failure_quota", loc(OSError(122, "Disk quota exceeded")))
check("local_failure_text", loc(Exception("ERROR: [Errno 2] No such file or directory: 'downloads/t/cookie.txt'")))
check("local_failure_netscape", loc(Exception("'users/1/cookie.txt' does not look like a Netscape format cookies file")))
check("not_local_timeout", not loc(TimeoutError("timed out")))
check("not_local_ytdlp", not loc(Exception("Sign in to confirm you're not a bot")))

# ------------------------------------------------------------------ pot_helper probe (#465)
import requests
for mod_name in ("URL_PARSERS.youtube",):
    stub = types.ModuleType(mod_name)
    stub.is_youtube_url = lambda u: "youtu" in u
    sys.modules[mod_name] = stub
from HELPERS import pot_helper as ph

cap = LogCapture()
ph.logger.addHandler(cap)


class Resp:
    def __init__(self, status, body=None, text=""):
        self.status_code = status
        self._body = body
        self.text = text

    def json(self):
        if self._body is None:
            raise ValueError("no json")
        return self._body


def probe(resp_or_exc, n=1):
    calls = []

    def fake_get(url, **kw):
        calls.append(url)
        if isinstance(resp_or_exc, Exception):
            raise resp_or_exc
        return resp_or_exc
    results = []
    with mock.patch.object(ph.requests, "get", side_effect=fake_get):
        for _ in range(n):
            ph._pot_provider_cache["last_check"] = 0  # bypass 30s cache
            results.append(ph.check_pot_provider_availability("http://127.0.0.1:4416"))
    return results, calls


ph.clear_pot_provider_cache()
cap.records.clear()
res, calls = probe(Resp(200, {"version": "2.0.2"}), n=5)
check("pot_ping_url", calls[0] == "http://127.0.0.1:4416/ping", calls[0])
check("pot_200_available", all(res))
check("pot_200_logged_once", len([m for m in cap.at(logging.INFO) if "available" in m]) == 1
      and not cap.at(logging.WARNING), cap.at(logging.INFO))
cap.records.clear()
res, _ = probe(requests.exceptions.ConnectionError("refused"), n=4)
check("pot_down_unavailable", not any(res))
check("pot_down_single_warning", len(cap.at(logging.WARNING)) == 1, cap.at(logging.WARNING))
cap.records.clear()
res, _ = probe(Resp(503, text="boom"), n=3)
check("pot_5xx_same_down_state_not_relogged", not any(res) and not cap.at(logging.ERROR))
ph._pot_provider_cache["state"] = "ok"
cap.records.clear()
res, _ = probe(Resp(503, text="boom"), n=3)
check("pot_5xx_unavailable", not any(res) and len(cap.at(logging.ERROR)) == 1)
cap.records.clear()
res, _ = probe(Resp(400, text="This server is not meant to be accessed directly"), n=3)
check("pot_400_alive_single_warning", all(res) and len(cap.at(logging.WARNING)) == 1)
cap.records.clear()
res, _ = probe(Resp(200, {"version": "2.0.2"}), n=1)
check("pot_recovery_logged", res == [True] and len(cap.at(logging.INFO)) == 1)

# ------------------------------------------------------------------ anti_bot retry (#463)
fake_logger = logging.getLogger("antibot_test")
cap2 = LogCapture()
fake_logger.addHandler(cap2)
g = extract("HELPERS/anti_bot_protection.py",
            {"_run_async", "_run_async_retry", "_is_timeout_error", "_CHANNEL_BAN_ATTEMPTS",
             "_CHANNEL_BAN_BACKOFF", "_CHANNEL_BAN_BACKOFF_FACTOR"},
            {"logger": fake_logger, "time": time, "get_app": lambda: None})
sleeps = []
g["time"] = types.SimpleNamespace(sleep=lambda s: sleeps.append(s))

loop = asyncio.new_event_loop()
t = threading.Thread(target=loop.run_forever, daemon=True)
t.start()
asyncio.set_event_loop(loop)  # _run_async uses get_event_loop() and requires a running loop

attempts = {"n": 0}


def make_slow_then_ok(fail_times):
    async def coro():
        attempts["n"] += 1
        if attempts["n"] <= fail_times:
            await asyncio.sleep(5)
        return "banned"
    return coro


attempts["n"] = 0
r = g["_run_async_retry"](make_slow_then_ok(2), timeout=0.2, what="ban_chat_member")
check("antibot_recovers_on_3rd_attempt", r == "banned" and attempts["n"] == 3)
check("antibot_exponential_backoff", sleeps == [2.0, 8.0], sleeps)
sleeps.clear()
attempts["n"] = 0
try:
    g["_run_async_retry"](make_slow_then_ok(99), timeout=0.2, what="ban_chat_member")
    final = None
except Exception as e:
    final = e
check("antibot_gives_up_after_3", attempts["n"] == 3 and g["_is_timeout_error"](final), repr(final))


sleeps.clear()

async def boom():
    raise ValueError("CHAT_ADMIN_REQUIRED")
attempts["n"] = 0
try:
    g["_run_async_retry"](lambda: boom(), timeout=0.2)
except ValueError:
    pass
check("antibot_no_retry_on_non_timeout", sleeps == [])
time.sleep(0.3)
pending = [tk for tk in asyncio.all_tasks(loop) if not tk.done()]
check("antibot_timed_out_calls_cancelled", not pending, pending)
loop.call_soon_threadsafe(loop.stop)

# ------------------------------------------------------------------ upload_guard (#372, #326)
app_stub = types.SimpleNamespace(is_connected=True)
import HELPERS.app_instance as ai
ai.set_app(app_stub)
from HELPERS import upload_guard as ug
from CONFIG.limits import LimitsConfig
base = LimitsConfig.UPLOAD_TIMEOUT_SECONDS
check("upload_timeout_small_file_base", ug.compute_upload_timeout(10 * 1024 * 1024, base) == base)
t2g = ug.compute_upload_timeout(2 * 1024 ** 3, base)
check("upload_timeout_scales_2gb", base < t2g <= base * 4, t2g)
check("upload_timeout_capped", ug.compute_upload_timeout(50 * 1024 ** 3, base) == base * 4)
big = os.path.join(WORK, "v.mp4")
with open(big, "wb") as fh:
    fh.truncate(2 * 1024 ** 3)  # sparse
check("upload_size_from_dedup_key", ug._infer_file_size(None, (1, big)) == 2 * 1024 ** 3)
check("upload_ok", ug.timed_upload(lambda: "sent", timeout=5, dedup_key=("k", 1)) == "sent")
check("upload_key_released", ("k", 1) not in ug._ACTIVE_UPLOAD_KEYS)

ai.mark_app_stopping()
try:
    ug.timed_upload(lambda: "sent", timeout=5, dedup_key=("k", 2))
    stopped = None
except ug.ClientNotReadyError as e:
    stopped = e
check("upload_fails_fast_on_shutdown", stopped is not None)
check("upload_key_released_when_not_started", ("k", 2) not in ug._ACTIVE_UPLOAD_KEYS)
ai._app_stopping.clear()

app_stub.is_connected = False
start = time.monotonic()
with mock.patch.object(ug, "_APP_READY_WAIT_SECONDS", 1.5):
    threading.Timer(0.6, lambda: setattr(app_stub, "is_connected", True)).start()
    r = ug.timed_upload(lambda: "late-ok", timeout=5)
check("upload_waits_for_startup", r == "late-ok" and 0.5 < time.monotonic() - start < 1.5)
check("upload_never_calls_start", not hasattr(app_stub, "start"))

cap3 = LogCapture()
ug.logger.addHandler(cap3)
ev = threading.Event()
try:
    ug.timed_upload(lambda: (ev.wait(1.0), "late")[1], timeout=0.2, dedup_key=("k", 3))
except TimeoutError:
    pass
ev.set()
time.sleep(0.3)
check("upload_late_completion_logged", any("completed late" in m for m in cap3.at(logging.WARNING)), cap3.at(logging.WARNING))

# ------------------------------------------------------------------ download_firebase (#487, #464)
from CONFIG.config import Config
Config.FIREBASE_CONF = {"databaseURL": "https://example-rtdb.firebaseio.com", "apiKey": "k"}
Config.FIREBASE_USER = "u"
Config.FIREBASE_PASSWORD = "p"
Config.FIREBASE_CACHE_FILE = os.path.join(WORK, "dump.json")
import DATABASE.download_firebase as dfb


class FakeStreamResp:
    def __init__(self, chunks, fail_after=None, status=200):
        self.chunks = chunks
        self.fail_after = fail_after
        self.status_code = status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def raise_for_status(self):
        if self.status_code >= 400:
            err = requests.exceptions.HTTPError(f"{self.status_code}")
            err.response = self
            raise err

    def iter_content(self, chunk_size=None):
        for i, c in enumerate(self.chunks):
            if self.fail_after is not None and i == self.fail_after:
                raise requests.exceptions.ConnectionError("Read timed out. (read timeout=300)")
            yield c


class FakeSession:
    def __init__(self, gets):
        self.gets = list(gets)
        self.get_calls = []

    def post(self, url, json=None, timeout=None):
        r = FakeStreamResp([])
        r.json = lambda: {"idToken": "tok"}
        return r

    def get(self, url, timeout=None, stream=False):
        self.get_calls.append(timeout)
        nxt = self.gets.pop(0)
        if isinstance(nxt, Exception):
            raise nxt
        return nxt


def run_dump(session):
    mgr = types.SimpleNamespace(get_session=lambda: session, close=lambda: None)
    sleeps = []
    out, err = io.StringIO(), io.StringIO()
    with mock.patch("HELPERS.http_manager.get_managed_session", return_value=mgr), \
         mock.patch.object(dfb.time, "sleep", side_effect=lambda s: sleeps.append(s)), \
         redirect_stdout(out), redirect_stderr(err):
        ok = dfb.download_firebase_dump()
    return ok, sleeps, err.getvalue()


s = FakeSession([
    FakeStreamResp([b'{"bot": ', b'{"a": 1}}'], fail_after=1),   # mid-stream read timeout
    requests.exceptions.ConnectTimeout("connect timeout"),
    FakeStreamResp([b'{"bot": ', b'{"a": 1}}']),
])
ok, sl, err = run_dump(s)
check("dump_retries_mid_stream_failure", ok and sl == [10, 30], (ok, sl, err))
check("dump_timeout_tuple", s.get_calls[0] == (10, 60), s.get_calls)
check("dump_written", json.load(open(Config.FIREBASE_CACHE_FILE)) == {"bot": {"a": 1}})

s = FakeSession([FakeStreamResp([b'{"bot": {"a": 1'])])
ok, sl, err = run_dump(s)
check("dump_truncated_rejected", not ok and "not a complete JSON object" in err, err)
check("dump_truncated_keeps_old", json.load(open(Config.FIREBASE_CACHE_FILE)) == {"bot": {"a": 1}})

s = FakeSession([requests.exceptions.ReadTimeout("Read timed out")] * 4)
ok, sl, err = run_dump(s)
check("dump_gives_up_after_4_with_reason", not ok and len(s.get_calls) == 4 and sl == [10, 30, 90]
      and err.startswith("DUMP FAILED:") and "ReadTimeout" in err, (sl, err))

s = FakeSession([FakeStreamResp([], status=404)])
ok, sl, err = run_dump(s)
check("dump_4xx_not_retried", not ok and len(s.get_calls) == 1 and sl == [], (sl, err))

# ------------------------------------------------------------------ firebase_init REST retry (#464)
fb_logger = logging.getLogger("fb_test")
g = extract("DATABASE/firebase_init.py",
            {"_REST_TIMEOUT", "_REST_RETRY_DELAYS", "_REST_TRANSIENT_ERRORS", "_rest_request"},
            {"requests": requests, "logger": fb_logger, "time": types.SimpleNamespace(sleep=lambda s: None)})


class RS:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = []

    def request(self, method, url, **kw):
        self.calls.append((method, kw.get("timeout")))
        o = self.outcomes.pop(0)
        if isinstance(o, Exception):
            raise o
        return types.SimpleNamespace(raise_for_status=lambda: None, json=lambda: {"ok": 1})


rs = RS([requests.exceptions.ReadTimeout("t"), requests.exceptions.ConnectionError("c"), "ok"])
g["_rest_request"](rs, "GET", "https://x/.json")
check("rest_get_retried_twice", len(rs.calls) == 3 and rs.calls[0][1] == (10, 30), rs.calls)
rs = RS([requests.exceptions.ReadTimeout("t")])
try:
    g["_rest_request"](rs, "POST", "https://x/.json", retry=False)
    posted = True
except requests.exceptions.ReadTimeout:
    posted = False
check("rest_post_not_retried", not posted and len(rs.calls) == 1)

# ------------------------------------------------------------------ downloads janitor (#460, #385)
from HELPERS import downloads_janitor as dj
users = os.path.join(WORK, "jusers")
now = time.time()
old = now - 72 * 3600


def mk(path, mtime, data=b"x"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)
    os.utime(path, (mtime, mtime))


mk(os.path.join(users, "1", "downloads", "stale", "v.mp4"), old)
os.utime(os.path.join(users, "1", "downloads", "stale"), (old, old))
mk(os.path.join(users, "1", "downloads", "active", "v.mp4.part"), old)
mk(os.path.join(users, "1", "downloads", "active", "v.f137.mp4"), now - 60)  # still being written
os.utime(os.path.join(users, "1", "downloads", "active"), (old, old))
mk(os.path.join(users, "1", "cookie.txt"), old, GOOD)
mk(os.path.join(users, "1", "lang.txt"), old, b"en")
mk(os.path.join(users, "1", "old.mp4"), old)
mk(os.path.join(users, "2", "downloads", "stale2", "a.mp3"), old)
os.utime(os.path.join(users, "2", "downloads", "stale2"), (old, old))

removed = dj.purge_stale_downloads(users, 48 * 3600, active_user_ids={"2"}, now=now)
check("janitor_removes_stale_dir", not os.path.exists(os.path.join(users, "1", "downloads", "stale")))
check("janitor_keeps_recently_touched_dir", os.path.exists(os.path.join(users, "1", "downloads", "active", "v.mp4.part")))
check("janitor_keeps_settings", os.path.exists(os.path.join(users, "1", "cookie.txt")))
check("janitor_preserves_root_media", os.path.exists(os.path.join(users, "1", "old.mp4")))
check("janitor_skips_active_user", os.path.exists(os.path.join(users, "2", "downloads", "stale2", "a.mp3")))
check("janitor_counts", removed == 1, removed)
active_path = os.path.join(users, "2", "downloads", "stale2")
removed = dj.purge_stale_downloads(users, 48 * 3600, active_user_ids=set(), active_paths=(active_path,), now=now)
check("janitor_skips_active_path", removed == 0 and os.path.exists(active_path))
marker_dir = os.path.join(users, "4", "downloads", "marked")
mk(os.path.join(marker_dir, "do_not_delete_me"), old)
os.utime(marker_dir, (old, old))
removed = dj.purge_stale_downloads(users, 48 * 3600, active_user_ids={"2"}, now=now)
check("janitor_respects_stale_marker", os.path.exists(marker_dir))

print("ALL", len(PASSED), "CHECKS PASSED")
