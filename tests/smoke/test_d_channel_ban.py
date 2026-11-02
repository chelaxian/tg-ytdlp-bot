"""Offline smoke tests: channel ban from ChannelGuard / worker threads, shutdown drops (#326).

Regression after 0516767: ChannelGuard ran the blocking block executor on the
Pyrogram loop thread, so every channel ban was rejected ("Blocking channel ban
cannot run on the Pyrogram event-loop thread", 204 failures, 0 bans on DE).
No network: the Pyrogram sync wrapper is emulated; functions are AST-extracted.
Run: python test_d_channel_ban.py [repo_root]
"""
import ast
import asyncio
import functools
import inspect
import logging
import os
import sys
import threading
import time
import types

REPO = sys.argv[1] if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
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


def extract(path, names, extra_globals, cls=None):
    """Exec only the named top-level (or class-level, when cls is given) defs of a module."""
    src = open(os.path.join(REPO, path), encoding="utf-8").read()
    tree = ast.parse(src)
    scope = tree.body
    if cls:
        scope = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == cls).body
    body = [n for n in scope
            if (isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.name in names)
            or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in names for t in n.targets))]
    g = dict(extra_globals)
    exec(compile(ast.Module(body=body, type_ignores=[]), path, "exec"), g)
    return g


# ------------------------------------------------------------------ Pyrogram-like client
# The bot loop runs in its own thread (stands for the main thread running app.loop).
loop = asyncio.new_event_loop()
threading.Thread(target=loop.run_forever, daemon=True).start()
LOOP_THREAD = []
loop.call_soon_threadsafe(lambda: LOOP_THREAD.append(threading.current_thread()))
time.sleep(0.05)


def pyrogram_sync(fn):
    """Emulates pyrogram.sync for a worker thread: blocks on the main loop and returns the RESULT."""
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        coro = fn(*args, **kwargs)
        if threading.current_thread() is LOOP_THREAD[0]:
            return coro
        return asyncio.run_coroutine_threadsafe(coro, loop).result()
    return wrap


class FakeClient:
    delay = 0.0

    def __init__(self):
        self.loop = loop
        self.calls = []

    async def _get_chat_member(self, chat_id, user_id):
        await asyncio.sleep(self.delay)
        self.calls.append(("get_chat_member", chat_id, user_id))
        return types.SimpleNamespace(status="ADMIN", user_id=user_id)

    get_chat_member = pyrogram_sync(_get_chat_member)


app = FakeClient()
lg = logging.getLogger("channel_ban_test")
cap = LogCapture()
lg.addHandler(cap)
g = extract("HELPERS/anti_bot_protection.py",
            {"_run_async", "_run_async_retry", "_pyro_coro", "_is_timeout_error", "_CHANNEL_BAN_ATTEMPTS",
             "_CHANNEL_BAN_BACKOFF", "_CHANNEL_BAN_BACKOFF_FACTOR"},
            {"logger": lg, "time": types.SimpleNamespace(sleep=lambda s: None), "get_app": lambda: app})

check("pyro_coro_returns_real_coroutine", inspect.iscoroutine(c := g["_pyro_coro"](app, "get_chat_member", -100, 1)))
c.close()

res = []
th = threading.Thread(target=lambda: res.append(
    g["_run_async_retry"](lambda: g["_pyro_coro"](app, "get_chat_member", -100, 42), timeout=1)))
th.start()
th.join(5)
check("worker_thread_ban_call_succeeds", res and res[0].user_id == 42, res)

# Old call shape: the sync wrapper already returned a result -> must not raise TypeError
res.clear()
th = threading.Thread(target=lambda: res.append(g["_run_async"](app.get_chat_member(-100, 7), timeout=1)))
th.start()
th.join(5)
check("run_async_accepts_already_executed_result", res and res[0].user_id == 7, res)

# Timeout must apply in worker threads (the wrapper alone would block forever)
app.delay = 5
err = []


