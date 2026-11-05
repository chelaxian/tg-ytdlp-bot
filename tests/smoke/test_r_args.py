"""Smoke test: /args validation, yt-dlp option mapping, masking, input ownership.

Needs the bot's venv (pyrogram, yt-dlp). No network, no Telegram: the Pyrogram
client is replaced by a stub before COMMANDS.args_cmd is imported. Runs in a
temporary directory (users/<id>/args.txt is written there).

Run: python tests/smoke/test_r_args.py
"""
import asyncio
import json
import os
import sys
import tempfile
import types as pytypes

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)


class _StubApp:
    def __getattr__(self, name):
        def deco_factory(*a, **k):
            return lambda f: f
        return deco_factory


import HELPERS.app_instance as _app_instance  # noqa: E402
_app_instance.get_app = lambda: _StubApp()

os.chdir(tempfile.mkdtemp(prefix="args_smoke_"))

from COMMANDS import args_cmd as A  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


def valid(value, param):
    return A.validate_input(value, param, None)[0]


# ---- validation ----
check("UA with ; and quotes accepted",
      valid('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "x"', "user_agent"))
check("control chars rejected", not valid("a\r\nX-Evil: 1", "user_agent"))
check("referer must be URL", not valid("example.com", "referer") and valid("https://example.com/a", "referer"))
check("date 20230231 rejected", not valid("20230231", "date"))
check("date 20230930 accepted", valid("20230930", "datebefore"))
check("xff values", all(valid(v, "xff") for v in ("default", "never", "US", "de", "10.0.0.0/8", "2001:db8::/32"))
      and not valid("zz1", "xff") and not valid("999.1.1.1", "xff"))
check("playlist_items ranges", all(valid(v, "playlist_items") for v in ("1,3,5-7", "2:10", "-1", "1:10:2"))
      and not valid("1;rm", "playlist_items") and not valid("abc", "playlist_items"))
check("headers JSON object of strings",
      valid('{"Authorization": "Bearer x", "X-A": "b"}', "http_headers")
      and not valid('{"a": 1}', "http_headers") and not valid('["a"]', "http_headers")
      and not valid('{"a": "b\\nc"}', "http_headers"))

# ---- mapping to yt-dlp ----
UID = 4242
A.save_user_args(UID, {
    "check_certificate": False, "no_check_certificates": True,
    "force_ipv4": False, "force_ipv6": True,
    "live_from_start": False, "no_live_from_start": True,
    "xff": "US", "dateafter": "20230101", "datebefore": "20231231",
    "no_continue": True, "sleep_subtitles": 3, "legacy_server_connect": True,
    "user_agent": "UA/1.0 (X; Y)", "referer": "https://ref.example/",
    "http_headers": '{"Authorization": "Bearer secret-token", "X-Num": 5}',
    "impersonate": "firefox", "concurrent_fragments": 4,
    "min_filesize": 1, "password": "hunter2", "username": "me",
    "video_format": "mkv", "write_thumbnail": False,
})
o = A.get_user_ytdlp_args(UID)
check("nocheckcertificate", o.get("nocheckcertificate") is True)
check("source_address ::", o.get("source_address") == "::")
check("live_from_start False", o.get("live_from_start") is False)
check("geo_bypass_country", o.get("geo_bypass_country") == "US" and o.get("geo_bypass") is True)
from yt_dlp.utils import DateRange  # noqa: E402
dr = o.get("daterange")
check("daterange", isinstance(dr, DateRange) and "20230615" in dr and "20240101" not in dr)
check("continuedl False", o.get("continuedl") is False)
check("sleep_interval_subtitles", o.get("sleep_interval_subtitles") == 3)
check("legacyserverconnect", o.get("legacyserverconnect") is True)
check("headers merged, non-string dropped",
      o.get("http_headers") == {"User-Agent": "UA/1.0 (X; Y)", "Referer": "https://ref.example/",
                                "Authorization": "Bearer secret-token"})
check("concurrent_fragment_downloads", o.get("concurrent_fragment_downloads") == 4)
check("min_filesize bytes", o.get("min_filesize") == 1024 * 1024)
check("writethumbnail off", o.get("writethumbnail") is False)
check("video_format passed for the sender", o.get("video_format") == "mkv" and "ext=mkv" in o.get("format", ""))
unknown = {"check_certificate", "no_check_certificates", "force_ipv4", "force_ipv6", "xff", "date",
           "datebefore", "dateafter", "no_continue", "continue_dl", "sleep_subtitles",
           "legacy_server_connect", "no_live_from_start"}
