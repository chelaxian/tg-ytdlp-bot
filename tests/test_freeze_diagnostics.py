"""Tests for the whole-process freeze diagnostics (issue: watchdog SIGABRT
recurrence on 16/19 Nov 2026 left zero evidence of the stuck thread)."""
import subprocess
import sys
import unittest

sys.path.insert(0, ".")

from HELPERS.freeze_diagnostics import (
    DEFAULT_DUMP_SECONDS,
    arm_freeze_dump,
    cancel_freeze_dump,
)


class FreezeDiagnosticsTests(unittest.TestCase):
    def test_default_timeout_between_loop_cadence_and_watchdogsec(self):
        # loop cadence: 20 s responsive check + 30 s sleep = 50 s worst case;
        # unit WatchdogSec=120. Dump must fire in between.
        self.assertGreater(DEFAULT_DUMP_SECONDS, 50)
        self.assertLess(DEFAULT_DUMP_SECONDS, 120)

    def test_arm_and_cancel_is_clean(self):
        # arming then cancelling must not raise and must leave no timer
        arm_freeze_dump(300)
        cancel_freeze_dump()

    def test_cancel_without_arm_is_noop(self):
        cancel_freeze_dump()

    def test_dump_fires_when_loop_stops_rearming(self):
        # End-to-end: arm with a short timeout, do NOT re-arm, and check the
        # native thread prints a traceback to the child's stderr.
        code = (
            "import sys; sys.path.insert(0, '.'); "
            "from HELPERS.freeze_diagnostics import arm_freeze_dump; "
            "import time; arm_freeze_dump(1); time.sleep(3)"
        )
        proc = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True, text=True, timeout=30,
        )
        self.assertIn("Thread 0x", proc.stderr, "expected a stack dump on stderr")
        self.assertIn("Timeout (", proc.stderr)


if __name__ == "__main__":
    unittest.main()
