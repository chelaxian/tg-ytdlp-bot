"""Run actual terminal-error and fallback message AST blocks offline."""
exec(open(__file__.replace('test_b1_menu_paths.py','test_b1.py'),encoding='utf-8').read().replace('sys.exit(1 if failures else 0)', 'assert not failures'))
import copy
sent=[]
ns.update({'send_error_to_user':lambda msg,text:sent.append(text), 'safe_send_message':lambda *a,**kw:None,
           'message':types.SimpleNamespace(id=11), 'user_id':88, 'url':'https://example.com/video',
           'ReplyParameters':ptypes.ReplyParameters, 'enums':pyrogram.enums})
# Avoid loading platform clients: playlist URL predicate is mocked.
pl=types.ModuleType('URL_PARSERS.playlist_utils');pl.is_playlist_url=lambda u:False
sys.modules['URL_PARSERS.playlist_utils']=pl
branch=next(n for n in ast.walk(tree) if isinstance(n,ast.If) and "'UNSUPPORTED_URL', 'PERMANENT_UNAVAILABLE', 'RATE_LIMITED'" in ast.unparse(n.test))
fn=ast.FunctionDef(name='terminal',args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=[copy.deepcopy(branch)],decorator_list=[])
exec(compile(ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[])),'terminal','exec'),ns)
for err,key in cases.items():
    ns['info']={'error':'PERMANENT_UNAVAILABLE','original_error':err}
    sent.clear();ns['terminal']()
    assert getattr(EN,key) in sent[0],(key,sent)
print('PASS actual PERMANENT_UNAVAILABLE branch: 11 categories')
ns['_RECENT_EXTRACT_FAILS'].clear()
for _ in range(3):ns['terminal']()
assert ns['_check_extract_cooldown'](88,ns['url'])>0
print('PASS actual terminal branch records all 3 failures')
# Compile the actual friendly fallback composition, not a replica.
start=src.index('                logger.info(f"Gallery-dl recommendation')
end=src.index('                # Create inline keyboard with gallery-dl option',start)
import textwrap
code=textwrap.dedent(src[start:end])
ns.update(original_error='ERROR: [Pinterest] 123: No video formats found!',range_info='',range_examples='')
exec(compile(code,'fallback','exec'),ns)
assert EN.ALWAYS_ASK_PINTEREST_NO_VIDEO_MSG in ns['fallback_message']
assert 'ERROR:' not in ns['fallback_message']
print('PASS actual Pinterest fallback: friendly text, no raw error')
ns['original_error']='ERROR: [facebook] 3: Cannot parse data; please report this issue'
exec(compile(code,'fallback','exec'),ns)
assert EN.ALWAYS_ASK_EXTRACTOR_ERROR_MSG in ns['fallback_message']
assert 'Cannot parse data' not in ns['fallback_message']
print('PASS actual Facebook fallback: classified text, no raw error')
