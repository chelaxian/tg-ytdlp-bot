"""Admin multi-URL gallery-dl mode (#admin-multi-img): real-branch tests.

Covers:
* is_gallerydl_url — gallery-dl URL classification incl. vk.ru -> vk.com
  normalization (reuses _normalize_img_url from COMMANDS/image_cmd.py);
* process_admin_gallery_batch — sequential image_command runs, status message
  lifecycle identical to process_multiple_urls_queue, continue-on-error;
* the gate inside url_distractor — admin-only, /img-command-excluded,
  multi-URL-only, all-gallery-only, range-syntax-excluded, and ordered before
  route_if_gallerydl_only;
* regression guards: video multi-URL queue and its MAX_MULTI_URL_LIMIT check
  are untouched.

Run with: python3 -m unittest test_img_admin_multi_url
"""
import ast
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
ENGINE_ROUTER = ROOT / 'URL_PARSERS' / 'engine_router.py'
URL_EXTRACTOR = ROOT / 'URL_PARSERS' / 'url_extractor.py'
VIDEO_EXTRACTOR = ROOT / 'URL_PARSERS' / 'video_extractor.py'
IMAGE_CMD = ROOT / 'COMMANDS' / 'image_cmd.py'


def _fn_from(path, name):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    return next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)


class _Log:
    def __init__(self):
        self.lines = []

    def info(self, msg, *a):
        self.lines.append(('info', msg))

    def error(self, msg, *a):
        self.lines.append(('error', msg))

    def debug(self, msg, *a):
        self.lines.append(('debug', msg))

    def warning(self, msg, *a):
        self.lines.append(('warning', msg))


def _load_is_gallerydl_url():
    """Exec the real is_gallerydl_url (engine_router) + _normalize_img_url
    (image_cmd) against the real DomainsConfig."""
    from CONFIG.domains import DomainsConfig
    from urllib.parse import urlparse
    router_fn = _fn_from(ENGINE_ROUTER, 'is_gallerydl_url')
    norm_fn = _fn_from(IMAGE_CMD, '_normalize_img_url')
    log = _Log()
    env = dict(DomainsConfig=DomainsConfig, urlparse=urlparse, logger=log,
               _normalize_img_url=None)
    module = ast.fix_missing_locations(ast.Module(body=[norm_fn, router_fn], type_ignores=[]))
    exec(compile(module, str(ENGINE_ROUTER), 'exec'), env)
    return env['is_gallerydl_url'], log


class IsGallerydlUrlTests(unittest.TestCase):
    def setUp(self):
        self.fn, self.log = _load_is_gallerydl_url()

    def test_gallery_paths_are_recognized(self):
        for url in (
            'https://vk.com/album-216920803_301835103',
            'https://vk.com/wall-1_2',
            'https://www.vk.com/album-1_2',
            'https://instagram.com/p/CxYz/',
            # gallery-dl-only domains
            'https://e-hentai.org/g/123/abc',
            'https://www.gelbooru.com/index.php?page=post&s=view&id=1',
        ):
            with self.subTest(url=url):
                self.assertTrue(self.fn(url), url)

    def test_vk_ru_is_normalized_to_vk_com(self):
        # existing vk.ru -> vk.com normalization must make vk.ru batches work
        for url in ('https://vk.ru/album-1_2', 'https://m.vk.ru/album-1_2',
                    'https://www.vk.ru/album-1_2', 'https://vk.ru/wall-1_2?x=1'):
            with self.subTest(url=url):
                self.assertTrue(self.fn(url), url)

    def test_non_gallery_urls_are_rejected(self):
        for url in (
            'https://youtube.com/watch?v=x',          # yt-dlp only
            'https://vk.ru/video-1_2',                # vk, but not album/wall path
            'https://evilvk.ru/album-1_2',            # hostname is not vk
            'https://vk.ru.evil.com/album-1_2',
            'https://example.com/album-1_2',
            '',
        ):
            with self.subTest(url=url):
                self.assertFalse(self.fn(url), url)

    def test_bad_input_does_not_raise(self):
        # None / weird input is normalized to '' and simply rejected
        self.assertFalse(self.fn(None))
        self.assertFalse(self.fn(''))
        self.assertEqual(self.log.lines, [])  # no crash, no error spam


