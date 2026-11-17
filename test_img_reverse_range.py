import unittest
import ast
import logging
import os
import tempfile
import time
from unittest.mock import patch
from pathlib import Path
from types import SimpleNamespace
from URL_PARSERS.img_ranges import parse_img_range, plan_img_range


class ImageRangeTests(unittest.TestCase):
    def test_yt_dlp_compatible_negative_shorthand(self):
        self.assertEqual(parse_img_range('-213-1'), (-213, -1))
        self.assertEqual(parse_img_range('-213--1'), (-213, -1))
        self.assertEqual(parse_img_range('-1--3'), (-1, -3))
        self.assertEqual(parse_img_range('3--1'), None)

    def test_real_command_parser_preserves_shorthand(self):
        path = Path(__file__).parent / 'COMMANDS/image_cmd.py'
        tree = ast.parse(path.read_text())
        fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'image_command')
        start = next(i for i, n in enumerate(fn.body) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'manual_range' for t in n.targets))
        end = next(i for i in range(start, len(fn.body)) if isinstance(fn.body[i], ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'url' for t in fn.body[i].targets))
        body = fn.body[start:end] + [ast.Return(value=ast.Tuple(elts=[ast.Name(id='manual_range', ctx=ast.Load()), ast.Name(id='url', ctx=ast.Load())], ctx=ast.Load()))]
        wrapper = ast.FunctionDef(name='run', args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='text')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=body, decorator_list=[])
        env = dict(extract_url_range_tags=lambda text: ('https://example.com', -213, 1, None, [], '', None), logger=logging.getLogger(), LoggerMsg=SimpleNamespace(IMG_DEBUG_EXTRACT_URL_RANGE_LOG_MSG='{parsed_url}', IMG_DEBUG_RANGE_DETECTED_LOG_MSG='{_s}', IMG_DEBUG_NO_RANGE_LOG_MSG='none'))
        exec(compile(ast.fix_missing_locations(ast.Module(body=[wrapper], type_ignores=[])), str(path), 'exec'), env)
        for token in ('-213-1', '-213--1'):
            self.assertEqual(env['run']('/img ' + token + ' https://example.com'), ((-213, -1), 'https://example.com'))

    def test_direction_is_based_on_resolved_indices(self):
        self.assertEqual(plan_img_range(-213, -1, 300, 250), (300, 88, True))
        self.assertEqual(plan_img_range(-3, -1, 20, 2), (20, 19, True))
        self.assertEqual(plan_img_range(-1, -3, 20, 250), (20, 18, True))
        self.assertEqual(plan_img_range(-5, -2, 20, 250), (16, 19, False))
        self.assertEqual(plan_img_range(8, 3, None, 10), (8, 3, True))
        self.assertEqual(plan_img_range(-1, None, 20, 3), (20, 18, True))

    def test_production_loop_requests_and_scans_reverse_in_order(self):
        source = Path(__file__).parent / 'COMMANDS/image_cmd.py'
        tree = ast.parse(source.read_text())
        command = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'image_command')
        reverse = next(n for n in ast.walk(command) if isinstance(n, ast.FunctionDef) and n.name == 'run_and_collect_reverse')
        loop = next(n for n in ast.walk(command) if isinstance(n, ast.While) and n.lineno > reverse.lineno and any(isinstance(x, ast.Name) and x.id == 'run_and_collect_reverse' for x in ast.walk(n)))
        scan_end = next(n.lineno for n in ast.walk(loop) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute) and n.value.func.attr == 'append' and isinstance(n.value.func.value, ast.Name) and n.value.func.value.id == 'photos_videos_buffer')
        # Execute the actual download and filesystem scan, excluding Telegram delivery.
        class Trim(ast.NodeTransformer):
            def generic_visit(self, node):
                for field, value in ast.iter_fields(node):
                    if isinstance(value, list):
                        setattr(node, field, [self.visit(x) if isinstance(x, ast.AST) else x for x in value
                                              if not isinstance(x, ast.stmt) or x.lineno <= scan_end])
                    elif isinstance(value, ast.AST):
                        setattr(node, field, self.visit(value))
                return node
        loop = Trim().visit(loop)
        assigned = sorted({n.id for n in ast.walk(loop) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)})
        wrapper = ast.FunctionDef(name='run', args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Global(names=assigned), reverse, loop, ast.Return(value=ast.Name(id='photos_videos_buffer', ctx=ast.Load()))], decorator_list=[])
        program = ast.fix_missing_locations(ast.Module(body=[wrapper], type_ignores=[]))
        class Messages:
            def __getattr__(self, name): return ''
        for token in ('-213-1', '-213--1'):
            with self.subTest(token=token), tempfile.TemporaryDirectory() as directory:
                requests = []
                def download(url, expr, user_id, proxy, output_dir):
                    index = int(expr.split('-')[0]); requests.append(index)
                    Path(output_dir, f'{index}.jpg').write_bytes(b'x')
                    return True
                start, end, rev = plan_img_range(*parse_img_range(token), 300, 250)
                env = dict(current_start=start, manual_end_cap=end, is_reverse_order_img=rev,
                           request_batch_size=1, batch_size=1000, total_expected=213,
                           total_start_time=time.time(), last_activity_time=time.time(),
                           max_total_wait_time=10000, max_inactivity_time=10000,
                           photos_videos_buffer=[], seen_files=set(), total_downloaded=0,
                           is_admin=True, total_limit=250, gallery_dl_dir=directory, run_dir=directory,
                           logger=logging.getLogger(), LoggerMsg=Messages(), time=time, os=os,
                           url='https://example.com', user_id=1, use_proxy=False,
                           download_image_range_cli=download, download_image_range=download,
                           _IMG_SCAN_EXTS=('.jpg',), Config=SimpleNamespace(), message=None,
                           nsfw_flag=False, _is_paid_delivery=lambda *a: False,
                           prepare_media=lambda p, *a, **k: ('photo', p, [], ''),
                           _photo_send_problem=None, prepared_photo_files=[], files_to_cleanup=[],
                           others_buffer=[], _TG_PHOTO_EXTS={'.jpg'}, _TG_VIDEO_EXTS=set())
                with patch.object(time, 'sleep', lambda _: None):
                    exec(compile(program, str(source), 'exec'), env)
                    env['run']()
                scanned = [int(Path(item[0]).stem) for item in env['photos_videos_buffer']]
                self.assertEqual(requests, list(range(300, 87, -1)))
                self.assertEqual(scanned, requests)

    def test_unknown_length_fails_closed(self):
        with self.assertRaises(ValueError):
            plan_img_range(-3, -1, None, 10)

    def test_out_of_range_clips_and_limits_in_requested_direction(self):
        self.assertEqual(plan_img_range(-8, -1, 5, 10), (5, 1, True))
        self.assertEqual(plan_img_range(9, 1, None, 3), (9, 7, True))
        self.assertEqual(plan_img_range(-1, -8, 5, 10), (5, 1, True))

if __name__ == '__main__':
    unittest.main()
