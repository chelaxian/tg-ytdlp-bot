"""Offline smoke tests for B1 fixes (#470, #472, #474, #481, Always Ask error UX, #445 cooldown).

No network: pyrogram is stubbed; always_ask_menu helpers are extracted via AST
(the full module pulls in the whole bot).
Run: python test_b1.py <repo_root>
"""
import ast
import asyncio
import logging
import re
import sys
import time
import types

REPO = sys.argv[1] if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
sys.path.insert(0, REPO)
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(name)s: %(message)s")

# ---------------------------------------------------------------- pyrogram stub
class RPCError(Exception):
    ID = None
    def __init__(self, value=None):
        super().__init__(f"Telegram says: [400 {self.ID}]")
        self.value = value

def _err(name, ident):
    return type(name, (RPCError,), {"ID": ident})

errors = types.ModuleType("pyrogram.errors")
errors.RPCError = RPCError
errors.FloodWait = _err("FloodWait", "FLOOD_WAIT_X")
errors.QueryIdInvalid = _err("QueryIdInvalid", "QUERY_ID_INVALID")
errors.PeerIdInvalid = _err("PeerIdInvalid", "PEER_ID_INVALID")
errors.UserIsBlocked = _err("UserIsBlocked", "USER_IS_BLOCKED")
errors.InputUserDeactivated = _err("InputUserDeactivated", "INPUT_USER_DEACTIVATED")
errors.ChatWriteForbidden = _err("ChatWriteForbidden", "CHAT_WRITE_FORBIDDEN")
errors.ChannelPrivate = _err("ChannelPrivate", "CHANNEL_PRIVATE")
errors.MessageIdInvalid = _err("MessageIdInvalid", "MESSAGE_ID_INVALID")

ptypes = types.ModuleType("pyrogram.types")
class CallbackQuery:
    def __init__(self, exc=None, coro=False):
        self.id = "cbq1"
        self._exc = exc
        self._coro = coro
        self.calls = 0
    def answer(self, text=None, show_alert=False):
        self.calls += 1
        if self._coro:
            async def _c():
                if self._exc:
                    raise self._exc
                return True
            return _c()
        if self._exc:
            raise self._exc
        return True
ptypes.CallbackQuery = CallbackQuery
ptypes.ReplyParameters = lambda **kw: kw
pyrogram = types.ModuleType("pyrogram")
pyrogram.errors = errors
pyrogram.types = ptypes
pyrogram.enums = types.SimpleNamespace(ParseMode=types.SimpleNamespace(HTML="html"))
sys.modules.update({"pyrogram": pyrogram, "pyrogram.errors": errors, "pyrogram.types": ptypes,
                    "pyrogram.enums": pyrogram.enums})

