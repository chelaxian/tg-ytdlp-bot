"""Offline smoke tests: stall-based upload wait (#372).

A slow but progressing upload must not be declared failed at the size-scaled
timeout; a stalled one must; the hard limit still applies. Also checks the
Client.save_file heartbeat wrapper. No network, no Telegram session.
Run: python test_e_upload_stall.py [repo_root]
"""
import asyncio
import os
import sys
import tempfile
import threading
import time
import types

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
sys.path.insert(0, REPO)
os.chdir(tempfile.mkdtemp(prefix="test_e_"))  # HELPERS.logger writes bot.log into cwd

PASSED = []


def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    PASSED.append(name)
    print(f"ok  {name}")


from HELPERS import upload_guard as ug

ug._UPLOAD_STALL_SECONDS = 0.4
ug._UPLOAD_HARD_TIMEOUT_FACTOR = 10
path = os.path.abspath("video.mp4")
open(path, "wb").close()


def uploading(seconds, beat=0.1, result="sent"):
    def fn():
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            ug.note_upload_progress(path)
            time.sleep(beat)
        return result
    return fn


t0 = time.monotonic()
r = ug.timed_upload(uploading(1.2), timeout=0.3, dedup_key=(1, path))
check("progressing_upload_outlives_timeout", r == "sent" and time.monotonic() - t0 >= 1.1, time.monotonic() - t0)
check("progress_entry_cleaned", path not in ug._UPLOAD_PROGRESS)

ev = threading.Event()
t0 = time.monotonic()
try:
    ug.timed_upload(lambda: (ev.wait(3), "late")[1], timeout=0.3, dedup_key=(2, path))
    err = None
except TimeoutError as e:
    err = e
check("stalled_upload_times_out", err is not None and time.monotonic() - t0 < 1.0, time.monotonic() - t0)
ev.set()

ug._UPLOAD_HARD_TIMEOUT_FACTOR = 3
t0 = time.monotonic()
try:
    ug.timed_upload(uploading(3), timeout=0.3, dedup_key=(3, path))
    err = None
except TimeoutError as e:
    err = e
elapsed = time.monotonic() - t0
check("hard_limit_applies", err is not None and 0.8 <= elapsed < 1.6, elapsed)
time.sleep(2.5)  # let the background upload finish before the next case

# ------------------------------------------------------------------ heartbeat callbacks
calls = []
hb = ug._with_progress_heartbeat(path, lambda c, t, *a: calls.append((c, t, a)) or "sync-ret")
ug._UPLOAD_PROGRESS.clear()
check("sync_callback_kept", hb(1, 2, "x") == "sync-ret" and calls == [(1, 2, ("x",))])
check("sync_callback_marks_progress", path in ug._UPLOAD_PROGRESS)


async def acb(c, t, *a):
    calls.append(("async", c, t))
    return "async-ret"


ahb = ug._with_progress_heartbeat(path, acb)
ug._UPLOAD_PROGRESS.clear()
check("async_callback_stays_async", asyncio.iscoroutinefunction(ahb))
check("async_callback_kept", asyncio.run(ahb(3, 4)) == "async-ret" and calls[-1] == ("async", 3, 4))
check("async_callback_marks_progress", path in ug._UPLOAD_PROGRESS)
ug._UPLOAD_PROGRESS.clear()
nhb = ug._with_progress_heartbeat(path, None)
check("no_callback_heartbeat_is_async", asyncio.iscoroutinefunction(nhb))
asyncio.run(nhb(5, 6))
check("no_callback_still_marks_progress", path in ug._UPLOAD_PROGRESS)

# ------------------------------------------------------------------ save_file wrapper
seen = {}


class StubClient:
    def save_file(self, path, file_id=None, file_part=0, progress=None, progress_args=()):
        seen.update(path=path, progress=progress, file_id=file_id)
        return "input-file"


real_pyrogram = sys.modules.get("pyrogram")
sys.modules["pyrogram"] = types.SimpleNamespace(Client=StubClient)
try:
    ug._install_save_file_heartbeat()
    ug._install_save_file_heartbeat()  # idempotent
    c = StubClient()
    check("save_file_wrapped_once", StubClient.save_file._upload_heartbeat and
          not getattr(StubClient.save_file.__wrapped__, "_upload_heartbeat", False))
    check("save_file_result_passthrough", c.save_file(path) == "input-file")
    ug._UPLOAD_PROGRESS.clear()
    asyncio.run(seen["progress"](1, 1))
    check("save_file_injects_heartbeat", path in ug._UPLOAD_PROGRESS)
    import io
    c.save_file(io.BytesIO(b"x"))
    check("save_file_skips_non_paths", seen["progress"] is None)
    c.save_file(path, 7, 0, "positional-progress")
    check("save_file_keeps_positional_progress", seen["progress"] == "positional-progress" and seen["file_id"] == 7)
finally:
    if real_pyrogram is not None:
        sys.modules["pyrogram"] = real_pyrogram

try:
    import pyrogram
    check("real_client_save_file_wrapped", getattr(pyrogram.Client.save_file, "_upload_heartbeat", False))
except ImportError:
    print("skip real_client_save_file_wrapped (pyrogram not installed)")

# ------------------------------------------------------------------ quarantined dump retention
import ast
import logging
src = open(os.path.join(REPO, "services/stats_collector.py"), encoding="utf-8").read()
nodes = [n for n in ast.parse(src).body
         if (isinstance(n, ast.FunctionDef) and n.name == "_prune_corrupt_dumps")
         or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) == "_CORRUPT_DUMPS_KEEP" for t in n.targets))]
g = {"os": os, "logger": logging.getLogger("prune_test")}
exec(compile(ast.Module(body=nodes, type_ignores=[]), "stats_collector", "exec"), g)
d = tempfile.mkdtemp(prefix="dumps_")
dump = os.path.join(d, "dump.json")
open(dump, "w").close()
for i in range(6):
    f = os.path.join(d, f"dump.json.corrupt.{1000 + i}")
    open(f, "w").close()
    os.utime(f, (1000 + i, 1000 + i))
open(os.path.join(d, "other.json.corrupt.1"), "w").close()
g["_prune_corrupt_dumps"](dump)
left = sorted(os.listdir(d))
check("prune_keeps_newest_3", left == ["dump.json", "dump.json.corrupt.1003", "dump.json.corrupt.1004",
                                       "dump.json.corrupt.1005", "other.json.corrupt.1"], left)

print("ALL", len(PASSED), "CHECKS PASSED")
