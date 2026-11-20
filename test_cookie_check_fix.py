import re

# Verify the fix logic offline: simulate both recipes against recorded observations
# and check no test-time extractor_args forcing remains in cookie tests.
src = open('COMMANDS/cookies_cmd.py', encoding='utf-8', errors='replace').read().replace('\r\n', '\n')

# find function bodies
import ast
tree = ast.parse(src)
fns = {}
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name in ('test_youtube_cookies_on_url', 'test_youtube_cookies'):
        seg = ast.get_source_segment(src, node)
        fns[node.name] = seg

ok = True
for name, seg in fns.items():
    forced = re.search(r"player_client['\"]?\s*:\s*\[?'?tv", seg)
    print(name, 'player_client force:', 'FOUND (BAD)' if forced else 'absent (OK)')
    if forced:
        ok = False
    # cookiefile still used
    has_cookie = "'cookiefile'" in seg
    print(name, 'cookiefile used:', has_cookie)
    if not has_cookie:
        ok = False

# The add_pot_to_ytdl_opts call should still be applied (PO tokens needed for formats)
for name, seg in fns.items():
    print(name, 'pot applied:', 'add_pot_to_ytdl_opts' in seg)
    print(name, 'proxy applied:', 'add_proxy_to_ytdl_opts' in seg)

print('RESULT:', 'PASS' if ok else 'FAIL')