# --------------------------------------------------- messages / app stubs
import importlib.util
def _load_messages(locale):
    spec = importlib.util.spec_from_file_location(f"m_{locale}", f"{REPO}/CONFIG/LANGUAGES/messages_{locale}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Messages
EN = _load_messages("EN")
RU = _load_messages("RU")
msgs_stub = types.ModuleType("CONFIG.messages")
msgs_stub.Messages = EN
msgs_stub.safe_get_messages = lambda *_a, **_k: EN
sys.modules["CONFIG.messages"] = msgs_stub

class FakeApp:
    def __init__(self):
        self.calls = 0
        self.exc = None
    def send_message(self, chat_id, text, **kw):
        self.calls += 1
        if self.exc:
            raise self.exc
        return types.SimpleNamespace(id=1)
    def forward_messages(self, chat_id, from_chat_id, message_ids, **kw):
        return self.send_message(chat_id, "")
APP = FakeApp()
app_stub = types.ModuleType("HELPERS.app_instance")
app_stub.get_app = lambda: APP
sys.modules["HELPERS.app_instance"] = app_stub

failures = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        failures.append(name)

# ================================================================ safe_messeger
import HELPERS.safe_messeger as sm  # installs the CallbackQuery guard at import

# #470: expired query swallowed (sync + async), other RPC errors propagate
cq = CallbackQuery(exc=errors.QueryIdInvalid())
check("#470 sync QUERY_ID_INVALID swallowed", sm.safe_callback_answer(cq, "x") is False)
cq = CallbackQuery(exc=errors.QueryIdInvalid(), coro=True)
check("#470 async QUERY_ID_INVALID swallowed", asyncio.run(sm.safe_callback_answer(cq, "x")) is False)
cq = CallbackQuery(exc=errors.PeerIdInvalid())
try:
    sm.safe_callback_answer(cq, "x")
    check("#470 other RPC errors still raised", False)
except errors.PeerIdInvalid:
    check("#470 other RPC errors still raised", True)
check("#470 normal answer passes through", sm.safe_callback_answer(CallbackQuery(), "ok") is True)
# #472: permanent peer errors -> one attempt, WARNING once, then DEBUG
records = []
class H(logging.Handler):
    def emit(self, r):
        records.append(r)
sm.logger.addHandler(H())
for exc_cls in (errors.PeerIdInvalid, errors.UserIsBlocked, errors.InputUserDeactivated, errors.ChatWriteForbidden):
    APP.calls = 0
    APP.exc = exc_cls()
    records.clear()
    chat = 1000 + APP.calls + hash(exc_cls.__name__) % 1000
    sm._last_message_sent.clear()
    r = sm.safe_send_message(chat, "hi")
    warn = [x for x in records if x.levelno >= logging.WARNING and "unreachable" in x.getMessage()]
    err = [x for x in records if x.levelno >= logging.ERROR]
    check(f"#472 {exc_cls.__name__}: single attempt, None, 1 WARNING, no ERROR",
          r is None and APP.calls == 1 and len(warn) == 1 and not err)
records.clear(); APP.calls = 0; APP.exc = errors.PeerIdInvalid()
sm._last_message_sent.clear()
sm.safe_send_message(1000 + hash("PeerIdInvalid") % 1000, "again")
check("#472 repeat within window logged at DEBUG only",
      not [x for x in records if x.levelno >= logging.WARNING and "unreachable" in x.getMessage()])
APP.calls = 0; APP.exc = errors.UserIsBlocked(); records.clear()
check("#472 forward: single attempt", sm.safe_forward_messages(4242, 1, [1]) is None and APP.calls == 1)
APP.exc = None

# ================================================== always_ask_menu helpers (AST)
src = open(f"{REPO}/DOWN_AND_UP/always_ask_menu.py", encoding="utf-8").read()
tree = ast.parse(src)
WANT_FUNCS = {"_extract_fail_key", "_fail_cooldown_remaining", "_bump_fail_counter", "_check_extract_cooldown",
              "_record_extract_fail", "record_download_fail", "clear_download_fail", "_clear_extract_fail",
              "_classify_ask_error", "_ask_error_message", "_is_error_info", "delete_processing_message",
              "safe_callback_answer", "set_user_proc_msg", "get_user_proc_msg", "clear_user_proc_msg"}
WANT_VARS = {"_RECENT_EXTRACT_FAILS", "EXTRACT_FAIL_COOLDOWN_SEC", "EXTRACT_FAIL_THRESHOLD", "_RECENT_DOWNLOAD_FAILS",
             "DOWNLOAD_FAIL_COOLDOWN_SEC", "_ASK_ERROR_CATEGORY_MESSAGES", "_ASK_ERROR_NO_COOKIE_HINT",
             "_HTTP_AUTH_4XX_RE", "_PROC_MSG_CACHE"}
body = []
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name in WANT_FUNCS:
        body.append(node)
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in WANT_VARS for t in node.targets):
        body.append(node)
mod = ast.Module(body=body, type_ignores=[])
deleted = []
safe_msgr_stub = types.SimpleNamespace(safe_delete_messages=lambda **kw: deleted.append(kw["message_ids"]))
sys.modules["HELPERS.safe_messeger"] = safe_msgr_stub  # delete_processing_message imports it lazily
aam_logger = logging.getLogger("aam")
ns = {"re": re, "logger": aam_logger, "safe_get_messages": lambda *_: EN,
      "QueryIdInvalid": errors.QueryIdInvalid, "RPCError": RPCError, "safe_callback_answer": sm.safe_callback_answer}
exec(compile(mod, "always_ask_menu_extract", "exec"), ns)

# category -> message mapping, using the real CONFIG.errors + HELPERS.ytdlp_errors
cases = {
    "ERROR: [youtube] abc: Join this channel to get access to members-only content like this video": "ALWAYS_ASK_MEMBERS_ONLY_MSG",
    "ERROR: [youtube] abc: This video is available to this channel's members on level: Fan": "ALWAYS_ASK_MEMBERS_ONLY_MSG",
    "ERROR: [youtube] abc: Sign in to confirm your age. This video may be inappropriate for some users.": "ALWAYS_ASK_AGE_RESTRICTED_MSG",
    "ERROR: [youtube] abc: Take a few minutes to verify your age": "ALWAYS_ASK_AGE_RESTRICTED_MSG",
    "ERROR: [Douyin] 7: Fresh cookies (not necessarily logged in) are needed": "ALWAYS_ASK_COOKIES_REQUIRED_MSG",
    "ERROR: [generic] track: Unable to download webpage: HTTP Error 400: Bad Request": "ALWAYS_ASK_SITE_REJECTED_REQUEST_MSG",
    "ERROR: [generic] track: Unable to download webpage: HTTP Error 403: Forbidden": "ALWAYS_ASK_SITE_REJECTED_REQUEST_MSG",
    "ERROR: [facebook] 123: Cannot parse data; please report this issue on https://github.com/yt-dlp/yt-dlp/issues": "ALWAYS_ASK_EXTRACTOR_ERROR_MSG",
    "ERROR: [youtube] abc: Video unavailable. This video has been removed by the uploader": "ALWAYS_ASK_VIDEO_UNAVAILABLE_MSG",
    "ERROR: [youtube] abc: Premieres in 5 hours": "ALWAYS_ASK_PREMIERE_PENDING_MSG",
    "[twitter][error] 'Unavailable'": "ALWAYS_ASK_VIDEO_UNAVAILABLE_MSG",
}
for err, key in cases.items():
    cat = ns["_classify_ask_error"](err, "https://example.com/x")
    text = ns["_ask_error_message"](1, cat)
    check(f"menu msg {key:40s} <- {err[:55]}", text == getattr(EN, key))