def slow():
    try:
        g["_run_async_retry"](lambda: g["_pyro_coro"](app, "get_chat_member", -100, 9), timeout=0.2)
    except BaseException as e:
        err.append(e)


th = threading.Thread(target=slow)
t0 = time.monotonic()
th.start()
th.join(5)
check("worker_thread_timeout_enforced", err and g["_is_timeout_error"](err[0]) and time.monotonic() - t0 < 3, err)
app.delay = 0

# ------------------------------------------------------------------ ChannelGuard executor off the loop
cg = extract("HELPERS/channel_guard.py", {"_auto_block_user"}, {"asyncio": asyncio, "logger": lg}, cls="ChannelGuard")
seen = {}


def executor(user_id, reason):
    seen["thread"] = threading.current_thread()
    # What the real executor ends with: a blocking Pyrogram call waiting on the loop
    seen["member"] = g["_run_async_retry"](lambda: g["_pyro_coro"](app, "get_chat_member", -100, user_id), timeout=1)


guard = types.SimpleNamespace(_block_executor=executor, mark_user_blocked=lambda *a: None)
ok = asyncio.run_coroutine_threadsafe(cg["_auto_block_user"](guard, 555, "auto_window"), loop).result(5)
check("guard_executor_runs_off_loop_thread", seen.get("thread") is not LOOP_THREAD[0], seen)
check("guard_ban_completes", ok is True and seen.get("member") is not None and seen["member"].user_id == 555, seen)
check("guard_no_errors_logged", not cap.at(logging.ERROR), cap.at(logging.ERROR))

# ------------------------------------------------------------------ shutdown drops (#326)
stopping = {"v": False}
cap.records.clear()
sm = extract("HELPERS/safe_messeger.py", {"_dropped_during_shutdown"},
             {"logger": lg, "is_app_stopping": lambda: stopping["v"]})
exc = ConnectionError("Client has not been started yet")
check("no_drop_while_running", sm["_dropped_during_shutdown"](exc, "send_message", 1) is False)
stopping["v"] = True
check("drop_during_shutdown", sm["_dropped_during_shutdown"](exc, "send_message", 1) is True)
check("drop_logged_as_warning_not_error", len(cap.at(logging.WARNING)) == 1 and not cap.at(logging.ERROR))

# ------------------------------------------------------------------ real Pyrogram wrapper (only where installed)
try:
    import pyrogram.sync  # noqa: F401
    from pyrogram import Client
    wrapped = getattr(Client.get_chat_member, "__wrapped__", None)
    check("real_pyrogram_keeps_original_coroutine_fn",
          wrapped is not None and inspect.iscoroutinefunction(wrapped))
except ImportError:
    print("skip real_pyrogram_keeps_original_coroutine_fn (pyrogram not installed)")

# ------------------------------------------------------------------ bounded client stop (#489)
stop_loop = asyncio.new_event_loop()
mg = extract("magic.py", {"_stop_client_bounded", "_CLIENT_STOP_TIMEOUT"}, {"logger": lg})


class HangingClient:
    loop = stop_loop

    async def _stop(self, block=True):
        await asyncio.sleep(30)  # dispatcher waiting for a long upload handler

    stop = functools.wraps(_stop)(lambda self, block=True: None)
    stop.__wrapped__ = _stop


cap.records.clear()
t0 = time.monotonic()
mg["_stop_client_bounded"](HangingClient(), timeout=0.3)
check("client_stop_bounded", time.monotonic() - t0 < 2, time.monotonic() - t0)
check("client_stop_timeout_warned", any("did not stop within" in m for m in cap.at(logging.WARNING)))


class QuickClient:
    loop = stop_loop
    stopped = False

    async def _stop(self, block=True):
        QuickClient.stopped = True

    stop = functools.wraps(_stop)(lambda self, block=True: None)
    stop.__wrapped__ = _stop


mg["_stop_client_bounded"](QuickClient(), timeout=1)
check("client_stop_normal_path", QuickClient.stopped)

loop.call_soon_threadsafe(loop.stop)
print("ALL", len(PASSED), "CHECKS PASSED")
