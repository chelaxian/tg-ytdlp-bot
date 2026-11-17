"""Run with: python3 -m unittest test_command_reverse_ranges"""
import logging
import sys
import types
import ast
import pathlib
import re
import unittest
from unittest.mock import patch

try:
    import HELPERS.logger  # noqa: F401
except Exception:
    module = types.ModuleType('HELPERS.logger')
    module.logger = logging.getLogger(__name__)
    sys.modules['HELPERS.logger'] = module

from URL_PARSERS import playlist_utils as pu

URL = 'https://www.youtube.com/playlist?list=PLtest'


class CommandReverseRangeTests(unittest.TestCase):
    def test_reverse_command_selects_absolute_positions_on_120_item_playlist(self):
        for command in ('-100-1', '-100--1'):
            with self.subTest(command=command):
                text = pu.command_args_to_range_text([command, URL, '#music'], 100)
                self.assertEqual(text, URL + '*100*1 #music')
                start, end = map(int, text.split()[0].split('*')[1:])
                self.assertEqual(pu.playlist_indices_for_range(start, end, URL, 1), list(range(100, 0, -1)))

    def test_all_negative_command_forms_are_absolute_descending(self):
        for spec, expected in [('-10-3', '10*3'), ('-3--10', '10*3'), ('-10-', '10*1'), ('-100-', '100*51')]:
            with self.subTest(spec=spec):
                self.assertEqual(pu.command_args_to_range_text([spec, URL], 50), URL + '*' + expected)

    def test_reverse_video_does_not_stop_after_five_missing_items(self):
        path = pathlib.Path(__file__).resolve().parent / 'DOWN_AND_UP/down_and_up.py'
        tree = ast.parse(path.read_text(encoding='utf-8'))
        threshold = next(n for n in ast.walk(tree) if isinstance(n, ast.If)
                         and 'consecutive_no_videos_skips >= MAX_CONSECUTIVE_NO_VIDEOS_SKIPS' in ast.unparse(n.test))
        condition = compile(ast.Expression(threshold.test), str(path), 'eval')
        self.assertFalse(eval(condition, dict(consecutive_no_videos_skips=5,
                                              MAX_CONSECUTIVE_NO_VIDEOS_SKIPS=5,
                                              is_reverse_order=True)))
        self.assertTrue(eval(condition, dict(consecutive_no_videos_skips=5,
                                             MAX_CONSECUTIVE_NO_VIDEOS_SKIPS=5,
                                             is_reverse_order=False)))

    def test_audio_handler_passes_normalized_text_to_downloader(self):
        path = pathlib.Path(__file__).resolve().parent / 'COMMANDS/other_handlers.py'
        tree = ast.parse(path.read_text(encoding='utf-8'))
        node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'audio_command_handler')
        node.decorator_list = []
        # Exercise actual handler with external services replaced by small stubs.
        config = types.ModuleType('HELPERS.limitter')
        config.range_limit_for_url = lambda url: (100, '', False, False)
        parsed = []
        def extract(text):
            m = re.search(r'\*(-?\d+)\*(-?\d+)', text)
            return URL, *(map(int, m.groups()) if m else (1, 1)), None, [], '', None
        def download(app, message, url, tags, **kwargs):
            parsed.append((message.text, kwargs['video_start_with'], kwargs['video_count']))
        env = dict(Config=types.SimpleNamespace(ADMIN=[]), _check_access=lambda m: True,
                   can_start_download=lambda uid: True, os=__import__('os'), create_directory=lambda p: None,
                   extract_url_range_tags=extract, save_user_tags=lambda *a: None,
                   check_playlist_range_limits=lambda *a: True, down_and_audio=download)
        exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), env)
        for command in ('-100-1', '-100--1'):
            message = types.SimpleNamespace(chat=types.SimpleNamespace(id=123), text=f'/audio {command} {URL}', caption=None)
            with patch.dict(sys.modules, {'HELPERS.limitter': config}):
                env['audio_command_handler'](None, message)
            self.assertEqual(parsed.pop(), (f'/audio {URL}*100*1', 100, 100))

    def test_partial_reverse_cache_is_not_replayed_before_downloads(self):
        root = pathlib.Path(__file__).resolve().parent
        for file in ('DOWN_AND_UP/down_and_up.py', 'DOWN_AND_UP/down_and_audio.py'):
            tree = ast.parse((root / file).read_text(encoding='utf-8'))
            guards = [n for n in ast.walk(tree) if isinstance(n, ast.If)
                      and ast.unparse(n.test) == 'is_reverse_order'
                      and 'cached_videos = {}' in ast.unparse(n)]
            self.assertEqual(len(guards), 1, file)
            # even a fully cached (stale) descending range bypasses the cache
            for uncached in ([99], []):
                with self.subTest(file=file, uncached=uncached):
                    env = {'is_reverse_order': True, 'uncached_indices': list(uncached),
                           'cached_videos': {100: 42, 98: 43}, 'requested_indices': list(range(100, 0, -1))}
                    exec(compile(ast.Module(body=guards, type_ignores=[]), file, 'exec'), env)
                    self.assertEqual(env['cached_videos'], {})
                    self.assertEqual(env['uncached_indices'], list(range(100, 0, -1)))
            # forward ranges keep the cache
            env = {'is_reverse_order': False, 'uncached_indices': [3],
                   'cached_videos': {1: 42, 2: 43}, 'requested_indices': [1, 2, 3]}
            exec(compile(ast.Module(body=guards, type_ignores=[]), file, 'exec'), env)
            self.assertEqual(env['cached_videos'], {1: 42, 2: 43})
            self.assertEqual(env['uncached_indices'], [3])

    def test_quality_menu_callback_bypasses_cache_for_descending_range(self):
        root = pathlib.Path(__file__).resolve().parent
        tree = ast.parse((root / 'DOWN_AND_UP/always_ask_menu.py').read_text(encoding='utf-8'))
        guards = [n for n in ast.walk(tree) if isinstance(n, ast.If)
                  and ast.unparse(n.test) == 'len(requested_indices) > 1 and requested_indices[0] > requested_indices[-1]'
                  and 'cached_videos = {}' in ast.unparse(n)]
        self.assertEqual(len(guards), 1)
        # a stale FULL cache of a descending range is bypassed too (old guard
        # required uncached_indices and let a full cache replay out of order)
        env = {'requested_indices': [10, 9, 8], 'cached_videos': {10: 1, 9: 2, 8: 3},
               'uncached_indices': []}
        exec(compile(ast.Module(body=guards, type_ignores=[]), 'aam', 'exec'), env)
        self.assertEqual(env['cached_videos'], {})
        self.assertEqual(env['uncached_indices'], [10, 9, 8])
        # forward ranges keep the cache
        env = {'requested_indices': [8, 9, 10], 'cached_videos': {8: 1},
               'uncached_indices': [9, 10]}
        exec(compile(ast.Module(body=guards, type_ignores=[]), 'aam', 'exec'), env)
        self.assertEqual(env['cached_videos'], {8: 1})
        self.assertEqual(env['uncached_indices'], [9, 10])

    def test_quality_menu_recovers_reverse_range_from_command_message(self):
        # reply_to_message.text still carries the raw '/vid -10-3 URL' form: the
        # menu callback must rebuild the normalized 'URL*N*M' range from it.
        root = pathlib.Path(__file__).resolve().parent
        tree = ast.parse((root / 'DOWN_AND_UP/always_ask_menu.py').read_text(encoding='utf-8'))
        node = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                    and n.name == '_recover_command_range_text')
        limitter = types.ModuleType('HELPERS.limitter')
        limitter.range_limit_for_url = lambda url: (100, '', False, False)
        env = {}
        exec(compile(ast.Module(body=[node], type_ignores=[]), 'aam', 'exec'), env)
        recover = env['_recover_command_range_text']
        with patch.dict(sys.modules, {'HELPERS.limitter': limitter}):
            self.assertEqual(recover(f'/vid -10-3 {URL}'), f'{URL}*10*3')
            self.assertEqual(recover(f'/audio -100--1 {URL} #music'), f'{URL}*100*1 #music')
            self.assertEqual(recover(f'/vid @bot -10-3 {URL}'), f'{URL}*10*3')
            self.assertEqual(recover('/vid -10-3'), '/vid -10-3')      # no URL: unchanged
            self.assertEqual(recover(''), '')
        # non-command text passes through untouched (already normalized or plain)
        self.assertEqual(recover(f'{URL}*10*3'), f'{URL}*10*3')
        self.assertEqual(recover(f'{URL}-3*-10'), f'{URL}-3*-10')

    def test_quality_menu_playlist_branch_normalizes_message_text(self):
        # The downloader re-parses message.text for the range end/direction: the
        # menu callback must rewrite it with the recovered URL*N*M form before
        # calling down_and_up/down_and_audio (3 branches: generic, manual, other_id).
        root = pathlib.Path(__file__).resolve().parent
        tree = ast.parse((root / 'DOWN_AND_UP/always_ask_menu.py').read_text(encoding='utf-8'))
        mutations = [n for n in ast.walk(tree) if isinstance(n, ast.Try)
                     if 'original_message.text = original_text' in ast.unparse(n)]
        self.assertEqual(len(mutations), 3)

    def test_audio_short_playlist_skips_empty_positions(self):
        # /audio -100-1 on a playlist shorter than 100: yt-dlp answers missing
        # positions with empty entries; the loop must SKIP them (like the video
        # loop's NO_VIDEOS_SKIP), not raise and abort the whole playlist.
        root = pathlib.Path(__file__).resolve().parent
        tree = ast.parse((root / 'DOWN_AND_UP/down_and_audio.py').read_text(encoding='utf-8'))
        sites = [n for n in ast.walk(tree) if isinstance(n, ast.If)
                 and 'actual_index < len(entries)' in ast.unparse(n.test)
                 and 'entries[actual_index] is not None' in ast.unparse(n.test)]
        self.assertEqual(len(sites), 2)  # metadata pass + safe-filename retry
        class _Msgs:
            DOWN_UP_NO_CONTENT_FOUND_MSG = 'no content at {index}'
        class _Log:
            def info(self, *a, **k): pass
        notified = []
        for node in sites:
            for entries, index, expect in (
                ([{'id': 'a'}, None, {'id': 'c'}], 3, {'id': 'c'}),  # existing -> picked
                ([{'id': 'a'}, None, None], 3, 'SKIP'),              # empty slot -> skip
                ([{'id': 'a'}, {'id': 'b'}], 100, 'SKIP'),           # past the end -> skip
            ):
                with self.subTest(site=ast.unparse(node.test)[:40], index=index):
                    env = dict(info_dict={'entries': list(entries)},
                               entries=list(entries),  # assigned by the parent block in production
                               current_index=index, playlist_item_index=index,
                               actual_index=index - 1,  # set by the parent block in production
                               current_playlist_items_override=None,
                               logger=_Log(), user_id=1, message=object(),
                               original_playlist_index=index,
                               safe_get_messages=lambda uid: _Msgs(),
                               send_error_to_user=lambda msg, text, **k: notified.append(text))
                    fn = ast.FunctionDef(
                        name='run',
                        args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[],
                                           kw_defaults=[], defaults=[]),
                        body=[node, ast.Return(value=ast.Name(id='info_dict', ctx=ast.Load()))],
                        decorator_list=[])
                    exec(compile(ast.fix_missing_locations(ast.Module(body=[fn], type_ignores=[])),
                                 'site', 'exec'), env)
                    self.assertEqual(env['run'](), expect)
        self.assertEqual(len(notified), 4)  # a user notice for every skipped slot

    def test_positive_and_raw_negative_ranges_remain_unchanged(self):
        self.assertEqual(pu.command_args_to_range_text(['3-7', URL], 100), URL + '*3*7')
        self.assertEqual(pu.command_args_to_range_text(['7-3', URL], 100), URL + '*7*3')
        self.assertEqual(pu.resolve_negative_indices(pu.range_indices(-1, -3), 120), [120, 119, 118])


if __name__ == '__main__':
    unittest.main()
