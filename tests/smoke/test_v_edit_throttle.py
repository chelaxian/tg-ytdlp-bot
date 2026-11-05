"""Offline test: safe_edit_message_text contract + per-chat edit throttle.

Callers treat `result is None` as "progress message is gone" (download progress
stops for good, hourglass stops). It used to return None for MESSAGE_NOT_MODIFIED,
for FloodWait > 60 s and for any other failure, so one hiccup killed the progress
bar; private chats had no edit throttle at all.

Run: python test_v_edit_throttle.py [repo_root]
"""
import ast
import os
import sys
import threading
import time
import types

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
PASSED = []


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    PASSED.append(name)
    print(f"ok  {name}")


src = open(os.path.join(REPO, "HELPERS/safe_messeger.py"), encoding="utf-8").read()
names = {"_EDIT_SPACING_PRIVATE", "_EDIT_SPACING_GROUP", "_EDIT_MAX_QUEUE_WAIT", "_EDIT_INLINE_FLOOD_MAX",
         "_edit_state_lock", "_edit_next_slot", "_edit_paused_until", "_edit_cleanup_mono",
         "_edit_reserve_slot", "_edit_pause_chat", "safe_edit_message_text"}
tree = ast.parse(src)
body = [n for n in tree.body
        if (isinstance(n, ast.FunctionDef) and n.name in names)
        or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in names for t in n.targets))]
check("extracted all edit helpers", len(body) == len(names), f"{len(body)} of {len(names)}")


class FloodWait(Exception):
    def __init__(self, value):
        super().__init__(f"FLOOD_WAIT {value}")
        self.value = value


class PeerGone(Exception):
    pass


calls = []
script = []          # exceptions / results returned by the fake pyrogram call, in order
flood_files = []
sleeps = []

ns = {
    "time": types.SimpleNamespace(monotonic=time.monotonic, time=time.time,
                                  sleep=lambda s: sleeps.append(s)),
    "threading": threading,
    "logger": types.SimpleNamespace(debug=lambda *a, **k: None, warning=lambda *a, **k: None),
    "safe_get_messages": lambda _u: types.SimpleNamespace(HELPER_MESSAGE_ID_INVALID_MSG="MESSAGE_ID_INVALID"),
    "get_app_safe": lambda: types.SimpleNamespace(edit_message_text=lambda *a, **k: None),
    "FloodWait": FloodWait,
    "_PERMANENT_PEER_ERRORS": (PeerGone,),
    "_log_unreachable_chat": lambda *a, **k: None,
    "_dropped_during_shutdown": lambda *a, **k: False,
    "_should_retry": lambda e, u, d=5: "FLOOD_WAIT" in str(e) or "seqno" in str(e),
    "_write_flood_wait_file": lambda c, v: flood_files.append((c, v)),
}


def fake_run(app, coro):
    calls.append(1)
    item = script.pop(0)
    if isinstance(item, BaseException):
        raise item
    return item


ns["run_pyrogram_client_coroutine"] = fake_run
exec(compile(ast.Module(body=body, type_ignores=[]), "safe_messeger_extract", "exec"), ns)
edit = ns["safe_edit_message_text"]


def reset():
    calls.clear()
    script.clear()
    sleeps.clear()
    flood_files.clear()
    ns["_edit_next_slot"].clear()
    ns["_edit_paused_until"].clear()


# 1. success returns the message
reset(); script.append("MSG")
check("edit ok -> message", edit(1, 10, "t") == "MSG")

# 2. not modified: alive, not dead
reset(); script.append(Exception("[400 MESSAGE_NOT_MODIFIED]"))
r = edit(2, 10, "t")
check("not modified -> False (not None)", r is False and len(calls) == 1, (r, len(calls)))

# 3. deleted message -> None
reset(); script.append(Exception("[400 MESSAGE_ID_INVALID]"))
check("message deleted -> None", edit(3, 10, "t") is None)

# 4. unreachable chat -> None, no retries
reset(); script.append(PeerGone("blocked"))
check("blocked user -> None, one call", edit(4, 10, "t") is None and len(calls) == 1)

# 5. unknown failure: alive (False), not three instant retries
reset(); script.append(Exception("boom"));
r = edit(5, 10, "t")
check("unknown error -> False", r is False, r)
check("unknown error not retried", len(calls) == 1, len(calls))

# 6. short FloodWait: sleeps and retries once
reset(); script.extend([FloodWait(3), "MSG"])
r = edit(6, 10, "t")
check("short FloodWait retried", r == "MSG" and len(calls) == 2, (r, len(calls)))
check("short FloodWait slept 4s", 4 in sleeps, sleeps)

# 7. long FloodWait: no sleep, not dead, chat paused, next edits skipped without a request
reset(); script.append(FloodWait(300))
r = edit(7, 10, "t")
check("long FloodWait -> False (alive)", r is False, r)
check("long FloodWait did not sleep", not [s for s in sleeps if s > 10], sleeps)
check("long FloodWait recorded", flood_files == [(7, 300)], flood_files)
before = len(calls)
check("paused chat skips the request", edit(7, 10, "t2") is False and len(calls) == before)
check("other chat unaffected", (script.append("MSG") or edit(8, 10, "t")) == "MSG")

# 8. private chat spacing: second edit waits ~1s, third ~2s, a long queue is dropped
reset(); script.extend(["A", "B", "C"])
edit(20, 1, "a"); edit(20, 1, "b")
check("second private edit waits ~1s", sleeps and 0.5 < sleeps[-1] <= 1.0, sleeps)
reset(); ns["_edit_next_slot"][21] = time.monotonic() + 100
check("overloaded queue -> dropped without request", edit(21, 1, "x") is False and not calls)

# 9. groups use the long spacing
reset(); script.extend(["A", "B"])
edit(-100, 1, "a"); edit(-100, 1, "b")
check("group spacing ~5s", sleeps and 4.0 < sleeps[-1] <= 5.0, sleeps)

# 10. concurrent edits to one chat get distinct slots (no stampede)
reset()
waits = [ns["_edit_reserve_slot"](30, 1.0) for _ in range(4)]
check("slots increase by spacing", all(abs((waits[i + 1] - waits[i]) - 1.0) < 0.05 for i in range(3)), waits)

# 11. cleanup drops stale entries
reset()
ns["_edit_next_slot"][99] = time.monotonic() - 1000
ns["_edit_paused_until"][98] = time.monotonic() - 1000
ns["_edit_cleanup_mono"] = 0.0
ns["_edit_reserve_slot"](31, 1.0)
check("stale chat entries pruned", 99 not in ns["_edit_next_slot"] and 98 not in ns["_edit_paused_until"])

print(f"\n{len(PASSED)} passed")
