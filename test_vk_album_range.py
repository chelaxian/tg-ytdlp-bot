import ast
import pathlib
import sys
import types
import unittest

SOURCE = pathlib.Path(__file__).resolve().parent / 'DOWN_AND_UP/gallery_dl_hook.py'


def helpers():
    tree = ast.parse(SOURCE.read_text())
    names = {'_is_vk_album', '_disable_vk_album_skip', '_range_cli_prefix'}
    module = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names], type_ignores=[])
    ns = {'sys': sys}
    exec(compile(module, str(SOURCE), 'exec'), ns)
    return ns


class VkAlbumRangeTests(unittest.TestCase):
    def test_scope(self):
        h = helpers()
        for url in ('https://vk.com/album-216920803_301835103', 'https://m.vk.ru/album1_2?x=1'):
            self.assertTrue(h['_is_vk_album'](url))
        for url in ('https://vk.com/wall1_2', 'https://evilvk.com/album1_2', 'https://example.com/a'):
            self.assertFalse(h['_is_vk_album'](url))
            self.assertEqual(h['_range_cli_prefix'](url), [sys.executable, '-m', 'gallery_dl'])

    def test_skip_is_per_extractor_not_filter(self):
        h = helpers()
        vk = 'https://vk.com/album-216920803_301835103'
        original = lambda n: n
        ext = types.SimpleNamespace(skip_files=original, config={'image-filter': 'width > 100', 'file-filter': 'height > 100'})
        h['_disable_vk_album_skip'](types.SimpleNamespace(extractor=ext), vk)
        self.assertEqual(ext.skip_files(11), 0)
        self.assertEqual(ext.config, {'image-filter': 'width > 100', 'file-filter': 'height > 100'})
        other = types.SimpleNamespace(skip_files=original)
        h['_disable_vk_album_skip'](types.SimpleNamespace(extractor=other), 'https://example.com/a')
        self.assertIs(other.skip_files, original)
        h['_disable_vk_album_skip'](object(), vk)

    def test_production_paths_use_fix_and_preserve_legacy(self):
        tree = ast.parse(SOURCE.read_text())
        funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
        api = funcs['download_image_range']
        cli = funcs['download_image_range_cli']
        calls = lambda n, name: sum(isinstance(x, ast.Call) and isinstance(x.func, ast.Name) and x.func.id == name for x in ast.walk(n))
        self.assertEqual(calls(api, '_disable_vk_album_skip'), 3)
        self.assertEqual(calls(cli, '_range_cli_prefix'), 2)
        self.assertNotIn('image-filter', ast.get_source_segment(SOURCE.read_text(), api))
        self.assertNotIn('image-filter', ast.get_source_segment(SOURCE.read_text(), cli))

if __name__ == '__main__':
    unittest.main()
