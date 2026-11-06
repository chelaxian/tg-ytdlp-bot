"""The per-user download slot must really be taken and always released.

Before: set_active_download(user_id, True) was never called, so the counter stayed 0 and
MAX_CONCURRENT_DOWNLOADS ("playlist/multi-URL: only 1") was never enforced.
"""
import ast
import threading
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_status_functions(limit=3):
    src = ROOT / 'HELPERS' / 'download_status.py'
    tree = ast.parse(src.read_text(encoding='utf-8'))
    names = {'get_active_download', 'can_start_download', 'set_active_download'}
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {f.name for f in funcs} == names
    env = {'active_downloads': {}, 'active_downloads_lock': threading.Lock(),
           'LimitsConfig': types.SimpleNamespace(MAX_CONCURRENT_DOWNLOADS=limit)}
    exec(compile(ast.Module(body=funcs, type_ignores=[]), str(src), 'exec'), env)
    return env


def is_slot_call(stmt, flag):
    return (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call)
            and getattr(stmt.value.func, 'id', None) == 'set_active_download'
            and [getattr(a, 'id', None) or getattr(a, 'value', None) for a in stmt.value.args]
            == ['user_id', flag])


class SlotBehaviour(unittest.TestCase):
    def test_single_url_limit_and_release(self):
        env = load_status_functions(limit=3)
        can, take = env['can_start_download'], env['set_active_download']
        for _ in range(3):
            self.assertTrue(can(1))
            take(1, True)
        self.assertFalse(can(1))          # 4th single URL is refused
        self.assertTrue(can(2))           # other users are independent
        take(1, False)
        self.assertTrue(can(1))

    def test_playlist_and_multi_url_need_an_idle_user(self):
        env = load_status_functions()
        can, take = env['can_start_download'], env['set_active_download']
        self.assertTrue(can(1, is_playlist=True))
        take(1, True)
        self.assertFalse(can(1, is_playlist=True))
        self.assertFalse(can(1, is_multi_url=True))
        take(1, False)
        self.assertTrue(can(1, is_multi_url=True))

    def test_release_without_take_never_goes_negative(self):
        env = load_status_functions()
        env['set_active_download'](5, False)
        self.assertEqual(env['get_active_download'](5), 0)


class SlotIsPairedInDownloaders(unittest.TestCase):
    def check_function(self, filename, funcname):
        tree = ast.parse((ROOT / 'DOWN_AND_UP' / filename).read_text(encoding='utf-8'))
        fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == funcname)
        body = fn.body
        tries = [i for i, n in enumerate(body) if isinstance(n, ast.Try) and n.finalbody]
        self.assertTrue(tries, 'no top-level try/finally')
        i = tries[-1]
        # taken immediately before the try, released first thing in its finally
        self.assertTrue(is_slot_call(body[i - 1], True), f'{funcname}: slot not taken right before try')
        self.assertTrue(is_slot_call(body[i].finalbody[0], False), f'{funcname}: slot not released first in finally')
        # and released exactly once
        releases = [n for n in ast.walk(fn) if isinstance(n, ast.Expr) and is_slot_call(n, False)]
        takes = [n for n in ast.walk(fn) if isinstance(n, ast.Expr) and is_slot_call(n, True)]
        self.assertEqual((len(takes), len(releases)), (1, 1))

    def test_down_and_up(self):
        self.check_function('down_and_up.py', 'down_and_up')

    def test_down_and_audio(self):
        self.check_function('down_and_audio.py', 'down_and_audio')


if __name__ == '__main__':
    unittest.main()
