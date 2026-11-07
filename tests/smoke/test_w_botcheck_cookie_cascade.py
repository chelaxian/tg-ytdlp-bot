"""Smoke test: the YouTube bot-check must reach the cookie cascade (offline).

2026-11-07 live case: "Sign in to confirm you're not a bot" was classified PERMANENT
(since commit 0516767), should_abort_retries() returned True, and every
cookie-retry hook skipped the cascade - the user had to swap cookies by hand
(/cookie youtube). The bot-check is AUTH_REQUIRED now: still terminal for
format/proxy rotation, but the single cookie-cascade pass runs first.
Run: python tests/smoke/test_w_botcheck_cookie_cascade.py
"""
import ast
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

from HELPERS.ytdlp_errors import (  # noqa: E402
    classify_retryability, should_abort_retries, AUTH_REQUIRED, RATE_LIMITED, PERMANENT)

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


BOTCHECK = ("Failed to extract video information: ERROR: [youtube] Af6i6ChAVTw: "
            "Sign in to confirm you’re not a bot. This helps protect our community. "
            "Use --cookies-from-browser or --cookies for the authentication.")
RATE = ("ERROR: [youtube] X: Video unavailable. This content isn't available, try again "
        "later. The current session has been rate-limited by YouTube for up to an hour.")

# 1. classification: bot-check is AUTH_REQUIRED (cookie-fixable), not PERMANENT
check("bot-check -> AUTH_REQUIRED", classify_retryability(BOTCHECK) == AUTH_REQUIRED)
check("bot-check still aborts format/proxy rotation", should_abort_retries(BOTCHECK))
check("rate-limit stays RATE_LIMITED", classify_retryability(RATE) == RATE_LIMITED)
for text, cat in (("Private video. If the owner ... please sign in.", None),
                  ("page needs to be reloaded", PERMANENT),
                  ("This video is unavailable", PERMANENT)):
    with open(os.devnull, "w"):
        pass
check("challenge page stays PERMANENT", classify_retryability("page needs to be reloaded") == PERMANENT)
check("removed video stays PERMANENT", classify_retryability("Video unavailable. This content isn't available") == PERMANENT)
check("private video is not AUTH_REQUIRED", classify_retryability("Private video. If the owner of this video has granted you access, please sign in.") != AUTH_REQUIRED)


# 2. every cookie-retry hook lets AUTH_REQUIRED through despite should_abort_retries
def guard_pattern(path, err_expr):
    src = open(os.path.join(ROOT, path), encoding="utf-8").read()
    tree = ast.parse(src)
    found = 0
    for n in ast.walk(tree):
        if not isinstance(n, ast.If) or not isinstance(n.test, ast.BoolOp) or not isinstance(n.test.op, ast.And):
            continue
        def _has_auth(node):
            if isinstance(node, ast.Compare):
                f = getattr(node.left, "func", None)
                return getattr(f, "id", "") == "classify_retryability" and any(
                    getattr(c, "value", "") == AUTH_REQUIRED for c in node.comparators)
            if isinstance(node, ast.BoolOp):
                return any(_has_auth(v) for v in node.values)
            return False
        def _has_abort(node):
            if isinstance(node, ast.Call):
                return getattr(node.func, "id", "") == "should_abort_retries"
            if isinstance(node, ast.BoolOp):
                return any(_has_abort(v) for v in node.values)
            if isinstance(node, ast.UnaryOp):
                return _has_abort(node.operand)
            return False
        has_abort = any(_has_abort(v) for v in n.test.values)
        has_auth = any(_has_auth(v) for v in n.test.values)
        if has_abort and "is_age_restriction_error" not in ast.unparse(n.test):
            found += 1
            check(f"{path}: AUTH_REQUIRED guard next to should_abort_retries", has_auth)
    check(f"{path}: cookie hooks present", found > 0)


# hooks that must allow the cascade: down_and_up (2 places), down_and_audio, yt_dlp_hook (no abort check)
guard_pattern("DOWN_AND_UP/down_and_up.py", "error_message")
guard_pattern("DOWN_AND_UP/down_and_audio.py", "last_audio_error")

# yt_dlp_hook gates with _terminal_error_result(..., cookie_pass_done): an auth-required
# error (now including the bot-check) returns None = retryable, so the cookie pass runs
hook = open(os.path.join(ROOT, "DOWN_AND_UP/yt_dlp_hook.py"), encoding="utf-8").read()
check("yt_dlp_hook lets auth-required errors through to the cookie pass",
      "if not cookie_pass_done and is_auth_required(error_text)" in hook)
sys.path.insert(0, ROOT)
from HELPERS.ytdlp_errors import is_auth_required  # noqa: E402
check("bot-check counts as auth-required for the hook gate", is_auth_required(BOTCHECK))

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
