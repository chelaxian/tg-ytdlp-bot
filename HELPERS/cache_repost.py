"""Repost cached media from a log channel with as few Telegram requests as possible.

Cached videos live as messages in the log channel; a cache hit forwards them.
Forwarding one message per request cost one API call (and FloodWait budget) per
playlist item, and a message deleted from the channel failed the repost without
telling the caller which ids were dead, so the stale cache entry was tried again
on every later request.
"""
from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple

from HELPERS.logger import logger

# messages.forwardMessages accepts at most 100 ids per request
FORWARD_BATCH = 100

# RPC errors that mean "the source message is gone" (the cache entry is stale).
# Anything else (user blocked the bot, no rights in the group, network...) says
# nothing about the cache, so the entry is kept.
_DEAD_SOURCE_ERRORS = ("MessageIdInvalid", "MessageIdsEmpty", "MessageEmpty")


def _is_dead_source(exc: BaseException) -> bool:
    name = type(exc).__name__
    return name in _DEAD_SOURCE_ERRORS or "MESSAGE_ID_INVALID" in str(exc)


def _runs(ids: Sequence[int]) -> List[List[int]]:
    """Split ids into ascending runs of at most FORWARD_BATCH.

    Telegram delivers a batch in message-id order, so only an ascending run keeps
    the requested order (a reverse playlist stays one request per item)."""
    runs: List[List[int]] = []
    for mid in ids:
        if runs and len(runs[-1]) < FORWARD_BATCH and mid > runs[-1][-1]:
            runs[-1].append(mid)
        else:
            runs.append([mid])
    return runs


def _source_id(msg) -> Optional[int]:
    origin = getattr(msg, "forward_origin", None)
    mid = getattr(origin, "message_id", None)
    if mid is None:
        mid = getattr(msg, "forward_from_message_id", None)
    return mid


def _forward(app, chat_id, from_chat_id, ids, thread_id) -> list:
    kwargs = {"chat_id": chat_id, "from_chat_id": from_chat_id, "message_ids": list(ids)}
    if thread_id:
        kwargs["message_thread_id"] = thread_id
    result = app.forward_messages(**kwargs)
    if result is None:
        return []
    return list(result) if isinstance(result, (list, tuple)) else [result]


def forward_cached(app, chat_id, from_chat_id, message_ids: Iterable[int],
                   thread_id: Optional[int] = None) -> Tuple[List[int], List[int], List[int]]:
    """Forward `message_ids` from the log channel.

    Returns (delivered, dead, failed): `dead` ids no longer exist in the channel
    (drop them from the cache), `failed` ids were not sent for another reason.
    Telegram skips deleted messages of a batch silently, so a short batch is
    matched back by forward origin; a batch error is retried one by one."""
    ids = [int(m) for m in message_ids]
    delivered: List[int] = []
    dead: List[int] = []
    failed: List[int] = []
    for run in _runs(ids):
        try:
            sent = _forward(app, chat_id, from_chat_id, run, thread_id)
        except Exception as e:
            if len(run) == 1:
                (dead if _is_dead_source(e) else failed).append(run[0])
                logger.warning(f"[CACHE REPOST] message {run[0]} from {from_chat_id} not forwarded: {type(e).__name__}: {e}")
                continue
            if not _is_dead_source(e):
                # the destination refused (blocked bot, rights...): retrying each id would fail the same way
                failed.extend(run)
                logger.warning(f"[CACHE REPOST] batch of {len(run)} from {from_chat_id} failed: {type(e).__name__}: {e}")
                continue
            for mid in run:  # some ids of the batch are dead: find which
                try:
                    (delivered if _forward(app, chat_id, from_chat_id, [mid], thread_id) else dead).append(mid)
                except Exception as e1:
                    (dead if _is_dead_source(e1) else failed).append(mid)
            continue
        if len(sent) == len(run):
            delivered.extend(run)
            continue
        origins = {_source_id(m) for m in sent} - {None}
        if origins:
            delivered.extend(mid for mid in run if mid in origins)
            dead.extend(mid for mid in run if mid not in origins)
        elif not sent:
            dead.extend(run)
        else:
            # some arrived but their origin is unknown: never resend them, keep the cache
            delivered.extend(run)
    return delivered, dead, failed


def repost_playlist_items(app, chat_id, from_chat_id, requested_indices, cached: dict,
                          thread_id: Optional[int] = None) -> Tuple[List[int], List[int]]:
    """Forward cached playlist items in request order.

    `cached` maps index -> message id or list of ids (split video).
    Returns (dead_indices, undelivered_indices): dead ones have to be dropped
    from the cache; both have to be downloaded again."""
    order = []
    for index in requested_indices:
        if index in cached:
            value = cached[index]
            for mid in (value if isinstance(value, (list, tuple)) else [value]):
                order.append((index, int(mid)))
    if not order:
        return [], []
    delivered, dead, failed = forward_cached(app, chat_id, from_chat_id, [m for _, m in order], thread_id)
    dead_set, failed_set = set(dead), set(failed)
    dead_idx: List[int] = []
    undelivered: List[int] = []
    for index, mid in order:
        if mid in dead_set and index not in dead_idx:
            dead_idx.append(index)
        if (mid in dead_set or mid in failed_set) and index not in undelivered:
            undelivered.append(index)
    logger.info(f"[CACHE REPOST] playlist: {len(delivered)}/{len(order)} message(s) forwarded"
                + (f", stale indices {dead_idx}" if dead_idx else "")
                + (f", not sent {failed}" if failed else ""))
    return dead_idx, undelivered


def repost_single(app, chat_id, from_chat_id, message_ids, thread_id: Optional[int] = None) -> Tuple[bool, bool]:
    """Forward a cached video/audio. Returns (ok, stale): ok when every part
    arrived, stale when a part is gone from the channel (drop the cache entry)."""
    delivered, dead, failed = forward_cached(app, chat_id, from_chat_id, message_ids, thread_id)
    if dead or failed:
        logger.warning(f"[CACHE REPOST] {len(delivered)}/{len(delivered) + len(dead) + len(failed)} part(s) forwarded "
                       f"from {from_chat_id} (gone: {dead}, not sent: {failed})")
    return bool(delivered) and not dead and not failed, bool(dead)
