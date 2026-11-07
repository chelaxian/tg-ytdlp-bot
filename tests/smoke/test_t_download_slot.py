"""Smoke test: per-user download slots are taken atomically and honour the limit.

Needs the bot's config (imports HELPERS.download_status), so run on a bot checkout:
    python tests/smoke/test_t_download_slot.py
"""
import os
import sys
import threading
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from HELPERS import download_status as ds  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


LIMIT = ds.LimitsConfig.MAX_CONCURRENT_DOWNLOADS
U = 987650001
check("limit is the documented 3", LIMIT == 3)

# 1. sequential: LIMIT slots, then refusal; refusal takes nothing
got = [ds.acquire_download_slot(U) for _ in range(LIMIT + 2)]
check("first LIMIT acquisitions succeed", got[:LIMIT] == [True] * LIMIT)
check("extra acquisitions are refused", got[LIMIT:] == [False, False])
check("refusals do not change the counter", ds.get_active_download(U) == LIMIT)
check("can_start_download agrees (False)", ds.can_start_download(U) is False)

# 2. finishing one task frees exactly one slot
ds.set_active_download(U, False)
check("one slot freed", ds.can_start_download(U) is True and ds.get_active_download(U) == LIMIT - 1)
check("re-acquire works", ds.acquire_download_slot(U) is True)
for _ in range(LIMIT):
    ds.set_active_download(U, False)
check("counter back to 0 and entry removed", ds.get_active_download(U) == 0 and U not in ds.active_downloads)

# 3. the race: many simultaneous starts, never more than LIMIT winners
U2 = 987650002
barrier = threading.Barrier(40)
results = []


def starter():
    barrier.wait()
    results.append(ds.acquire_download_slot(U2))


threads = [threading.Thread(target=starter) for _ in range(40)]
[t.start() for t in threads]
[t.join() for t in threads]
check("40 simultaneous starts -> exactly LIMIT winners", results.count(True) == LIMIT)
check("counter equals winners", ds.get_active_download(U2) == LIMIT)
for _ in range(LIMIT):
    ds.set_active_download(U2, False)

# 4. playlist / multi-URL: only when the user has nothing running
U3 = 987650003
check("playlist starts on an idle user", ds.acquire_download_slot(U3, is_playlist=True) is True)
check("second playlist refused", ds.acquire_download_slot(U3, is_playlist=True) is False)
ds.set_active_download(U3, False)
check("single running blocks a playlist", ds.acquire_download_slot(U3) is True
      and ds.acquire_download_slot(U3, is_playlist=True) is False)
check("multi-url also needs an idle user", ds.acquire_download_slot(U3, is_multi_url=True) is False)
ds.set_active_download(U3, False)

# 5. users are isolated from each other
U4, U5 = 987650004, 987650005
[ds.acquire_download_slot(U4) for _ in range(LIMIT)]
check("another user is not affected by a full user", ds.acquire_download_slot(U5) is True)
for _ in range(LIMIT):
    ds.set_active_download(U4, False)
ds.set_active_download(U5, False)

# 6. /clean-style cancel only touches this user's tasks
a1, a2 = ds.register_download_cancel_event(U4), ds.register_download_cancel_event(U4)
b1 = ds.register_download_cancel_event(U5)
check("cancel returns the user's task count", ds.cancel_user_downloads(U4) == 2)
check("user's events set, other user's untouched", a1.is_set() and a2.is_set() and not b1.is_set())
ds.unregister_download_cancel_event(U5, b1)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
