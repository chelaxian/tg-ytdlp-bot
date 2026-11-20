"""Execute the production audio age handler with an offline recursive callback."""
import ast
import logging
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def production_functions(path, names, env):
    tree = ast.parse((ROOT / path).read_text(encoding='utf-8-sig'))
    nodes = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name in names]
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[])), str(path), 'exec'), env)


class AudioAgeRetryTests(unittest.TestCase):
    def setUp(self):
        self.pot = types.ModuleType('HELPERS.pot_helper')
        self.pot.logger = logging.getLogger(__name__)
        production_functions('HELPERS/pot_helper.py', {'add_web_creator_to_opts', 'is_age_restriction_error'}, self.pot.__dict__)
        self.errors = {'__name__': 'age_test_errors'}
        exec(compile((ROOT / 'HELPERS/ytdlp_errors.py').read_text(), 'ytdlp_errors.py', 'exec'), self.errors)
        tree = ast.parse((ROOT / 'DOWN_AND_UP/down_and_audio.py').read_text(encoding='utf-8-sig'))
        node = next(n for n in ast.walk(tree) if isinstance(n, ast.If) and isinstance(n.test, ast.BoolOp) and 'did_age_retry' in ast.unparse(n.test) and 'is_age_restriction_error' in ast.unparse(n.test))
        # This is the real handler; compile it in a function so its return statements work.
        fn = ast.FunctionDef(name='handle', args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Global(names=['did_age_retry']), node, ast.Return(value=ast.Constant(value=None))], decorator_list=[])
        self.code = compile(ast.fix_missing_locations(ast.Module(body=[fn], type_ignores=[])), '<audio-age-handler>', 'exec')

    def test_repeated_age_is_bounded_and_preserves_options(self):
        opts = {'cookiefile': '/cookie', 'proxy': 'http://proxy', 'extractor_args': {'youtube': {'player_client': ['web'], 'po_token': ['x']}, 'youtubepot-bgutilhttp': {'base_url': ['provider']}}}
        calls = []
        env = {'did_age_retry': False, 'is_age_restriction_error': self.pot.is_age_restriction_error,
               'classify_retryability': self.errors['classify_retryability'], 'error_text': 'Sign in to confirm your age',
               'logger': Mock(), 'user_id': 1, 'url': 'https://youtube.com/watch?v=x', 'current_index': 1, 'ytdl_opts': opts}
        exec(self.code, env)
        def retry(url, index, retry_opts):
            calls.append(retry_opts)
            return env['handle']()
        env['try_download_audio'] = retry
        with patch.dict(sys.modules, {'HELPERS.pot_helper': self.pot}):
            self.assertIsNone(env['handle']())
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0]['proxy'], opts['proxy'])
        self.assertEqual(calls[0]['cookiefile'], opts['cookiefile'])
        self.assertEqual(calls[0]['extractor_args']['youtube']['po_token'], ['x'])
        self.assertEqual(calls[0]['extractor_args']['youtube']['player_client'], ['web', 'web_creator'])
        self.assertEqual(opts['extractor_args']['youtube']['player_client'], ['web'])

    def test_audio_retry_keeps_new_proxy_and_cookie(self):
        tree = ast.parse((ROOT / 'DOWN_AND_UP/down_and_audio.py').read_text(encoding='utf-8-sig'))
        node = next(n for n in ast.walk(tree) if isinstance(n, ast.If)
                    and ast.unparse(n.test) == 'age_retry_opts is not None'
                    and any(isinstance(x, ast.Assign) and "extractor_args" in ast.unparse(x) for x in ast.walk(n)))
        code = compile(ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[])), '<audio-options>', 'exec')
        env = {'age_retry_opts': {'proxy': 'old-proxy', 'cookiefile': 'old-cookie',
                                  'extractor_args': {'youtube': {'player_client': ['web_creator']}}},
               'ytdl_opts': {'proxy': 'new-proxy', 'cookiefile': 'new-cookie'}}
        exec(code, env)
        self.assertEqual(env['ytdl_opts']['proxy'], 'new-proxy')
        self.assertEqual(env['ytdl_opts']['cookiefile'], 'new-cookie')
        self.assertIn('web_creator', env['ytdl_opts']['extractor_args']['youtube']['player_client'])

    def test_all_age_phrases_retry_once(self):
        for text in ('verify your age', 'age verification required', 'inappropriate for some users', 'age restricted', 'age-restricted', 'age gate'):
            with self.subTest(text=text):
                calls = []
                env = {'did_age_retry': False, 'is_age_restriction_error': self.pot.is_age_restriction_error,
                       'classify_retryability': self.errors['classify_retryability'], 'error_text': text,
                       'logger': Mock(), 'user_id': 1, 'url': 'https://youtube.com/watch?v=x', 'current_index': 1,
                       'ytdl_opts': {}, 'try_download_audio': lambda *args: calls.append(args)}
                exec(self.code, env)
                with patch.dict(sys.modules, {'HELPERS.pot_helper': self.pot}):
                    env['handle']()
                self.assertEqual(len(calls), 1)

    def test_rate_limit_does_not_retry(self):
        env = {'did_age_retry': False, 'is_age_restriction_error': self.pot.is_age_restriction_error,
               'classify_retryability': self.errors['classify_retryability'], 'error_text': 'Sign in to confirm your age; HTTP Error 429'}
        exec(self.code, env)
        self.assertIsNone(env['handle']())
        self.assertFalse(env['did_age_retry'])


if __name__ == '__main__':
    unittest.main()