check("no CLI-style keys left", not (unknown & set(o)))

import yt_dlp  # noqa: E402
try:
    with yt_dlp.YoutubeDL({**o, "quiet": True}) as ydl:
        built = ydl.params.get("source_address") == "::"
except Exception as e:
    built = False
    print("  YoutubeDL error:", e)
check("YoutubeDL accepts the options", built)

empty_uid = 4343
check("defaults: thumbnails only", A.get_user_ytdlp_args(empty_uid) == {"writethumbnail": True, "embed_thumbnail": True})
A.save_user_args(empty_uid, {"check_certificate": True, "no_check_certificates": False})
check("certificate check kept when on", "nocheckcertificate" not in A.get_user_ytdlp_args(empty_uid))

# ---- merge keeps bot extractor args ----
opts = {"extractor_args": {"generic": {"impersonate": ["chrome"]}, "youtubetab": {"skip": ["authcheck"]}},
        "http_headers": {"Accept": "*/*"}}
A.merge_user_ytdlp_args(opts, o)
check("merge keeps youtubetab", opts["extractor_args"].get("youtubetab") == {"skip": ["authcheck"]})
check("merge applies impersonate", opts["extractor_args"]["generic"] == {"impersonate": ["firefox"]})
check("merge keeps headers", opts["http_headers"].get("Accept") == "*/*" and "User-Agent" in opts["http_headers"])
lo = {"live_from_start": True, "continuedl": True}
A.merge_user_ytdlp_args(lo, o, skip={"live_from_start", "continuedl"})
check("merge skip", lo["live_from_start"] is True and lo["continuedl"] is True)

# ---- secrets not shown / logged ----
logged = json.dumps(A.mask_args_for_log({**A.get_user_args(UID)}), ensure_ascii=False) + \
    json.dumps(A.mask_args_for_log(o), default=str, ensure_ascii=False)
check("logs hide password and header values", "hunter2" not in logged and "secret-token" not in logged)
view = A.format_current_args(A.get_user_args(UID), None)
check("view hides password", "hunter2" not in view)
export = A.create_export_message(A.get_user_args(UID), None)
check("export hides password", "hunter2" not in export)
A.save_user_args(UID + 1, {"user_agent": "<b>x</b>"})
check("view escapes HTML", "&lt;b&gt;" in A.format_current_args(A.get_user_args(UID + 1), None))
imported = A.parse_import_message(export.replace("<b>", "").replace("</b>", "")
                                  .replace("<code>", "").replace("</code>", ""), None)
check("import skips masked password", "password" not in imported and imported.get("username") == "me")
check("import keeps validated values", imported.get("xff") == "US" and imported.get("datebefore") == "20231231")

# ---- input ownership ----
def msg(chat_id, uid, text="hello", thread=0):
    return pytypes.SimpleNamespace(chat=pytypes.SimpleNamespace(id=chat_id), from_user=pytypes.SimpleNamespace(id=uid),
                                   text=text, message_thread_id=thread)


GROUP, TOPIC, OWNER, OTHER = -1001, 7, 501, 502
A.user_input_states_topic[(GROUP, TOPIC)] = {"param": "user_agent", "type": "text", "owner": OWNER}
f = lambda m: asyncio.run(A._has_args_state(None, None, m))  # noqa: E731
check("topic: owner's message is the answer", f(msg(GROUP, OWNER, thread=TOPIC)))
check("topic: other member is not swallowed", not f(msg(GROUP, OTHER, thread=TOPIC)))
A.user_input_states_topic.clear()

sent = []
A.safe_send_message = lambda *a, **k: sent.append(a)
A.user_input_states_dm[OWNER] = {"param": "user_agent", "type": "text", "owner": OWNER}
A.handle_args_text_input(None, msg(GROUP, OWNER, text="MyAgent/2"))
check("group: value saved", A.get_user_args(OWNER).get("user_agent") == "MyAgent/2")
check("group: input state closed", OWNER not in A.user_input_states_dm and OWNER not in A.input_state_timers_dm)

A.user_input_states_dm[OWNER] = {"param": "date", "type": "text", "owner": OWNER}
A.handle_args_text_input(None, msg(OWNER, OWNER, text="2023-09-30"))
check("invalid date not saved, prompt stays", "date" not in A.get_user_args(OWNER) and OWNER in A.user_input_states_dm)
A.clear_input_state_timer(OWNER)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
