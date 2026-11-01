"""Additional offline tests of real C helper code (AST-isolated heavy modules)."""
import ast
import os
import sys
import types
import threading
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

def extract(name, wanted, env):
    tree = ast.parse((ROOT / name).read_text(encoding='utf-8'))
    nodes = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in wanted]
    exec(compile(ast.Module(body=nodes, type_ignores=[]), name, 'exec'), env)
    return env

# #386: no duplicate final no-cookie request; opts/outer thread-local restored.
env = dict(os=os, threading=threading, logger=Mock(),
           _non_youtube_fallback_active=set(), cleanup_expired_tasks=Mock(),
           start_cookie_task=Mock(return_value='task'), finish_cookie_task=Mock(),
           get_service_name_from_url=lambda url: None,
           ensure_valid_cookie_file=lambda path: None,
           Config=types.SimpleNamespace(COOKIE_FILE_PATH='missing'))
# Only CONFIG.limits is imported inside this function (no Pyrogram/network).
extract('COMMANDS/cookies_cmd.py', {'try_non_youtube_cookie_fallback'}, env)
f=env['try_non_youtube_cookie_fallback']
opts={'cookiefile':None}
operation=Mock(return_value=None)
f(1,'https://example.test/item',operation,opts)
assert operation.call_count == 0, 'duplicate no-cookie attempt ran'
assert opts == {'cookiefile':None}
opts={'cookiefile':'old-cookie'}
threading.current_thread().cookiefile_override='outer'
with patch.object(os.path,'exists',return_value=False):
    f(1,'https://example.test/item',operation,opts)
assert operation.call_count == 1, 'new no-cookie strategy must run when original used cookies'
assert opts == {'cookiefile':'old-cookie'}
assert threading.current_thread().cookiefile_override == 'outer'
del threading.current_thread().cookiefile_override
print('PASS #386 no-cookie dedup and thread-local/opts restoration')

# #316: LocalDBAdapter children share a lock; failed serialization keeps file.
from typing import Dict, Any, List
import json, time
from HELPERS.atomic_io import atomic_write_json
from HELPERS.cookie_file import validate_cookie_bytes
assert not validate_cookie_bytes(b'# Netscape HTTP Cookie File\n.x\tTRUE\t/\tTRUE\t0\ta\tb\nbroken tail')[0]
env=dict(os=os,json=json,time=time,threading=threading,Dict=Dict,Any=Any,List=List,
         logger=Mock(), _local_file_locks={}, _local_file_locks_guard=threading.Lock(),
         _SnapshotCompat=lambda value: value)
extract('DATABASE/firebase_init.py', {'_local_file_lock','LocalDBAdapter'},env)
with tempfile.TemporaryDirectory(prefix='c-local-db-') as temp:
    path=os.path.join(temp,'dump.json')
    root=env['LocalDBAdapter'](path)
    children=[root.child(str(i)) for i in range(10)]
    assert all(child._lock is root._lock for child in children)
    threads=[threading.Thread(target=child.set,args=({'ok':True},)) for child in children]
    for t in threads: t.start()
    for t in threads: t.join()
    assert len(json.loads(Path(path).read_text())) == 10
    before=Path(path).read_bytes()
    try: root.child('bad').set(object())
    except TypeError: pass
    else: raise AssertionError('expected TypeError')
    assert Path(path).read_bytes() == before
print('PASS #316 concurrent LocalDBAdapter child writes and serialization failure')

# #460: cross-process dashboard fails closed, no filesystem mutations.
env=dict(Dict=Dict,Any=Any)
extract('services/system_service.py', {'cleanup_user_files'},env)
assert env['cleanup_user_files']()['status']=='error'
print('PASS #460 dashboard refuses destructive cross-process cleanup')
print('ALL EXTRA TESTS PASSED (offline)')
