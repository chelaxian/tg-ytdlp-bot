from HELPERS.app_instance import get_app
from HELPERS.logger import send_to_user, send_to_logger, send_to_all, send_error_to_user
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from HELPERS.safe_messeger import safe_send_message, safe_send_message_with_auto_delete, safe_edit_message_text, safe_delete_messages
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from datetime import datetime
import subprocess
import sys
import math
import time
import os
import re
import threading
# from DATABASE.cache_db import reload_firebase_cache, get_from_local_cache  # moved to lazy imports
from DATABASE.firebase_init import db
from URL_PARSERS.youtube import is_youtube_url, youtube_to_short_url, youtube_to_long_url
from URL_PARSERS.normalizer import normalize_url_for_cache, get_clean_playlist_url
from HELPERS.limitter import TimeFormatter, is_user_in_channel
# from DATABASE.cache_db import get_url_hash, db_child_by_path  # moved to lazy imports
from HELPERS.logger import logger

# Global variable for bot start time
starting_point = [time.time()]

# Get app instance for decorators
app = get_app()

async def reload_firebase_cache_command(app, message):
    messages = safe_get_messages(message.chat.id)
    """The processor of command for rebooting the local cache Firebase"""
    if int(message.chat.id) not in Config.ADMIN:
        await safe_send_message_with_auto_delete(message.chat.id, safe_get_messages(message.chat.id).ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG, delete_after_seconds=60)
        return
    
    # Check if this is a fake message (called programmatically)
    is_fake_message = getattr(message, '_is_fake_message', False) or message.id == 0
    
    try:
        # 1) Download fresh dump via external script path
        script_path = getattr(Config, "DOWNLOAD_FIREBASE_SCRIPT_PATH", "DATABASE/download_firebase.py")
        # Ensure we have the full path to the script
        if not os.path.isabs(script_path):
            script_path = os.path.join(os.getcwd(), script_path)
        
        # Verify script exists
        if not os.path.exists(script_path):
            error_msg = safe_get_messages(message.chat.id).ADMIN_SCRIPT_NOT_FOUND_MSG.format(script_path=script_path)
            await safe_send_message_with_auto_delete(message.chat.id, error_msg, delete_after_seconds=60)
            await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_SCRIPT_NOT_FOUND_LOG_MSG.format(script_path=script_path))
            return
            
        # Send initial status message (skip for fake_message)
        status_msg = None
        if not is_fake_message:
            status_msg = await safe_send_message(message.chat.id, safe_get_messages(message.chat.id).ADMIN_DOWNLOADING_MSG.format(script_path=script_path))
            if not status_msg:
                await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_FAILED_SEND_STATUS_LOG_MSG)
                return
        
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=os.path.dirname(os.path.dirname(script_path)))
        if result.returncode != 0:
            error_msg = safe_get_messages(message.chat.id).ADMIN_ERROR_SCRIPT_MSG.format(script_path=script_path, stdout=result.stdout, stderr=result.stderr)
            if is_fake_message:
                # Do not send anything to chat on fake_message
                from HELPERS.logger import log_error_to_channel
                await log_error_to_channel(message, error_msg)
                await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG.format(script_path=script_path, stdout=result.stdout, stderr=result.stderr))
            else:
                await safe_edit_message_text(message.chat.id, status_msg.id, error_msg)
                # Schedule deletion after 60 seconds for real messages
                async def delete_msg():
                    messages = safe_get_messages(message.chat.id)
                    time.sleep(60)
                    await safe_delete_messages(message.chat.id, [status_msg.id])
                threading.Thread(target=delete_msg, daemon=True).start()
                from HELPERS.logger import log_error_to_channel
                await log_error_to_channel(message, error_msg)
                await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG.format(script_path=script_path, stdout=result.stdout, stderr=result.stderr))
            return
        
        # Update status to reloading
        if is_fake_message:
            # Do not send anything to chat on fake_message
            pass
        else:
            await safe_edit_message_text(message.chat.id, status_msg.id, safe_get_messages(message.chat.id).ADMIN_RELOADING_CACHE_MSG)
        
        # 2) Reload local cache into memory
        from DATABASE.cache_db import reload_firebase_cache as _reload_local
        success = _reload_local()
        if success:
            final_msg = safe_get_messages(message.chat.id).ADMIN_CACHE_RELOADED_MSG
            if is_fake_message:
                # Only log to channel/logger
                await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_CACHE_RELOADED_AUTO_LOG_MSG)
            else:
                await safe_edit_message_text(message.chat.id, status_msg.id, final_msg)
                # Schedule deletion after 60 seconds for real messages
                async def delete_msg():
                    time.sleep(60)
                    await safe_delete_messages(message.chat.id, [status_msg.id])
                threading.Thread(target=delete_msg, daemon=True).start()
                await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG)
        else:
            cache_file = getattr(Config, 'FIREBASE_CACHE_FILE', 'firebase_cache.json')
            final_msg = safe_get_messages(message.chat.id).ADMIN_CACHE_FAILED_MSG.format(cache_file=cache_file)
            if is_fake_message:
                # Only log to channel/logger
                from HELPERS.logger import log_error_to_channel
                await log_error_to_channel(message, final_msg)
                await send_to_logger(message, final_msg)
            else:
                await safe_edit_message_text(message.chat.id, status_msg.id, final_msg)
                # Schedule deletion after 60 seconds for real messages
                async def delete_msg():
                    time.sleep(60)
                    await safe_delete_messages(message.chat.id, [status_msg.id])
                threading.Thread(target=delete_msg, daemon=True).start()
                from HELPERS.logger import log_error_to_channel
                await log_error_to_channel(message, final_msg)
    except Exception as e:
        # ГЛОБАЛЬНАЯ ЗАЩИТА: Убедимся, что messages инициализирована
        if 'messages' not in locals() or messages is None:
            try:
                messages = safe_get_messages(message.chat.id)
            except Exception:
                # Если все не удается, создаем минимальную защиту
                class EmergencyMessages:
                    async def __getattr__(self, name):
                        return f"[{name}]"
                messages = EmergencyMessages()
        error_msg = safe_get_messages(message.chat.id).ADMIN_ERROR_RELOADING_MSG.format(error=str(e))
        # Try to update the status message if it exists, otherwise send new message
        if 'status_msg' in locals() and status_msg and not is_fake_message:
            await safe_edit_message_text(message.chat.id, status_msg.id, error_msg)
            # Schedule deletion after 60 seconds
            async def delete_msg():
                time.sleep(60)
                await safe_delete_messages(message.chat.id, [status_msg.id])
            threading.Thread(target=delete_msg, daemon=True).start()
        else:
            # For fake messages, do not send to chat; only log
            if not is_fake_message:
                await safe_send_message_with_auto_delete(message.chat.id, error_msg, delete_after_seconds=60)
        from HELPERS.logger import log_error_to_channel
        await log_error_to_channel(message, error_msg)
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_ERROR_RELOADING_CACHE_LOG_MSG.format(error=str(e)))

