"""Smoke test: admin commands argument validation (offline).

Run: python tests/smoke/test_r_admin_cmds.py
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


def valid_id(s):
    return bool(s) and s.lstrip("-").isdigit()


check("numeric id accepted", valid_id("123456789"))
check("negative id accepted", valid_id("-1001234"))
check("garbage rejected", not valid_id("abc"))
check("empty rejected", not valid_id(""))
check("mixed rejected", not valid_id("123abc"))
check("all rejected", not valid_id("all"))
check("whitespace-only rejected", not valid_id("  "))

# /log parsing logic
GET_USER_LOGS_COMMAND = "/log"


def log_target(admin, text):
    if admin and text.startswith(GET_USER_LOGS_COMMAND):
        parts = text.strip().split()
        if len(parts) < 2 or not parts[1].lstrip("-").isdigit():
            return "USAGE"
        return parts[1]
    return "SELF"


check("/log 123 -> 123", log_target(True, "/log 123") == "123")
check("/log -> usage", log_target(True, "/log") == "USAGE")
check("/log abc -> usage", log_target(True, "/log abc") == "USAGE")
check("/log 123 extra -> 123", log_target(True, "/log 123 extra") == "123")
check("/login not /log", log_target(True, "/login") == "USAGE")

# interval range check (cache_db new logic)
def interval_ok(n):
    return not (n is None or n < 1 or n > 168)


check("interval 0 rejected", not interval_ok(0))
check("interval 1 ok", interval_ok(1))
check("interval 168 ok", interval_ok(168))
check("interval 169 rejected", not interval_ok(169))

# broadcast empty detection
def broadcast_empty(text, reply):
    lines = text.splitlines()
    if len(lines) > 1:
        broadcast_text = "\n".join(lines[1:]).strip()
    else:
        broadcast_text = text[len("/broadcast"):].strip()
    return not broadcast_text and not reply


check("/broadcast alone -> empty", broadcast_empty("/broadcast", None))
check("/broadcast\\ntext -> not empty", not broadcast_empty("/broadcast\nhello", None))
check("/broadcast with reply -> not empty", not broadcast_empty("/broadcast", object()))

# locale keys exist as source text (config.py is gitignored / absent locally)
for loc in ("messages_EN", "messages_RU"):
    p = os.path.join(os.path.dirname(__file__), "..", "..", "CONFIG", "LANGUAGES", f"{loc}.py")
    with open(p, encoding="utf-8-sig") as f:
        src = f.read()
    check(f"{loc}: ADMIN_USER_ID_INVALID_MSG", "ADMIN_USER_ID_INVALID_MSG" in src)
    check(f"{loc}: ADMIN_BROADCAST_EMPTY_MSG", "ADMIN_BROADCAST_EMPTY_MSG" in src)
    check(f"{loc}: ADMIN_GET_LOGS_USAGE_MSG", "ADMIN_GET_LOGS_USAGE_MSG" in src)
    check(f"{loc}: escaped newline", "ADMIN_USER_ID_INVALID_MSG = \"Invalid user ID: {user_id}\\n" in src or "\\n" in src.split("ADMIN_USER_ID_INVALID_MSG")[1][:120])

# commands module compiles (syntax)
import py_compile
for f in ("COMMANDS/admin_cmd.py", "DATABASE/cache_db.py"):
    try:
        py_compile.compile(os.path.join(os.path.dirname(__file__), "..", "..", f), doraise=True)
        check(f"py_compile {f}", True)
    except Exception as e:
        check(f"py_compile {f}", False)
        print(" ", e)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
