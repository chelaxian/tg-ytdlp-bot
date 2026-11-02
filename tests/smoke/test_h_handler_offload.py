"""Offline tests: handlers never occupy Pyrogram's dispatcher threads.

Root cause of "bot alive but ignores everything": sync handlers (Always Ask
quality clicks run the whole download) and sync upload-progress callbacks ran
in Client.executor (8 threads); with them all busy no update was dispatched.
install_handler_offload() moves every sync handler to a worker pool and
@background_handler jobs to the heavy pool, so the dispatcher only enqueues.
Run: python test_h_handler_offload.py [repo_root]
"""
import ast
import concurrent.futures
import functools
import os
import sys
import threading
import time
import types
from functools import wraps

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
PASSED = []


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    PASSED.append(name)
    print(f"ok  {name}")


src = open(os.path.join(REPO, "HELPERS/decorators.py"), encoding="utf-8").read()
names = {"_init_pools", "background_queue_depth", "background_handler", "_light_offload",
         "install_handler_offload", "_extract_message_arg", "_format_handler_context",
         "_BG_EXECUTOR", "_BG_INFLIGHT_SEM", "_LIGHT_EXECUTOR", "_POOL_INIT_LOCK", "_BG_QUEUED",
         "_BG_QUEUED_LOCK", "_OFFLOAD_WRAPPERS"}
tree = ast.parse(src)
body = [n for n in tree.body
        if (isinstance(n, ast.FunctionDef) and n.name in names)
        or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in names for t in n.targets))]
logs = []
limits = types.SimpleNamespace(detect_system_resources=lambda: {
    "bg_workers": 2, "inflight": 3, "light_workers": 4, "max_uploads": 1, "cpu_count": 1})
sys.modules["CONFIG.limits"] = types.SimpleNamespace(LimitsConfig=limits)
g = dict(os=os, threading=threading, concurrent=concurrent, wraps=wraps,
         logger=types.SimpleNamespace(info=logs.append, warning=logs.append, exception=logs.append),
         safe_send_message=lambda *a, **k: logs.append(("busy", a)),
         safe_get_messages=lambda *_: types.SimpleNamespace())
exec(compile(ast.Module(body=body, type_ignores=[]), "decorators", "exec"), g)


class FakeClient:
    """Mimics Pyrogram's decorators: register the function, return it unchanged."""

    def __init__(self):
        self.registered = []

    def on_message(self, filters=None, group=0):
        def deco(func):
            self.registered.append(func)
            return func
        return deco

    on_callback_query = on_message


client = FakeClient()
g["install_handler_offload"](client)

release = threading.Event()
ran = {}


def msg(i):
    return types.SimpleNamespace(chat=types.SimpleNamespace(id=i, type="private"), from_user=None, text=f"t{i}")


@client.on_callback_query("askq")
@g["background_handler"](label="askq")
def slow_callback(app, cq):  # an Always Ask quality click: runs a whole download
    ran.setdefault("heavy", []).append(threading.current_thread().name)
    release.wait(5)


@client.on_callback_query("page")
def page_callback(app, cq):  # a cheap menu callback that blocks for a while
    ran.setdefault("light", []).append(threading.current_thread().name)
    time.sleep(0.3)


@client.on_message("menu")
def menu(app, m):
    ran["menu"] = threading.current_thread().name


async def async_handler(app, m):
    pass


client.on_message("async")(async_handler)

check("heavy_handler_not_double_wrapped", client.registered[0] is slow_callback)
check("module_name_keeps_original", page_callback.__name__ == "page_callback" and client.registered[1] is not page_callback)
check("async_handler_untouched", client.registered[-1] is async_handler)

# 8 dispatcher threads deliver 8 quality clicks: every call returns at once
t0 = time.monotonic()
dispatch = concurrent.futures.ThreadPoolExecutor(8)
list(dispatch.map(lambda i: client.registered[0](None, msg(i)), range(8)))
check("dispatcher_never_blocks", time.monotonic() - t0 < 0.5, time.monotonic() - t0)
time.sleep(0.2)
# bg_workers=2, inflight=3: 2 run, 1 waits, the other 5 users get "busy" instead of silence
check("heavy_overload_reported", sum(1 for x in logs if isinstance(x, tuple) and x[0] == "busy") == 5)
check("queue_depth_visible", g["background_queue_depth"]() == 1, g["background_queue_depth"]())
check("queued_logged_separately", any("[HANDLER-QUEUED]" in str(x) for x in logs))
# ...and while all downloads hang, menus and messages are still handled
list(dispatch.map(lambda i: client.registered[1](None, msg(i)), range(3)))
client.registered[2](None, msg(99))
deadline = time.monotonic() + 2
while "menu" not in ran and time.monotonic() < deadline:
    time.sleep(0.01)
check("menu_handled_while_downloads_hang", "menu" in ran)
time.sleep(0.5)
check("light_callbacks_ran", len(ran.get("light", [])) == 3 and all(n.startswith("light") for n in ran["light"]), ran)
release.set()
time.sleep(0.5)
check("queue_drains", g["background_queue_depth"]() == 0 and len(ran["heavy"]) == 3, ran.get("heavy"))
check("heavy_runs_on_bg_pool", all(n.startswith("bg") for n in ran["heavy"]), ran["heavy"])
print("ALL", len(PASSED), "CHECKS PASSED")
