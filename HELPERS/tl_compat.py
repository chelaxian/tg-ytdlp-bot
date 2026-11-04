"""Compatibility shims for MTProto constructors the installed Pyrogram does not know.

Since 2026-11-04 Telegram answers some channel requests (channels.GetChannels,
channels.GetAdminLog...) with an older `channel` constructor, 0x83259464, which
PyroTGFork (Layer 227) no longer ships. Pyrogram then cannot parse the reply:
"The server sent an unknown constructor: 0x83259464", the request times out, and
ChannelGuard scans / resolve_peer for the subscription channel fail.

The old definition (CRC32 verified) is the Layer 227 `channel#1c32b11c` minus the
flags2 fields added later (stories, colors, emoji status, level, monoforum...),
with all remaining fields in the same order:

    channel#83259464 flags:# creator:flags.0?true left:flags.2?true
      broadcast:flags.5?true verified:flags.7?true megagroup:flags.8?true
      restricted:flags.9?true signatures:flags.11?true min:flags.12?true
      scam:flags.19?true has_link:flags.20?true has_geo:flags.21?true
      slowmode_enabled:flags.22?true call_active:flags.23?true
      call_not_empty:flags.24?true fake:flags.25?true gigagroup:flags.26?true
      noforwards:flags.27?true join_to_send:flags.28?true
      join_request:flags.29?true forum:flags.30?true flags2:# id:long
      access_hash:flags.13?long title:string username:flags.6?string
      photo:ChatPhoto date:int restriction_reason:flags.9?Vector<RestrictionReason>
      admin_rights:flags.14?ChatAdminRights banned_rights:flags.15?ChatBannedRights
      default_banned_rights:flags.18?ChatBannedRights participants_count:flags.17?int
      usernames:flags2.0?Vector<Username> = Chat;

It is parsed into a regular `raw.types.Channel`, so the rest of Pyrogram and the
bot see a normal channel. Registration is idempotent and never overrides a
constructor that Pyrogram itself knows (a future Pyrogram release wins).
"""

from io import BytesIO
from typing import Any

CHANNEL_LEGACY_ID = 0x83259464


def _read_channel_legacy(b: BytesIO, *args: Any):
    from pyrogram.raw import types
    from pyrogram.raw.core import Int, Long, String, TLObject

    flags = Int.read(b)
    flags2 = Int.read(b)
    id_ = Long.read(b)
    access_hash = Long.read(b) if flags & (1 << 13) else None
    title = String.read(b)
    username = String.read(b) if flags & (1 << 6) else None
    photo = TLObject.read(b)
    date = Int.read(b)
    restriction_reason = TLObject.read(b) if flags & (1 << 9) else []
    admin_rights = TLObject.read(b) if flags & (1 << 14) else None
    banned_rights = TLObject.read(b) if flags & (1 << 15) else None
    default_banned_rights = TLObject.read(b) if flags & (1 << 18) else None
    participants_count = Int.read(b) if flags & (1 << 17) else None
    usernames = TLObject.read(b) if flags2 & (1 << 0) else []

    return types.Channel(
        id=id_,
        title=title,
        photo=photo,
        date=date,
        creator=bool(flags & (1 << 0)),
        left=bool(flags & (1 << 2)),
        broadcast=bool(flags & (1 << 5)),
        verified=bool(flags & (1 << 7)),
        megagroup=bool(flags & (1 << 8)),
        restricted=bool(flags & (1 << 9)),
        signatures=bool(flags & (1 << 11)),
        min=bool(flags & (1 << 12)),
        scam=bool(flags & (1 << 19)),
        has_link=bool(flags & (1 << 20)),
        has_geo=bool(flags & (1 << 21)),
        slowmode_enabled=bool(flags & (1 << 22)),
        call_active=bool(flags & (1 << 23)),
        call_not_empty=bool(flags & (1 << 24)),
        fake=bool(flags & (1 << 25)),
        gigagroup=bool(flags & (1 << 26)),
        noforwards=bool(flags & (1 << 27)),
        join_to_send=bool(flags & (1 << 28)),
        join_request=bool(flags & (1 << 29)),
        forum=bool(flags & (1 << 30)),
        # flags2 bits this layer lacks: False, exactly as Pyrogram's own read() leaves them
        stories_hidden=False,
        stories_hidden_min=False,
        stories_unavailable=False,
        signature_profiles=False,
        autotranslation=False,
        broadcast_messages_allowed=False,
        monoforum=False,
        forum_tabs=False,
        access_hash=access_hash,
        username=username,
        restriction_reason=restriction_reason,
        admin_rights=admin_rights,
        banned_rights=banned_rights,
        default_banned_rights=default_banned_rights,
        participants_count=participants_count,
        usernames=usernames,
    )


class ChannelLegacy:
    """Registry entry for channel#83259464: TLObject.read() calls `.read(b)` on it."""

    ID = CHANNEL_LEGACY_ID
    QUALNAME = "types.ChannelLegacy"
    read = staticmethod(_read_channel_legacy)


def install() -> bool:
    """Register the shims in Pyrogram's constructor table. Returns True if added."""
    try:
        import pyrogram.raw  # noqa: F401  (resolves the objects table to classes)
        from pyrogram.raw.all import objects
    except Exception:
        return False
    if CHANNEL_LEGACY_ID in objects:
        return False
    objects[CHANNEL_LEGACY_ID] = ChannelLegacy
    return True
