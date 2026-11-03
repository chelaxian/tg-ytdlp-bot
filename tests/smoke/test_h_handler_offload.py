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
         "_BG_QUEUED_LOCK", "_OFFLOAD_WRAPPERS", "message_has_url", "_URL_RE", "light_only",
         "send_reply_keyboard_always", "_send_reply_keyboard_locked", "reply_keyboard_msg_ids",
         "_reply_kb_cleanup_counter", "_REPLY_KB_CLEANUP_INTERVAL", "_reply_kb_locks", "_reply_kb_locks_guard",
         "_reply_kb_last", "_REPLY_KB_MIN_INTERVAL", "_PriorityExecutor", "PRIORITY_SINGLE",
         "_BG_BULK_SEM", "_PLAYLIST_HINTS", "_request_text", "request_priority",
         "UNKNOWN_COST_MB", "_extract_update"}
tree = ast.parse(src)


def _targets(n):
    for t in n.targets:
        yield from ([getattr(e, "id", None) for e in t.elts] if isinstance(t, ast.Tuple) else [getattr(t, "id", None)])


body = [n for n in tree.body
        if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names)
        or (isinstance(n, ast.Assign) and any(t in names for t in _targets(n)))]
logs = []
limits = types.SimpleNamespace(detect_system_resources=lambda: {
    "bg_workers": 2, "inflight": 3, "light_workers": 4, "max_uploads": 1, "cpu_count": 1})
sys.modules["CONFIG.limits"] = types.SimpleNamespace(LimitsConfig=limits)
import contextlib  # noqa: E402
_scopes = []


@contextlib.contextmanager
def _task_scope(label):
    _scopes.append(label)
    yield None


sys.modules["HELPERS.warp_tunnel"] = types.SimpleNamespace(task_scope=_task_scope)
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
# catch-all text handler: commands/menus never wait for the busy heavy pool
@client.on_message("text")
@g["background_handler"](label="url_distractor", heavy_if=g["message_has_url"])
def text_handler(app, m):
    ran.setdefault("text", []).append((m.text, threading.current_thread().name))


def tmsg(text, entities=None):
    return types.SimpleNamespace(chat=types.SimpleNamespace(id=7, type="private"), from_user=None,
                                 text=text, entities=entities)


has_url = g["message_has_url"]
for t, want in (("/clean", False), ("/help", False), ("🧹", False), ("hello there", False), ("/clean 3", False),
                ("https://youtu.be/x", True), ("/audio https://x.com/a/b", True), ("www.example.com", True),
                ("youtube.com/watch?v=1", True), ("see example.org/page", True)):
    check(f"has_url {t!r}", has_url(tmsg(t)) is want)
check("has_url_text_link_entity", has_url(tmsg("click", [types.SimpleNamespace(type="MessageEntityType.TEXT_LINK")])))
busy_before = sum(1 for x in logs if isinstance(x, tuple) and x[0] == "busy")
handler = client.registered[-1]
t0 = time.monotonic()
for _ in range(14):
    handler(None, tmsg("/clean"))
deadline = time.monotonic() + 2
while len(ran.get("text", [])) < 14 and time.monotonic() < deadline:
    time.sleep(0.01)
check("commands_answered_while_heavy_pool_full", len(ran.get("text", [])) == 14
      and all(n.startswith("light") for _, n in ran["text"]), ran.get("text"))
