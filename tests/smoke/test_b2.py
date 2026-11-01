"""Isolated smoke tests for B2 fixes (#486, #473, #472, #480). No network, no pyrogram.

Functions are extracted from the repo sources via AST and executed with mocks.
Run: python -I test_b2.py <repo_root>
"""
import ast
import html
import os
import re
import sys
import tempfile
import types

REPO = sys.argv[1]


def load_defs(rel_path, names, extra_globals):
    src = open(os.path.join(REPO, rel_path), encoding="utf-8-sig").read()
    tree = ast.parse(src)
    picked = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names:
            picked.append(node)
        elif isinstance(node, ast.Assign):
            targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if any(t in names for t in targets):
                picked.append(node)
    found = {getattr(n, "name", None) or n.targets[0].id for n in picked}
    missing = set(names) - found
    assert not missing, f"missing in {rel_path}: {missing}"
    mod = ast.Module(body=picked, type_ignores=[])
    g = dict(extra_globals)
    exec(compile(mod, rel_path, "exec"), g)
    return g


failures = 0


def check(cond, label):
    global failures
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        failures += 1


# ---------------- gallery_dl_hook classifier ----------------
class _Msgs:
    GALLERY_DL_AUTH_ERROR_MSG = "Authentication Error"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Unknown Error"


gdl_names = [
    "GDL_FAILURE_TWITTER_UNAVAILABLE", "GDL_FAILURE_UNSPLASH_BLOCKED", "GDL_FAILURE_NOT_FOUND",
    "GDL_FAILURE_RATE_LIMITED", "_TWITTER_REASON_RE", "_TWITTER_PERMANENT_REASONS",
    "_NOT_FOUND_MARKERS", "_RATE_LIMIT_MARKERS", "classify_gallery_dl_failure", "_is_fatal_error",
]
G = load_defs("DOWN_AND_UP/gallery_dl_hook.py", gdl_names, {"re": re})
classify = G["classify_gallery_dl_failure"]
is_fatal = G["_is_fatal_error"]

cases = [
    ("[twitter][error] 'Unavailable'", "twitter_unavailable"),
    ("[twitter][error] Tweet unavailable ('Suspended')", "twitter_unavailable"),
    ("[twitter][error] 'Protected'", None),  # cookies may help -> auth path
    ("[twitter][error] 'NsfwLoggedOut'", None),
    ("[unsplash][error] HttpError: '401 Unauthorized' for 'https://unsplash.com/napi/photos/x'", "unsplash_blocked"),
    ("[pinterest][error] NotFoundError: Requested pin could not be found", "not_found"),
    ("[foo][error] HttpError: '404 Not Found' for 'https://example.com/x'", "not_found"),
    ("[twitter][error] 429 Too Many Requests (Rate limit exceeded)", "rate_limited"),
    ("[instagram][error] HttpError: '401 Unauthorized'", None),
    ("", None),
]
for text, expected in cases:
    check(classify(text) == expected, f"classify({text[:60]!r}) == {expected!r} (got {classify(text)!r})")

check(is_fatal("[twitter][error] 'Unavailable'"), "twitter Unavailable is fatal (no retries)")
check(is_fatal("[somesite][error] HttpError: '404 Not Found' for 'x'"), "generic 404 on non-listed site is now fatal")
check(is_fatal("[unsplash][error] HttpError: '401 Unauthorized'"), "unsplash 401 fatal")
check(not is_fatal("[generic][warning] something transient"), "plain warning not fatal")

# ---------------- image_cmd: photo validator ----------------
from PIL import Image

img_names = [
    "TG_PHOTO_MAX_BYTES", "TG_PHOTO_MAX_DIMENSIONS_SUM", "TG_PHOTO_MAX_ASPECT_RATIO", "TG_PHOTO_FORMATS",
    "TG_INVALID_PHOTO_ERROR_IDS", "_photo_send_problem", "_is_invalid_photo_rpc_error",
    "_send_files_as_documents", "_report_gallery_dl_fatal_error",
]


class Logger:
    def __init__(self):
        self.lines = []

    def __getattr__(self, name):
        return lambda msg, *a, **k: self.lines.append((name, msg))


calls = {"edit": [], "send": [], "channel": [], "docs": []}


class FakeMsgs(_Msgs):
    IMG_TWITTER_UNAVAILABLE_MSG = "TW {url}"
    IMG_UNSPLASH_BLOCKED_MSG = "UNS {url}"
    IMG_CONTENT_NOT_FOUND_MSG = "NF {url}"
    IMG_RATE_LIMITED_MSG = "RL {url}"
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "IG {error_type} {url} {error_details}"
    SAVE_AS_COOKIE_HINT = "COOKIE"


class LoggerMsg:
    IMG_FATAL_ERROR_DETECTED_LOG_MSG = "fatal {result}"


class App:
    def send_document(self, user_id, document, caption=None, reply_parameters=None, message_thread_id=None):
        calls["docs"].append((document, caption))
        return types.SimpleNamespace(id=len(calls["docs"]))


fake_globals = {
    "os": os, "html": html, "PILImage": Image, "logger": Logger(),
    "LoggerMsg": LoggerMsg,
    "safe_get_messages": lambda uid: FakeMsgs,
    "classify_gallery_dl_failure": classify,
    "GDL_FAILURE_TWITTER_UNAVAILABLE": "twitter_unavailable",
    "GDL_FAILURE_UNSPLASH_BLOCKED": "unsplash_blocked",
    "GDL_FAILURE_NOT_FOUND": "not_found",
    "GDL_FAILURE_RATE_LIMITED": "rate_limited",
    "safe_edit_message_text": lambda chat, mid, text, **k: calls["edit"].append(text),
    "safe_send_message": lambda uid, text, **k: calls["send"].append(text),
    "log_error_to_channel": lambda m, text, url: calls["channel"].append(text),
    "is_cookie_error": lambda t: "[twitter][error]" in t or "401" in t,
    "enums": types.SimpleNamespace(ParseMode=types.SimpleNamespace(HTML="html")),
    "ReplyParameters": lambda message_id=None: message_id,
    "get_reply_message_id": lambda m: 1,
    "timed_upload": lambda fn: fn(),
}
I = load_defs("COMMANDS/image_cmd.py", img_names, fake_globals)
problem = I["_photo_send_problem"]

