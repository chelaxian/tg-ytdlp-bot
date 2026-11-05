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
bot see a normal channel.

Since 2026-11-05 the same happens with an older `user` constructor, 0x8f97c628
(seen in channels.GetAdminLog replies to the ChannelGuard user session:
"KeyError: 2409088552" / "unknown constructor: 0x8f97c628"). Its definition
(CRC32 verified, Telethon v1.28 schema) is the Layer 227 `user#31774388` with
only the first flags2 field (usernames); everything else keeps its order:

    user#8f97c628 flags:# self:flags.10?true contact:flags.11?true
      mutual_contact:flags.12?true deleted:flags.13?true bot:flags.14?true
      bot_chat_history:flags.15?true bot_nochats:flags.16?true
      verified:flags.17?true restricted:flags.18?true min:flags.20?true
      bot_inline_geo:flags.21?true support:flags.23?true scam:flags.24?true
      apply_min_photo:flags.25?true fake:flags.26?true
      bot_attach_menu:flags.27?true premium:flags.28?true
      attach_menu_enabled:flags.29?true flags2:# id:long
      access_hash:flags.0?long first_name:flags.1?string last_name:flags.2?string
      username:flags.3?string phone:flags.4?string photo:flags.5?UserProfilePhoto
      status:flags.6?UserStatus bot_info_version:flags.14?int
      restriction_reason:flags.18?Vector<RestrictionReason>
      bot_inline_placeholder:flags.19?string lang_code:flags.22?string
      emoji_status:flags.30?EmojiStatus usernames:flags2.0?Vector<Username> = User;

It is parsed into a regular `raw.types.User`.

Those legacy users carry legacy statuses too (2026-11-05 12:05 UTC:
"unknown constructor: 0xe26f42f1"). Before `by_me` was added the "recently /
within a week / within a month" statuses had no fields (CRC32 verified):

    userStatusRecently#e26f42f1 = UserStatus;
    userStatusLastWeek#7bf09fc = UserStatus;
    userStatusLastMonth#77ebc742 = UserStatus;

They are parsed into the current types with by_me=False.

Registration is idempotent and never overrides a constructor that Pyrogram
itself knows (a future Pyrogram release wins).

The legacy objects show up in the ChannelGuard admin-log scans (00:05 / 12:05
UTC); each scan so far brought one more of them.
"""

from io import BytesIO
from typing import Any

CHANNEL_LEGACY_ID = 0x83259464
USER_LEGACY_ID = 0x8f97c628


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


def _read_user_legacy(b: BytesIO, *args: Any):
    from pyrogram.raw import types
    from pyrogram.raw.core import Int, Long, String, TLObject

    flags = Int.read(b)
    flags2 = Int.read(b)
    id_ = Long.read(b)
    access_hash = Long.read(b) if flags & (1 << 0) else None
    first_name = String.read(b) if flags & (1 << 1) else None
    last_name = String.read(b) if flags & (1 << 2) else None
    username = String.read(b) if flags & (1 << 3) else None
    phone = String.read(b) if flags & (1 << 4) else None
    photo = TLObject.read(b) if flags & (1 << 5) else None
    status = TLObject.read(b) if flags & (1 << 6) else None
    bot_info_version = Int.read(b) if flags & (1 << 14) else None
    restriction_reason = TLObject.read(b) if flags & (1 << 18) else []
    bot_inline_placeholder = String.read(b) if flags & (1 << 19) else None
    lang_code = String.read(b) if flags & (1 << 22) else None
    emoji_status = TLObject.read(b) if flags & (1 << 30) else None
    usernames = TLObject.read(b) if flags2 & (1 << 0) else []

    return types.User(
        id=id_,
        is_self=bool(flags & (1 << 10)),
        contact=bool(flags & (1 << 11)),
        mutual_contact=bool(flags & (1 << 12)),
        deleted=bool(flags & (1 << 13)),
        bot=bool(flags & (1 << 14)),
        bot_chat_history=bool(flags & (1 << 15)),
        bot_nochats=bool(flags & (1 << 16)),
        verified=bool(flags & (1 << 17)),
        restricted=bool(flags & (1 << 18)),
        min=bool(flags & (1 << 20)),
        bot_inline_geo=bool(flags & (1 << 21)),
        support=bool(flags & (1 << 23)),
        scam=bool(flags & (1 << 24)),
        apply_min_photo=bool(flags & (1 << 25)),
        fake=bool(flags & (1 << 26)),
        bot_attach_menu=bool(flags & (1 << 27)),
        premium=bool(flags & (1 << 28)),
        attach_menu_enabled=bool(flags & (1 << 29)),
        # flags2 bits this layer lacks: False, exactly as Pyrogram's own read() leaves them
        bot_can_edit=False,
        close_friend=False,
        stories_hidden=False,
        stories_unavailable=False,
        contact_require_premium=False,
        bot_business=False,
        bot_has_main_app=False,
        bot_forum_view=False,
        bot_forum_can_manage_topics=False,
        bot_can_manage_bots=False,
        bot_guestchat=False,
        bot_guard=False,
        access_hash=access_hash,
        first_name=first_name,
        last_name=last_name,
        username=username,
        phone=phone,
        photo=photo,
        status=status,
        bot_info_version=bot_info_version,
        restriction_reason=restriction_reason,
        bot_inline_placeholder=bot_inline_placeholder,
        lang_code=lang_code,
        emoji_status=emoji_status,
        usernames=usernames,
    )


class UserLegacy:
    """Registry entry for user#8f97c628."""

    ID = USER_LEGACY_ID
    QUALNAME = "types.UserLegacy"
    read = staticmethod(_read_user_legacy)


def _status_legacy(constructor_id: int, type_name: str):
    """Registry entry for a field-less legacy userStatus* constructor."""

    def read(b: BytesIO, *args: Any):
        from pyrogram.raw import types
        return getattr(types, type_name)(by_me=False)

    return type(f"{type_name}Legacy", (), {
        "ID": constructor_id,
        "QUALNAME": f"types.{type_name}Legacy",
        "read": staticmethod(read),
    })


USER_STATUS_RECENTLY_LEGACY_ID = 0xE26F42F1
USER_STATUS_LAST_WEEK_LEGACY_ID = 0x07BF09FC
USER_STATUS_LAST_MONTH_LEGACY_ID = 0x77EBC742

_SHIMS = (
    ChannelLegacy,
    UserLegacy,
    _status_legacy(USER_STATUS_RECENTLY_LEGACY_ID, "UserStatusRecently"),
    _status_legacy(USER_STATUS_LAST_WEEK_LEGACY_ID, "UserStatusLastWeek"),
    _status_legacy(USER_STATUS_LAST_MONTH_LEGACY_ID, "UserStatusLastMonth"),
)


def install() -> bool:
    """Register the shims in Pyrogram's constructor table. Returns True if any was added."""
    try:
        import pyrogram.raw  # noqa: F401  (resolves the objects table to classes)
        from pyrogram.raw.all import objects
    except Exception:
        return False
    added = False
    for shim in _SHIMS:
        if shim.ID not in objects:
            objects[shim.ID] = shim
            added = True
    return added
