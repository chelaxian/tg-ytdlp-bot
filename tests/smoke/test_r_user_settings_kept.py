"""Smoke test: media cleanup keeps per-user settings (/proxy, /format, /split...).

The image pre-cleanup calls remove_media(message) with no `only`; it used to delete
users/<id>/proxy.txt, format.txt, args.txt... so every image download reset them.

Run from the bot root (needs the bot's venv): python tests/smoke/test_r_user_settings_kept.py
Optional: FS_HLP=/path/to/filesystem_hlp.py to test a file outside the package.
"""
import importlib.util
import os
import sys
import tempfile
from types import SimpleNamespace

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

path = os.environ.get("FS_HLP") or os.path.join(ROOT, "HELPERS", "filesystem_hlp.py")
spec = importlib.util.spec_from_file_location("fs_hlp_under_test", path)
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


SETTINGS = sorted(fs.USER_SETTINGS_FILES)
MEDIA = ["video.mp4", "pic.jpg", "available_qualities.txt", "ask_formats.json",
         "caption_description.txt", "dump.json"]

uid = 990000001
for parallel in (True, False):
    fs.is_parallel_download_allowed = lambda message, _p=parallel: _p
    fs.is_download_dir_in_use = lambda *a, **k: False
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            user_dir = os.path.join("users", str(uid))
            os.makedirs(user_dir)
            for name in SETTINGS + MEDIA:
                with open(os.path.join(user_dir, name), "w", encoding="utf-8") as f:
                    f.write("US" if name == "proxy.txt" else "x")
            message = SimpleNamespace(chat=SimpleNamespace(id=uid))
            fs.remove_media(message)
            left = set(os.listdir(user_dir))
            check(f"parallel={parallel}: all settings kept", set(SETTINGS) <= left)
            check(f"parallel={parallel}: media and caches removed", not (set(MEDIA) & left))
            fs.remove_media(message, only=["proxy.txt"])
            check(f"parallel={parallel}: /clean proxy still removes proxy.txt",
                  not os.path.exists(os.path.join(user_dir, "proxy.txt")))
        finally:
            os.chdir(cwd)

for name in ("proxy.txt", "format.txt", "format_prefs.json", "args.txt", "split.txt",
             "subs.txt", "nsfw_blur.txt", "lang.txt", "cookie.txt"):
    check(f"{name} is protected", name in fs.USER_SETTINGS_FILES)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
