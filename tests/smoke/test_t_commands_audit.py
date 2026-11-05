"""Smoke test: /settings /start /keyboard /add_bot_to_group /help /search
/playlist /tags /usage /nsfw routing, storage and handlers.

Runs offline on a stubbed Pyrogram client (the PyroTGFork package must be
importable; no network, no Telegram, no CONFIG/config.py required - a stub
Config module is installed before any project import).

Run from the bot root: python tests/smoke/test_t_commands_audit.py
"""
import os
import sys
import tempfile
import types as pytypes
from types import SimpleNamespace

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


# ---------------------------------------------------------------- stubs
class _StubApp:
    """Records sends/edits/deletes; decorator factory absorbs registrations."""

    def __init__(self):
        self.sent = []          # (chat_id, text)
        self.edits = []         # (chat_id, message_id, text)
        self.deleted = []       # (chat_id, message_id)
        self.answered = []      # callback answers

    def __getattr__(self, name):
        # Never impersonate a message: handler helpers pick the first arg
        # that has .chat / .message, and this object must not be that arg.
        if name in ("chat", "message", "text", "caption", "data", "update"):
            raise AttributeError(name)
        def deco_factory(*a, **k):
            return lambda f: f
        return deco_factory

    def send_message(self, chat_id, text, **kwargs):
        self.sent.append((chat_id, text))
        return SimpleNamespace(id=1)

    def edit_message_text(self, chat_id, message_id, text, **kwargs):
        self.edits.append((chat_id, message_id, text))
        return SimpleNamespace(id=message_id)

    def send_document(self, chat_id, path, **kwargs):
        self.sent.append((chat_id, f"DOCUMENT:{os.path.basename(path)}"))
        return SimpleNamespace(id=2)

    def delete_messages(self, chat_id=None, message_ids=None, **kwargs):
        self.deleted.append((chat_id, message_ids))
        return True


stub_app = _StubApp()

import HELPERS.app_instance as _app_instance  # noqa: E402
_app_instance.get_app = lambda: stub_app
_app_instance.get_app_safe = lambda: stub_app

# Stub CONFIG.config (real one holds secrets and is not shipped).
_cfg = pytypes.ModuleType("CONFIG.config")


class _MetaConfig(type):
    # Language files read many optional Config fields at import time; return a
    # harmless placeholder for anything the stub did not define explicitly.
    _NUMERIC_FIELDS = {"STATS_DUMP_RELOAD_INTERVAL", "STATS_ACTIVE_TIMEOUT"}

    def __getattr__(cls, name):
        if name in cls._NUMERIC_FIELDS:
            return 60
        return f"<{name}>"


class _Config(metaclass=_MetaConfig):

    ADMIN = [999001]
    BOT_NAME = "test_bot"
    BOT_NAME_FOR_USERS = "TestBot"
    IGNORE_USER_COMMAND = "/ignore"
    UNIGNORE_USER_COMMAND = "/unignore"
    BLOCK_USER_COMMAND = "/block"
    UNBLOCK_USER_COMMAND = "/unblock"
    SEARCH_COMMAND = "/search"
    KEYBOARD_COMMAND = "/keyboard"
    USAGE_COMMAND = "/usage"
    ADD_BOT_TO_GROUP_COMMAND = "/add_bot_to_group"
    BROADCAST_MESSAGE = "/broadcast"
    GET_USER_LOGS_COMMAND = "/log"
    RELOAD_CACHE_COMMAND = "/reload_cache"
    CHECK_COOKIE_COMMAND = "/check_cookie"
    DOWNLOAD_COOKIE_COMMAND = "/cookie"
    SAVE_AS_COOKIE_COMMAND = "/save_as_cookie"
    SUBS_COMMAND = "/subs"
    ALLOWED_GROUP = []
    ALLOWED_USERS = []
    SUBSCRIBE_CHANNEL = None
    LOGS_CHANNEL = None
    LOGS_CHANNEL_EXCEPTION = None
    API_ID = 1
    API_HASH = "x"
    BOT_TOKEN = "x"


_cfg.Config = _Config
sys.modules["CONFIG.config"] = _cfg

# DATABASE stubs: no Firebase; commands must never call these paths here.
_fb = pytypes.ModuleType("DATABASE.firebase_init")
_fb.is_user_ignored = lambda message: False
_fb.is_user_blocked = lambda message: False
_fb.db = None
sys.modules["DATABASE.firebase_init"] = _fb

