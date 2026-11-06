"""Smoke test: WARP egress rotation (HELPERS/warp_tunnel), offline - no wireproxy needed.

Run: python tests/smoke/test_t_warp_rotation.py
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import logging  # noqa: E402
import types  # noqa: E402

# HELPERS.logger needs the real (secret, untracked) CONFIG/config.py - stub it
_stub = types.ModuleType("HELPERS.logger")
_stub.logger = logging.getLogger("warp-test")
sys.modules["HELPERS.logger"] = _stub

from HELPERS import warp_tunnel as w  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


# ---- fake tunnel: no processes, egress comes from a script ----
script = []


def fake_start_once(self):
    self.egress = script.pop(0)
    self.started_at = w.time.monotonic()
    self.proc = object()  # truthy, "alive" is patched below
    return self


w.Tunnel._start_once = fake_start_once
w.Tunnel._kill = lambda self: setattr(self, "proc", None)
w.Tunnel.stop = lambda self: setattr(self, "proc", None)
w.Tunnel.alive = lambda self: self.proc is not None
w._cfg = lambda name: {"WARP_PER_TASK": True, "WARP_REROLL_ATTEMPTS": 3, "WARP_RECENT_EGRESS": 256,
                       "WARP_SHARED_MAX_AGE": 120, "WARP_PROXY_HOST": "127.0.0.1"}.get(name, w._DEFAULTS.get(name))

# /64 helper
check("net64 groups one /64", w._net64("2a09:bac5:27bb:2478::3a2:21") == w._net64("2a09:bac5:27bb:2478::1d8:99"))
check("net64 splits different /64", w._net64("2a09:bac5:27bb:2478::1") != w._net64("2a09:bac5:27ba:2482::1"))

# a repeated address or /64 is re-rolled
script[:] = ["2a09:1::1", "2a09:1::1", "2a09:1::2", "2a09:2::1"]
t1 = w.Tunnel("a")
t1.start()
check("first tunnel keeps first IP", t1.egress == "2a09:1::1")
t2 = w.Tunnel("b")
t2.start()
check("same IP/same /64 re-rolled until fresh", t2.egress == "2a09:2::1" and not script)

# when every re-roll repeats, the tunnel still starts (no infinite loop)
script[:] = ["2a09:2::1"] * 4
t3 = w.Tunnel("c")
t3.start()
check("gives up after WARP_REROLL_ATTEMPTS", t3.egress == "2a09:2::1" and not script)

# rotation inside a task scope
script[:] = ["2a09:3::1", "2a09:4::1", "2a09:5::1"]
w.Tunnel.url = property(lambda self: "http://127.0.0.1:1")
with w.task_scope("task one") as scope:
    check("rotate before first request does nothing", w.rotate_current_task("early") is None)
    url = scope.proxy_url()
    first = scope.tunnel.egress
    new = w.rotate_current_task("cookie source 2")
    check("rotate gives a new egress", new == "2a09:4::1" and new != first)
    check("proxy URL unchanged by rotation", scope.proxy_url() == url)
    check("rotations counted", scope.rotations == 1)
    new2 = w.rotate_current_task("cookie source 3")
    check("second rotation again new", new2 == "2a09:5::1" and scope.rotations == 2)
check("no scope -> rotate is a no-op", w.rotate_current_task("x") is None)
check("tunnel released after task", w.active_count() == 0)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
