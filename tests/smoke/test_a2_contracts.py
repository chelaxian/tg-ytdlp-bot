"""Additional offline source-contract tests: actual cascade AST and sender reasons."""
import ast
import threading
import sys
import types
import unittest
_errors=types.ModuleType('CONFIG.errors');_errors.is_geo_block_error=lambda *a:False
sys.modules['CONFIG.errors']=_errors
from pathlib import Path
from unittest.mock import Mock
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[2]

class Contracts(unittest.TestCase):
    def test_cascade_attempt_counts(self):
        tree=ast.parse((R/'DOWN_AND_UP/down_and_up.py').read_text(encoding='utf-8'))
        loop=next(n for n in ast.walk(tree) if isinstance(n,ast.For) and isinstance(n.target,ast.Tuple) and [x.id for x in n.target.elts if isinstance(x,ast.Name)]==['attempt_no','attempt'])
        classifier={};exec((R/'HELPERS/ytdlp_errors.py').read_text(encoding='utf-8'),classifier)
        terminal=('TERMINAL_ERROR','FORMAT_NOT_AVAILABLE','FFMPEG_ERROR','POSTPROCESSING_ERROR','LIVE_STREAM')
        for error,result,expected in [('Private video',None,1),('HTTP Error 429',None,1),('disk quota exceeded',None,1),('unknown extractor error',None,3),('', 'FFMPEG_ERROR',1),('', 'FORMAT_NOT_AVAILABLE',1),('', 'POSTPROCESSING_ERROR',1)]:
            with self.subTest(error=error,result=result):
                fn=Mock(return_value=result)
                e=dict(attempts=[{'format':str(i)} for i in range(3)],try_download=fn,url='test',is_youtube_url=lambda *a:False,
                       did_cookie_retry=False,error_message=error,should_abort_retries=classifier['should_abort_retries'],logger=Mock(),
                       current_index=1,_TERMINAL_ATTEMPT_RESULTS=terminal)
                exec(compile(ast.fix_missing_locations(ast.Module(body=[loop],type_ignores=[])),'cascade','exec'),e)
                self.assertEqual(fn.call_count,expected)
    def test_sender_reason_is_thread_local(self):
        tree=ast.parse((R/'DOWN_AND_UP/sender.py').read_text(encoding='utf-8'))
        f=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('_send_failed','get_last_send_failure')]
        e=dict(_send_failure=threading.local(),logger=Mock())
        exec(compile(ast.Module(body=f,type_ignores=[]),'sender','exec'),e)
        self.assertIsNone(e['_send_failed']('file_vanished_before_upload'))
        self.assertEqual(e['get_last_send_failure'](),'file_vanished_before_upload')
        other=[];t=threading.Thread(target=lambda:other.append(e['get_last_send_failure']()));t.start();t.join()
        self.assertEqual(other,[None])
    def test_no_unreasoned_sender_none_returns(self):
        tree=ast.parse((R/'DOWN_AND_UP/sender.py').read_text(encoding='utf-8'))
        send=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='send_videos')
        # Nested thumbnail helpers legitimately return None; top-level send paths do not.
        class Returns(ast.NodeVisitor):
            def __init__(self):self.bad=[]
            def visit_FunctionDef(self,n):pass
            def visit_Return(self,n):
                if n.value is None or isinstance(n.value,ast.Constant) and n.value.value is None:self.bad.append(n.lineno)
        visitor=Returns()
        for n in send.body:visitor.visit(n)
        self.assertEqual(visitor.bad,[])
if __name__=='__main__':unittest.main(verbosity=2)