# SEND BRODCAST Message to All Users

async def send_promo_message(app, message):
    messages = safe_get_messages(message.chat.id)
    # We get a list of users from the base
    user_nodes = db.child("bot").child(Config.BOT_NAME_FOR_USERS).child("users").get().each()
    user_nodes = user_nodes or []
    user_lst = []
    for user in user_nodes:
        try:
            key = user.key()
            if key is not None:
                user_lst.append(int(key))
        except Exception:
            continue
    # Add administrators if they are not on the list
    for admin in Config.ADMIN:
        if admin not in user_lst:
            user_lst.append(admin)

    # We extract the text of Boadcast. If the message contains lines transfers, take all the lines after the first.
    lines = message.text.splitlines()
    if len(lines) > 1:
        broadcast_text = "\n".join(lines[1:]).strip()
    else:
        broadcast_text = message.text[len(Config.BROADCAST_MESSAGE):].strip()

    # If the message is a reference, we get it
    reply = message.reply_to_message if message.reply_to_message else None

    await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_BROADCAST_INITIATED_LOG_MSG.format(broadcast_text=broadcast_text))

    try:
        # We send a message to all users
        for user in user_lst:
            try:
                if user != 0:
                    # If the message is a reference, send it (depending on the type of content)
                    if reply:
                        try:
                            if reply.text:
                                await safe_send_message_async(user, reply.text)
                            elif reply.video:
                                await app.send_video(user, reply.video.file_id, caption=reply.caption)
                            elif reply.photo:
                                try:
                                    # Use supported API: take the largest available size's file_id
                                    largest = reply.photo.sizes[-1] if getattr(reply.photo, 'sizes', None) else None
                                    file_id = largest.file_id if largest else None
                                except Exception:
                                    file_id = None
                                if file_id:
                                    await app.send_photo(user, file_id, caption=reply.caption)
                                else:
                                    # Fallback: try to forward original message with photo
                                    try:
                                        await app.copy_message(chat_id=user, from_chat_id=message.chat.id, message_id=reply.id)
                                    except Exception:
                                        pass
                            elif reply.sticker:
                                await app.send_sticker(user, reply.sticker.file_id)
                            elif reply.document:
                                await app.send_document(user, reply.document.file_id, caption=reply.caption)
                            elif reply.audio:
                                await app.send_audio(user, reply.audio.file_id, caption=reply.caption)
                            elif reply.animation:
                                await app.send_animation(user, reply.animation.file_id, caption=reply.caption)
                        except AttributeError as e:
                            logger.error(safe_get_messages(message.chat.id).ADMIN_ERROR_PROCESSING_REPLY_MSG.format(user=user, error=e))
                            continue
                    # If there is an additional text, we send it
                    if broadcast_text:
                        await safe_send_message_async(user, broadcast_text)
            except Exception as e:
                logger.error(safe_get_messages(message.chat.id).ADMIN_ERROR_SENDING_BROADCAST_MSG.format(user=user, error=e))
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_PROMO_SENT_MSG)
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_BROADCAST_SENT_LOG_MSG)
    except Exception as e:
        await send_error_to_user(message, safe_get_messages(message.chat.id).ADMIN_CANNOT_SEND_PROMO_MSG)
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_BROADCAST_FAILED_LOG_MSG.format(error=str(e)))


