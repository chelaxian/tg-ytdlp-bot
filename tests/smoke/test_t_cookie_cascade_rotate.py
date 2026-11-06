"""Smoke test: the YouTube cookie cascade rotates the WARP egress before every source.

Offline: cookies_cmd.py pulls in Pyrogram, so the helper and the loop are checked by AST.
Run: python tests/smoke/test_t_cookie_cascade_rotate.py
"""
import ast
import logging
import os
import sys
import types

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(ROOT, "COMMANDS", "cookies_cmd.py")

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


with open(SRC, encoding="utf-8") as fh:
    tree = ast.parse(fh.read())
funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}

# 1. loop in retry_download_with_different_cookies: rotate comes before the cookie download
retry = funcs["retry_download_with_different_cookies"]
loops = [n for n in ast.walk(retry) if isinstance(n, ast.For)
         and isinstance(n.target, ast.Tuple) and len(n.target.elts) == 2]
check("cascade loop found", len(loops) == 1)
body_calls = []
for node in ast.walk(loops[0]):
    if isinstance(node, ast.Call):
        name = getattr(node.func, "id", getattr(node.func, "attr", None))
        body_calls.append((node.lineno, name))
rot = [ln for ln, n in body_calls if n == "_rotate_warp_egress"]
dl = [ln for ln, n in body_calls if n == "_download_content"]
check("rotate called once inside the loop", len(rot) == 1)
check("rotate precedes the cookie download", rot and dl and rot[0] < min(dl))

# 2. the helper: calls rotate_current_task, never raises
src = ast.get_source_segment(open(SRC, encoding="utf-8").read(), funcs["_rotate_warp_egress"])
calls = []


def make_ns(rotate):
    mod = types.ModuleType("HELPERS.warp_tunnel")
    mod.rotate_current_task = rotate
    sys.modules["HELPERS.warp_tunnel"] = mod
    ns = {"logger": logging.getLogger("t")}
    exec(src, ns)
    return ns["_rotate_warp_egress"]


helper = make_ns(lambda: calls.append(1) or "2a09::1")
helper("cookie source 2")
check("helper calls rotate_current_task", calls == [1])

def boom():
    raise RuntimeError("tunnel gone")

try:
    make_ns(boom)("cookie source 3")
    check("helper swallows rotate errors", True)
except Exception:
    check("helper swallows rotate errors", False)

make_ns(lambda: None)("no WARP / no scope")
check("helper is a no-op when rotate returns None", True)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
