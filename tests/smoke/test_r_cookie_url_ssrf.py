"""Smoke test: cookie downloads pass the SSRF check (regression of 2026-11-04).

The dashboard rewrite dropped `allowed_urls` from services.lists_service._validate_url_for_ssrf,
while COMMANDS/cookies_cmd._download_content still passes it: every cookie download
(/cookie buttons, YouTube cookie rotation, service cookie fallback) failed with
"unexpected keyword argument 'allowed_urls'" before any request was made.

Run: python tests/smoke/test_r_cookie_url_ssrf.py   (offline, no pyrogram needed)
"""
import ast
import inspect
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

try:
    import CONFIG.config  # noqa: F401
except ModuleNotFoundError:  # dev checkout without the secret config: a stub is enough here
    import types
    _stub = types.ModuleType("CONFIG.config")
    _stub.Config = type("Config", (), {})
    sys.modules["CONFIG.config"] = _stub

from services.lists_service import _validate_url_for_ssrf  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


# 1. every keyword cookies_cmd.py passes exists in the validator signature
params = set(inspect.signature(_validate_url_for_ssrf).parameters)
with open(os.path.join(ROOT, "COMMANDS", "cookies_cmd.py"), encoding="utf-8") as fh:
    tree = ast.parse(fh.read())
calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)
         and getattr(n.func, "id", getattr(n.func, "attr", None)) == "_validate_url_for_ssrf"]
check("cookies_cmd calls the validator", bool(calls))
used = {kw.arg for c in calls for kw in c.keywords}
check(f"keywords {sorted(used)} accepted by the validator", used <= params)

# 2. trusted exact URL (local cookie webserver) passes; the rest of localhost stays blocked
trusted = frozenset({"http://localhost:8080/cookies/youtube_1.txt"})
check("trusted exact URL allowed", _validate_url_for_ssrf("http://localhost:8080/cookies/youtube_1.txt",
                                                          allowed_urls=trusted) == (True, ""))
check("other localhost path blocked", not _validate_url_for_ssrf("http://localhost:8080/admin",
                                                                 allowed_urls=trusted)[0])
check("loopback IP blocked", not _validate_url_for_ssrf("http://127.0.0.1/x.txt", allowed_urls=trusted)[0])
check("private IP blocked", not _validate_url_for_ssrf("http://10.0.0.1/x.txt")[0])
check("non-http scheme blocked", not _validate_url_for_ssrf("file:///etc/passwd", allowed_urls=trusted)[0])
check("old call form (no allowed_urls) still works", not _validate_url_for_ssrf("http://localhost/x")[0])

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
