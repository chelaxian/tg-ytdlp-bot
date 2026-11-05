"""Offline smoke tests for /subs and /dubs helpers (no pyrogram / yt-dlp / network).

Helpers are extracted from the modules via AST, as in test_c.py.
Run: python tests/smoke/test_s_subs_dubs.py [repo_root]
"""
import ast
import glob
import logging
import os
import sys
import tempfile

REPO = sys.argv[1] if len(sys.argv) > 1 else str(__import__("pathlib").Path(__file__).resolve().parents[2])
WORK = tempfile.mkdtemp(prefix="test_s_")
os.chdir(WORK)

ok = fail = 0


def check(name, cond, detail=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} {detail}")


def extract(path, names, extra_globals):
    src = open(os.path.join(REPO, path), encoding="utf-8").read()
    tree = ast.parse(src)
    body = [n for n in tree.body
            if (isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names)
            or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in names for t in n.targets))]
    g = dict(extra_globals)
    exec(compile(ast.Module(body=body, type_ignores=[]), path, "exec"), g)
    return g


log = logging.getLogger("t")


class _Msg:
    def __getattr__(self, name):
        return name


subs = extract("COMMANDS/subtitles_cmd.py", {
    "LANGUAGES", "DEFAULT_FLAG", "LANG_FALLBACK_FLAGS", "get_flag", "resolve_language_code",
    "language_info", "_SUBS_CACHE_KEY_SUFFIXES", "clear_subs_check_cache", "ensure_utf8_srt",
}, {"os": os, "glob": glob, "logger": log, "LoggerMsg": _Msg(),
    "_subs_check_cache": {}, "_subs_check_cache_ts": {}})

# ---- language codes ----
r = subs["resolve_language_code"]
check("exact code", r("ru") == "ru")
check("mixed case pt-br -> pt-BR", r("pt-br") == "pt-BR")
check("upper EN -> en", r("EN") == "en")
check("zh-hans -> zh-Hans", r("zh-hans") == "zh-Hans")
check("underscore en_us -> en-US", r("en_us") == "en-US")
check("unknown -> None", r("xx-yy") is None and r("") is None)
info = subs["language_info"]("en-orig")
check("language_info for code outside LANGUAGES", info["name"] == "en-orig" and info["flag"])

# ---- cache clearing is per user ----
cache, ts = subs["_subs_check_cache"], subs["_subs_check_cache_ts"]
url = "https://youtu.be/abc_1_True"
for uid in (1, 22):
    for suf in ("True", "False", "normal_langs", "auto_langs", "client"):
        cache[f"{url}_{uid}_{suf}"] = suf
        ts[f"{url}_{uid}_{suf}"] = 1.0
for uid in (1, 22):
    os.makedirs(f"users/{uid}", exist_ok=True)
    open(f"users/{uid}/ask_subs_deadbeef.json", "w").close()
    open(f"users/{uid}/subs.txt", "w").write("ru")
subs["clear_subs_check_cache"](1)
check("user 1 cache entries removed", not any(k.endswith(("_1_True", "_1_False", "_1_normal_langs", "_1_auto_langs", "_1_client")) for k in cache))
check("user 22 cache entries kept", len([k for k in cache if "_22_" in k]) == 5 and len(ts) == 5)
check("user 1 ask_subs file removed", not os.path.exists("users/1/ask_subs_deadbeef.json"))
check("user 22 ask_subs file kept", os.path.exists("users/22/ask_subs_deadbeef.json"))
check("settings untouched", open("users/1/subs.txt").read() == "ru")
subs["clear_subs_check_cache"]()
check("global clear empties cache", not cache and not ts)
check("global clear removes all ask_subs files", not glob.glob("users/*/ask_subs_*.json"))
same = cache is subs["_subs_check_cache"]
check("cache dict identity kept (imported elsewhere by reference)", same)

# ---- ensure_utf8_srt ----
try:
    import chardet  # noqa: F401
    have_chardet = True
except ImportError:
    have_chardet = False
if have_chardet:
    text = ("1\n00:00:01,000 --> 00:00:03,000\nПривет, как дела? Это проверка кодировки субтитров.\n\n"
            "2\n00:00:04,000 --> 00:00:06,000\nВсё хорошо, спасибо! Съешь же ещё этих мягких булок.\n")
    for enc in ("utf-8", "cp1251"):
        p = f"sub_{enc}.srt"
        open(p, "wb").write(text.encode(enc))
        subs["ensure_utf8_srt"](p)
        check(f"{enc} subtitles decoded correctly", open(p, encoding="utf-8").read() == text)
else:
    print("SKIP ensure_utf8_srt (chardet not installed)")

# ---- dubs ----
dubs = extract("COMMANDS/dubs_cmd.py", {
    "_dubs_file_path", "get_user_dubs_language", "match_dub_language", "apply_dubs_preference",
}, {"os": os, "logger": log})
m = dubs["match_dub_language"]
check("de -> de-DE", m("de", ["en", "de-DE", "es-US"]) == "de-DE")
check("exact wins", m("en", ["en-US", "en"]) == "en")
check("case-insensitive", m("pt-BR", ["pt-br"]) == "pt-br")
check("en-GB -> en-US when only US", m("en-GB", ["en-US", "fr-FR"]) == "en-US")
check("zh-Hans never -> zh-Hant", m("zh-Hans", ["zh-Hant"]) is None)
check("zh-Hans -> zh", m("zh-Hans", ["zh"]) == "zh")
check("missing language -> None", m("ru", ["en", "de-DE"]) is None)

os.makedirs("users/5", exist_ok=True)
open("users/5/dubs.txt", "w").write("de")
apply = dubs["apply_dubs_preference"]
st = apply(5, {"has_dubs": True, "available_dubs": ["de-DE", "en"], "audio_lang": None})
check("preference mapped to real track", st["selected_audio_langs"] == ["de-DE"] and st["audio_lang"] == "de-DE")
st = apply(5, {"has_dubs": True, "available_dubs": ["en", "fr-FR"]})
check("absent language not injected", not st.get("selected_audio_langs") and not st.get("audio_lang"))
st = apply(5, {"has_dubs": False, "available_dubs": []})
check("no dubs video untouched", "selected_audio_langs" not in st)
st = apply(5, {"has_dubs": True, "available_dubs": ["de-DE", "en"], "selected_audio_langs": ["en"]})
check("manual selection wins", st["selected_audio_langs"] == ["en"])
st = apply(6, {"has_dubs": True, "available_dubs": ["de-DE", "en"]})
check("no preference -> untouched", "selected_audio_langs" not in st)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
