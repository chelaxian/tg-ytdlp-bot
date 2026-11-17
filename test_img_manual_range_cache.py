"""Regression tests for the real /img early-cache path, without Telegram I/O."""
import ast
import logging
import unittest
from pathlib import Path
from types import SimpleNamespace

SOURCE = Path(__file__).resolve().parent / 'COMMANDS' / 'image_cmd.py'


def run_cache_path(manual_range, cached):
    tree = ast.parse(SOURCE.read_text(encoding='utf-8'))
    function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'image_command')
    start = next(i for i, n in enumerate(function.body)
                 if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'cached_map' for t in n.targets))
    end = next(i for i in range(start, len(function.body))
               if isinstance(function.body[i], ast.Try)
               and 'get_image_info' in ast.unparse(function.body[i]))
    body = function.body[start:end] + [ast.Return(value=ast.Tuple(
        elts=[ast.Name(id='manual_range', ctx=ast.Load()), ast.Name(id='cached_map', ctx=ast.Load())], ctx=ast.Load()))]
    wrapper = ast.FunctionDef(name='run', args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='manual_range')], kwonlyargs=[], kw_defaults=[], defaults=[]),
                              body=body, decorator_list=[])
    module = ast.fix_missing_locations(ast.Module(body=[wrapper], type_ignores=[]))
    calls = []
    def get_posts(url, indices=None):
        calls.append(('lookup', indices))
        return {k: v for k, v in cached.items() if indices is None or k in indices}
    def forward(*args, **kwargs):
        calls.append(('forward', args))
    noop = lambda *a, **kw: None
    class Messages:
        def __getattr__(self, name): return ''
    env = dict(manual_range=manual_range, nsfw_flag=False, url='https://example.com/gallery',
               get_cached_image_posts=get_posts, get_cached_image_post_indices=lambda url: set(cached),
               logger=logging.getLogger(__name__), message_thread_id=None, chat_id=1, user_id=1,
               get_log_channel=lambda _: 2, sm=SimpleNamespace(safe_forward_messages=forward),
               app=SimpleNamespace(forward_messages=forward), daily_quota=SimpleNamespace(record=noop, IMAGE='image'),
               message=None, safe_edit_message_text=noop, safe_get_messages=lambda _: Messages(),
               status_msg=SimpleNamespace(id=1), enums=SimpleNamespace(ParseMode=SimpleNamespace(HTML='html')),
               send_to_logger=noop, LoggerMsg=Messages())
    exec(compile(module, str(SOURCE), 'exec'), env)
    return env['run'](manual_range), calls


class ManualRangeCacheTests(unittest.TestCase):
    def test_unranged_request_still_uses_cache(self):
        _, calls = run_cache_path(None, {1: [101, 102]})
        self.assertEqual(calls[0], ('lookup', None))
        self.assertEqual(calls[1][0], 'forward')

    def test_manual_ranges_bypass_album_cache(self):
        # Album keys are not source photo indexes; partial, sparse and negative
        # ranges cannot safely be served or resumed using these keys.
        for requested, cache in [
            ((1, 200), {1: list(range(10)), 2: list(range(10, 20))}),
            ((1, 4), {1: [101, 102], 3: [103]}),
            ((2, 2), {2: [201, 202, 203]}),
            ((-5, -1), {1: [101], 2: [102]}),
            ((-3, None), {1: [101], 4: [104]}),
            ((8, 3), {3: [103], 8: [108]}),
            ((4, None), {4: [104]}),
        ]:
            with self.subTest(requested=requested, cache=cache):
                result, calls = run_cache_path(requested, cache)
                self.assertEqual(result, (requested, {}))
                self.assertEqual(calls, [])


if __name__ == '__main__':
    unittest.main()