# Getting the User Logs

async def get_user_log(app, message):
    messages = safe_get_messages(message.chat.id)
    # Lazy import to avoid cycles
    from DATABASE.cache_db import get_from_local_cache
    user_id = str(message.chat.id)
    if int(message.chat.id) in Config.ADMIN and Config.GET_USER_LOGS_COMMAND in message.text:
        user_id = message.text.split(Config.GET_USER_LOGS_COMMAND + " ")[1]

    logs_dict = get_from_local_cache(["bot", Config.BOT_NAME_FOR_USERS, "logs", user_id])
    if not logs_dict:
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_USER_NO_DOWNLOADS_MSG)
        return

    logs = list(logs_dict.values())
    data, data_tg = [], []

    for l in logs:
        ts_raw = l.get("timestamp")
        try:
            ts = datetime.fromtimestamp(int(ts_raw)) if ts_raw is not None else datetime.fromtimestamp(0)
        except Exception:
            ts = datetime.fromtimestamp(0)
        id_val = l.get('ID', '-')
        name_val = l.get('name', '-')
        title_val = l.get('title', '-')
        urls_val = l.get('urls', '-')
        row = f"{ts} | {id_val} | {name_val} | {title_val} | {urls_val}"
        row_2 = f"<b>{ts}</b> | <code>{id_val}</code> | <b>{name_val}</b> | {title_val} | {urls_val}"
        data.append(row)
        data_tg.append(row_2)

    total = len(data_tg)
    least_10 = sorted(data_tg[-10:], key=str.lower) if total and total > 10 else sorted(data_tg, key=str.lower)
    format_str = "\n\n".join(least_10)
    now = datetime.fromtimestamp(math.floor(time.time()))
    txt_format = safe_get_messages(message.chat.id).ADMIN_LOGS_FORMAT_MSG.format(bot_name=Config.BOT_NAME_FOR_USERS, user_id=user_id, total=total, now=now, logs='\n'.join(sorted(data, key=str.lower)))

    user_dir = os.path.join("users", str(message.chat.id))
    os.makedirs(user_dir, exist_ok=True)
    log_path = os.path.join(user_dir, "logs.txt")
    with open(log_path, 'w', encoding="utf-8") as f:
        f.write(txt_format)

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(safe_get_messages(message.chat.id).URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG, callback_data="userlogs_close|close")]])
    from HELPERS.safe_messeger import safe_send_message_async
    await safe_send_message_async(message.chat.id, safe_get_messages(message.chat.id).ADMIN_USER_LOGS_TOTAL_MSG.format(total=total, user_id=user_id, format_str=format_str), parse_mode=enums.ParseMode.HTML, reply_markup=keyboard)
    await app.send_document(message.chat.id, log_path, caption=safe_get_messages(message.chat.id).ADMIN_USER_LOGS_CAPTION_MSG.format(user_id=user_id))
    from HELPERS.logger import get_log_channel
    await app.send_document(get_log_channel("general"), log_path, caption=safe_get_messages(message.chat.id).ADMIN_USER_LOGS_CAPTION_MSG.format(user_id=user_id))


