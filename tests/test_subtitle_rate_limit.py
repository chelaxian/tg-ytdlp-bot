"""Проверки защиты от повторов HTTP 429 без Telegram/YouTube."""
import ast
import logging
from pathlib import Path
import unittest
from unittest.mock import patch

from HELPERS import subtitle_rate_limit as rate


class SubtitleRateLimitTests(unittest.TestCase):
    def setUp(self):
        rate._blocked.clear()

    def tearDown(self):
        rate._blocked.clear()

    def test_user_url_isolation_and_expiration(self):
        with patch.object(rate.time, 'monotonic', return_value=100):
            rate.block_subtitles('video', 1)
            self.assertTrue(rate.subtitles_rate_limited('video', 1))
            self.assertTrue(rate.subtitles_rate_limited('video', '1'))
            self.assertFalse(rate.subtitles_rate_limited('video', 2))
            self.assertFalse(rate.subtitles_rate_limited('other', 1))
        with patch.object(rate.time, 'monotonic', return_value=3701):
            self.assertFalse(rate.subtitles_rate_limited('video', 1))

    def test_blocked_paths_do_not_start_extraction(self):
        # Берём реальные функции через AST, не импортируя весь бот.
        path = Path(__file__).resolve().parents[1] / 'COMMANDS/subtitles_cmd.py'
        tree = ast.parse(path.read_text(encoding='utf-8-sig'))
        names = {'download_subtitles_ytdlp', 'get_available_subs_languages'}
        nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
        namespace = {
            'subtitles_rate_limited': rate.subtitles_rate_limited,
            'logger': logging.getLogger(__name__),
        }
        exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), namespace)
        rate.block_subtitles('video', 1)
        self.assertIsNone(namespace['download_subtitles_ytdlp']('video', 1, '/unused', ['es']))
        self.assertEqual(namespace['get_available_subs_languages']('video', 1), [])

    def test_memory_is_bounded(self):
        with patch.object(rate, '_MAX_ENTRIES', 3):
            for i in range(10):
                rate.block_subtitles(str(i), 1)
            self.assertEqual(len(rate._blocked), 3)


if __name__ == '__main__':
    unittest.main()
