"""Offline integration tests for active-directory /clean and timedtext 429 unwind."""
import ast
import io
import os
import shutil
import sys
import tempfile
import threading
import types
import unittest
from pathlib import Path
from unittest.mock import MagicMock, Mock
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from HELPERS.cookie_file import validated_cookie_options

def module(name,**kw):
    m=types.ModuleType(name);m.__dict__.update(kw);sys.modules[name]=m;return m

def load_functions(rel,names,env):
    env.setdefault("validated_cookie_options", validated_cookie_options)
    tree=ast.parse((ROOT/rel).read_text(encoding='utf-8-sig'))
    fs=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name in names]
    exec(compile(ast.Module(body=fs,type_ignores=[]),str(rel),'exec'),env)
    return env

class CleanTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.env=dict(os=os,shutil=shutil,threading=threading,logger=Mock(),LoggerMsg=MagicMock(),get_logger_msg=MagicMock(),
                      _ACTIVE_DOWNLOAD_DIRS={},_ACTIVE_DOWNLOAD_DIRS_LOCK=threading.Lock())
        load_functions('HELPERS/filesystem_hlp.py',['_download_dir_key','acquire_download_dir','release_download_dir','is_download_dir_in_use','is_directory_protected'],self.env)
        self.names=['scan_and_remove_recursive_emoji','scan_and_remove_recursive_all','scan_and_remove_recursive']
        load_functions('URL_PARSERS/url_extractor.py',self.names,self.env)
    def test_all_clean_branches_preserve_active_tree(self):
        for name in self.names:
            with self.subTest(branch=name):
                root=Path(self.tmp.name)/name;active=root/'downloads'/'active';active.mkdir(parents=True)
                part=active/'vid.mp4.part';part.write_bytes(b'active')
                self.env['acquire_download_dir'](str(active))
                self.assertEqual(self.env[name](str(root)),[])
                self.assertEqual(part.read_bytes(),b'active')
                self.env['release_download_dir'](str(active))
                removed=self.env[name](str(root));self.assertTrue(removed);self.assertFalse(root.exists())
    def test_all_clean_branches_preserve_active_root_files(self):
        for name in self.names:
            with self.subTest(branch=name):
                root=Path(self.tmp.name)/name;root.mkdir();part=root/'vid.mp4.part';part.write_bytes(b'active')
                self.env['acquire_download_dir'](str(root))
                self.assertEqual(self.env[name](str(part)),[]);self.assertTrue(part.exists())
                self.env['release_download_dir'](str(root));self.env[name](str(part));self.assertFalse(part.exists())
    def test_callbacks_remain_safe(self):
        tree=ast.parse((ROOT/'URL_PARSERS/url_extractor.py').read_text(encoding='utf-8'))
        calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='safe_callback_answer']
        self.assertTrue(calls)

class SubtitleTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.fetches=[];self.instances=0;self.fail_at=1;self.blocked=False
        self.block=Mock(side_effect=self.set_blocked)
        module('HELPERS.subtitle_rate_limit',subtitles_rate_limited=lambda *a:self.blocked,block_subtitles=self.block)
        self.languages=Mock(return_value=['en','ru'])
        module('COMMANDS.subtitles_cmd',get_available_subs_languages=self.languages,lang_match=lambda l,keys:l if l in keys else None,
               get_user_subs_auto_mode=lambda *a:True,ensure_utf8_srt=lambda p:p)
        module('HELPERS.proxy_helper',add_proxy_to_ytdl_opts=lambda o,*a:o,build_proxy_url=lambda *a:'http://mock-proxy')
        module('HELPERS.pot_helper',add_pot_to_ytdl_opts=lambda o,*a:o)
        module('CONFIG.config',Config=MagicMock())
        outer=self
        class DownloadError(Exception):pass
        class YDL:
            def __init__(self,opts):outer.instances+=1
            def __enter__(self):return self
            def __exit__(self,*a):return False
            def extract_info(self,*a,**kw):
                return {'automatic_captions':{l:[{'ext':'srt','url':f'https://timedtext.test/{l}'}] for l in ['en','ru']}}
            def urlopen(self,url):
                outer.fetches.append(url)
                if len(outer.fetches)==outer.fail_at:raise DownloadError('HTTP Error 429: Too Many Requests')
                if outer.fail_at is not None:raise DownloadError('HTTP Error 503: unavailable')
                return io.BytesIO(b'1\n00:00:00,000 --> 00:00:01,000\ntext\n')
        module('yt_dlp',YoutubeDL=YDL,utils=types.SimpleNamespace(DownloadError=DownloadError))
        self.env=dict(os=os,logger=Mock())
        load_functions('DOWN_AND_UP/ffmpeg.py',['download_all_subtitles'],self.env)
    def set_blocked(self,*a):self.blocked=True
    def run_subs(self):return self.env['download_all_subtitles']('https://video.test/xyz',1,self.tmp.name,selected_langs=['en','ru'])
    def test_existing_cooldown_no_metadata_or_fetch(self):
        self.blocked=True;self.assertEqual(self.run_subs(),[])
        self.assertEqual(self.instances,0);self.languages.assert_not_called();self.assertEqual(self.fetches,[])
    def test_first_429_stops_formats_proxies_and_languages(self):
        self.assertEqual(self.run_subs(),[]);self.assertEqual(len(self.fetches),1);self.assertEqual(self.instances,1)
        self.block.assert_called_once_with('https://video.test/xyz',1)
        self.assertEqual(self.run_subs(),[]);self.assertEqual(len(self.fetches),1)
    def test_proxy1_429_unwinds_broad_handler(self):
        self.fail_at=6  # 5 attempts on initial route, then first proxy fetch
        self.assertEqual(self.run_subs(),[]);self.assertEqual(len(self.fetches),6);self.assertEqual(self.instances,2)
        self.block.assert_called_once()
    def test_proxy2_429_unwinds_broad_handler(self):
        self.fail_at=11  # 5 initial + 5 proxy1, then first proxy2 fetch
        self.assertEqual(self.run_subs(),[]);self.assertEqual(len(self.fetches),11);self.assertEqual(self.instances,3)
        self.block.assert_called_once()
    def test_success_returns_list(self):
        self.fail_at=None;result=self.run_subs();self.assertEqual([x['language'] for x in result],['en','ru'])
        self.assertEqual(len(self.fetches),2);self.block.assert_not_called()

if __name__=='__main__':unittest.main(verbosity=2)