async def get_user_usage_stats(app, message):
    """Get usage statistics for regular users"""
    # Lazy import to avoid cycles
    from DATABASE.cache_db import get_from_local_cache
    user_id = str(message.chat.id)

    logs_dict = get_from_local_cache(["bot", Config.BOT_NAME_FOR_USERS, "logs", user_id])
    if not logs_dict:
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_USER_NO_DOWNLOADS_MSG)
        return

    logs = list(logs_dict.values())
    data, data_tg = [], []

    for l in logs:
        ts_raw = l.get("timestamp")
        try:
            ts = datetime.fromtimestamp(int(ts_raw)) if ts_raw is not None else datetime.fromtimestamp(0)
        except Exception:
            ts = datetime.fromtimestamp(0)
        id_val = l.get('ID', '-')
        name_val = l.get('name', '-')
        title_val = l.get('title', '-')
        urls_val = l.get('urls', '-')
        row = f"{ts} | {id_val} | {name_val} | {title_val} | {urls_val}"
        row_2 = f"<b>{ts}</b> | <code>{id_val}</code> | <b>{name_val}</b> | {title_val} | {urls_val}"
        data.append(row)
        data_tg.append(row_2)

    total = len(data_tg)
    least_10 = sorted(data_tg[-10:], key=str.lower) if total and total > 10 else sorted(data_tg, key=str.lower)
    format_str = "\n\n".join(least_10)
    now = datetime.fromtimestamp(math.floor(time.time()))
    txt_format = safe_get_messages(message.chat.id).ADMIN_LOGS_FORMAT_MSG.format(bot_name=Config.BOT_NAME_FOR_USERS, user_id=user_id, total=total, now=now, logs='\n'.join(sorted(data, key=str.lower)))

    user_dir = os.path.join("users", str(message.chat.id))
    os.makedirs(user_dir, exist_ok=True)
    log_path = os.path.join(user_dir, "logs.txt")
    with open(log_path, 'w', encoding="utf-8") as f:
        f.write(txt_format)

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(safe_get_messages(message.chat.id).URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG, callback_data="userlogs_close|close")]])
    from HELPERS.safe_messeger import safe_send_message_async
    await safe_send_message_async(message.chat.id, safe_get_messages(message.chat.id).ADMIN_USER_LOGS_TOTAL_MSG.format(total=total, user_id=user_id, format_str=format_str), parse_mode=enums.ParseMode.HTML, reply_markup=keyboard)
    await app.send_document(message.chat.id, log_path, caption=safe_get_messages(message.chat.id).ADMIN_USER_LOGS_CAPTION_MSG.format(user_id=user_id))


