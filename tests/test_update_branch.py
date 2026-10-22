"""Выбор ветки обновления без импорта runtime-конфигурации бота."""
import ast
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


class UpdateBranchTests(unittest.TestCase):
    def test_default_pinned_and_environment_branches(self):
        source = Path(__file__).resolve().parents[1] / 'scripts/update_from_repo.py'
        tree = ast.parse(source.read_text(encoding='utf-8-sig'))
        node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'resolve_update_branch')
        namespace = {'os': os, 'Path': Path}
        exec(compile(ast.Module(body=[node], type_ignores=[]), str(source), 'exec'), namespace)
        resolve = namespace['resolve_update_branch']
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {'TGYTDLP_UPDATE_BRANCH': ''}):
            self.assertEqual(resolve(tmp), 'main')
            (Path(tmp) / '.update-branch').write_text('fix/reliability\n', encoding='utf-8')
            self.assertEqual(resolve(tmp), 'fix/reliability')
            with patch.dict(os.environ, {'TGYTDLP_UPDATE_BRANCH': 'release'}):
                self.assertEqual(resolve(tmp), 'release')


if __name__ == '__main__':
    unittest.main()
