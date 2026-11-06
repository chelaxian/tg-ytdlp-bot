"""Anti-bot: groups are exempt from per-user bans; unblock forgets history.

Runs the real functions from HELPERS/anti_bot_protection.py without Telegram or a DB.
"""
import ast
import threading
import types
import typing
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'HELPERS' / 'anti_bot_protection.py'
tree = ast.parse(SRC.read_text(encoding='utf-8'))
NAMES = {'_is_group_chat', 'reset_user_state', 'record_user_activity', 'check_and_ban_user'}
funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in NAMES]
assert {f.name for f in funcs} == NAMES


class UserData:
    def __init__(self):
        self.lock = threading.Lock()
        self.url_history = [('u', 1.0)]
        self.command_history = [('c', 1.0)]
        self.message_history = [('m', 1.0)]
        self.message_timestamps = [1.0]
        self.activity_hours = {1: 1.0}


def make_env():
    bans = []
    registry = {}
    env = {
        'Optional': typing.Optional, 'Tuple': typing.Tuple, 'List': typing.List,
        'LimitsConfig': types.SimpleNamespace(TURN_OFF_LIMITS_FOR_ADMINS=True,
                                              ANTI_BOT_PROTECTION_ENABLED=True),
        '_registry': registry,
        '_dirty': threading.Event(),
        '_get_user': lambda uid: registry.setdefault(uid, UserData()),
        '_do_ban_async': lambda uid, reason: bans.append(uid),
        'time': types.SimpleNamespace(time=lambda: 100.0),
        '_bot_start_time': 0.0,
        '_cleanup_user': lambda ud, now: None,
        '_check_flood': lambda ud, now: 'flood',  # would always ban if reached
    }
    exec(compile(ast.Module(body=funcs, type_ignores=[]), str(SRC), 'exec'), env)
    return env, bans, registry


class AntiBotGroupsUnblockTest(unittest.TestCase):
    def test_group_chats_are_never_banned_or_tracked(self):
        env, bans, registry = make_env()
        self.assertEqual(env['check_and_ban_user'](-100123, 'http://x', is_command=False), (False, None))
        env['record_user_activity'](-100123, message_text='hi')
        self.assertEqual(bans, [])
        self.assertNotIn(-100123, registry)

    def test_private_user_still_checked(self):
        env, bans, registry = make_env()
        should_ban, reason = env['check_and_ban_user'](42, 'http://x')
        self.assertTrue(should_ban)
        self.assertEqual(reason, 'flood')
        self.assertEqual(bans, [42])

    def test_reset_clears_history_for_one_user_only(self):
        env, bans, registry = make_env()
        registry[1], registry[2] = UserData(), UserData()
        env['reset_user_state'](1)
        a, b = registry[1], registry[2]
        self.assertFalse(a.url_history or a.command_history or a.message_history
                         or a.message_timestamps or a.activity_hours)
        self.assertTrue(b.url_history and b.message_history and b.activity_hours)
        self.assertTrue(env['_dirty'].is_set())

    def test_reset_is_safe_for_unknown_or_bad_ids(self):
        env, bans, registry = make_env()
        env['reset_user_state'](999)       # never seen
        env['reset_user_state']('abc')     # not numeric
        env['reset_user_state'](None)
        self.assertEqual(registry, {})

    def test_unblock_paths_call_reset(self):
        admin = (ROOT / 'COMMANDS' / 'admin_cmd.py').read_text(encoding='utf-8')
        stats = (ROOT / 'services' / 'stats_service.py').read_text(encoding='utf-8')
        self.assertEqual(admin.count('_reset_antibot_history('), 3)  # def + single + "all"
        self.assertIn('_reset_antibot_state(user_id)', stats)


if __name__ == '__main__':
    unittest.main()
