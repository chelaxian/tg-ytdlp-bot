"""Regression tests for URL handling in the real /img command."""
import ast
import logging
import re
import unittest
from pathlib import Path
from urllib.parse import urlsplit

SOURCE = Path(__file__).resolve().parent / 'COMMANDS' / 'image_cmd.py'


def run_url_extraction(url):
    tree = ast.parse(SOURCE.read_text(encoding='utf-8'))
    command = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'image_command')
    start = next(i for i, n in enumerate(command.body) if isinstance(n, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == 'manual_range' for t in n.targets))
    end = next(i for i, n in enumerate(command.body) if isinstance(n, ast.FunctionDef) and n.name == '_dedupe_tags_text')
    helpers = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_normalize_img_url']
    body = command.body[start:end] + [ast.Return(value=ast.Name(id='url', ctx=ast.Load()))]
    wrapper = ast.FunctionDef(name='run', args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='text')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=body, decorator_list=[])
    module = ast.fix_missing_locations(ast.Module(body=helpers + [wrapper], type_ignores=[]))
    class Messages:
        def __getattr__(self, name): return '{parsed_url} {_s} {_e} {text}'
    env = dict(re=re, urlsplit=urlsplit, logger=logging.getLogger(__name__), LoggerMsg=Messages(),
               extract_url_range_tags=lambda text: (url, 1, 1, [], [], '', None))
    exec(compile(module, str(SOURCE), 'exec'), env)
    return env['run']('/img ' + url)


class ImageVkNormalizationTests(unittest.TestCase):
    def test_vk_domains_preserve_url_parts(self):
        for source, expected in [
            ('https://vk.ru/album-1_2?x=vk.ru#vk.ru', 'https://vk.com/album-1_2?x=vk.ru#vk.ru'),
            ('http://m.vk.ru:8080/a?q=1#f', 'http://m.vk.com:8080/a?q=1#f'),
            ('https://www.VK.RU/a', 'https://www.vk.com/a'),
        ]:
            with self.subTest(source=source):
                self.assertEqual(run_url_extraction(source), expected)

    def test_other_hosts_are_untouched(self):
        for url in ['https://evilvk.ru/a', 'https://vk.ru.evil.com/a',
                    'https://vk.ru@evil.com/a', 'https://other.vk.ru/a',
                    'https://vk.com/a?v=vk.ru#vk.ru']:
            with self.subTest(url=url):
                self.assertEqual(run_url_extraction(url), url)


if __name__ == '__main__':
    unittest.main()