def _run_batch(urls, fail_on=None, status_msg_id=42):
    """Exec the real process_admin_gallery_batch with stubbed externals."""
    fn = _fn_from(ENGINE_ROUTER, 'process_admin_gallery_batch')
    sent, edits, img_calls = [], [], []
    log = _Log()

    class _Msgs:
        TOTAL_PROGRESS_MSG = 'Total progress'
        URL_PROGRESS_MSG = '<b>URL:</b> {current} / {total}'
        MULTI_URL_COMPLETED_MSG = 'Processing completed'

    def fake_message(text, user_id, command=None, original_chat_id=None,
                     message_thread_id=None, original_message=None):
        m = types.SimpleNamespace(text=text, chat=types.SimpleNamespace(id=user_id),
                                  from_user=types.SimpleNamespace(id=user_id),
                                  message_thread_id=message_thread_id,
                                  _original_message=original_message, id=0)
        img_calls.append(m)
        return m

    def image_command(app, msg):
        if fail_on is not None and fail_on in msg.text:
            raise RuntimeError('boom')
        return 'ok'

    safe = types.ModuleType('HELPERS.safe_messeger')
    safe.fake_message = fake_message
    safe.safe_send_message = lambda uid, text, **kw: sent.append(text) or (
        types.SimpleNamespace(id=status_msg_id) if status_msg_id is not None else None)
    safe.safe_edit_message_text = lambda uid, mid, text, **kw: edits.append(text) or True
    msgs_mod = types.ModuleType('CONFIG.messages')
    msgs_mod.safe_get_messages = lambda uid: _Msgs()
    pyro = types.ModuleType('pyrogram.types')
    pyro.ReplyParameters = lambda **kw: kw
    log_mod = types.ModuleType('HELPERS.logger')
    log_mod.logger = log
    log_mod.send_to_logger = lambda message, text, **kw: sent.append(('LOG', text))
    stubs = {'HELPERS.safe_messeger': safe, 'CONFIG.messages': msgs_mod,
             'pyrogram.types': pyro, 'HELPERS.logger': log_mod}
    message = types.SimpleNamespace(
        chat=types.SimpleNamespace(id=7, first_name='Admin'),
        from_user=types.SimpleNamespace(id=7, username='admin'),
        text=' '.join(urls), id=5, message_thread_id=None)
    env = dict(fake_message=fake_message, image_command=image_command, logger=log,
               send_to_logger=lambda message, text, **kw: sent.append(('LOG', text)))
    with patch.dict(sys.modules, stubs):
        exec(compile(ast.Module(body=[fn], type_ignores=[]), str(ENGINE_ROUTER), 'exec'), env)
        result = env['process_admin_gallery_batch'](None, message, list(urls), tags_text='#tag1')
    return dict(result=result, sent=sent, edits=edits, img_calls=img_calls, log=log)


class ProcessAdminGalleryBatchTests(unittest.TestCase):
    URLS = ['https://vk.com/album-1_2', 'https://vk.ru/album-3_4',
            'https://instagram.com/p/abc/']

    def test_each_url_becomes_a_separate_sequential_img_task(self):
        out = _run_batch(self.URLS)
        self.assertTrue(out['result'])
        self.assertEqual(len(out['img_calls']), 3)
        # each fake message is exactly "/img <url> #tag1" in the original order
        self.assertEqual([m.text for m in out['img_calls']],
                         [f'/img {u} #tag1' for u in self.URLS])

    def test_status_message_lifecycle_matches_multi_url_queue(self):
        out = _run_batch(self.URLS)
        # 1 initial status send, one edit per URL, 1 final edit with completion
        self.assertEqual(len(out['edits']), 4)
        self.assertIn('<b>URL:</b> 1 / 3', out['edits'][0])
        self.assertIn('<b>URL:</b> 3 / 3', out['edits'][2])
        self.assertIn('Processing completed', out['edits'][3])
        self.assertIn('Total progress', out['edits'][3])
        # multi-url request is logged to the log channel
        self.assertTrue(any(e == ('LOG', unittest.mock.ANY) and 'MULTI_URL_IMG' in e[1]
                            for e in out['sent'] if isinstance(e, tuple)))

    def test_one_failing_url_does_not_stop_the_queue(self):
        out = _run_batch(self.URLS, fail_on='album-3_4')
        self.assertEqual(len(out['img_calls']), 3)  # all attempted
        self.assertTrue(any(kind == 'error' for kind, _ in out['log'].lines))
        self.assertIn('Processing completed', out['edits'][-1])  # final status still set

    def test_none_status_message_is_survivable(self):
        out = _run_batch(self.URLS[:2], status_msg_id=None)
        self.assertEqual(out['edits'], [])           # nothing to edit
        self.assertEqual(len(out['img_calls']), 2)   # downloads still run


