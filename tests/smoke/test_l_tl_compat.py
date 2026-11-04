"""Smoke test: HELPERS/tl_compat parses channel#83259464 (offline, needs pyrogram).

Run: python tests/smoke/test_l_tl_compat.py
"""
import os
import sys
from io import BytesIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from pyrogram.raw import types  # noqa: E402
from pyrogram.raw.core import Int, Long, String, TLObject  # noqa: E402

from HELPERS import tl_compat  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


def legacy_channel_bytes(cid, title, username=None, access_hash=None, participants=None,
                         usernames=None, broadcast=True):
    flags = 0
    flags |= (1 << 5) if broadcast else 0
    flags |= (1 << 6) if username is not None else 0
    flags |= (1 << 13) if access_hash is not None else 0
    flags |= (1 << 17) if participants is not None else 0
    flags2 = (1 << 0) if usernames else 0
    b = BytesIO()
    b.write(Int(tl_compat.CHANNEL_LEGACY_ID, False))
    b.write(Int(flags))
    b.write(Int(flags2))
    b.write(Long(cid))
    if access_hash is not None:
        b.write(Long(access_hash))
    b.write(String(title))
    if username is not None:
        b.write(String(username))
    b.write(types.ChatPhotoEmpty().write())
    b.write(Int(1730000000))
    if participants is not None:
        b.write(Int(participants))
    if usernames:
        b.write(Int(0x1CB5C415, False))
        b.write(Int(len(usernames)))
        for u in usernames:
            b.write(types.Username(username=u, active=True).write())
    return b.getvalue()


def chats_reply(*chat_blobs):
    b = BytesIO()
    b.write(Int(types.messages.Chats.ID, False))
    b.write(Int(0x1CB5C415, False))
    b.write(Int(len(chat_blobs)))
    for blob in chat_blobs:
        b.write(blob)
    return b.getvalue()


# before install the constructor is unknown (same failure as on DE)
from pyrogram.raw.all import objects  # noqa: E402

check("unknown before install", tl_compat.CHANNEL_LEGACY_ID not in objects)
check("install() registers", tl_compat.install() is True)
check("install() is idempotent", tl_compat.install() is False)

legacy = legacy_channel_bytes(-1001234567890 & 0xFFFFFFFFFF, "My channel", username="mychan",
                              access_hash=0x1122334455667788, participants=4242,
                              usernames=["mychan", "mychan2"])
modern = types.Channel(id=777, title="Modern", photo=types.ChatPhotoEmpty(), date=1,
                       access_hash=5, megagroup=True).write()
reply = TLObject.read(BytesIO(chats_reply(legacy, modern)))

check("reply is messages.Chats", isinstance(reply, types.messages.Chats))
check("two chats parsed", len(reply.chats) == 2)
ch = reply.chats[0]
check("legacy -> raw.types.Channel", isinstance(ch, types.Channel))
check("title", ch.title == "My channel")
check("username", ch.username == "mychan")
check("access_hash", ch.access_hash == 0x1122334455667788)
check("participants_count", ch.participants_count == 4242)
check("broadcast flag", ch.broadcast is True and ch.megagroup is False)
check("usernames vector", [u.username for u in ch.usernames] == ["mychan", "mychan2"])
check("stream stays aligned (next chat)", isinstance(reply.chats[1], types.Channel)
      and reply.chats[1].title == "Modern" and reply.chats[1].megagroup is True)

# minimal form: no optional fields at all
mini = TLObject.read(BytesIO(legacy_channel_bytes(5, "x", broadcast=False)))
check("minimal legacy channel", isinstance(mini, types.Channel) and mini.access_hash is None
      and mini.usernames == [] and mini.restriction_reason == [])

# field-for-field identical to Pyrogram's own parse of the equivalent Layer 227 channel
native = TLObject.read(BytesIO(types.Channel(
    id=ch.id, title="My channel", photo=types.ChatPhotoEmpty(), date=1730000000,
    broadcast=True, username="mychan", access_hash=0x1122334455667788,
    participants_count=4242,
    usernames=[types.Username(username="mychan", active=True),
               types.Username(username="mychan2", active=True)],
).write()))
diff = [k for k in types.Channel.__slots__ if repr(getattr(ch, k)) != repr(getattr(native, k))]
check("same fields as native Layer 227 parse", not diff)
if diff:
    print("  differing:", diff)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
