"""Smoke test: /img audit fixes in DOWN_AND_UP/gallery_dl_hook.py.

1. _mask_config_for_log redacts proxy/cookies/headers (no credentials in journal).
2. reset_gallery_dl_config restores the pristine snapshot after mutation,
   and _apply_config wipes a previous user's cookies/proxy/range (no leak).

Run: python tests/smoke/test_r_img_audit.py   (needs gallery_dl importable)
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


from DOWN_AND_UP import gallery_dl_hook as gdl  # noqa: E402
import gallery_dl  # noqa: E402

# ---- 1. masking ----
cfg = {
    "extractor": {
        "timeout": 30,
        "retries": 3,
        "proxy": "socks5://user:SECRETPW@1.2.3.4:1080",
        "cookies": "users/123/cookie.txt",
        "headers": {"Authorization": "Bearer SECRET.JWT.TOKEN"},
        "image-range": "11-20",
    },
    "output": {"directory": ["users/123/run"]},
}
masked = gdl._mask_config_for_log(cfg)
text = str(masked)
check("proxy redacted", "SECRETPW" not in text and masked["extractor"]["proxy"] == "<redacted>")
check("cookies redacted", "cookie.txt" not in text and masked["extractor"]["cookies"] == "<redacted>")
check("headers redacted", "Bearer" not in text and masked["extractor"]["headers"] == "<redacted>")
check("plain values kept", masked["extractor"]["timeout"] == 30 and masked["output"]["directory"] == ["users/123/run"])
check("original untouched", "SECRETPW" in cfg["extractor"]["proxy"])

# ---- 2. config reset / leak ----
cfg_table = gallery_dl.config._config  # private dict that set/unset/clear mutate
gdl.reset_gallery_dl_config()
snapshot = dict(cfg_table)

# simulate user A with cookies + proxy + range
def _set(key, value):
    gallery_dl.config.set(key[:-1], key[-1], value)

_set(("extractor", "cookies"), "users/A/cookie.txt")
_set(("extractor", "proxy"), "socks5://u:p@1.2.3.4:1080")
_set(("extractor", "image-range"), "1-10")
gdl.reset_gallery_dl_config()
after = dict(cfg_table)
check("reset drops stale cookies", after.get("extractor", {}).get("cookies") is None)
check("reset drops stale proxy", after.get("extractor", {}).get("proxy") is None)
check("reset drops stale range", after.get("extractor", {}).get("image-range") is None)
check("reset equals snapshot", after == snapshot)

# _apply_config must also clear whatever a previous call left
gdl._apply_config({"extractor": {"timeout": 5}, "output": {"mode": "info"}})
check("apply clears previous keys",
      cfg_table.get("extractor", {}).get("cookies") is None
      and cfg_table.get("extractor", {}).get("timeout") == 5)
gdl.reset_gallery_dl_config()
check("config restored after apply", dict(cfg_table) == snapshot)

# lock exists and is reentrant
check("lock is reentrant", gdl._GDL_LOCK.acquire() and gdl._GDL_LOCK.release() is None and gdl._GDL_LOCK.acquire() and gdl._GDL_LOCK.release() is None)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