GATE_TEST_SRC = "is_admin and not text.startswith(Config.IMG_COMMAND)"


def _find_node(root, pred):
    for node in ast.walk(root):
        if pred(node):
            return node
    return None


def _find_gate(distractor):
    """Find the admin gallery gate by structure, robust to unparse parentheses."""
    for node in ast.walk(distractor):
        if isinstance(node, ast.If):
            src = ast.unparse(node.test).replace('(', '').replace(')', '')
            if src == GATE_TEST_SRC.replace('(', '').replace(')', ''):
                return node
    return None


def _run_gate(text, is_admin, urls=None, has_range=False, gallery=True,
              extracted_ok=True, batch_result=True):
    """Exec the real admin-gallery gate (If node from url_distractor)."""
    tree = ast.parse(URL_EXTRACTOR.read_text(encoding='utf-8'))
    distractor = _fn_from(URL_EXTRACTOR, 'url_distractor')
    gate = _find_node(distractor,
                      lambda n: isinstance(n, ast.If) and n is _find_gate(distractor))
    assert gate is not None, 'admin gallery gate not found in url_distractor'
    url_list = urls if urls is not None else \
        ['https://vk.com/album-1_2', 'https://vk.ru/album-3_4']
    batches = []
    video_mod = types.ModuleType('URL_PARSERS.video_extractor')
    video_mod.extract_multiple_urls = lambda t: url_list
    video_mod.has_range_syntax = lambda t: has_range
    router_mod = types.ModuleType('URL_PARSERS.engine_router')
    router_mod.is_gallerydl_url = lambda u: gallery
    router_mod.process_admin_gallery_batch = \
        lambda app, message, urls, tags_text='': batches.append((urls, tags_text)) or batch_result
    message = types.SimpleNamespace(
        chat=types.SimpleNamespace(id=1), from_user=types.SimpleNamespace(id=1),
        text=text, id=3)
    env = dict(is_admin=is_admin, text=text, user_id=message.chat.id,
               Config=types.SimpleNamespace(IMG_COMMAND='/img'),
               message=message, logger=_Log(), app=None,
               extract_url_range_tags=lambda t: (url_list[0] if url_list else None, 1, 1,
                                                 None, [], '#tag1' if extracted_ok else '', None))
    # the gate contains a `return` (batch handled) — wrap it in a probe function
    # that reports whether the distractor would stop processing the message.
    wrapper = ast.FunctionDef(
        name='gate_probe', args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[],
                                              kw_defaults=[], defaults=[]),
        body=[gate, ast.Return(value=ast.Constant(value='fell-through'))],
        decorator_list=[])
    module = ast.fix_missing_locations(ast.Module(body=[wrapper], type_ignores=[]))
    with patch.dict(sys.modules, {'URL_PARSERS.video_extractor': video_mod,
                                  'URL_PARSERS.engine_router': router_mod}):
        exec(compile(module, str(URL_EXTRACTOR), 'exec'), env)
        fell_through = env['gate_probe']()
    return batches, dict(fell_through=fell_through, env=env)


