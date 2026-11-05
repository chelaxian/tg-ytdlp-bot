"""Exercise the real size-limit functions without starting the bot or network."""
import ast
from pathlib import Path
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[2]
source = (ROOT / 'HELPERS' / 'limitter.py').read_text(encoding='utf-8')
tree = ast.parse(source)
names = {'get_file_size_limit_bytes', 'check_file_size_limit'}
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
assert len(functions) == len(names)
config = SimpleNamespace(MAX_FILE_SIZE_GB=8)
limits = SimpleNamespace(GROUP_MULTIPLIER=2)
chat_type = SimpleNamespace(PRIVATE='private')
namespace = {
    'Config': config,
    'LimitsConfig': limits,
    'enums': SimpleNamespace(ChatType=chat_type),
    'safe_get_messages': lambda _: SimpleNamespace(HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG='missing'),
    'logger': SimpleNamespace(warning=lambda *args: None),
    'should_apply_limits_to_admin': lambda **kwargs: True,
}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(ROOT / 'HELPERS' / 'limitter.py'), 'exec'), namespace)
get_limit = namespace['get_file_size_limit_bytes']
check = namespace['check_file_size_limit']


def message(kind):
    return SimpleNamespace(chat=SimpleNamespace(id=100, type=kind))


class FileSizeLimitTest(unittest.TestCase):
    def test_private_and_group_boundaries(self):
        gib = 1024 ** 3
        for kind, expected in [('private', 8 * gib), ('group', 16 * gib)]:
            msg = message(kind)
            self.assertEqual(get_limit(msg), expected)
            self.assertTrue(check({'filesize': expected}, message=msg))
            self.assertFalse(check({'filesize': expected + 1}, message=msg))

    def test_configured_fractional_multiplier(self):
        old = limits.GROUP_MULTIPLIER
        try:
            limits.GROUP_MULTIPLIER = 1.25
            self.assertEqual(get_limit(message('group')), 10 * 1024 ** 3)
        finally:
            limits.GROUP_MULTIPLIER = old

    def test_explicit_limit_remains_supported(self):
        self.assertFalse(check({'filesize': 101}, max_size_bytes=100, message=message('private')))
        self.assertTrue(check({'filesize': 100}, max_size_bytes=100, message=message('group')))

    def test_downloader_uses_same_limit(self):
        downloader = (ROOT / 'DOWN_AND_UP' / 'down_and_up.py').read_text(encoding='utf-8')
        self.assertIn('max_size_bytes = get_file_size_limit_bytes(message)', downloader)
        self.assertIn('check_file_size_limit(selected_format, max_size_bytes=max_size_bytes, message=message)', downloader)
        self.assertNotIn("getattr(Config, 'MAX_FILE_SIZE', 10)", downloader)


if __name__ == '__main__':
    unittest.main()