tmp = tempfile.mkdtemp(prefix="b2_")


def mk(name, size, fmt="JPEG"):
    p = os.path.join(tmp, name)
    Image.new("RGB", size, (120, 30, 200)).save(p, fmt)
    return p


ok_jpg = mk("ok.jpg", (800, 600))
check(problem(ok_jpg) is None, "normal 800x600 JPEG accepted as photo")
check(problem(mk("ok.png", (1000, 1000), "PNG")) is None, "PNG accepted")
check("aspect ratio" in (problem(mk("strip.png", (4200, 200), "PNG")) or ""), "21:1 strip rejected (ratio > 20)")
check("width+height" in (problem(mk("huge.png", (6000, 4500), "PNG")) or ""), "6000x4500 rejected (w+h > 10000)")
empty = os.path.join(tmp, "empty.jpg"); open(empty, "wb").close()
check(problem(empty) == "empty file", "zero-byte file rejected")
fake = os.path.join(tmp, "fake.jpg"); open(fake, "wb").write(b"<html>not an image</html>")
check("not a valid image" in (problem(fake) or ""), "HTML saved as .jpg rejected")
big = os.path.join(tmp, "big.jpg")
with open(big, "wb") as f:
    f.write(open(ok_jpg, "rb").read())
    f.write(os.urandom(11 * 1024 * 1024))
check("size" in (problem(big) or ""), ">10 MB file rejected")
check(problem(mk("bmp.bmp", (100, 100), "BMP")) is not None, "unconverted BMP rejected (format)")
check(problem(os.path.join(tmp, "missing.jpg")).startswith("unreadable"), "missing file reported, no exception")

# Pillow-less degradation
I_nopil = load_defs("COMMANDS/image_cmd.py", img_names, dict(fake_globals, PILImage=None))
check(I_nopil["_photo_send_problem"](fake) is None, "without Pillow only size checks apply")


# RPC error detection
class FakeRpc(Exception):
    def __init__(self, ID, text):
        super().__init__(text)
        self.ID = ID


is_bad_photo = I["_is_invalid_photo_rpc_error"]
check(is_bad_photo(FakeRpc("PHOTO_SAVE_FILE_INVALID", "Telegram says: [400 PHOTO_SAVE_FILE_INVALID]")), "PHOTO_SAVE_FILE_INVALID detected")
check(is_bad_photo(FakeRpc("PHOTO_INVALID_DIMENSIONS", "x")), "PHOTO_INVALID_DIMENSIONS detected")
check(not is_bad_photo(FakeRpc("PEER_ID_INVALID", "Telegram says: [400 PEER_ID_INVALID]")), "PEER_ID_INVALID not treated as photo error")

# Document fallback
sent = I["_send_files_as_documents"](App(), 42, object(), [ok_jpg, os.path.join(tmp, "gone.jpg"), fake], caption="CAP", message_thread_id=None)
check(len(sent) == 2 and calls["docs"][0] == (ok_jpg, "CAP") and calls["docs"][1] == (fake, None),
      "document fallback: caption only on first, vanished file skipped")

# ---------------- fatal error reporting ----------------
report = I["_report_gallery_dl_fatal_error"]
status = types.SimpleNamespace(chat=types.SimpleNamespace(id=1), id=2)
msg = types.SimpleNamespace(id=3)


def run_report(result):
    for k in ("edit", "send", "channel"):
        calls[k].clear()
    report(msg, 42, "https://x.com/a/status/1?a=1&b=2", status, result)
    return dict((k, list(v)) for k, v in calls.items())


r = run_report("Unknown Error: [twitter][error] 'Unavailable'")
check(r["edit"] == ["TW https://x.com/a/status/1?a=1&amp;b=2"], "#486 twitter Unavailable -> friendly message, URL escaped")
check(r["channel"] == [] and r["send"] == [], "#486 no LOG_EXCEPTION noise and no separate cookie hint")

r = run_report("Ошибка аутентификации: [unsplash][error] HttpError: '401 Unauthorized'")
check(r["edit"][0].startswith("UNS"), "#473 unsplash 401 (localized label) -> clear message")
check(len(r["channel"]) == 1 and r["send"] == [], "#473 still logged to channel, no cookie hint")

r = run_report("Rate Limit Exceeded: [twitter][error] 429 Too Many Requests")
check(r["edit"][0].startswith("RL") and len(r["channel"]) == 1, "rate limit -> 'try later', logged (transient)")

r = run_report("Authentication Error: [foo][error] HttpError: '401 Unauthorized' <b>")
check("&lt;b&gt;" in r["edit"][0] and r["send"] == ["COOKIE"], "generic error: details HTML-escaped, cookie hint kept")

r = run_report("Unknown Error: [pinterest][error] NotFoundError: Requested pin could not be found")
check(r["edit"][0].startswith("NF") and r["channel"] == [], "#480 pinterest missing pin -> 'not found', no channel noise")

print(f"\n{'ALL PASSED' if not failures else str(failures) + ' FAILED'}")
sys.exit(1 if failures else 0)
