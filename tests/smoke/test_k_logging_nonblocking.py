"""Offline test: logging never blocks the caller (HELPERS/logger.py).

When the sinks (stderr -> journald, bot.log) stall on a slow disk, logger.info()
must still return at once; records beyond the queue size are dropped.
Run: python test_k_logging_nonblocking.py [repo_root]
"""
import ast
import logging
import os
import queue
import sys
import threading
import time

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
src = open(os.path.join(REPO, "HELPERS/logger.py"), encoding="utf-8").read()
cls = [n for n in ast.parse(src).body if isinstance(n, ast.ClassDef) and n.name == "_DroppingQueueHandler"][0]
import logging.handlers as _log_handlers  # noqa: E402
g = {"_log_handlers": _log_handlers, "_queue": queue}
exec(compile(ast.Module(body=[cls], type_ignores=[]), "logger", "exec"), g)

release = threading.Event()


class StalledSink(logging.Handler):
    def emit(self, record):
        release.wait(10)  # journald / disk stalled


q = queue.Queue(maxsize=100)
listener = _log_handlers.QueueListener(q, StalledSink())
listener.start()
log = logging.getLogger("nonblocking-test")
log.propagate = False
log.addHandler(g["_DroppingQueueHandler"](q))
t0 = time.monotonic()
for i in range(1000):
    log.warning("record %d", i)
elapsed = time.monotonic() - t0
assert elapsed < 1.0, f"logging blocked for {elapsed:.1f}s"
print(f"ok  1000 records in {elapsed*1000:.0f} ms while the sink is stalled")
assert g["_DroppingQueueHandler"].dropped >= 800, g["_DroppingQueueHandler"].dropped
print(f"ok  overflow dropped ({g['_DroppingQueueHandler'].dropped}) instead of blocking")
release.set()
time.sleep(0.5)
listener.stop()
assert "class _DroppingQueueHandler" in src and "QueueListener(" in src and "_DroppingQueueHandler(_log_queue)" in src
print("ok  logger.py routes the root logger through the queue")
print("ALL 3 CHECKS PASSED")
