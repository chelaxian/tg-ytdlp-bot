"""Проверки атомарной записи и диагностики subprocess без сети."""
import ast
import html
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from HELPERS.atomic_io import atomic_write_json


class AtomicJsonTests(unittest.TestCase):
    def test_failed_serialization_preserves_previous_file(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / 'cache.json'
            atomic_write_json(path, {'old': True})
            with self.assertRaises(TypeError):
                atomic_write_json(path, {'bad': object()})
            self.assertEqual(json.loads(path.read_text()), {'old': True})

    def test_failed_replace_preserves_previous_file(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / 'cache.json'
            atomic_write_json(path, {'old': True})
            with patch('HELPERS.atomic_io.os.replace', side_effect=OSError('quota')):
                with self.assertRaises(OSError):
                    atomic_write_json(path, {'new': True})
            self.assertEqual(json.loads(path.read_text()), {'old': True})
            self.assertEqual(list(Path(tmp).iterdir()), [path])


class ScriptDiagnosticsTests(unittest.TestCase):
    def test_failure_reason_precedes_banner_and_is_html_safe(self):
        path = Path(__file__).resolve().parents[1] / 'COMMANDS/admin_cmd.py'
        tree = ast.parse(path.read_text(encoding='utf-8-sig'))
        node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_script_failure_details')
        namespace = {'html': html}
        exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), namespace)
        output = namespace['_script_failure_details'](SimpleNamespace(
            returncode=3, stderr='network <timeout>', stdout='banner' * 1000))
        self.assertTrue(output.startswith('Exit code: 3'))
        self.assertIn('network &lt;timeout&gt;', output)
        self.assertLess(output.index('stderr:'), output.index('stdout'))
        self.assertLessEqual(len(output), 3000)


if __name__ == '__main__':
    unittest.main()