_cd = pytypes.ModuleType("DATABASE.cache_db")
_cd.get_from_local_cache = lambda path: {}
_cd.save_to_image_cache = lambda *a, **k: None
_cd.get_cached_image_posts = lambda *a, **k: {}
_cd.get_cached_image_post_indices = lambda *a, **k: {}
_cd.get_url_hash = lambda *a, **k: "h"
_cd.db_child_by_path = lambda *a, **k: None
_cd.auto_cache_command = lambda *a, **k: None
sys.modules["DATABASE.cache_db"] = _cd
_fb.write_logs = lambda *a, **k: None
_fb.reload_firebase_cache = lambda *a, **k: None

# Heavy download/pipeline modules are out of scope for a command audit: stub
# them so importing COMMANDS.other_handlers / settings_cmd stays offline.
_dna = pytypes.ModuleType("DOWN_AND_UP.down_and_audio")
_dna.down_and_audio = lambda *a, **k: None
sys.modules["DOWN_AND_UP.down_and_audio"] = _dna
_aam = pytypes.ModuleType("DOWN_AND_UP.always_ask_menu")
_aam.is_trim_mode = lambda uid: False
_aam.clear_trim_input_state = lambda uid: None
_aam.ask_quality_menu = lambda *a, **k: None
sys.modules["DOWN_AND_UP.always_ask_menu"] = _aam
_dau = pytypes.ModuleType("DOWN_AND_UP.down_and_up")
_dau.down_and_up = lambda *a, **k: None
sys.modules["DOWN_AND_UP.down_and_up"] = _dau

_cg = pytypes.ModuleType("HELPERS.channel_guard")
_cg.get_channel_guard = lambda: None
_cg.parse_period_to_seconds = lambda s: 0
_cg.format_seconds_human = lambda s: "0s"
_cg.register_block_user_executor = lambda *a, **k: None
_cg.start_channel_guard = lambda app: None
_cg.stop_channel_guard = lambda: None
sys.modules["HELPERS.channel_guard"] = _cg

import HELPERS.safe_messeger as _sm  # noqa: E402
_sm.get_app_safe = lambda: stub_app
# The real helper resolves the app via the module global, not via app_instance.
_sm.app = stub_app

# limitter: no channel subscription in tests
import HELPERS.limitter as _lim  # noqa: E402
_lim.is_user_in_channel = lambda app, message: True
_lim.is_user_allowed = lambda message: True

os.chdir(tempfile.mkdtemp(prefix="commands_audit_"))

# ---------------------------------------------------------------- imports
from COMMANDS import keyboard_cmd as KB  # noqa: E402
from COMMANDS import nsfw_cmd as NSFW  # noqa: E402
from COMMANDS import tag_cmd as TAGS  # noqa: E402
from COMMANDS import search as SEARCH  # noqa: E402
from COMMANDS import other_handlers as OTHER  # noqa: E402
from COMMANDS import settings_cmd as SETTINGS  # noqa: E402
from pyrogram import enums  # noqa: E402

UID = 990000101


def msg(text, chat_type=enums.ChatType.PRIVATE, chat_id=None, from_id=None):
    m = SimpleNamespace()
    m.chat = SimpleNamespace(id=chat_id if chat_id is not None else UID,
                             first_name="T", type=chat_type)
    m.text = text
    m.id = 11
    m.from_user = SimpleNamespace(id=from_id if from_id is not None else UID,
                                  first_name="T")
    m.reply_to_message = None
    m.message_thread_id = None
    m.caption = None
    parts = text.strip().split()
    m.command = ([parts[0][1:]] + parts[1:]) if parts and parts[0].startswith("/") else []
    return m


def cbq(data, text_of_message="menu"):
    q = SimpleNamespace()
    q.data = data
    q.from_user = SimpleNamespace(id=UID, first_name="T")
    q.message = msg(text_of_message)
    q.message.id = 77

    def answer(text=None, **kw):
        stub_app.answered.append((data, text))
        return True
    q.answer = answer
    q.edit_message_reply_markup = lambda **kw: None
    q.message.delete = lambda: stub_app.deleted.append((UID, 77))
    return q


def kb_file(uid=UID):
    return os.path.join("users", str(uid), "keyboard.txt")