# Get All Kinds of Users (Users/ Blocked/ Unblocked)

async def get_user_details(app, message):
    messages = safe_get_messages(message.chat.id)
    # Lazy import
    from DATABASE.cache_db import get_from_local_cache
    command = message.text.split(Config.GET_USER_DETAILS_COMMAND)[1].strip()
    path_map = {
        "_blocked": "blocked_users",
        "_unblocked": "unblocked_users",
        "_users": "users"
    }
    path = path_map.get(command)
    if not path:
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_INVALID_COMMAND_MSG)
        return

    data_dict = get_from_local_cache(["bot", Config.BOT_NAME_FOR_USERS, path])
    if not data_dict:
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_NO_DATA_FOUND_MSG.format(path=path))
        return

    # Support both dict and list structures from cache
    if isinstance(data_dict, dict):
        iterable = data_dict.values()
    elif isinstance(data_dict, list):
        iterable = data_dict
    else:
        iterable = []

    modified_lst, txt_lst = [], []
    for user in iterable:
        try:
            if isinstance(user, dict):
                user_id = str(user.get("ID")) if user.get("ID") is not None else None
                ts_raw = user.get("timestamp")
            else:
                # If element is not dict, treat it as a user id
                user_id = str(user)
                ts_raw = None

            if not user_id or user_id == "0":
                continue

            try:
                ts_val = int(ts_raw) if ts_raw is not None else 0
            except Exception:
                ts_val = 0
            ts = datetime.fromtimestamp(ts_val)

            txt_lst.append(f"TS: {ts} | ID: {user_id}")
            modified_lst.append(f"TS: <b>{ts}</b> | ID: <code>{user_id}</code>")
        except Exception:
            continue

    modified_lst.sort(key=str.lower)
    txt_lst.sort(key=str.lower)
    display_list = modified_lst[-20:] if len(modified_lst) > 20 else modified_lst

    now = datetime.fromtimestamp(math.floor(time.time()))
    txt_format = safe_get_messages(message.chat.id).ADMIN_BOT_DATA_FORMAT_MSG.format(bot_name=Config.BOT_NAME_FOR_USERS, path=path, count=len(modified_lst), now=now, data='\n'.join(txt_lst))
    mod = safe_get_messages(message.chat.id).ADMIN_TOTAL_USERS_MSG.format(count=len(modified_lst), path=path, display_list='\n'.join(display_list))

    file = f"{path}.txt"
    with open(file, 'w', encoding="utf-8") as f:
        f.write(txt_format)

    await send_to_all(message, mod)
    await app.send_document(message.chat.id, f"./{file}", caption=safe_get_messages(message.chat.id).ADMIN_BOT_DATA_CAPTION_MSG.format(bot_name=Config.BOT_NAME_FOR_USERS, path=path))
    from HELPERS.logger import get_log_channel
    await app.send_document(get_log_channel("general"), f"./{file}", caption=safe_get_messages(message.chat.id).ADMIN_BOT_DATA_CAPTION_MSG.format(bot_name=Config.BOT_NAME_FOR_USERS, path=path))
    logger.info(mod)

# Block User

async def block_user(app, message):
    messages = safe_get_messages(message.chat.id)
    if int(message.chat.id) in Config.ADMIN:
        dt = math.floor(time.time())
        parts = (message.text or "").strip().split(maxsplit=1)
        if len(parts) < 2:
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_BLOCK_USER_USAGE_MSG)
            return
        b_user_id = parts[1].strip()

        try:
            if int(b_user_id) in Config.ADMIN:
                await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_CANNOT_DELETE_ADMIN_MSG)
                return
        except Exception:
            pass

        snapshot = db.child(f"{Config.BOT_DB_PATH}/blocked_users").get()
        all_blocked_users = snapshot.each() if snapshot else []
        b_users = [str(b_user.key()) for b_user in (all_blocked_users or []) if b_user is not None]

        if b_user_id not in b_users:
            data = {"ID": b_user_id, "timestamp": str(dt)}
            db.child(f"{Config.BOT_DB_PATH}/blocked_users/{b_user_id}").set(data)
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_USER_BLOCKED_MSG.format(user_id=b_user_id, date=datetime.fromtimestamp(dt)))
        else:
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_USER_ALREADY_BLOCKED_MSG.format(user_id=b_user_id))
    else:
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_NOT_ADMIN_MSG)


