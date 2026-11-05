"""Isolated tests for /mediainfo; no Telegram, configuration or network required.

Run: python tests/smoke/test_t_mediainfo.py
"""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import types
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]


class Filter:
    def __and__(self, other):
        return self


class App:
    def on_message(self, *args, **kwargs):
        return lambda fn: fn

    on_callback_query = on_message


app = App()


def module(name, **values):
    result = types.ModuleType(name)
    result.__dict__.update(values)
    return result


class FlexibleString(str):
    def format(self, *args, **kwargs):
        return self


class FlexibleMessages:
    def __getattr__(self, name):
        return FlexibleString(name)


def identity_decorator(**kwargs):
    return lambda fn: fn


def create_directory(path):
    os.makedirs(path, exist_ok=True)


modules = {
    'pyrogram': module('pyrogram', filters=types.SimpleNamespace(command=lambda *a: Filter(), regex=lambda *a: Filter(), private=Filter())),
    'pyrogram.types': module('pyrogram.types', InlineKeyboardMarkup=lambda x: x, InlineKeyboardButton=lambda *a, **kw: (a, kw), ReplyParameters=lambda **kw: types.SimpleNamespace(**kw)),
    'CONFIG.config': module('CONFIG.config', Config=types.SimpleNamespace(ADMIN=[], ALLOWED_GROUP=[-100], IGNORE_USER_COMMAND='/ignore', UNIGNORE_USER_COMMAND='/unignore')),
    'CONFIG.messages': module('CONFIG.messages', safe_get_messages=lambda uid: FlexibleMessages()),
    'HELPERS.app_instance': module('HELPERS.app_instance', get_app=lambda: app),
    'HELPERS.filesystem_hlp': module('HELPERS.filesystem_hlp', create_directory=create_directory),
    'HELPERS.logger': module('HELPERS.logger', send_to_logger=mock.Mock(), logger=mock.Mock(), send_to_all=mock.Mock(), send_error_to_user=mock.Mock()),
    'HELPERS.safe_messeger': module('HELPERS.safe_messeger', safe_send_message=mock.Mock(), safe_edit_message_text=mock.Mock(), safe_callback_answer=mock.Mock()),
    'HELPERS.decorators': module('HELPERS.decorators', background_handler=identity_decorator, light_only=None),
    'HELPERS.limitter': module('HELPERS.limitter', is_user_in_channel=lambda *args: True),
    'DATABASE.firebase_init': module('DATABASE.firebase_init', is_user_ignored=lambda m: False, is_user_blocked=lambda m: False),
}

with mock.patch.dict(sys.modules, modules):
    spec = importlib.util.spec_from_file_location('mediainfo_under_test', ROOT / 'COMMANDS' / 'mediainfo_cmd.py')
    target = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(target)


class MediaInfoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.old_cwd = os.getcwd()
        os.chdir(self.temp.name)
        target.send_error_to_user.reset_mock()
        self.message = types.SimpleNamespace(id=42, text='/mediainfo on', chat=types.SimpleNamespace(id=7))

    def tearDown(self):
        os.chdir(self.old_cwd)
        self.temp.cleanup()

    def enable(self, user_id=7):
        path = Path('users') / str(user_id)
        path.mkdir(parents=True, exist_ok=True)
        (path / 'mediainfo.txt').write_text('ON', encoding='utf-8')

    def test_private_commands_and_disabled_default(self):
        self.assertFalse(target.is_mediainfo_enabled(7))
        with mock.patch.dict(sys.modules, modules):
            target.mediainfo_command(app, self.message)
            self.assertTrue(target.is_mediainfo_enabled(7))
            self.message.text = '/mediainfo off'
            target.mediainfo_command(app, self.message)
        self.assertFalse(target.is_mediainfo_enabled(7))

    def test_group_command_uses_group_storage(self):
        self.message.chat.id = -100
        with mock.patch.dict(sys.modules, modules):
            target.mediainfo_command(app, self.message)
        self.assertTrue(target.is_mediainfo_enabled(-100))
        self.assertFalse(target.is_mediainfo_enabled(7))

    def test_group_callback_uses_chat_not_clicker(self):
        callback = types.SimpleNamespace(from_user=types.SimpleNamespace(id=7), message=types.SimpleNamespace(id=2, chat=types.SimpleNamespace(id=-100)), data='mediainfo_option|on')
        target.mediainfo_option_callback(app, callback)
        self.assertTrue(target.is_mediainfo_enabled(-100))
        self.assertFalse(target.is_mediainfo_enabled(7))
        callback.data = 'mediainfo_option|off'
        target.mediainfo_option_callback(app, callback)
        self.assertFalse(target.is_mediainfo_enabled(-100))

    def test_removed_group_cannot_change_setting(self):
        callback = types.SimpleNamespace(from_user=types.SimpleNamespace(id=7), message=types.SimpleNamespace(id=2, chat=types.SimpleNamespace(id=-200)), data='mediainfo_option|on')
        target.mediainfo_option_callback(app, callback)
        self.assertFalse(Path('users/-200/mediainfo.txt').exists())

    def test_parallel_reports_use_separate_files(self):
        self.enable()
        barrier = threading.Barrier(2)
        paths = []
        errors = []

        def send(chat_id, path, **kwargs):
            paths.append(path)
            try:
                barrier.wait(timeout=5)
                if not Path(path).exists():
                    errors.append('report disappeared before upload')
            except Exception as exc:
                errors.append(str(exc))

        with mock.patch.object(target, 'get_mediainfo_cli', return_value='info'), mock.patch.object(app, 'send_document', side_effect=send, create=True):
            workers = [threading.Thread(target=target.send_mediainfo_if_enabled, args=(7, 'x.mp4', self.message)) for _ in range(2)]
            for worker in workers:
                worker.start()
            for worker in workers:
                worker.join(timeout=10)
        self.assertFalse(errors)
        self.assertEqual(len(set(paths)), 2)
        self.assertTrue(all(not Path(path).exists() for path in paths))

    def test_cli_arguments_timeout_and_errors(self):
        with mock.patch.object(target.subprocess, 'run', return_value=types.SimpleNamespace(stdout='ok')) as run:
            self.assertEqual(target.get_mediainfo_cli('x.mp4'), 'ok')
            self.assertEqual(run.call_args.args[0], ['mediainfo', 'x.mp4'])
            self.assertEqual(run.call_args.kwargs['timeout'], 60)
            self.assertTrue(run.call_args.kwargs['check'])
        for error in (FileNotFoundError(), subprocess.TimeoutExpired('mediainfo', 60), subprocess.CalledProcessError(1, 'mediainfo')):
            with self.subTest(error=type(error).__name__), mock.patch.object(target.subprocess, 'run', side_effect=error):
                with self.assertRaises(RuntimeError):
                    target.get_mediainfo_cli('x.mp4')

    def test_disabled_no_subprocess_or_send(self):
        with mock.patch.object(target, 'get_mediainfo_cli') as cli, mock.patch.object(app, 'send_document', create=True) as send:
            target.send_mediainfo_if_enabled(7, 'x.mp4', self.message)
            cli.assert_not_called()
            send.assert_not_called()

    def test_success_and_failed_send_cleanup_preserves_existing_file(self):
        self.enable()
        video = Path('users/7/example.mp4')
        video.write_text('video')
        existing = video.with_name('example_mediainfo.txt')
        existing.write_text('keep')
        report_paths = []

        def send(chat_id, path, **kwargs):
            report_paths.append(Path(path))
            self.assertTrue(Path(path).exists())
            self.assertNotIn(str(video.resolve()), Path(path).read_text(encoding='utf-8'))
            self.assertEqual(kwargs['reply_parameters'].message_id, 42)

        with mock.patch.object(target, 'get_mediainfo_cli', return_value=f'Complete name: {video.resolve()}'), mock.patch.object(app, 'send_document', side_effect=send, create=True):
            target.send_mediainfo_if_enabled(7, str(video), self.message)
        self.assertFalse(report_paths[0].exists())
        self.assertEqual(existing.read_text(), 'keep')

        def fail_send(chat_id, path, **kwargs):
            report_paths.append(Path(path))
            raise RuntimeError('upload failed')

        with mock.patch.object(target, 'get_mediainfo_cli', return_value='ok'), mock.patch.object(app, 'send_document', side_effect=fail_send, create=True):
            target.send_mediainfo_if_enabled(7, str(video), self.message)
        self.assertFalse(report_paths[1].exists())
        self.assertEqual(existing.read_text(), 'keep')
        target.send_error_to_user.assert_called_once()

    def test_cli_failure_does_not_send_fake_report(self):
        self.enable()
        with mock.patch.object(target, 'get_mediainfo_cli', side_effect=RuntimeError('failed')), mock.patch.object(app, 'send_document', create=True) as send:
            target.send_mediainfo_if_enabled(7, 'x.mp4', self.message)
        send.assert_not_called()
        target.send_error_to_user.assert_called_once()


if __name__ == '__main__':
    unittest.main()
