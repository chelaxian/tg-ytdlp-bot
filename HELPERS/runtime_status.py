"""Small heartbeat file the bot writes for the dashboard.

The dashboard runs in a separate process and must not import bot internals, so
the bot publishes what the dashboard needs (is it alive, how many tasks run or
wait) to CONFIG/.bot_runtime.json every few seconds. The dashboard uses it for
the live status and for "restart when idle".
"""

from __future__ import annotations

import json
import os
import tempfile
import threading
import time
from pathlib import Path

RUNTIME_FILE = Path(os.environ.get("TG_DASHBOARD_PROJECT_DIR", str(Path(__file__).resolve().parent.parent))) / "CONFIG" / ".bot_runtime.json"
INTERVAL = 5

_started = threading.Event()
_STARTED_AT = time.time()


def snapshot() -> dict:
    data = {"pid": os.getpid(), "started_at": int(_STARTED_AT), "ts": int(time.time()),
            "running": 0, "queued": 0, "warp_tunnels": 0}
    try:
        from HELPERS.decorators import heavy_pool_stats
        data.update(heavy_pool_stats())
    except Exception:
        pass
    try:
        from HELPERS.warp_tunnel import active_count
        data["warp_tunnels"] = int(active_count())
    except Exception:
        pass
    try:
        from HELPERS.app_instance import is_app_stopping
        data["stopping"] = bool(is_app_stopping())
    except Exception:
        pass
    return data


def _write(data: dict) -> None:
    RUNTIME_FILE.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".runtime.", dir=str(RUNTIME_FILE.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        os.replace(tmp, RUNTIME_FILE)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _loop() -> None:
    while True:
        try:
            _write(snapshot())
        except Exception:
            pass
        time.sleep(INTERVAL)


def start() -> None:
    if _started.is_set():
        return
    _started.set()
    threading.Thread(target=_loop, name="runtime_status", daemon=True).start()


def read(max_age: int = 30) -> dict:
    """Dashboard side: the last heartbeat, with `alive` = fresh enough."""
    try:
        with open(RUNTIME_FILE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError
    except Exception:
        return {"alive": False}
    data["alive"] = (time.time() - float(data.get("ts") or 0)) <= max_age
    return data
