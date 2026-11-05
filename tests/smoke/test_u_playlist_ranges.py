"""Smoke test: playlist ranges (forward / reverse / from the end), /vid & /audio range
syntax and covers taken from yt-dlp metadata.

Pure helpers run anywhere (logger is stubbed when the bot config is missing).
The parts that need the real bot modules (URL_PARSERS.tags, HELPERS.limitter,
ffmpeg) run when they import, i.e. in the bot's venv on a server.
Run: python tests/smoke/test_u_playlist_ranges.py
"""
import http.server
import os
import socket
import sys
import tempfile
import threading
import types

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

try:
    import HELPERS.logger  # noqa: F401
    FULL = True
except Exception:  # no CONFIG/config.py here: stub the logger only
    FULL = False
    import logging
    m = types.ModuleType("HELPERS.logger")
    m.logger = logging.getLogger("t")
    sys.modules["HELPERS.logger"] = m

from URL_PARSERS import playlist_utils as pu  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


# ---- counting: one formula for every direction (old code: *-1*-100 -> -98, *-5*-1 -> -3)
for (a, b), n in {(1, 5): 5, (5, 1): 5, (-1, -5): 5, (-5, -1): 5, (3, 3): 1, (-1, -100): 100}.items():
    check(f"range_count({a},{b}) == {n}", pu.range_count(a, b) == n)

check("indices forward", pu.range_indices(1, 5) == [1, 2, 3, 4, 5])
check("indices reverse", pu.range_indices(5, 1) == [5, 4, 3, 2, 1])
check("indices from end, last first", pu.range_indices(-1, -3) == [-1, -2, -3])
check("indices from end, ascending", pu.range_indices(-3, -1) == [-3, -2, -1])

# ---- resolving from-the-end indices keeps the user's order (old code always sorted desc)
check("resolve -1..-3 of 20", pu.resolve_negative_indices([-1, -2, -3], 20) == [20, 19, 18])
check("resolve -3..-1 of 20 keeps order", pu.resolve_negative_indices([-3, -2, -1], 20) == [18, 19, 20])
check("resolve drops beyond start", pu.resolve_negative_indices([-4, -5, -6], 5) == [2, 1])

# ---- playlist length: asks for the LAST item once, cached for menu + download
calls = []


def fake_get_video_formats(url, user_id=None, start=1, checked=False, proxy=False, end=None):
    calls.append((url, start, end))
    # what yt-dlp returns for playlist_items='-1' on a 20-item playlist
    return {"id": "v20", "playlist_index": 20, "playlist_count": 20}


hook = types.ModuleType("DOWN_AND_UP.yt_dlp_hook")
hook.get_video_formats = fake_get_video_formats
sys.modules["DOWN_AND_UP.yt_dlp_hook"] = hook
pu._TOTAL_CACHE.clear()
idx = pu.playlist_indices_for_range(-1, -5, "https://www.youtube.com/playlist?list=PLx", 1)
check("*-1*-5 -> last five, last first", idx == [20, 19, 18, 17, 16])
idx2 = pu.playlist_indices_for_range(-5, -1, "https://www.youtube.com/playlist?list=PLx", 1)
check("*-5*-1 -> last five, ascending", idx2 == [16, 17, 18, 19, 20])
check("length looked up once, with item -1", calls == [("https://www.youtube.com/playlist?list=PLx", -1, None)])
check("positive range needs no lookup",
      pu.playlist_indices_for_range(3, 1, "https://x/playlist?list=PLy", 1) == [3, 2, 1] and len(calls) == 1)

# old behaviour for reference: item 1 -> len(entries)==1 -> *-1*-3 became [1, 0, -1]
hook.get_video_formats = lambda *a, **k: {"error": "PERMANENT_UNAVAILABLE"}
pu._TOTAL_CACHE.clear()
check("unknown length keeps negatives for yt-dlp",
      pu.playlist_indices_for_range(-1, -3, "https://x/p?list=PLz", 1) == [-1, -2, -3])

# ---- /vid and /audio range words -> URL*a*b, tags stay outside the range
U = "https://www.youtube.com/playlist?list=PL1"
cases = {
    ("3-7", U): f"{U}*3*7",
    ("3-7", U, "#music", "#rock"): f"{U}*3*7 #music #rock",   # old: 'URL #music #rock*3*7'
    ("-3-7", U): f"{U}*-3*-7",
    ("-3--7", U): f"{U}*-3*-7",                              # old: not recognised at all
    ("7-3", U): f"{U}*7*3",
    ("5-", U): f"{U}*5*54",                                   # old: 'URL*5*' -> playlist name '5'
    ("-1-", U): f"{U}*-1*-50",
}
for args, want in cases.items():
    got = pu.command_args_to_range_text(list(args), 50)
    check(f"command range {args[0]!r} {args[2:]}", got == want)
    if got != want:
        print("   got:", got)
