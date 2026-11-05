"""Offline regression tests for the selected yt-dlp stream URLs."""
import ast
from pathlib import Path
import unittest

# Avoid importing the running bot and its Telegram client in offline tests.
source = (Path(__file__).resolve().parents[1] / 'COMMANDS' / 'link_cmd.py').read_text(encoding='utf-8')
tree = ast.parse(source)
function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_selected_stream_urls')
namespace = {}
exec(compile(ast.Module(body=[function], type_ignores=[]), '<stream-selection>', 'exec'), namespace)
selected = namespace['_selected_stream_urls']


class SelectedStreamTests(unittest.TestCase):
    def test_selected_single_video_does_not_choose_another_format(self):
        self.assertEqual(selected({'url': 'selected', 'vcodec': 'h264', 'acodec': 'aac',
                                   'formats': [{'url': 'other', 'height': 1080}]}), ('selected', None))

    def test_audio_only(self):
        self.assertEqual(selected({'url': 'audio', 'vcodec': 'none', 'acodec': 'aac'}), (None, 'audio'))

    def test_separate_streams(self):
        info = {'requested_formats': [{'url': 'video', 'vcodec': 'h264', 'acodec': 'none'},
                                      {'url': 'audio', 'vcodec': 'none', 'acodec': 'aac'}]}
        self.assertEqual(selected(info), ('video', 'audio'))

    def test_combined_requested_format(self):
        self.assertEqual(selected({'requested_formats': [{'url': 'both', 'vcodec': 'h264', 'acodec': 'aac'}]}), ('both', None))

    def test_video_with_unknown_codec(self):
        info = {'requested_formats': [{'url': 'video'},
                                      {'url': 'audio', 'vcodec': 'none', 'acodec': 'aac'}]}
        self.assertEqual(selected(info), ('video', 'audio'))

    def test_absent_streams(self):
        self.assertEqual(selected({}), (None, None))

class ExtractionRouteTests(unittest.TestCase):
    def setUp(self):
        from unittest.mock import Mock
        outer = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'get_direct_link')
        function = next(n for n in ast.walk(outer) if isinstance(n, ast.FunctionDef) and n.name == 'extract_with_fallback')
        self.operation = Mock()
        self.fallback = Mock()
        ns = {'extract_info_operation': self.operation, 'try_with_proxy_fallback': self.fallback,
              'url': 'https://example.test/video', 'user_id': 1, 'logger': Mock(),
              'has_alternative_proxy_route': Mock(return_value=True)}
        self.has_route = ns['has_alternative_proxy_route']
        exec(compile(ast.Module(body=[function], type_ignores=[]), '<extraction-route>', 'exec'), ns)
        self.extract = ns['extract_with_fallback']

    def test_initial_route_runs_before_fallback(self):
        self.operation.return_value = {'id': 'ok'}
        self.assertEqual(self.extract({'format': 'best'}), {'id': 'ok'})
        self.fallback.assert_not_called()

    def test_fallback_after_failure(self):
        self.operation.side_effect = ValueError('failed')
        self.fallback.return_value = {'id': 'fallback'}
        self.assertEqual(self.extract({}), {'id': 'fallback'})

    def test_no_alternative_route_does_not_repeat(self):
        self.has_route.return_value = False
        self.operation.side_effect = ValueError('initial')
        with self.assertRaisesRegex(ValueError, 'initial'):
            self.extract({})
        self.operation.assert_called_once()
        self.fallback.assert_not_called()

    def test_none_triggers_alternative_route(self):
        self.operation.return_value = None
        self.fallback.return_value = {'id': 'fallback'}
        self.assertEqual(self.extract({}), {'id': 'fallback'})

    def test_preserves_initial_error_when_fallback_empty(self):
        self.operation.side_effect = ValueError('initial')
        self.fallback.return_value = None
        with self.assertRaisesRegex(ValueError, 'initial'):
            self.extract({})


if __name__ == '__main__':
    unittest.main()