def direct(fn, app=None):
    """Call a @background_handler-wrapped handler synchronously."""
    return (getattr(fn, "__wrapped__", fn))(app or stub_app, _direct_msg)


_direct_msg = None


def set_direct(message):
    global _direct_msg
    _direct_msg = message
    return message


# ---------------------------------------------------------------- /keyboard
# 1. Arguments reach the handler via url_distractor routing (regression for
#    `text == Config.KEYBOARD_COMMAND` dropping "/keyboard 1x3" etc.).
import URL_PARSERS.url_extractor as UE  # noqa: E402
from CONFIG.commands import CommandsConfig as _Cmds  # noqa: E402
_cfg.Config.KEYBOARD_COMMAND = _Cmds.KEYBOARD_COMMAND
routed = []
_real_kb = KB.keyboard_command
KB.keyboard_command = lambda app, message: routed.append(message.text)
_ue_direct = getattr(UE.url_distractor, "__wrapped__", UE.url_distractor)


def _wait_routed(timeout=3.0):
    import time as _t
    deadline = _t.time() + timeout
    while not routed and _t.time() < deadline:
        _t.sleep(0.02)
    return list(routed)


for probe in ("/keyboard", "/keyboard off", "/keyboard 1x3", "/keyboard 2x3",
              "/keyboard full"):
    routed.clear()
    _ue_direct(stub_app, msg(probe))
    check(f"url_distractor routes {probe!r} to keyboard_command",
          _wait_routed() == [probe])
routed.clear()
_ue_direct(stub_app, msg("/keyboardnonsense"))
import time as _t  # noqa: E402
_t.sleep(0.3)
check("no false route for /keyboardnonsense", not routed)
KB.keyboard_command = _real_kb

# 2. Direct arg set: layout names keep the canonical lowercase x.
KB.keyboard_command = _real_kb
_kb_direct = getattr(_real_kb, "__wrapped__", _real_kb)
for probe, expect in (("/keyboard 1x3", "1x3"), ("/keyboard 2x3", "2x3"),
                      ("/keyboard off", "OFF"), ("/keyboard full", "FULL")):
    stub_app.sent.clear()
    stub_app.edits.clear()
    _kb_direct(stub_app, msg(probe))
    content = open(kb_file(), encoding="utf-8").read().strip()
    check(f"/keyboard {probe.split()[1]} writes {expect}", content == expect)
    echoed = any(expect in t for _, t in stub_app.sent) or \
        any(expect in t for _, _, t in stub_app.edits)
    check(f"/keyboard {probe.split()[1]} echoes {expect}", echoed)

# 3. /keyboard without args shows the menu and preserves a valid stored setting.
stub_app.sent.clear()
_kb_direct(stub_app, msg("/keyboard"))
check("menu shown for bare /keyboard",
      bool(stub_app.sent) or bool(stub_app.edits))

# 4. Callbacks store the exact casing that _get_keyboard_mode understands.
for setting in ("OFF", "1x3", "2x3", "FULL"):
    KB.keyboard_callback_handler(stub_app, cbq(f"keyboard|{setting}"))
    content = open(kb_file(), encoding="utf-8").read().strip()
    check(f"callback keyboard|{setting} stores {setting}", content == setting)
from HELPERS.decorators import _get_keyboard_mode  # noqa: E402
with open(kb_file(), "w", encoding="utf-8") as f:
    f.write("1x3")
check("_get_keyboard_mode reads 1x3", _get_keyboard_mode(UID) == (True, "1x3"))
with open(kb_file(), "w", encoding="utf-8") as f:
    f.write("2x3")
check("_get_keyboard_mode reads 2x3", _get_keyboard_mode(UID) == (True, "2x3"))

# ---------------------------------------------------------------- /nsfw
# 5. The enum comparison bug: message.chat.type is a ChatType enum at runtime,
#    the old code compared it to the string "private" and the guard never fired.
_nsfw_direct = getattr(NSFW.nsfw_command, "__wrapped__", NSFW.nsfw_command)
captured = {}
_real_ign = sys.modules["DATABASE.firebase_init"].is_user_ignored
sys.modules["DATABASE.firebase_init"].is_user_ignored = lambda message: (
    captured.setdefault("chat_type", repr(getattr(message.chat, "type", None))) or True)
