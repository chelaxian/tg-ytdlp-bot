"""Smoke test: CREDITS_MSG shows only this server's bot (offline).

The credits block lists all five country bots in every language file and is the
same on all five servers; users should see only the bot they are talking to.
Run: python tests/smoke/test_x_credits_own_bot.py
"""
import os
import sys
import types

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

from CONFIG.messages import credits_own_bot_only, _FLEET_BOTS  # noqa: E402

ok = fail = 0


def check(name, cond, info=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name} {info}")


EN = ("<blockquote><i>Managed by</i> @iilililiiillliiliililliilliliiil\n"
      "🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n"
      "🇫🇷 @tgytdlp_fr_bot\n🇩🇪 @tgytdlp_de_bot</blockquote>\n"
      "<b>🌍 Change language: /lang</b>")


def with_own(username):
    mod = types.ModuleType("CONFIG.config")
    mod.Config = type("Config", (), {}) if username is None else type(
        "Config", (), {"BOT_USERNAME": username})
    old = sys.modules.get("CONFIG.config")
    sys.modules["CONFIG.config"] = mod
    try:
        return credits_own_bot_only(EN)
    finally:
        if old is not None:
            sys.modules["CONFIG.config"] = old
        else:
            sys.modules.pop("CONFIG.config", None)


out = with_own("@tgytdlp_de_bot")
check("DE bot: other bots removed", all(f"@{b}" not in out for b in _FLEET_BOTS if b != "tgytdlp_de_bot"), out)
check("DE bot: own line kept", "@tgytdlp_de_bot" in out)
check("manager and /lang kept", "@iilililiiillliiliililliilliliiil" in out and "/lang" in out)
check("no empty lines left", "\n\n" not in out.replace("</blockquote>\n<b>", "X"))

out = with_own("tgytdlp_it_bot")
check("IT bot: only IT line", "@tgytdlp_it_bot" in out and "tgytdlp_de_bot" not in out and "tgytdlp_fr_bot" not in out)

check("unknown bot -> text unchanged", with_own("@some_other_bot") == EN)
check("no BOT_USERNAME -> text unchanged", with_own(None) == EN)
check("text without fleet bots passes through", credits_own_bot_only("plain message") == "plain message")
check("empty text ok", credits_own_bot_only("") == "")

# the real per-server source: BOT_NAME (config.py has BOT_NAME="tgytdlp_de_bot")
mod = types.ModuleType("CONFIG.config")
mod.Config = type("Config", (), {"BOT_NAME": "tgytdlp_de_bot"})
old = sys.modules.get("CONFIG.config")
sys.modules["CONFIG.config"] = mod
try:
    out = credits_own_bot_only(EN)
finally:
    if old is not None:
        sys.modules["CONFIG.config"] = old
    else:
        sys.modules.pop("CONFIG.config", None)
check("BOT_NAME fallback works (DE config.py)", "@tgytdlp_de_bot" in out and "tgytdlp_it_bot" not in out, out)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
