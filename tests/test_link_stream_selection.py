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

    def test_absent_streams(self):
        self.assertEqual(selected({}), (None, None))


if __name__ == '__main__':
    unittest.main()