check("unknown error -> None", ns["_classify_ask_error"]("ERROR: something totally new", "u") is None)
check("no cookie hint for HTTP 4xx / premiere",
      {"HTTP_CLIENT_ERROR", "PREMIERE_PENDING"} <= ns["_ASK_ERROR_NO_COOKIE_HINT"])
for key in ("ALWAYS_ASK_PREMIERE_PENDING_MSG", "ALWAYS_ASK_COOKIES_REQUIRED_MSG",
            "ALWAYS_ASK_SITE_REJECTED_REQUEST_MSG", "ALWAYS_ASK_MENU_EXPIRED_MSG"):
    check(f"RU has {key} and it differs from EN", getattr(RU, key, None) and getattr(RU, key) != getattr(EN, key))

# error dicts are not cached / treated as info
check("_is_error_info(PERMANENT dict)", ns["_is_error_info"]({"error": "PERMANENT_UNAVAILABLE", "original_error": "x"}))
check("_is_error_info(proxy-fail dict)", ns["_is_error_info"]({"error": "Failed to extract video information with all available proxies"}))
check("_is_error_info(real info) is False", not ns["_is_error_info"]({"title": "t", "formats": [{}]}))

# #445/#476/#479 cooldown: 3 extraction failures engage it; menu used to clear+record -> stuck at 1
ns["_RECENT_EXTRACT_FAILS"].clear()
u, url = 7, "https://youtu.be/dead"
for _ in range(3):
    if not ns["_is_error_info"]({"error": "PERMANENT_UNAVAILABLE"}):  # mirrors the fixed menu code
        ns["_clear_extract_fail"](u, url)
    ns["_record_extract_fail"](u, url)
check("#479 cooldown engages after 3 permanent failures", ns["_check_extract_cooldown"](u, url) > 0)
ns["_RECENT_EXTRACT_FAILS"].clear()
for _ in range(3):
    ns["record_download_fail"](u, url)
    ns["_clear_extract_fail"](u, url)  # extraction itself succeeds every time (#476)
check("#476 download failures survive successful extraction", ns["_check_extract_cooldown"](u, url) > 0)
ns["clear_download_fail"](u, url)
check("clear_download_fail lifts cooldown", ns["_check_extract_cooldown"](u, url) == 0)
ns["_RECENT_EXTRACT_FAILS"][(u, url)] = (time.time() - 10_000, 5)
check("expired entry ignored", ns["_check_extract_cooldown"](u, url) == 0)

# #474: None proc_msg -> cache fallback, else DEBUG no-op
rec = []
class H2(logging.Handler):
    def emit(self, r):
        rec.append(r)
aam_logger.addHandler(H2()); aam_logger.setLevel(logging.DEBUG)
ns["_PROC_MSG_CACHE"].clear(); deleted.clear()
ns["set_user_proc_msg"](5, types.SimpleNamespace(id=77))
ns["delete_processing_message"](None, 5, None)
check("#474 None falls back to cached proc_msg", deleted == [[77]] and ns["get_user_proc_msg"](5) is None)
rec.clear()
ns["delete_processing_message"](None, 5, None)
check("#474 nothing cached -> no WARNING/ERROR", not [r for r in rec if r.levelno >= logging.WARNING])
sys.modules["HELPERS.safe_messeger"] = sm

# safe_callback_answer: precise exceptions
ns["safe_callback_answer"](CallbackQuery(exc=errors.QueryIdInvalid()), "t")
check("safe_callback_answer swallows QueryIdInvalid", True)

# #481: the hard-coded cache file lookup is gone
check("#481 hard-coded formats_cache_75170fc2 removed", '"formats_cache_75170fc2.json")' not in src and 'logger.error(f"Cache file not found' not in src)

print("\nFAILURES:", failures if failures else "none")
sys.exit(1 if failures else 0)
