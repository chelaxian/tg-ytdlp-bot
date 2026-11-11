"""Regression test: ban_chat_member must not be called with until_date=0.

Root cause (log audit 2026-11-11): until_date=0 is falsy, pyrogram's
utils.datetime_to_timestamp() maps it to None, and raw serialization of
ChatBannedRights crashes with AttributeError
("'NoneType' object has no attribute 'to_bytes'"), so the channel ban
silently fails. The fix omits until_date entirely (pyrogram default =
ban forever). The ban call goes through a helper as a string name, so the
check is a source-level AST text match around ban_chat_member call sites.
"""
import os
import re

TARGET = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "HELPERS",
    "anti_bot_protection.py",
)


def _ban_call_snippets(source: str):
    """Return source snippets containing a ban_chat_member call site."""
    return [
        m.group(0)
        for m in re.finditer(r"ban_chat_member", source)
    ]


def test_ban_chat_member_does_not_pass_until_date_zero():
    with open(TARGET, encoding="utf-8") as f:
        raw = f.read()
    assert _ban_call_snippets(raw), "ban_chat_member call not found in anti_bot_protection.py"
    # Strip comment lines so documentation cannot trip the check; only real code counts.
    source = re.sub(r"^\s*#.*$", "", raw, flags=re.M)
    # Find the actual invocation block (parens after the string literal)
    block = re.search(r'"ban_chat_member",\s*(?:app,)?[^)]*\)', source)
    assert block, "ban_chat_member invocation block not found"
    assert "until_date" not in block.group(0), (
        "ban_chat_member must not pass until_date=0 (causes AttributeError: "
        "'NoneType' object has no attribute 'to_bytes' in pyrogram raw serialization); "
        "omit the argument to use the default (ban forever)"
    )