# Unblock User

async def unblock_user(app, message):
    messages = safe_get_messages(message.chat.id)
    if int(message.chat.id) in Config.ADMIN:
        parts = (message.text or "").strip().split(maxsplit=1)
        if len(parts) < 2:
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_UNBLOCK_USER_USAGE_MSG)
            return
        ub_user_id = parts[1].strip()

        snapshot = db.child(f"{Config.BOT_DB_PATH}/blocked_users").get()
        all_blocked_users = snapshot.each() if snapshot else []
        b_users = [str(b_user.key()) for b_user in (all_blocked_users or []) if b_user is not None]

        if ub_user_id in b_users:
            dt = math.floor(time.time())

            data = {"ID": ub_user_id, "timestamp": str(dt)}
            db.child(f"{Config.BOT_DB_PATH}/unblocked_users/{ub_user_id}").set(data)
            db.child(f"{Config.BOT_DB_PATH}/blocked_users/{ub_user_id}").remove()
            await send_to_user(
                message, safe_get_messages(message.chat.id).ADMIN_USER_UNBLOCKED_MSG.format(user_id=ub_user_id, date=datetime.fromtimestamp(dt)))

        else:
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_USER_ALREADY_UNBLOCKED_MSG.format(user_id=ub_user_id))
    else:
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_NOT_ADMIN_MSG)


# Check Runtime

async def check_runtime(message):
    messages = safe_get_messages(message.chat.id)
    if int(message.chat.id) in Config.ADMIN:
        now = time.time()
        now = math.floor((now - starting_point[0]) * 1000)
        now = TimeFormatter(now)
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_BOT_RUNNING_TIME_MSG.format(time=now))
    pass



async def uncache_command(app, message):
    messages = safe_get_messages(message.chat.id)
    """
    Admin command to clear cache for a specific URL
    Usage: /uncache <URL>
    """
    # Lazy imports to avoid cycles
    from DATABASE.cache_db import get_url_hash
    from DATABASE.firebase_init import db_child_by_path

    user_id = message.chat.id
    text = message.text.strip()
    if len(text.split()) < 2:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_UNCACHE_USAGE_MSG)
        return
    url = text.split(maxsplit=1)[1].strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_UNCACHE_INVALID_URL_MSG)
        return
    removed_any = False
    try:
        # Clearing the cache by video
        normalized_url = normalize_url_for_cache(url)
        url_hash = get_url_hash(normalized_url)
        video_cache_path = f"{Config.VIDEO_CACHE_DB_PATH}/{url_hash}"
        db_child_by_path(db, video_cache_path).remove()
        removed_any = True
        # Clear cache by image posts (for /img)
        try:
            img_cache_path = f"{Config.IMAGE_CACHE_DB_PATH}/{url_hash}"
            db_child_by_path(db, img_cache_path).remove()
            removed_any = True
        except Exception:
            pass
        # Clear cache by playlist (if any)
        playlist_url = get_clean_playlist_url(url)
        if playlist_url:
            playlist_normalized = normalize_url_for_cache(playlist_url)
            playlist_hash = get_url_hash(playlist_normalized)
            playlist_cache_path = f"{Config.PLAYLIST_CACHE_DB_PATH}/{playlist_hash}"
            db_child_by_path(db, playlist_cache_path).remove()
            removed_any = True
            # If there is a range (eg *1*5), clear the cache for each index
            m = re.search(r"\*(\d+)\*(\d+)", url)
            if m:
                start, end = int(m.group(1)), int(m.group(2))
                for idx in range(start, end + 1):
                    idx_path = f"{Config.PLAYLIST_CACHE_DB_PATH}/{playlist_hash}/{idx}"
                    db_child_by_path(db, idx_path).remove()
        # Clear cache for short/long YouTube links
        if is_youtube_url(url):
            short_url = youtube_to_short_url(url)
            long_url = youtube_to_long_url(url)
            for variant in [short_url, long_url]:
                norm = normalize_url_for_cache(variant)
                h = get_url_hash(norm)
                db_child_by_path(db, f"{Config.VIDEO_CACHE_DB_PATH}/{h}").remove()
                db_child_by_path(db, f"{Config.PLAYLIST_CACHE_DB_PATH}/{h}").remove()
        if removed_any:
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_CACHE_CLEARED_MSG.format(url=url))
            await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_CACHE_CLEARED_LOG_MSG.format(user_id=user_id, url=url))
        else:
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_NO_CACHE_FOUND_MSG)
    except Exception as e:
        await send_to_all(message, safe_get_messages(message.chat.id).ADMIN_ERROR_CLEARING_CACHE_MSG.format(error=e))


