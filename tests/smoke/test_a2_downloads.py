"""Offline AST-isolated smoke tests: real function bodies, no app/network imports."""
import ast
import os
import sys
import tempfile
import threading
import types
import unittest
from pathlib import Path
from unittest.mock import Mock
R=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R))
from HELPERS.cookie_file import validated_cookie_options

class DownloadError(Exception): pass
class Msg:
    def __getattr__(self,n): return n

def module(name, **attrs):
    m=types.ModuleType(name);m.__dict__.update(attrs);sys.modules[name]=m;return m

def functions(path, names, env, nonlocals=False):
    env.setdefault("validated_cookie_options", validated_cookie_options)
    tree=ast.parse((R/path).read_text(encoding='utf-8-sig'))
    selected=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name in names]
    if nonlocals:
        class Globals(ast.NodeTransformer):
            def visit_Nonlocal(self,n): return ast.copy_location(ast.Global(names=n.names),n)
        selected=[Globals().visit(n) for n in selected]
    exec(compile(ast.fix_missing_locations(ast.Module(body=selected,type_ignores=[])),str(path),'exec'),env)
    return env

class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.count=0;self.downloads=0;self.error=None;self.phase='extract';self.metadata={'id':'xyz','title':'title','formats':[]}
        outer=self
        class YDL:
            def __init__(self,opts): self.opts=opts
            def __enter__(self): return self
            def __exit__(self,*a): return False
            def extract_info(self,*a,**kw):
                outer.count+=1
                if outer.error and outer.phase=='extract': raise DownloadError(outer.error)
                return dict(outer.metadata)
            def download(self,*a):
                outer.downloads+=1
                if outer.error and outer.phase=='download': raise DownloadError(outer.error)
                return 0
        module('COMMANDS.args_cmd',get_user_ytdlp_args=lambda *a:{},log_ytdlp_options=lambda *a:None)
        module('COMMANDS.format_cmd',get_session_mkv_override=lambda *a:False,get_user_mkv_preference=lambda *a:False)
        module('COMMANDS.cookies_cmd',get_cookie_cache_result=lambda *a:None,set_cookie_cache_result=lambda *a:None)
        module('HELPERS.proxy_helper',is_no_proxy_domain=lambda *a:True,needs_auto_proxy=lambda *a:False,add_proxy_to_ytdl_opts=lambda o,*a:o,
               try_with_proxy_fallback=lambda o,u,i,fn:fn(o),try_with_impersonate_fallback=Mock(),is_cloudflare_error=lambda e:False,has_alternative_proxy_route=lambda *a:False)
        module('DOWN_AND_UP.yt_dlp_hook',get_video_formats=lambda *a,**kw:outer.metadata)
        module('HELPERS.filesystem_hlp',remove_protection_file=lambda *a:None)
        env=dict(os=os,html=__import__('html'),time=__import__('time'),threading=threading,urlparse=__import__('urllib.parse',fromlist=['urlparse']).urlparse,
                 yt_dlp=types.SimpleNamespace(YoutubeDL=YDL,utils=types.SimpleNamespace(DownloadError=DownloadError)),
                 safe_get_messages=lambda *a:Msg(),logger=Mock(),message=types.SimpleNamespace(chat=types.SimpleNamespace(id=1)),user_id=1,
                 user_dir_name=self.tmp.name,current_total_process='',error_message='',did_cookie_retry=False,did_proxy_retry=False,did_live_from_start_retry=False,
                 did_format_fallback=False,is_hls=False,error_message_sent=False,is_reverse_order=False,use_range_download=False,
                 current_playlist_items_override=None,range_entries_metadata=None,download_sections=None,hls_file_found=False,auto_range_added=False,
                 did_no_pp_retry=False,did_local_file_retry=False,did_resume_retry=False,download_stage='init',is_playlist=False,current_index=1,
                 is_no_filter_domain=lambda *a:True,is_no_cookie_domain=lambda *a:True,is_youtube_url=lambda *a:False,need_subs=False,
                 attempts=[{'format':'best'}],user_merge_format='mp4',use_proxy=False,add_pot_to_ytdl_opts=lambda o,*a:o,cached_video_info=None,
                 cookies_already_checked=True,original_text='',video_start_with=1,video_end_with=1,video_count=1,progress_func=lambda *a:None,
                 safe_edit_message_text=Mock(),proc_msg_id=1,full_bar='',send_error_to_user=Mock(),send_to_user=Mock(),log_error_to_channel=Mock(),
                 should_fallback_to_gallery_dl=lambda *a:False,is_skippable_video_error=lambda *a:False,sanitize_error_message=str,
                 is_cookie_error=lambda *a:False,is_age_restriction_error=lambda *a:False,is_youtube_geo_error=lambda *a:False)
        classifier={};exec((R/'HELPERS/ytdlp_errors.py').read_text(encoding='utf-8'),classifier)
        env.update({k:classifier[k] for k in ['should_abort_retries','is_format_unavailable','is_missing_local_file','classify_retryability']})
        env.update(is_playlist_from_info_dict=lambda *a:False, DomainsConfig=types.SimpleNamespace(YTDLP_ONLY_DOMAINS=[]), _record_net_error=Mock())
        module('CONFIG.errors',is_geo_block_error=lambda *a:False,has_country_list_in_error=lambda *a:False,classify_yt_dlp_error=lambda *a:'UNKNOWN')
        env['FORMAT_FALLBACK_SELECTOR']='bv*+ba/b'
        functions('DOWN_AND_UP/down_and_up.py',['_retry_backoff_seconds','try_download'],env,True)
        self.env=env
    def run_download(self): return self.env['try_download']('https://example.test/video',{'format':'requested'})
    def test_format_unavailable_two_extractions(self):
        self.error='ERROR: Requested format is not available'
        self.assertEqual(self.run_download(),'FORMAT_NOT_AVAILABLE');self.assertEqual(self.count,2)
    def test_ffmpeg_two_downloads(self):
        self.error='ERROR: ffmpeg exited with code 1';self.phase='download'
        self.assertEqual(self.run_download(),'FFMPEG_ERROR');self.assertEqual(self.downloads,2)
    def test_terminal_metadata_no_extraction(self):
        self.metadata={'error':'PERMANENT_UNAVAILABLE','original_error':'Private video'}
        self.assertEqual(self.run_download(),'TERMINAL_ERROR');self.assertEqual(self.count,0)
        self.assertEqual(self.env['error_message'],'Private video')
    def test_no_proxy_route_no_identical_repeat(self):
        self.error='Unknown extractor failure'
        self.assertIsNone(self.run_download());self.assertEqual(self.count,1)
    def test_enoent_one_retry(self):
        self.error='ERROR: unable to open for writing: [Errno 2] No such file or directory';self.phase='download'
        self.run_download();self.assertEqual(self.downloads,2)
        self.assertTrue(self.env['did_local_file_retry'])
    def test_eof_resume_once(self):
        (Path(self.tmp.name)/'vid_xyz.mp4.part').write_bytes(b'part')
        self.error='Got error: 10 bytes read, 20 more expected';self.phase='download'
        self.assertEqual(self.run_download(),'NETWORK_ERROR');self.assertEqual(self.downloads,2)
    def test_postprocessing_two_downloads(self):
        self.error='ERROR: Postprocessing: Conversion failed';self.phase='download'
        self.assertEqual(self.run_download(),'POSTPROCESSING_ERROR');self.assertEqual(self.downloads,2)
    def test_strict_av1_reason(self):
        self.metadata['formats']=[{'vcodec':'avc1','height':720}]
        result=self.env['try_download']('https://example.test/video',{'format':'bv[vcodec*=av01]'})
        self.assertIsNone(result);self.assertIn('AV1',self.env['error_message']);self.assertEqual(self.count,0)
    def test_av1_with_alternatives_not_rejected(self):
        self.metadata['formats']=[{'vcodec':'avc1','height':720}]
        result=self.env['try_download']('https://example.test/video',{'format':'bv[vcodec*=av01]/best'})
        self.assertEqual(result['id'],'xyz');self.assertEqual(self.downloads,1)
    def test_youtube_generic_auth_error_is_deferred_for_cookie_retry(self):
        self.env['is_youtube_url'] = lambda *a: True
        self.env['is_cookie_error'] = lambda *a: True
        self.error = "Sign in to confirm you're not a bot"
        # Raise a generic exception, as in the live-browser failure.
        self.env['yt_dlp'].utils.DownloadError = type('OtherDownloadError', (Exception,), {})
        self.assertIsNone(self.run_download())
        self.env['send_to_user'].assert_not_called()
        self.env['send_error_to_user'].assert_not_called()
        self.assertFalse(self.env['error_message_sent'])

    def test_youtube_cookie_cascade_and_final_failure(self):
        tree = ast.parse((R/'DOWN_AND_UP/down_and_up.py').read_text(encoding='utf-8-sig'))
        loop = next(n for n in ast.walk(tree) if isinstance(n, ast.For)
                    and isinstance(n.target, ast.Tuple)
                    and [getattr(x, 'id', '') for x in n.target.elts] == ['attempt_no', 'attempt'])
        final = next(n for n in ast.walk(tree) if isinstance(n, ast.If)
                     and n.lineno > loop.lineno and isinstance(n.test, ast.Compare)
                     and isinstance(n.test.left, ast.Name) and n.test.left.id == 'info_dict'
                     and isinstance(n.test.ops[0], ast.Is) and isinstance(n.test.comparators[0], ast.Constant)
                     and n.test.comparators[0].value is None and any(isinstance(x, ast.With) for x in n.body))
        # Execute the real outer format loop and final report, stopping before
        # bookkeeping/breaks belonging to the enclosing playlist loop.
        final.body = final.body[:next(i for i, n in enumerate(final.body) if isinstance(n, ast.With))]
        code = compile(ast.fix_missing_locations(ast.Module(body=[loop, final], type_ignores=[])), '<production-loop>', 'exec')
        for succeeds in (True, False):
            with self.subTest(succeeds=succeeds):
                self.env.update(is_youtube_url=lambda *a: True, is_cookie_error=lambda *a: True,
                                is_youtube_cookie_error=lambda *a: True,
                                url='https://youtube.com/watch?v=xyz', info_dict=None, result=None,
                                stop_all=False, skip_item=False, network_error=False,
                                consecutive_no_videos_skips=0, _TERMINAL_ATTEMPT_RESULTS=set(),
                                _clear_net_errors=Mock(), download_stage='extract', did_cookie_retry=False,
                                error_message='', error_message_sent=False)
                self.env['message'].id = 1
                self.env['safe_send_message'] = Mock()
                self.env['ReplyParameters'] = lambda **kw: kw
                self.env['enums'] = types.SimpleNamespace(ParseMode=types.SimpleNamespace(HTML='html'))
                self.env['send_to_user'].reset_mock(); self.env['send_error_to_user'].reset_mock()
                self.error = "Sign in to confirm you're not a bot"
                self.env['yt_dlp'].utils.DownloadError = type('OtherDownloadError', (Exception,), {})
                calls = []
                def rotate(uid, url, callback, *args):
                    calls.append(self.env['did_cookie_retry'])
                    self.assertIsNone(callback(*args))  # live browser failed
                    if succeeds:
                        self.error = None
                    return callback(*args)  # source 6
                self.env['retry_download_with_different_cookies'] = rotate
                exec(code, self.env)
                self.assertEqual(calls, [True])
                if succeeds:
                    self.assertIsInstance(self.env['info_dict'], dict)
                    self.env['send_to_user'].assert_not_called()
                    self.env['send_error_to_user'].assert_not_called()
                    self.env['safe_send_message'].assert_not_called()
                else:
                    self.assertIsNone(self.env['info_dict'])
                    self.assertEqual(self.env['send_error_to_user'].call_count, 1)
                    self.assertTrue(self.env['error_message_sent'])

    def test_success(self):
        self.assertEqual(self.run_download()['id'],'xyz');self.assertEqual(self.downloads,1)
    def test_backoff(self):
        self.assertEqual([self.env['_retry_backoff_seconds'](n=i) for i in range(7)],[1,2,4,8,15,15,15])

class FilesystemTests(unittest.TestCase):
    def test_active_directory_survives_cleanup(self):
        import shutil
        env=dict(os=os,threading=threading,shutil=shutil,logger=Mock(),_ACTIVE_DOWNLOAD_DIRS={},_ACTIVE_DOWNLOAD_DIRS_LOCK=threading.Lock())
        functions('HELPERS/filesystem_hlp.py',['_download_dir_key','acquire_download_dir','release_download_dir','is_download_dir_in_use','is_directory_protected','cleanup_media_in_download_folder'],env)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'vid.mp4.part';p.write_bytes(b'x');os.utime(p,(0,0))
            self.assertEqual(env['acquire_download_dir'](d),0)
            self.assertEqual(env['acquire_download_dir'](d),1)
            env['cleanup_media_in_download_folder'](d);self.assertTrue(p.exists())
            env['release_download_dir'](d);self.assertTrue(env['is_directory_protected'](d))
            env['release_download_dir'](d);env['cleanup_media_in_download_folder'](d);self.assertFalse(p.exists())

if __name__=='__main__': unittest.main(verbosity=2)
