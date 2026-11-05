"""Smoke test: /lang texts and lang.txt storage (needs CONFIG/config.py, run in the bot dir).

Run: python tests/smoke/test_s_lang.py
"""
import os
import shutil
import sys
import tempfile
import threading

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

import logging  # noqa: E402

logging.disable(logging.CRITICAL)

from CONFIG.LANGUAGES.language_router import LanguageRouter  # noqa: E402
from CONFIG.messages import Messages  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


router = LanguageRouter()
names = router.get_available_languages()
check("menu lists every supported language", set(names) == set(router.available_languages))

for code in router.available_languages:
    m = Messages(None, code)
    texts = {k: getattr(m, k) for k in ("LANG_SELECTION_MSG", "LANG_CHANGED_MSG", "LANG_ERROR_MSG",
                                         "LANG_CLOSED_MSG", "LANG_INVALID_ARGUMENT_MSG", "BTN_CLOSE")}
    placeholders = [k for k, v in texts.items() if v == f"[{k}]"]
    check(f"{code}: no [KEY] placeholders", not placeholders)
    if placeholders:
        print("  missing:", placeholders)
    try:
        changed = texts["LANG_CHANGED_MSG"].format(lang_name=names[code])
        check(f"{code}: LANG_CHANGED_MSG formats", names[code] in changed)
    except Exception as e:  # noqa: BLE001
        check(f"{code}: LANG_CHANGED_MSG formats ({e!r})", False)

# lang.txt storage (in a temp cwd, never touches the bot's users/)
tmp = tempfile.mkdtemp()
os.chdir(tmp)
try:
    check("set ru", router.set_user_language(1, "ru") and router.get_user_language(1) == "ru")
    check("unknown code rejected, old value kept",
          router.set_user_language(1, "xx") is False and router.get_user_language(1) == "ru")
    check("no temp files left", os.listdir("users/1") == ["lang.txt"])

    # concurrent writers/readers never observe an empty or foreign value
    seen = set()
    stop = threading.Event()

    def reader():
        while not stop.is_set():
            seen.add(open("users/1/lang.txt", encoding="utf-8").read())

    def writer(code):
        for _ in range(300):
            router.set_user_language(1, code)

    threads = [threading.Thread(target=reader)] + [threading.Thread(target=writer, args=(c,)) for c in ("en", "de", "fa")]
    for t in threads:
        t.start()
    for t in threads[1:]:
        t.join()
    stop.set()
    threads[0].join()
    check("concurrent writes: reader never sees an empty file", "" not in seen and seen <= {"ru", "en", "de", "fa"})
    check("concurrent writes: no temp files left", os.listdir("users/1") == ["lang.txt"])

    open("users/1/lang.txt", "w").close()
    check("empty lang.txt falls back to en", router.get_user_language(1) == "en")
finally:
    os.chdir(ROOT)
    shutil.rmtree(tmp)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
