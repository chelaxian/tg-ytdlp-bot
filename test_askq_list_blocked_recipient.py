"""Run with: python3 -m unittest test_askq_list_blocked_recipient

Regression for the 2026-11-27 14:47:12 UTC [HANDLER-CRASH] askq_callback
text='askq|list': a user who blocked the bot tapped the format-list button.
send_document raised USER_IS_BLOCKED, the except-branch tried to tell the same
user about it via send_message, that raised again and escaped the handler.

The real try/except block is extracted from the source with ast and executed
with mocked app/logger so the test exercises the shipped code, not a copy.
"""
import ast
import logging
import os
import pathlib
import sys
import tempfile
import types
import unittest
from unittest.mock import MagicMock

SRC = pathlib.Path(__file__).resolve().parent / 'DOWN_AND_UP/always_ask_menu.py'


class _Blocked(Exception):
    """Stand-in for pyrogram.errors.UserIsBlocked (message text is what the code checks)."""


BLOCKED_TEXT = 'Telegram says: [400 USER_IS_BLOCKED] (caused by "messages.SendMedia")'


def _raiser(text):
    def _raise(*_args, **_kwargs):
        raise _Blocked(text)
    return _raise


def _load_send_block():
    tree = ast.parse(SRC.read_text(encoding='utf-8'))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Try):
            continue
        src = ast.unparse(node)
        if 'app.send_document(' in src and 'ALWAYS_ASK_ERROR_SENDING_FORMATS_FILE_LOG_MSG' in src:
            return compile(ast.Module(body=[node], type_ignores=[]), str(SRC), 'exec')
    raise AssertionError('formats-list send block not found in always_ask_menu.py')


CODE = _load_send_block()


class AskqListBlockedRecipientTests(unittest.TestCase):
    def _run(self, error_text, message_raises=False):
        tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
        tmp.write('formats'); tmp.close()
        app = MagicMock()
        app.send_document.side_effect = _raiser(error_text)
        app.send_message.side_effect = _raiser(error_text) if message_raises else None

        class _Msgs:
            ALWAYS_ASK_USE_FORMAT_ID_MSG = 'use id'
            LIST_COMMAND_EXECUTED_LOG_MSG = 'list {user_id} {url}'
            AA_ERROR_SENDING_FORMATS_MSG = 'error {error}'
        safe_get_messages = lambda uid: _Msgs()

        class _LM:
            ALWAYS_ASK_ERROR_SENDING_FORMATS_FILE_LOG_MSG = 'Error sending formats file'
        logged = []
        logger = types.SimpleNamespace(error=logged.append, warning=logged.append)
        env = {
            'os': os, '_escape': lambda s: s, '_sanitize_error': lambda s: s,
            'logger': logger, 'LoggerMsg': _LM, 'safe_get_messages': safe_get_messages,
            '_list_caption': lambda url, text: 'cap', 'ReplyParameters': lambda **kw: kw,
            'send_to_logger': lambda *a, **k: None,
            'app': app, 'chat_id': 4242, 'user_id': 4242, 'url': 'https://example.invalid/v',
            'temp_file_path': tmp.name, 'original_message': types.SimpleNamespace(id=7),
        }
        raised = None
        fake_helpers = types.ModuleType('HELPERS.logger')
        fake_helpers.sanitize_error_message = lambda s: s
        fake_helpers.mark_user_blocked = lambda uid: None
        sys.modules['HELPERS.logger'] = fake_helpers
        try:
            exec(CODE, env)
        except Exception as exc:  # the defect: exception escapes the handler
            raised = exc
        finally:
            sys.modules.pop('HELPERS.logger', None)
        return raised, app, logged, tmp.name

    def test_blocked_recipient_does_not_crash_handler_and_cleans_up(self):
        raised, app, logged, path = self._run(BLOCKED_TEXT, message_raises=True)
        self.assertIsNone(raised, f'exception escaped handler: {raised!r}')
        # Nothing more can be delivered to this user: no second send attempt.
        app.send_message.assert_not_called()
        self.assertTrue(any('USER_IS_BLOCKED' in line for line in logged), logged)
        self.assertTrue(any('blocked the bot' in line for line in logged), logged)
        self.assertFalse(os.path.exists(path), 'temp formats file was not removed')

    def test_ordinary_send_error_still_reports_to_user(self):
        raised, app, logged, path = self._run('Telegram says: [400 FILE_PARTS_INVALID]')
        self.assertIsNone(raised)
        app.send_message.assert_called_once()
        self.assertIn('FILE_PARTS_INVALID', app.send_message.call_args.args[1])
        self.assertFalse(os.path.exists(path))


if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    unittest.main()