class AdminGateBranchTests(unittest.TestCase):
    TEXT = 'https://vk.com/album-1_2 https://vk.ru/album-3_4'

    def test_admin_multi_gallery_batch_is_processed(self):
        batches, meta = _run_gate(self.TEXT, is_admin=True)
        self.assertEqual(batches, [(['https://vk.com/album-1_2',
                                     'https://vk.ru/album-3_4'], '#tag1')])
        self.assertFalse(meta['fell_through'])  # url_distractor stops: handled

    def test_non_admin_is_untouched(self):
        batches, meta = _run_gate(self.TEXT, is_admin=False)
        self.assertEqual(batches, [])  # current behavior preserved
        self.assertTrue(meta['fell_through'])  # old flow continues

    def test_single_url_does_not_trigger_batch(self):
        batches, meta = _run_gate('https://vk.com/album-1_2', is_admin=True,
                               urls=['https://vk.com/album-1_2'])
        self.assertEqual(batches, [])
        self.assertTrue(meta['fell_through'])  # single-URL router handles it

    def test_mixed_urls_do_not_trigger_batch(self):
        # any non-gallery URL in the pack -> old video flow
        batches, meta = _run_gate(self.TEXT + ' https://youtube.com/watch?v=x', is_admin=True,
                                  urls=['https://vk.com/album-1_2',
                                        'https://vk.ru/album-3_4',
                                        'https://youtube.com/watch?v=x'],
                                  gallery=False)
        self.assertEqual(batches, [])
        self.assertTrue(meta['fell_through'])

    def test_range_syntax_falls_back_to_video_flow(self):
        # playlist ranges (*1*5 / /vid 1-5) keep their existing restrictions
        batches, meta = _run_gate(self.TEXT + '*1*5', is_admin=True, has_range=True)
        self.assertEqual(batches, [])
        self.assertTrue(meta['fell_through'])

    def test_img_command_text_never_enters_the_gate(self):
        batches, meta = _run_gate('/img https://vk.com/album-1_2', is_admin=True,
                                  urls=['https://vk.com/album-1_2'])
        self.assertEqual(batches, [])
        self.assertTrue(meta['fell_through'])

    def test_gate_failure_does_not_break_url_processing(self):
        # exception inside the gate must be swallowed (old flow continues)
        tree = ast.parse(URL_EXTRACTOR.read_text(encoding='utf-8'))
        distractor = _fn_from(URL_EXTRACTOR, 'url_distractor')
        gate = _find_node(distractor,
                          lambda n: isinstance(n, ast.If) and n is _find_gate(distractor))
        env = dict(is_admin=True, text=self.TEXT, user_id=1,
                   Config=types.SimpleNamespace(IMG_COMMAND='/img'),
                   message=types.SimpleNamespace(text=self.TEXT), logger=_Log(), app=None,
                   # startswith present on str; break the inner import instead
                   extract_url_range_tags=lambda t: (None, 1, 1, None, [], '', None))
        broken = types.ModuleType('URL_PARSERS.video_extractor')
        def _boom(*a, **k):
            raise ImportError('nope')
        broken.__getattr__ = _boom
        wrapper = ast.FunctionDef(
            name='gate_probe', args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[],
                                                  kw_defaults=[], defaults=[]),
            body=[gate, ast.Return(value=ast.Constant(value='fell-through'))],
            decorator_list=[])
        module = ast.fix_missing_locations(ast.Module(body=[wrapper], type_ignores=[]))
        with patch.dict(sys.modules, {'URL_PARSERS.video_extractor': broken}):
            exec(compile(module, str(URL_EXTRACTOR), 'exec'), env)
            self.assertEqual(env['gate_probe'](), 'fell-through')  # swallowed


class RegressionGuardsTests(unittest.TestCase):
    """Video multi-URL behavior and playlist limits must stay intact."""

    def test_gate_runs_before_single_url_gallery_router(self):
        """A gallery batch must not be eaten by route_if_gallerydl_only (which
        would process only the first URL)."""
        tree = ast.parse(URL_EXTRACTOR.read_text(encoding='utf-8'))
        distractor = _fn_from(URL_EXTRACTOR, 'url_distractor')
        gate = _find_node(distractor,
                          lambda n: isinstance(n, ast.If) and n is _find_gate(distractor))
        router = _find_node(distractor,
                            lambda n: isinstance(n, ast.Try)
                            and 'route_if_gallerydl_only' in ast.unparse(n))
        self.assertIsNotNone(gate)
        self.assertIsNotNone(router)
        self.assertLess(gate.lineno, router.lineno)

    def test_video_multi_url_queue_and_limit_unchanged(self):
        src = VIDEO_EXTRACTOR.read_text(encoding='utf-8')
        self.assertIn('process_multiple_urls_queue(app, message, all_urls, saved_format, is_admin, is_group)', src)
        self.assertIn('url_limit = LimitsConfig.MAX_MULTI_URL_LIMIT', src)
        # non-admins keep the 10-URL limit (admin unlimited path is separate)
        tree = ast.parse(src)
        fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                  and n.name == 'process_multiple_urls_queue')
        self.assertTrue(any('MAX_MULTI_URL_LIMIT' in ast.unparse(n) for n in ast.walk(fn)))
        # the video extractor multi-url branch is reached exactly as before
        multi = next(n for n in ast.walk(tree) if isinstance(n, ast.If)
                     and ast.unparse(n.test) == 'len(all_urls) > 1')
        self.assertTrue(any('process_multiple_urls_queue' in ast.unparse(n)
                            for n in ast.walk(multi)))


if __name__ == '__main__':
    unittest.main()
