"""Regression: a busy download slot must not be ignored after waiting."""
import ast
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / 'URL_PARSERS' / 'video_extractor.py'
tree = ast.parse(path.read_text(encoding='utf-8'))
fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'process_multiple_urls_queue')


class MultiUrlWaitTest(unittest.TestCase):
    def test_timeout_stops_before_starting_download(self):
        sent = []
        clock = iter([0, 301])
        m = types.SimpleNamespace(chat=types.SimpleNamespace(id=123), id=5)
        messages = types.SimpleNamespace(TOTAL_PROGRESS_MSG='progress', URL_PROGRESS_MSG='{current}/{total}', AUDIO_WAIT_MSG='busy')
        safe = types.ModuleType('HELPERS.safe_messeger')
        safe.safe_send_message = lambda uid, text, **kw: sent.append(text)
        safe.safe_edit_message_text = lambda *a, **kw: None
        pyro = types.ModuleType('pyrogram.types')
        pyro.ReplyParameters = lambda **kw: kw
        limits = types.ModuleType('CONFIG.limits')
        limits.LimitsConfig = types.SimpleNamespace(MAX_MULTI_URL_LIMIT=10, GROUP_COUNT_MULTIPLIER=10)
        limitter = types.ModuleType('HELPERS.limitter')
        limitter.should_apply_limits_to_admin = lambda **kw: True
        env = {'safe_get_messages': lambda _: messages,
               'extract_url_range_tags': lambda _: ('https://example.com/v', 1, 1, None, [], '', None),
               'has_range_syntax': lambda _: False,
               'Config': types.SimpleNamespace(BLACK_LIST=[]),
               'check_playlist_range_limits': lambda *a: True,
               'can_start_download': lambda _: False,
               'time': types.SimpleNamespace(time=lambda: next(clock), sleep=lambda _: None),
               'logger': types.SimpleNamespace(warning=lambda *a: None, error=lambda *a: self.fail(str(a)))}
        exec(compile(ast.Module(body=[fn], type_ignores=[]), str(path), 'exec'), env)
        modules = {'HELPERS.safe_messeger': safe, 'pyrogram.types': pyro,
                   'CONFIG.limits': limits, 'HELPERS.limitter': limitter}
        with patch.dict(sys.modules, modules):
            env['process_multiple_urls_queue'](None, m, ['https://example.com/v'], None, False, False)
        self.assertEqual(sent[-1], 'busy')
        self.assertEqual(len(sent), 2)


if __name__ == '__main__':
    unittest.main()
