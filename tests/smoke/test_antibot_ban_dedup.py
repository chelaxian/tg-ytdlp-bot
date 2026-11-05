"""Test anti-bot ban submission without connecting to Telegram or a database."""
import ast
from pathlib import Path
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / 'HELPERS' / 'anti_bot_protection.py'
tree = ast.parse(path.read_text(encoding='utf-8'))
fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == '_submit_ban_task')


class FakePool:
    def __init__(self):
        self.jobs = []
        self.lock = threading.Lock()
        self.fail = False

    def submit(self, fn):
        with self.lock:
            if self.fail:
                raise RuntimeError('executor unavailable')
            self.jobs.append(fn)


class BanDedupTest(unittest.TestCase):
    def setUp(self):
        self.pool = FakePool()
        self.namespace = {'_ban_pool': self.pool, '_pending_bans': set(),
                          '_pending_bans_lock': threading.Lock()}
        exec(compile(ast.Module(body=[fn], type_ignores=[]), str(path), 'exec'), self.namespace)
        self.submit = self.namespace['_submit_ban_task']

    def test_concurrent_duplicates_and_separate_users(self):
        called = []
        with ThreadPoolExecutor(max_workers=20) as workers:
            list(workers.map(lambda _: self.submit(1, lambda: called.append(1)), range(200)))
        self.submit(2, lambda: called.append(2))
        self.assertEqual(len(self.pool.jobs), 2)
        for job in list(self.pool.jobs):
            job()
        self.assertCountEqual(called, [1, 2])
        self.submit(1, lambda: None)
        self.assertEqual(len(self.pool.jobs), 3)

    def test_failed_submission_and_task_release_the_key(self):
        self.pool.fail = True
        with self.assertRaises(RuntimeError):
            self.submit(1, lambda: None)
        self.assertNotIn(1, self.namespace['_pending_bans'])
        self.pool.fail = False
        def fail():
            raise ValueError('failure')
        self.submit(1, fail)
        with self.assertRaises(ValueError):
            self.pool.jobs[-1]()
        self.assertNotIn(1, self.namespace['_pending_bans'])
        self.submit(1, lambda: None)
        self.assertEqual(len(self.pool.jobs), 2)


if __name__ == '__main__':
    unittest.main()