check("commands_not_reported_busy", sum(1 for x in logs if isinstance(x, tuple) and x[0] == "busy") == busy_before)
check("light_route_logged", any("(light)" in str(x) for x in logs) and any("[HANDLER-DONE] url_distractor" in str(x) for x in logs))
handler(None, tmsg("https://youtu.be/x"))
check("url_still_goes_to_heavy_pool", sum(1 for x in logs if isinstance(x, tuple) and x[0] == "busy") == busy_before + 1)
release.set()
time.sleep(0.5)
check("queue_drains", g["background_queue_depth"]() == 0 and len(ran["heavy"]) == 3, ran.get("heavy"))
check("heavy_runs_on_bg_pool", all(n.startswith("bg") for n in ran["heavy"]), ran["heavy"])
check("every_task_runs_in_a_warp_scope", any("askq" in l for l in _scopes) and any("page_callback" in l for l in _scopes), _scopes[:4])
# priority queue: single link first, several links / playlists last
prio = g["request_priority"]
S, N, B = g["PRIORITY_SINGLE"], g["PRIORITY_NORMAL"], g["PRIORITY_BULK"]
for t, want in (("https://youtu.be/abc", S), ("https://www.youtube.com/watch?v=abc&list=PLx", S),
                ("https://youtu.be/a https://youtu.be/b", B), ("https://www.youtube.com/playlist?list=PLx", B),
                ("https://youtube.com/@chan*1*10", B), ("https://soundcloud.com/u/sets/x", B),
                ("/check_cookie", N), ("hello", N)):
    check(f"priority {t!r}", prio(tmsg(t)) == want, prio(tmsg(t)))
menu = types.SimpleNamespace(text="Choose quality", reply_to_message=tmsg("https://youtu.be/a https://youtu.be/b"))
check("priority_menu_click_uses_users_links", prio(menu) == B)
order, gate = [], threading.Event()
ex = g["_PriorityExecutor"](2, bulk_max=1, name="bg")
for _ in range(2):
    ex.submit(gate.wait, 5, priority=N)  # both workers busy
time.sleep(0.1)
for name, p_ in (("bulk1", B), ("bulk2", B), ("single1", S), ("single2", S)):
    ex.submit(order.append, name, priority=p_)
gate.set()
deadline = time.monotonic() + 3
while len(order) < 4 and time.monotonic() < deadline:
    time.sleep(0.01)
check("singles_jump_ahead_of_bulk", order[:2] == ["single1", "single2"] and sorted(order[2:]) == ["bulk1", "bulk2"], order)
hold, started = threading.Event(), []


def long_bulk(n):
    started.append(n)
    hold.wait(5)


ex2 = g["_PriorityExecutor"](2, bulk_max=1, name="bg")
ex2.submit(long_bulk, "b1", priority=B)
ex2.submit(long_bulk, "b2", priority=B)
time.sleep(0.2)
check("bulk_never_takes_every_worker", started == ["b1"], started)
done = threading.Event()
ex2.submit(done.set, priority=S)
check("single_runs_while_playlist_downloads", done.wait(1))
hold.set()
time.sleep(0.2)
check("bulk_queue_continues_after_slot_frees", started == ["b1", "b2"], started)

# reply keyboard: a burst of commands from one user leaves one keyboard message, not a pile of empty ones
sent, deleted = [], []
_ids = iter(range(1000, 2000))


def _send(uid, text, reply_markup=None):
    time.sleep(0.05)  # Telegram round trip: lets concurrent calls interleave
    m = types.SimpleNamespace(id=next(_ids))
    sent.append(m.id)
    return m


class _App:
    def edit_message_text(self, *a, **k):
        raise RuntimeError("reply keyboards cannot be edited")

    def delete_messages(self, uid, ids):
        deleted.extend(ids)


g.update(app=_App(), safe_send_message=_send, get_main_reply_keyboard=lambda mode: mode)
kb = concurrent.futures.ThreadPoolExecutor(14)
list(kb.map(lambda _: g["send_reply_keyboard_always"](42, "2x3"), range(14)))
check("keyboard_burst_one_message", len(sent) - len(deleted) == 1 and len(sent) == 1, (sent, deleted))
g["_reply_kb_last"][42] = ("2x3", time.monotonic() - 60)
g["send_reply_keyboard_always"](42, "2x3")
check("keyboard_refreshed_after_interval", len(sent) == 2 and deleted == [sent[0]], (sent, deleted))
g["send_reply_keyboard_always"](42, "FULL")
check("keyboard_mode_change_applies_at_once", len(sent) == 3 and len(sent) - len(deleted) == 1, (sent, deleted))
print("ALL", len(PASSED), "CHECKS PASSED")