async def update_porn_command(app, message):
    messages = safe_get_messages(message.chat.id)
    """Admin command to run the porn list update script"""
    if int(message.chat.id) not in Config.ADMIN:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_ACCESS_DENIED_MSG)
        return
    
    script_path = getattr(Config, "UPDATE_PORN_SCRIPT_PATH", "./script.sh")
    
    try:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_UPDATE_PORN_RUNNING_MSG.format(script_path=script_path))
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_PORN_UPDATE_STARTED_LOG_MSG.format(user_id=message.chat.id, script_path=script_path))
        
        # Run the script
        result = subprocess.run(
            [script_path], 
            capture_output=True, 
            text=True, 
            encoding='utf-8', 
            errors='replace',
            cwd=os.getcwd()  # Run from bot root directory
        )
        
        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG.format(output=output))
            else:
                await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_SCRIPT_COMPLETED_MSG)
            await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG.format(user_id=message.chat.id))
        else:
            error_msg = result.stderr.strip() if result.stderr else "Unknown error"
            await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_SCRIPT_FAILED_MSG.format(returncode=result.returncode, error=error_msg))
            await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_PORN_UPDATE_FAILED_LOG_MSG.format(user_id=message.chat.id, error=error_msg))
            
    except FileNotFoundError:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_SCRIPT_NOT_FOUND_MSG.format(script_path=script_path))
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_SCRIPT_NOT_FOUND_LOG_MSG.format(user_id=message.chat.id, script_path=script_path))
    except Exception as e:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_ERROR_RUNNING_SCRIPT_MSG.format(error=str(e)))
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_PORN_UPDATE_ERROR_LOG_MSG.format(user_id=message.chat.id, error=str(e)))


async def reload_porn_command(app, message):
    messages = safe_get_messages(message.chat.id)
    """Admin command to reload porn domains and keywords cache without restarting the bot"""
    if int(message.chat.id) not in Config.ADMIN:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_ACCESS_DENIED_MSG)
        return
    
    try:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_RELOADING_PORN_MSG)
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG.format(user_id=message.chat.id))
        
        # Import and reload all caches (files + CONFIG/domains.py arrays)
        from HELPERS.porn import reload_all_porn_caches
        counts = reload_all_porn_caches()

        await send_to_user(
            message,
            safe_get_messages(message.chat.id).ADMIN_PORN_CACHES_RELOADED_MSG.format(
                porn_domains=counts.get('porn_domains', 0),
                porn_keywords=counts.get('porn_keywords', 0),
                supported_sites=counts.get('supported_sites', 0),
                whitelist=counts.get('whitelist', 0),
                greylist=counts.get('greylist', 0),
                black_list=counts.get('black_list', 0),
                white_keywords=counts.get('white_keywords', 0),
                proxy_domains=counts.get('proxy_domains', 0),
                proxy_2_domains=counts.get('proxy_2_domains', 0),
                clean_query=counts.get('clean_query', 0),
                no_cookie_domains=counts.get('no_cookie_domains', 0)
            )
        )

        await send_to_logger(
            message,
            safe_get_messages(message.chat.id).ADMIN_PORN_CACHE_RELOADED_MSG.format(
                admin_id=message.chat.id,
                domains=counts.get('porn_domains', 0),
                keywords=counts.get('porn_keywords', 0),
                sites=counts.get('supported_sites', 0),
                whitelist=counts.get('whitelist', 0),
                greylist=counts.get('greylist', 0),
                black_list=counts.get('black_list', 0),
                white_keywords=counts.get('white_keywords', 0),
                proxy_domains=counts.get('proxy_domains', 0),
                proxy_2_domains=counts.get('proxy_2_domains', 0),
                clean_query=counts.get('clean_query', 0),
                no_cookie_domains=counts.get('no_cookie_domains', 0)
            )
        )
        
    except Exception as e:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_ERROR_RELOADING_PORN_MSG.format(error=str(e)))
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG.format(user_id=message.chat.id, error=str(e)))


