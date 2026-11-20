"""Whole-process freeze diagnostics.

Twice (16 and 19 Nov 2026) the DE bot froze completely: every Python thread
stopped, including the watchdog heartbeat thread, so systemd killed the
process with SIGABRT and left zero evidence of where it was stuck. A freeze
that silences Python threads can only be reported from outside the
interpreter's GIL world.

``faulthandler.dump_traceback_later`` arms a native (C-level) watchdog
thread: if the timer is not re-armed within ``timeout`` seconds it prints
every thread's stack trace to stderr (the systemd journal) — even while the
GIL is held forever by a deadlocked C extension.

The healthy watchdog loop re-arms the timer on every beat, so the dump only
fires when the process truly stopped making progress.
"""

from __future__ import annotations

import faulthandler

# Must exceed the watchdog loop cadence (responsive check up to 20 s + 30 s
# sleep) so a merely busy bot never triggers a dump, and stay below the unit
# WatchdogSec=120 so the stacks land in the journal *before* systemd's SIGABRT.
DEFAULT_DUMP_SECONDS = 90


def arm_freeze_dump(timeout: float = DEFAULT_DUMP_SECONDS, file=None) -> None:
    """(Re)arm the native stack dump; the previous timer is discarded."""
    faulthandler.cancel_dump_traceback_later()
    if file is None:
        faulthandler.dump_traceback_later(timeout, repeat=False, exit=False)
    else:
        faulthandler.dump_traceback_later(timeout, repeat=False, exit=False, file=file)


def cancel_freeze_dump() -> None:
    """Disarm the native stack dump (no-op when not armed)."""
    faulthandler.cancel_dump_traceback_later()