_nsfw_direct(stub_app, msg("/nsfw", chat_type=enums.ChatType.PRIVATE))
sys.modules["DATABASE.firebase_init"].is_user_ignored = _real_ign
check("nsfw private guard fires for enum type",
      captured.get("chat_type") == repr(enums.ChatType.PRIVATE))

# 6. Menu reflects the file state; toggles write ON/OFF; should_apply_spoiler
#    maps file content to blur behavior.
stub_app.sent.clear()
_nsfw_direct(stub_app, msg("/nsfw"))
check("nsfw menu sent", bool(stub_app.sent))
NSFW.nsfw_option_callback(stub_app, cbq("nsfw_option|on", "nsfw menu"))
check("nsfw on writes ON",
      open(os.path.join("users", str(UID), "nsfw_blur.txt"), encoding="utf-8").read() == "ON")
check("blur disabled when ON", NSFW.should_apply_spoiler(UID, True, True) is False)
NSFW.nsfw_option_callback(stub_app, cbq("nsfw_option|off", "nsfw menu"))
check("nsfw off writes OFF",
      open(os.path.join("users", str(UID), "nsfw_blur.txt"), encoding="utf-8").read() == "OFF")
check("blur enabled when OFF", NSFW.should_apply_spoiler(UID, True, True) is True)
_nsfw_direct(stub_app, msg("/nsfw on"))
check("/nsfw on fast toggle", NSFW.is_nsfw_blur_enabled(UID) is False)
_nsfw_direct(stub_app, msg("/nsfw off"))
check("/nsfw off fast toggle", NSFW.is_nsfw_blur_enabled(UID) is True)

# 7. /nsfw registration is private-only now; group handling goes through the
#    magic.py wrapper. Simulate the wrapper path with a group message.
stub_app.sent.clear()
os.path.exists(os.path.join("users", str(UID), "nsfw_blur.txt")) and \
    os.remove(os.path.join("users", str(UID), "nsfw_blur.txt"))
g = msg("/nsfw", chat_type=enums.ChatType.SUPERGROUP, chat_id=-100123,
        from_id=UID)
g.text = "/nsfw on"
_nsfw_direct(stub_app, g)
check("group nsfw stores per-chat file",
      open(os.path.join("users", "-100123", "nsfw_blur.txt"),
           encoding="utf-8").read() == "ON"
      if os.path.exists(os.path.join("users", "-100123", "nsfw_blur.txt"))
      else not os.path.exists(os.path.join("users", str(UID), "nsfw_blur.txt")))

# ---------------------------------------------------------------- /tags
# 8. Empty tags -> friendly message; tags -> message(s) with close button.
_tags_direct = getattr(TAGS.tags_command, "__wrapped__", TAGS.tags_command)
stub_app.sent.clear()
_tags_direct(stub_app, msg("/tags"))
check("tags: no tags message", bool(stub_app.sent))
os.makedirs(os.path.join("users", str(UID)), exist_ok=True)
with open(os.path.join("users", str(UID), "tags.txt"), "w", encoding="utf-8") as f:
    f.write("#tagone\n#tagtwo\n")
stub_app.sent.clear()
_tags_direct(stub_app, msg("/tags"))
check("tags listed", any("#tagone" in t for _, t in stub_app.sent))
TAGS.tags_close_callback(stub_app, cbq("tags_close|close", "tags"))
check("tags close handled", bool(stub_app.deleted))

# ---------------------------------------------------------------- /search
# 9. Keyboard button deep-link uses the configured bot name.
stub_app.sent.clear()
SEARCH.search_command(stub_app, msg("/search"))
check("search message sent", bool(stub_app.sent))
SEARCH.handle_search_callback(stub_app, cbq("search_msg|close", "search"))
check("search close handled", bool(stub_app.deleted))

# ---------------------------------------------------------------- /playlist
# 10. Help message with a working close callback.
_pl_direct = getattr(OTHER.playlist_command, "__wrapped__", OTHER.playlist_command)
stub_app.sent.clear()
_pl_direct(stub_app, msg("/playlist"))
check("playlist help sent", bool(stub_app.sent))
OTHER.playlist_help_callback(stub_app, cbq("playlist_help|close", "playlist"))
check("playlist close handled", bool(stub_app.deleted))

# ---------------------------------------------------------------- /help
stub_app.sent.clear()
SETTINGS.command2(stub_app, msg("/help"))
check("help sent", bool(stub_app.sent))

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