check("not a range -> None", pu.command_args_to_range_text([U, "#tag"], 50) is None)
check("0 start -> None", pu.command_args_to_range_text(["0-5", U], 50) is None)
check("mixed sign 3--5 -> None", pu.command_args_to_range_text(["3--5", U], 50) is None)

# ---- covers from yt-dlp metadata
from URL_PARSERS import thumbnail_downloader as td  # noqa: E402

info = {"thumbnail": "https://cdn.example/a.jpg",
        "thumbnails": [{"url": "https://cdn.example/small.jpg"}, {"url": "https://cdn.example/big.jpg"},
                       {"url": "https://cdn.example/a.jpg"}]}
check("thumbnail urls best first, no dupes",
      td._info_thumbnail_urls(info) == ["https://cdn.example/a.jpg", "https://cdn.example/big.jpg",
                                        "https://cdn.example/small.jpg"])
check("no thumbnails -> []", td._info_thumbnail_urls({}) == [] and td._info_thumbnail_urls(None) == [])

JPEG = b"\xff\xd8\xff\xe0" + b"\x00" * 2000
REDIRECT_TO = {}


class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path == "/redir":
            self.send_response(302)
            self.send_header("Location", REDIRECT_TO["url"])
            self.end_headers()
            return
        if self.path == "/big":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"\xff\xd8\xff" + b"\x00" * (6 * 1024 * 1024))
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(JPEG)


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{srv.server_address[1]}"
tmp = tempfile.mkdtemp()
dest = os.path.join(tmp, "t.jpg")

check("localhost cover URL is refused (SSRF)", td.download_thumbnail_from_info({"thumbnail": base + "/a.jpg"}, dest) is False
      and not os.path.exists(dest))

real_validate = td._validate_url_for_ssrf
td._validate_url_for_ssrf = lambda u: (True, "") if u.startswith(base) else real_validate(u)
check("metadata cover downloaded", td.download_thumbnail_from_info({"thumbnail": base + "/a.jpg"}, dest) is True
      and open(dest, "rb").read(3) == b"\xff\xd8\xff")
os.remove(dest)
check("oversized cover rejected", td.download_thumbnail_from_info({"thumbnail": base + "/big"}, dest) is False)
REDIRECT_TO["url"] = "http://169.254.169.254/latest/meta-data"
check("redirect to metadata IP refused", td.download_thumbnail_from_info({"thumbnail": base + "/redir"}, dest) is False)
REDIRECT_TO["url"] = base + "/a.jpg"
check("redirect followed after check", td.download_thumbnail_from_info({"thumbnail": base + "/redir"}, dest) is True)
td._validate_url_for_ssrf = real_validate
srv.shutdown()

# ---- needs the bot modules (server venv)
if FULL:
    from URL_PARSERS.tags import extract_url_range_tags
    for text, (s, e) in {f"{U}*3*7 #music": (3, 7), f"{U}*-1*-5": (-1, -5), f"{U}*7*3": (7, 3)}.items():
        _, a, b, _, tags, _, err = extract_url_range_tags(text)
        check(f"parser reads {text[-12:]!r}", (a, b) == (s, e) and err is None)
    _, a, b, _, tags, _, err = extract_url_range_tags(pu.command_args_to_range_text(["2-4", U, "#music"], 50))
    check("/vid 2-4 URL #music -> range and tag", (a, b) == (2, 4) and "#music" in tags and err is None)
    from HELPERS.limitter import range_limit_for_url
    from CONFIG.config import Config
    check("tiktok limit", range_limit_for_url("https://www.tiktok.com/@u")[0] == Config.MAX_TIKTOK_COUNT)
    check("playlist limit", range_limit_for_url(U)[0] == Config.MAX_PLAYLIST_COUNT)
    png = os.path.join(tmp, "p.jpg")
    import subprocess
    r = subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=red:s=32x32", "-frames:v", "1", png + ".png"],
                       capture_output=True)
    if r.returncode == 0:
        os.replace(png + ".png", png)
        td._ensure_jpeg(png)
        check("PNG cover converted to JPEG", open(png, "rb").read(3) == b"\xff\xd8\xff")
else:
    print("SKIP bot-module checks (no CONFIG here)")

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
