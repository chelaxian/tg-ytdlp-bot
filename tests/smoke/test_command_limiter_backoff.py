"""Regression tests for command-limiter backoff and persisted state."""
import importlib
import logging
import os
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)
logger_module = types.ModuleType('HELPERS.logger')
logger_module.logger = logging.getLogger('command-limiter-test')
with tempfile.TemporaryDirectory() as initial_dir:
    original_dir = os.getcwd()
    os.chdir(initial_dir)
    try:
        with patch.dict(sys.modules, {'HELPERS.logger': logger_module}):
            limiter = importlib.import_module('HELPERS.command_limiter')
            limiter._save_stop.set()
            limiter._dirty.set()
            limiter._save_thread.join(timeout=5)
    finally:
        os.chdir(original_dir)


class CommandBackoffTest(unittest.TestCase):
    def setUp(self):
        limiter._registry = {}
        self.now = 1000000.0
        self.clock = patch.object(limiter.time, 'time', side_effect=lambda: self.now)
        self.clock.start()

    def tearDown(self):
        self.clock.stop()

    def burst(self, uid=1):
        for _ in range(limiter.LimitsConfig.COMMAND_LIMIT_PER_MINUTE):
            self.assertTrue(limiter.check_command_limit(uid)[0])
        self.assertFalse(limiter.check_command_limit(uid)[0])
        return limiter._registry[uid].cooldown['duration']

    def test_initial_backoff_repeated_and_forgiven(self):
        self.assertEqual(self.burst(), 60)
        self.assertFalse(limiter.check_command_limit(1)[0])
        self.now += 61
        self.assertEqual(self.burst(), 120)
        self.now += limiter._VIOLATION_RESET_AFTER + 1
        self.assertEqual(self.burst(), 60)

    def test_backoff_cap_and_user_isolation(self):
        data = limiter._get_user(1)
        data.violations = 100000
        data.last_violation = self.now
        self.assertEqual(self.burst(), limiter._MAX_COOLDOWN)
        self.assertTrue(limiter.check_command_limit(2)[0])

    def test_persistence_and_legacy_active_cooldown(self):
        self.assertEqual(self.burst(), 60)
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(limiter, '_COMMAND_LIMITS_FILE', os.path.join(directory, 'limits.json')), \
                 patch.object(limiter, '_COMMAND_COOLDOWNS_FILE', os.path.join(directory, 'cooldowns.json')):
                limiter._do_save()
                limiter._registry = {}
                limiter._load_from_disk()
                self.assertEqual(limiter._registry[1].last_violation, self.now)
                self.assertFalse(limiter.check_command_limit(1)[0])
                limiter._registry[1].last_violation = 0  # old on-disk records
                self.now += 61
                self.assertEqual(self.burst(), 60)


if __name__ == '__main__':
    unittest.main()
