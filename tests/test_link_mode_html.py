"""Offline tests for the actual LINK-mode branches, without starting the bot."""
import ast
import html
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]


def load_link_branch(filename, name):
    tree = ast.parse((ROOT / 'DOWN_AND_UP' / filename).read_text(encoding='utf-8'))
    func = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    index = next(i for i, n in enumerate(func.body)
                 if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'link_mode_active' for t in n.targets))
    branch = func.body[index:index + 2]
    wrapper = ast.parse('def run(app, message, url, user_id, quality_key, cookies_already_checked):\n    pass\n').body[0]
    wrapper.body = branch + [ast.Return(value=ast.Constant(value='download'))]
    module = ast.fix_missing_locations(ast.Module(body=[wrapper], type_ignores=[]))
    namespace = {'html': html}
    exec(compile(module, filename, 'exec'), namespace)
    return namespace['run'], namespace


class Messages:
    DIRECT_LINK_OBTAINED_MSG = '<b>Link</b>\n'
    TITLE_FIELD_MSG = '<b>Title:</b> {title}\n'
    DURATION_FIELD_MSG = '<b>Duration:</b> {duration}\n'
    FORMAT_FIELD_MSG = '<code>{format_spec}</code>\n'
    VIDEO_STREAM_FIELD_MSG = '<a href="{video_url}">{video_url}</a>\n'
    AUDIO_STREAM_FIELD_MSG = '<a href="{audio_url}">{audio_url}</a>\n'
    ERROR_GETTING_LINK_MSG = '<b>Error:</b> {error}'
    DOWN_UP_ERROR_GETTING_LINK_MSG = '<b>Error:</b> {error_msg}'
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = '{user_id} {url}'
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = '{user_id} {url}'
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = '{user_id} {url} {error}'
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = '{user_id} {url} {error}'


class LinkModeHtmlTests(unittest.TestCase):
    def run_branch(self, filename, function, result, enabled=True, fail_send=False):
        run, ns = load_link_branch(filename, function)
        menu = types.ModuleType('DOWN_AND_UP.always_ask_menu')
        menu.get_link_mode = lambda _: enabled
        link = types.ModuleType('COMMANDS.link_cmd')
        link.get_direct_link = lambda *a, **kw: result
        ns.update(safe_get_messages=lambda _: Messages(), logger=Mock(), send_to_logger=Mock(),
                  sanitize_error_message=lambda text: text,
                  log_error_to_channel=Mock(), ReplyParameters=lambda **kw: kw,
                  enums=types.SimpleNamespace(ParseMode=types.SimpleNamespace(HTML='HTML')))
        app = Mock()
        if fail_send:
            app.send_message.side_effect = RuntimeError('send failed')
        with patch.dict(sys.modules, {'DOWN_AND_UP.always_ask_menu': menu, 'COMMANDS.link_cmd': link}):
            outcome = run(app, types.SimpleNamespace(id=5), 'https://example.com', 1, 'best', False)
        return outcome, app

    def test_success_escapes_html_text_and_attributes(self):
        result = {'success': True, 'title': 'A <B> & "C"', 'duration': 3,
                  'format': 'x < y & z', 'video_url': 'https://example.com/?a=1&b="x"',
                  'audio_url': 'https://example.com/?a=2&b=<y>'}
        for filename, function in [('down_and_up.py', 'down_and_up'), ('down_and_audio.py', 'down_and_audio')]:
            with self.subTest(filename=filename):
                outcome, app = self.run_branch(filename, function, result)
                self.assertIsNone(outcome)
                text = app.send_message.call_args.args[1]
                for key in ('title', 'format', 'video_url', 'audio_url'):
                    self.assertIn(html.escape(result[key], quote=True), text)
                self.assertIn('<b>Title:</b>', text)

    def test_error_is_sanitized_and_escaped(self):
        for filename, function in [('down_and_up.py', 'down_and_up'), ('down_and_audio.py', 'down_and_audio')]:
            with self.subTest(filename=filename):
                outcome, app = self.run_branch(filename, function, {'error': 'bad <tag> & "value"'})
                self.assertIsNone(outcome)
                self.assertIn('bad &lt;tag&gt; &amp; &quot;value&quot;', app.send_message.call_args.args[1])

    def test_error_masks_proxy_credentials(self):
        sanitized = []
        def fake_sanitize(text):
            sanitized.append(text)
            return 'https://***@proxy/'
        for filename, function in [('down_and_up.py', 'down_and_up'), ('down_and_audio.py', 'down_and_audio')]:
            with self.subTest(filename=filename):
                run, ns = load_link_branch(filename, function)
                menu = types.ModuleType('DOWN_AND_UP.always_ask_menu')
                menu.get_link_mode = lambda _: True
                link = types.ModuleType('COMMANDS.link_cmd')
                link.get_direct_link = lambda *a, **kw: {'error': 'https://user:pass@proxy/ failed'}
                ns.update(safe_get_messages=lambda _: Messages(), logger=Mock(), send_to_logger=Mock(),
                          sanitize_error_message=fake_sanitize,
                          ReplyParameters=lambda **kw: kw,
                          enums=types.SimpleNamespace(ParseMode=types.SimpleNamespace(HTML='HTML')))
                app = Mock()
                with patch.dict(sys.modules, {'DOWN_AND_UP.always_ask_menu': menu, 'COMMANDS.link_cmd': link}):
                    run(app, types.SimpleNamespace(id=5), 'https://example.com', 1, 'best', False)
                self.assertIn('https://user:pass@proxy/ failed', sanitized)
                self.assertNotIn('user:pass', app.send_message.call_args.args[1])

    def test_send_failure_does_not_start_download(self):
        for filename, function in [('down_and_up.py', 'down_and_up'), ('down_and_audio.py', 'down_and_audio')]:
            with self.subTest(filename=filename):
                outcome, _ = self.run_branch(filename, function, {'error': 'failed'}, fail_send=True)
                self.assertIsNone(outcome)

    def test_disabled_mode_continues_download(self):
        for filename, function in [('down_and_up.py', 'down_and_up'), ('down_and_audio.py', 'down_and_audio')]:
            with self.subTest(filename=filename):
                outcome, app = self.run_branch(filename, function, {}, enabled=False)
                self.assertEqual(outcome, 'download')
                app.send_message.assert_not_called()


if __name__ == '__main__':
    unittest.main()
