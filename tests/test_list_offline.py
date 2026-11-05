"""Offline regression tests for /list without importing the running bot."""
import ast
import html
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / 'COMMANDS' / 'list_cmd.py').read_text(encoding='utf-8')
TREE = ast.parse(SOURCE)


def load_functions(names, namespace):
    nodes = [n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in names]
    for node in nodes:
        node.decorator_list = []
    exec(compile(ast.Module(body=nodes, type_ignores=[]), '<list>', 'exec'), namespace)
    return namespace


class ListTests(unittest.TestCase):
    def setUp(self):
        self.ns = load_functions({'_list_format_ids', '_list_caption', '_format_filesize_list', 'run_ytdlp_list'},
                                 {'escape': html.escape, 'logger': Mock()})

    def test_string_ids_and_resolution(self):
        formats = [dict(format_id='hls-720', vcodec='avc', acodec='none', resolution='1280x720'),
                   dict(format_id='audio-en', vcodec='none', acodec='aac'),
                   dict(format_id='both', vcodec='avc', acodec='aac')]
        self.assertEqual(self.ns['_list_format_ids'](formats), (['audio-en'], ['hls-720']))
        module = types.ModuleType('DOWN_AND_UP.yt_dlp_hook')
        module.get_video_formats = lambda *a: {'formats': formats}
        with patch.dict(sys.modules, {'DOWN_AND_UP.yt_dlp_hook': module}):
            ok, output, raw = self.ns['run_ytdlp_list']('https://x', 1, include_formats=True)
            self.assertEqual(len(self.ns['run_ytdlp_list']('https://x', 1)), 2)
        self.assertTrue(ok)
        self.assertIn('1280x720 (video only)', output)
        self.assertIs(raw, formats)

    def test_caption_bounds_and_escaping(self):
        caption = self.ns['_list_caption']('<&' + '😀' * 2000, '😀' * 2000)
        self.assertIn('&lt;&amp;', caption)
        self.assertLess(len(html.unescape(caption).encode('utf-16-le')) // 2, 1024)

    def test_command_cleans_processing_after_send_failure(self):
        import os
        messages = types.SimpleNamespace(**{name: '' for name in (
            'LIST_PROCESSING_MSG LIST_AVAILABLE_FORMATS_HEADER_MSG LIST_HOW_TO_USE_FORMAT_IDS_TITLE '
            'LIST_FORMAT_USAGE_INSTRUCTIONS LIST_FORMAT_EXAMPLE_401 LIST_FORMAT_EXAMPLE_401_SHORT '
            'LIST_FORMAT_EXAMPLE_140_AUDIO LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT LIST_USE_FORMAT_ID_MSG '
            'LIST_FORMATS_FILE_NAME_MSG LIST_ERROR_SENDING_MSG LIST_ERROR_OCCURRED_MSG').split()})
        process = Mock()
        app = Mock()
        app.send_document.side_effect = RuntimeError('send failed')
        msg = types.SimpleNamespace(chat=types.SimpleNamespace(id=1), text='/list https://example.org/a', id=4)
        self.ns.update(os=os, tempfile=tempfile, Config=types.SimpleNamespace(ADMIN=[1]),
                       safe_get_messages=lambda _: messages, safe_send_message=lambda *a, **kw: process,
                       send_error_to_user=Mock(), run_ytdlp_list=lambda *a, **kw: (True, 'table', []))
        load_functions({'list_command'}, self.ns)
        self.ns['list_command'](app, msg)
        process.delete.assert_called_once()
        self.ns['send_error_to_user'].assert_called_once()
        self.assertFalse(os.path.exists(app.send_document.call_args.kwargs['document']))

    def test_menu_routes_list_to_originating_chat(self):
        tree = ast.parse((ROOT / 'DOWN_AND_UP' / 'always_ask_menu.py').read_text(encoding='utf-8'))
        callback = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'askq_callback')
        branch = next(n for n in callback.body if isinstance(n, ast.If) and isinstance(n.test, ast.Compare)
                      and isinstance(n.test.left, ast.Name) and n.test.left.id == 'data'
                      and any(isinstance(c, ast.Constant) and c.value == 'list' for c in n.test.comparators))
        calls = [n for n in ast.walk(branch) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                 and n.func.attr in ('send_document', 'send_message')]
        self.assertEqual(len(calls), 3)
        destinations = [ast.unparse(call.args[0]) for call in calls]
        self.assertCountEqual(destinations, ['chat_id', 'chat_id', 'callback_query.message.chat.id'])


class SanitizedSendErrorTests(unittest.TestCase):
    def test_caption_limits_and_escape(self):
        ns = load_functions({'_list_caption'}, {'escape': html.escape})
        caption = ns['_list_caption']('https://examp' + 'le.com/' + 'x'*300 + '&<>"', 'use IDs')
        self.assertLessEqual(len(caption), 1024)
        self.assertNotIn('&<"', caption)

    def test_send_error_text_is_sanitized_in_menu(self):
        # the LIST callback in always_ask_menu.py must wrap str(e) with
        # sanitize_error_message + escape before sending it to the chat
        source = (ROOT / 'DOWN_AND_UP' / 'always_ask_menu.py').read_text(encoding='utf-8')
        idx = source.index('ALWAYS_ASK_ERROR_SENDING_FORMATS_FILE_LOG_MSG}: {e}")')
        snippet = source[idx:idx+700]
        self.assertIn('_sanitize_error(str(e))', snippet)
        self.assertIn('_escape(', snippet)


if __name__ == '__main__':
    unittest.main()