async def check_porn_command(app, message):
    messages = safe_get_messages(message.chat.id)
    """Admin command to check if a URL is NSFW and get detailed explanation"""
    user_id = message.chat.id
    
    # First check if user is subscribed to channel
    if not await is_user_in_channel(app, message):
        return
    
    # Then check if user is admin
    if int(user_id) not in Config.ADMIN:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_ACCESS_DENIED_MSG)
        return
    
    text = message.text.strip()
    if len(text.split()) < 2:
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_CHECK_PORN_USAGE_MSG)
        return
    
    url = text.split(maxsplit=1)[1].strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        await send_to_user(message, safe_get_messages(message.chat.id).ADMIN_CHECK_PORN_INVALID_URL_MSG)
        return
    
    try:
        # Send initial status message
        status_msg = await safe_send_message(user_id, safe_get_messages(message.chat.id).ADMIN_CHECKING_URL_MSG.format(url=url), parse_mode=enums.ParseMode.HTML)
        
        # Import the detailed check function
        from HELPERS.porn import check_porn_detailed
        
        # For now, we'll check without title/description since we don't have video info
        # In a real scenario, you might want to fetch video info first
        is_nsfw, explanation = check_porn_detailed(url, "", "", None)
        
        # Format the result
        status_icon = safe_get_messages(message.chat.id).ADMIN_STATUS_NSFW_MSG if is_nsfw else safe_get_messages(message.chat.id).ADMIN_STATUS_CLEAN_MSG
        status_text = safe_get_messages(message.chat.id).ADMIN_STATUS_NSFW_TEXT_MSG if is_nsfw else safe_get_messages(message.chat.id).ADMIN_STATUS_CLEAN_TEXT_MSG
        
        result_message = safe_get_messages(message.chat.id).ADMIN_PORN_CHECK_RESULT_MSG.format(
            status_icon=status_icon,
            url=url,
            status_text=status_text,
            explanation=explanation
        )
        
        # Update the status message with results
        if status_msg:
            await safe_edit_message_text(message.chat.id, status_msg.id, result_message, parse_mode=enums.ParseMode.HTML)
        else:
            await safe_send_message(user_id, result_message, parse_mode=enums.ParseMode.HTML)
        
        # Log the check
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_PORN_CHECK_LOG_MSG.format(user_id=message.chat.id, url=url, status=status_text))
        
    except Exception as e:
        error_msg = safe_get_messages(message.chat.id).ADMIN_ERROR_CHECKING_URL_MSG.format(error=str(e))
        if 'status_msg' in locals() and status_msg:
            await safe_edit_message_text(message.chat.id, status_msg.id, error_msg)
        else:
            await safe_send_message(user_id, error_msg, parse_mode=enums.ParseMode.HTML)
        await send_to_logger(message, safe_get_messages(message.chat.id).ADMIN_CHECK_PORN_ERROR_LOG_MSG.format(admin_id=message.chat.id, error=str(e)))

