"""
Core download functionality with yt-dlp integration
"""
import os
import time
import logging
import subprocess
import threading
import shutil
from pyrogram.errors import FloodWait
import yt_dlp
from config import Config

logger = logging.getLogger(__name__)

# Global variables for playlist error tracking
playlist_errors = {}
playlist_errors_lock = threading.Lock()

def down_and_up(app, message, url, playlist_name, video_count, video_start_with, tags_text, force_no_title=False, format_override=None, quality_key=None):
    """
    Now if part of the playlist range is already cached, we first repost the cached indexes, then download and cache the missing ones, without finishing after reposting part of the range.
    """
    playlist_indices = []
    playlist_msg_ids = []    

    user_id = message.chat.id
    logger.info(f"down_and_up called: url={url}, quality_key={quality_key}, format_override={format_override}, video_count={video_count}, video_start_with={video_start_with}")
    
    # Import needed functions from other modules
    from magic.processing.tags import is_playlist_with_range, generate_final_tags, save_user_tags
    from magic.download.cache import get_cached_playlist_videos, get_cached_message_ids, save_to_video_cache, save_to_playlist_cache, get_clean_playlist_url
    from magic.utils.filesystem import create_directory, cleanup_user_temp_files, get_user_split_size, check_disk_space, sanitize_filename
    from magic.utils.communication import safe_send_message, safe_forward_messages, safe_edit_message_text, safe_delete_messages, start_hourglass_animation, start_cycle_progress, send_to_logger, send_to_user, send_to_all
    from magic.utils.formatters import humanbytes, TimeFormatter
    from magic.processing.video import send_videos, get_duration_thumb, create_default_thumbnail, split_video_2
    from magic.processing.url_parser import extract_youtube_id, download_thumbnail
    from magic.database.firebase import write_logs, check_user
    from magic.user.settings import is_mediainfo_enabled, send_mediainfo_if_enabled
    from magic.download.quality import ceil_to_popular
    from magic.utils.filesystem import set_active_download, clear_download_start_time, check_download_timeout
    
    # We define a playlist not only by the number of videos, but also by the presence of a range in the URL
    original_text = message.text or message.caption or ""
    is_playlist = video_count > 1 or is_playlist_with_range(original_text)
    requested_indices = list(range(video_start_with, video_start_with + video_count)) if is_playlist else []
    cached_videos = {}
    uncached_indices = []
    if quality_key and is_playlist:
        cached_videos = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, requested_indices)
        uncached_indices = [i for i in requested_indices if i not in cached_videos]
        # First, repost the cached ones
        if cached_videos:
            for index in requested_indices:
                if index in cached_videos:
                    try:
                        app.forward_messages(
                            chat_id=user_id,
                            from_chat_id=Config.LOGS_ID,
                            message_ids=[cached_videos[index]]
                        )
                    except Exception as e:
                        logger.error(f"down_and_up: error reposting cached video index={index}: {e}")
            if len(uncached_indices) == 0:
                app.send_message(user_id, f"✅ Playlist videos sent from cache ({len(cached_videos)}/{len(requested_indices)} files).", reply_to_message_id=message.id)
                send_to_logger(message, f"Playlist videos sent from cache (quality={quality_key}) to user {user_id}")
                return
            else:
                app.send_message(user_id, f"♻️ {len(cached_videos)}/{len(requested_indices)} videos sent from cache, downloading missing ones...", reply_to_message_id=message.id)
    elif quality_key and not is_playlist:
        cached_ids = get_cached_message_ids(url, quality_key)
        if cached_ids:
            try:
                app.forward_messages(
                    chat_id=user_id,
                    from_chat_id=Config.LOGS_ID,
                    message_ids=cached_ids
                )
                app.send_message(user_id, "✅ Video sent from cache.", reply_to_message_id=message.id)
                send_to_logger(message, f"Video sent from cache (quality={quality_key}) to user {user_id}")
                return
            except Exception as e:
                logger.error(f"Error reposting video from cache: {e}")
                save_to_video_cache(url, quality_key, [], clear=True)
                app.send_message(user_id, "⚠️ Unable to get video from cache, starting new download...", reply_to_message_id=message.id)
    else:
        logger.info(f"down_and_up: quality_key is None, skipping cache check")

    status_msg = None
    status_msg_id = None
    hourglass_msg = None
    hourglass_msg_id = None
    anim_thread = None
    stop_anim = threading.Event()
    proc_msg = None
    proc_msg_id = None
    try:
        # Check if there is a saved waiting time
        user_dir = os.path.join("users", str(user_id))
        flood_time_file = os.path.join(user_dir, "flood_wait.txt")

        # We send the initial message
        if os.path.exists(flood_time_file):
            with open(flood_time_file, 'r') as f:
                wait_time = int(f.read().strip())
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = wait_time % 60
                time_str = f"{hours}h {minutes}m {seconds}s"
                proc_msg = app.send_message(user_id, f"⚠️ Telegram has limited message sending.\n\n⏳ Please wait: {time_str}\n\nTo update timer send URL again 2 times.")
        else:
            proc_msg = app.send_message(user_id, "⚠️ Telegram has limited message sending.\n\n⏳ Please wait: \n\nTo update timer send URL again 2 times.")

        # We are trying to replace with "Download started"
        try:
            app.edit_message_text(
                chat_id=user_id,
                message_id=proc_msg.id,
                text="Download started"
            )
            # If you managed to replace, then there is no flood error
            if os.path.exists(flood_time_file):
                os.remove(flood_time_file)
        except FloodWait as e:
            # Update the counter
            wait_time = e.value
            os.makedirs(user_dir, exist_ok=True)
            with open(flood_time_file, 'w') as f:
                f.write(str(wait_time))
            return
        except Exception as e:
            logger.error(f"Error editing message: {e}")
            return

        # If there is no flood error, send a normal message
        proc_msg = app.send_message(user_id, "Processing... ♻️", reply_to_message_id=message.id)
        proc_msg_id = proc_msg.id
        error_message = ""
        status_msg = None
        status_msg_id = None
        hourglass_msg = None
        hourglass_msg_id = None
        anim_thread = start_hourglass_animation(user_id, hourglass_msg_id, stop_anim)

        # Check if there's enough disk space (estimate 2GB per video)
        user_dir_name = os.path.abspath(os.path.join("users", str(user_id)))
        create_directory(user_dir_name)

        # We only need disk space for one video at a time, since files are deleted after upload
        if not check_disk_space(user_dir_name, 2 * 1024 * 1024 * 1024):
            send_to_user(message, f"❌ Not enough disk space to download videos.")
            return

        check_user(message)

        # Reset of the flag of errors for the new launch of the playlist
        if playlist_name:
            with playlist_errors_lock:
                error_key = f"{user_id}_{playlist_name}"
                if error_key in playlist_errors:
                    del playlist_errors[error_key]

        # if use_default_format is True, then do not take from format.txt, but use default ones
        custom_format_path = os.path.join(user_dir_name, "format.txt")
        use_default_format = False
        if not format_override and os.path.exists(custom_format_path):
            with open(custom_format_path, "r", encoding="utf-8") as f:
                custom_format = f.read().strip()
            if custom_format == "ALWAYS_ASK":
                use_default_format = True
        if use_default_format:
            format_override = None

        if format_override:
            attempts = [{'format': format_override, 'prefer_ffmpeg': True, 'merge_output_format': 'mp4'}]
        else:
            # if use_default_format is True, then do not take from format.txt, but use default ones
            if use_default_format:
                attempts = [
                    {'format': 'bestvideo+bestaudio/best', 'prefer_ffmpeg': True, 'merge_output_format': 'mp4', 'extract_flat': False},
                    {'format': 'best', 'prefer_ffmpeg': False, 'extract_flat': False}
                ]
            else:
                if os.path.exists(custom_format_path):
                    with open(custom_format_path, "r", encoding="utf-8") as f:
                        custom_format = f.read().strip()
                    if custom_format.lower() == "best":
                        attempts = [{'format': custom_format, 'prefer_ffmpeg': False}]
                    else:
                        attempts = [{'format': custom_format, 'prefer_ffmpeg': True, 'merge_output_format': 'mp4'}]
                else:
                    attempts = [
                        {'format': 'bv*[vcodec*=avc1][height<=1080]+ba[acodec*=mp4a]/bv*[vcodec*=avc1]+ba/best',
                        'prefer_ffmpeg': True, 'merge_output_format': 'mp4', 'extract_flat': False},
                        {'format': 'bestvideo+bestaudio/best',
                        'prefer_ffmpeg': True, 'merge_output_format': 'mp4', 'extract_flat': False},
                        {'format': 'best', 'prefer_ffmpeg': False, 'extract_flat': False}
                    ]

        status_msg = app.send_message(user_id, "📹 Video is processing...")
        hourglass_msg = app.send_message(user_id, "⌛️")
        # We save ID status messages
        status_msg_id = status_msg.id
        hourglass_msg_id = hourglass_msg.id

        anim_thread = start_hourglass_animation(user_id, hourglass_msg_id, stop_anim)

        current_total_process = ""
        last_update = 0
        full_bar = "🟩" * 10
        first_progress_update = True  # Flag for tracking the first update

        def progress_func(d):
            nonlocal last_update, first_progress_update
            # Check the timaut
            if check_download_timeout(user_id):
                raise Exception(f"Download timeout exceeded ({Config.DOWNLOAD_TIMEOUT // 3600} hours)")
            current_time = time.time()
            if current_time - last_update < 1.5:
                return
            if d.get("status") == "downloading":
                downloaded = d.get("downloaded_bytes", 0)
                total = d.get("total_bytes", 0)
                percent = (downloaded / total * 100) if total else 0
                blocks = int(percent // 10)
                bar = "🟩" * blocks + "⬜️" * (10 - blocks)
                try:
                    # With the first renewal of progress, we delete the first posts Processing
                    if first_progress_update:
                        try:
                            # We get more messages to search for all Processing messages
                            messages = app.get_chat_history(user_id, limit=20)
                            processing_messages = []
                            download_started_messages = []
                            for msg in messages:
                                if msg.text == "Processing... ♻️":
                                    processing_messages.append(msg.id)
                                elif msg.text == "Download started":
                                    download_started_messages.append(msg.id)
                            # We delete the first 2 promission messages (if there are more than 1)
                            if len(processing_messages) >= 2:
                                safe_delete_messages(chat_id=user_id, message_ids=processing_messages[-2:], revoke=True)
                            # We delete the first 2 Download Started Message (if there are more than 1)
                            if len(download_started_messages) >= 2:
                                safe_delete_messages(chat_id=user_id, message_ids=download_started_messages[-2:], revoke=True)
                        except Exception as e:
                            logger.error(f"Error deleting first processing messages: {e}")
                        first_progress_update = False

                    safe_edit_message_text(user_id, proc_msg_id, f"{current_total_process}\n{bar}   {percent:.1f}%")
                except Exception as e:
                    logger.error(f"Error updating progress: {e}")
            elif d.get("status") == "error":
                logger.error("Error occurred during download.")
                send_to_all(message, "❌ Sorry... Some error occurred during download.")
            last_update = current_time

        successful_uploads = 0

        def try_download(url, attempt_opts):
            nonlocal current_total_process, error_message
            common_opts = {
                'cookiefile': os.path.join("users", str(user_id), os.path.basename(Config.COOKIE_FILE_PATH)),
                'playlist_items': str(current_index),  # We use only current_index for playlists
                'outtmpl': os.path.join(user_dir_name, "%(title)s.%(ext)s")
            }
            
            # If this is not a playlist with a range, add --no-playlist to the URL with the list parameter
            if not is_playlist and 'list=' in url:
                common_opts['noplaylist'] = True
            
            is_hls = ("m3u8" in url.lower())
            if not is_hls:
                common_opts['progress_hooks'] = [progress_func]
            ytdl_opts = {**common_opts, **attempt_opts}
            try:
                with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=False)
                if "entries" in info_dict:
                    entries = info_dict["entries"]
                    if not entries:
                        raise Exception(f"No videos found in playlist at index {current_index}")
                    if len(entries) > 1:  # If the video in the playlist is more than one
                        if current_index < len(entries):
                            info_dict = entries[current_index]
                        else:
                            raise Exception(f"Video index {current_index} out of range (total {len(entries)})")
                    else:
                        # If there is only one video in the playlist, just download it
                        info_dict = entries[0]  # Just take the first video

                if ("m3u8" in url.lower()) or (info_dict.get("protocol") == "m3u8_native"):
                    is_hls = True
                    # if "format" in ytdl_opts:
                    # del ytdl_opts["format"]
                    ytdl_opts["downloader"] = "ffmpeg"
                    ytdl_opts["hls_use_mpegts"] = True
                try:
                    if is_hls:
                        safe_edit_message_text(user_id, proc_msg_id,
                            f"{current_total_process}\n\n__Detected HLS stream. Downloading...__ 📥")
                    else:
                        safe_edit_message_text(user_id, proc_msg_id,
                            f"{current_total_process}\n\n> __Downloading using format: {ytdl_opts.get('format', 'default')}...__ 📥")
                except Exception as e:
                    logger.error(f"Status update error: {e}")
                with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                    if is_hls:
                        cycle_stop = threading.Event()
                        cycle_thread = start_cycle_progress(user_id, proc_msg_id, current_total_process, user_dir_name, cycle_stop)
                        try:
                            with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                                ydl.download([url])
                        finally:
                            cycle_stop.set()
                            cycle_thread.join(timeout=1)
                    else:
                        with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                            ydl.download([url])
                try:
                    safe_edit_message_text(user_id, proc_msg_id, f"{current_total_process}\n{full_bar}   100.0%")
                except Exception as e:
                    logger.error(f"Final progress update error: {e}")
                return info_dict
            except yt_dlp.utils.DownloadError as e:
                nonlocal error_message
                error_message = str(e)
                send_to_user(message, f"❌ Error downloading: {error_message}\n\nPerhaps cookie authorization is required. More information: https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp")
                logger.error(f"DownloadError: {error_message}")
                return None
            except Exception as e:
                error_message = str(e)
                logger.error(f"Attempt with format {ytdl_opts.get('format', 'default')} failed: {e}")
                
                # Check if this is a "No videos found in playlist" error - skip it
                if "No videos found in playlist" in str(e):
                    logger.info(f"Skipping playlist item at index {current_index} (no video found)")
                    return "SKIP"  # Special return value to indicate skip
                
                send_to_user(message, f"❌ Unknown error: {e}")
                return None

        if is_playlist and quality_key:
            indices_to_download = uncached_indices
        else:
            indices_to_download = range(video_count)
        for idx, current_index in enumerate(indices_to_download):
            x = current_index - video_start_with  # Don't add quality if size is unknown
            total_process = f"""
**📶 Total Progress**
> **Video:** {idx + 1} / {len(indices_to_download)}
"""

            current_total_process = total_process

            # Determine rename_name based on the incoming playlist_name:
            if playlist_name and playlist_name.strip():
                # A new name for the playlist is explicitly set - let's use it
                rename_name = sanitize_filename(f"{playlist_name.strip()} - Part {idx + video_start_with}")
            else:
                # No new name set - extract name from metadata
                rename_name = None

            info_dict = None
            skip_item = False
            for attempt in attempts:
                result = try_download(url, attempt)
                if result == "SKIP":
                    skip_item = True
                    break
                elif result is not None:
                    info_dict = result
                    break

            if skip_item:
                logger.info(f"Skipping item at index {current_index} (no video content)")
                continue

            if info_dict is None:
                with playlist_errors_lock:
                    error_key = f"{user_id}_{playlist_name}"
                    if error_key not in playlist_errors:
                        playlist_errors[error_key] = True
                        send_to_all(
                            message,
                            f"❌ Failed to download video: {error_message}\n────────────────\n"
                            "> Check [here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) if your site supported\n"
                            "> You may need `cookie` for downloading this video. First, clean your workspace via **/clean** command\n"
                            "> For Youtube - get `cookie` via **/download_cookie** command. For any other supported site - send your own cookie ([guide1](https://t.me/c/2303231066/18)) ([guide2](https://t.me/c/2303231066/22)) and after that send your video link again."
                        )
                break

            successful_uploads += 1

            video_id = info_dict.get("id", None)
            original_video_title = info_dict.get("title", None)  # Original title with emojis
            full_video_title = info_dict.get("description", original_video_title)
            video_title = sanitize_filename(original_video_title) if original_video_title else "video"  # Sanitized for file operations

            # --- Use new centralized function for all tags ---
            tags_text_final = generate_final_tags(url, tags_text.split(), info_dict)
            save_user_tags(user_id, tags_text_final.split())

           # If rename_name is not set, set it equal to video_title
            if rename_name is None:
                rename_name = video_title

            dir_path = os.path.join("users", str(user_id))

            # Save the full name to a file
            full_title_path = os.path.join(dir_path, "full_title.txt")
            try:
                with open(full_title_path, "w", encoding="utf-8") as f:
                    f.write(full_video_title if full_video_title else original_video_title)
            except Exception as e:
                logger.error(f"Error saving full title: {e}")

            info_text = f"""
{total_process}

**📋 Video Info**
> **Number:** {idx + video_start_with}
> **Title:** {original_video_title}
> **ID:** {video_id}
"""

            try:
                safe_edit_message_text(user_id, proc_msg_id,
                    f"{info_text}\n\n{full_bar}   100.0%\n\n__Downloaded video. Processing for upload...__ ♻️")
            except Exception as e:
                logger.error(f"Status update error after download: {e}")

            dir_path = os.path.join("users", str(user_id))
            allfiles = os.listdir(dir_path)
            files = [fname for fname in allfiles if fname.endswith(('.mp4', '.mkv', '.webm', '.ts'))]
            files.sort()
            if not files:
                send_to_all(message, f"Skipping unsupported file type in playlist at index {idx + video_start_with}")
                continue

            downloaded_file = files[0]
            write_logs(message, url, downloaded_file)

            if rename_name == video_title:
                caption_name = original_video_title  # Original title for caption
                # Sanitize filename for disk storage while keeping original title for caption
                final_name = sanitize_filename(downloaded_file)
                if final_name != downloaded_file:
                    old_path = os.path.join(dir_path, downloaded_file)
                    new_path = os.path.join(dir_path, final_name)
                    try:
                        if os.path.exists(new_path):
                            os.remove(new_path)
                        os.rename(old_path, new_path)
                    except Exception as e:
                        logger.error(f"Error renaming file from {old_path} to {new_path}: {e}")
                        final_name = downloaded_file
            else:
                ext = os.path.splitext(downloaded_file)[1]
                # Sanitize filename for disk storage while keeping original title for caption
                final_name = sanitize_filename(rename_name + ext)
                caption_name = rename_name  # Original title for caption
                old_path = os.path.join(dir_path, downloaded_file)
                new_path = os.path.join(dir_path, final_name)

                if os.path.exists(new_path):
                    try:
                        os.remove(new_path)
                    except Exception as e:
                        logger.error(f"Error removing existing file {new_path}: {e}")

                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    logger.error(f"Error renaming file from {old_path} to {new_path}: {e}")
                    final_name = downloaded_file
                    caption_name = original_video_title  # Original title for caption

            user_vid_path = os.path.join(dir_path, final_name)
            if final_name.lower().endswith((".webm", ".ts")):
                try:
                    safe_edit_message_text(user_id, proc_msg_id,
                        f"{info_text}\n\n{full_bar}   100.0%\nConverting video using ffmpeg... ⏳")
                except Exception as e:
                    logger.error(f"Error updating status before conversion: {e}")

                mp4_basename = sanitize_filename(os.path.splitext(final_name)[0]) + ".mp4"
                mp4_file = os.path.join(dir_path, mp4_basename)

                ffmpeg_cmd = [
                    "ffmpeg",
                    "-y",
                    "-i", user_vid_path,
                    "-c:v", "libx264",
                    "-preset", "fast",
                    "-crf", "23",
                    "-c:a", "aac",
                    "-b:a", "128k",
                    mp4_file
                ]
                try:
                    subprocess.run(ffmpeg_cmd, check=True)
                    os.remove(user_vid_path)
                    user_vid_path = mp4_file
                    final_name = mp4_basename
                except Exception as e:
                    send_to_all(message, f"❌ Conversion to MP4 failed: {e}")
                    break

            after_rename_abs_path = os.path.abspath(user_vid_path)
            # --- New block: if YouTube, download preview ---
            youtube_thumb_path = None
            thumb_dir = None
            try:
                if ("youtube.com" in url or "youtu.be" in url):
                    yt_id = video_id or None
                    if not yt_id:
                        try:
                            yt_id = extract_youtube_id(url)
                        except Exception:
                            yt_id = None
                    if yt_id:
                        youtube_thumb_path = os.path.join(dir_path, f"yt_thumb_{yt_id}.jpg")
                        download_thumbnail(yt_id, youtube_thumb_path)
                        thumb_dir = youtube_thumb_path
            except Exception as e:
                logger.warning(f"YouTube thumbnail error: {e}")
            # --- End of block ---
            # If thumb_dir is not defined - use ffmpeg preview

            result = get_duration_thumb(message, dir_path, user_vid_path, sanitize_filename(caption_name))
            if result is None:
                logger.warning("Failed to get video duration and thumbnail, continuing without thumbnail")
                duration = 0
                if not youtube_thumb_path:
                    thumb_dir = None
            else:
                duration, thumb_dir_default = result
                if not youtube_thumb_path:
                    thumb_dir = thumb_dir_default
            
            # Check for the existence of a preview and create a default one if needed
            if thumb_dir and not os.path.exists(thumb_dir):
                logger.warning(f"Thumbnail not found at {thumb_dir}, creating default")
                thumb_dir = create_default_thumbnail(os.path.join(dir_path, "default_thumb.jpg"))
                if not thumb_dir:
                    logger.warning("Failed to create default thumbnail, continuing without thumbnail")
                    thumb_dir = None

            video_size_in_bytes = os.path.getsize(user_vid_path)
            video_size = humanbytes(int(video_size_in_bytes))
            max_size = get_user_split_size(user_id)  # 1.95 GB - close to Telegram's 2GB limit with 50MB safety margin
            if int(video_size_in_bytes) > max_size:
                safe_edit_message_text(user_id, proc_msg_id,
                    f"{info_text}\n\n{full_bar}   100.0%\n__⚠️ Your video size ({video_size}) is too large.__\n__Splitting file...__ ✂️")
                returned = split_video_2(dir_path, sanitize_filename(caption_name), after_rename_abs_path, int(video_size_in_bytes), max_size, duration)
                caption_lst = returned.get("video")
                path_lst = returned.get("path")
                # Накапливаем все ID частей split-видео
                split_msg_ids = []
                for p in range(len(caption_lst)):
                    part_result = get_duration_thumb(message, dir_path, path_lst[p], sanitize_filename(caption_lst[p]))
                    if part_result is None:
                        continue
                    part_duration, splited_thumb_dir = part_result
                    # --- TikTok: Don't Pass Title ---
                    video_msg = send_videos(message, path_lst[p], '' if force_no_title else caption_lst[p], part_duration, splited_thumb_dir, info_text, proc_msg.id, full_video_title, tags_text_final)
                    try:
                        forwarded_msgs = safe_forward_messages(Config.LOGS_ID, user_id, [video_msg.id])
                        logger.info(f"down_and_up: forwarded_msgs result: {forwarded_msgs}")
                        if forwarded_msgs:
                            logger.info(f"down_and_up: collecting forwarded message IDs for split video: {[m.id for m in forwarded_msgs]}")
                            if is_playlist:
                                # For playlists, save to playlist cache with index
                                current_video_index = x + video_start_with
                                rounded_quality_key = quality_key
                                try:
                                    if quality_key.endswith('p'):
                                        rounded_quality_key = f"{ceil_to_popular(int(quality_key[:-1]))}p"
                                except Exception:
                                    pass
                                save_to_playlist_cache(get_clean_playlist_url(url), rounded_quality_key, [current_video_index], [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "")
                                cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), rounded_quality_key, [current_video_index])
                                logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                playlist_indices.append(current_video_index)
                                playlist_msg_ids.extend([m.id for m in forwarded_msgs])
                            else:
                                # Накапливаем ID частей для split видео
                                split_msg_ids.extend([m.id for m in forwarded_msgs])
                        else:
                            logger.info(f"down_and_up: collecting video_msg.id for split video: {video_msg.id}")
                            if is_playlist:
                                # For playlists, save to playlist cache with video index
                                current_video_index = x + video_start_with
                                save_to_playlist_cache(get_clean_playlist_url(url), quality_key, [current_video_index], [video_msg.id], original_text=message.text or message.caption or "")
                                cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, [current_video_index])
                                logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                playlist_indices.append(current_video_index)
                                playlist_msg_ids.append(video_msg.id)
                            else:
                                # Накапливаем ID частей для split видео
                                split_msg_ids.append(video_msg.id)
                    except Exception as e:
                        logger.error(f"Error forwarding video to logger: {e}")
                        logger.info(f"down_and_up: collecting video_msg.id after error for split video: {video_msg.id}")
                        if is_playlist:
                            # For playlists, save to playlist cache with video index
                            current_video_index = x + video_start_with
                            save_to_playlist_cache(get_clean_playlist_url(url), quality_key, [current_video_index], [video_msg.id], original_text=message.text or message.caption or "")
                            cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, [current_video_index])
                            logger.info(f"Checking the cache immediately after writing: {cached_check}")
                            playlist_indices.append(current_video_index)
                            playlist_msg_ids.append(video_msg.id)
                        else:
                            # Накапливаем ID частей для split видео
                            split_msg_ids.append(video_msg.id)
                    safe_edit_message_text(user_id, proc_msg_id,
                                          f"{info_text}\n\n{full_bar}   100.0%\n__Splitted part {p + 1} file uploaded__")
                    if p < len(caption_lst) - 1:
                        threading.Event().wait(2)
                    os.remove(splited_thumb_dir)
                    send_mediainfo_if_enabled(user_id, path_lst[p], message)
                    os.remove(path_lst[p])
                
                # Сохраняем все части split-видео в кэш после завершения цикла
                if split_msg_ids and not is_playlist:
                    # Удаляем дубликаты
                    split_msg_ids = list(dict.fromkeys(split_msg_ids))
                    logger.info(f"down_and_up: saving all split video parts to cache: {split_msg_ids}")
                    save_to_video_cache(url, quality_key, split_msg_ids, original_text=message.text or message.caption or "")
                os.remove(thumb_dir)
                os.remove(user_vid_path)
                success_msg = f"**✅ Upload complete** - {video_count} files uploaded.\n\n{Config.CREDITS_MSG}"
                safe_edit_message_text(user_id, proc_msg_id, success_msg)
                send_to_logger(message, "Video upload completed with file splitting.")
                break
            else:
                if final_name:
                    # Read the full name from the file
                    full_caption = caption_name
                    try:
                        if os.path.exists(full_title_path):
                            with open(full_title_path, "r", encoding="utf-8") as f:
                                full_caption = f.read().strip()
                    except Exception as e:
                        logger.error(f"Error reading full title: {e}")

                    # Check for preview existence before sending
                    if thumb_dir and not os.path.exists(thumb_dir):
                        logger.warning(f"Thumbnail not found before sending, creating default")
                        thumb_dir = create_default_thumbnail(os.path.join(dir_path, "default_thumb.jpg"))
                        if not thumb_dir:
                            logger.warning("Failed to create default thumbnail before sending, continuing without thumbnail")
                            thumb_dir = None

                    try:
                        # --- TikTok: Don't Pass Title ---
                        video_msg = send_videos(message, after_rename_abs_path, '' if force_no_title else original_video_title, duration, thumb_dir, info_text, proc_msg.id, full_video_title, tags_text_final)
                        try:
                            forwarded_msgs = safe_forward_messages(Config.LOGS_ID, user_id, [video_msg.id])
                            logger.info(f"down_and_up: forwarded_msgs result: {forwarded_msgs}")
                            if forwarded_msgs:
                                logger.info(f"down_and_up: saving to cache with forwarded message IDs: {[m.id for m in forwarded_msgs]}")
                                if is_playlist:
                                    # For playlists, save to playlist cache with video index
                                    current_video_index = x + video_start_with
                                    save_to_playlist_cache(get_clean_playlist_url(url), quality_key, [current_video_index], [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "")
                                    cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, [current_video_index])
                                    logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                    playlist_indices.append(current_video_index)
                                    playlist_msg_ids.extend([m.id for m in forwarded_msgs])
                                else:
                                    # For single videos, save to regular cache
                                    save_to_video_cache(url, quality_key, [m.id for m in forwarded_msgs], original_text=message.text or message.caption or "")
                            else:
                                logger.info(f"down_and_up: saving to cache with video_msg.id: {video_msg.id}")
                                if is_playlist:
                                    # For playlists, save to playlist cache with video index
                                    current_video_index = x + video_start_with
                                    save_to_playlist_cache(get_clean_playlist_url(url), quality_key, [current_video_index], [video_msg.id], original_text=message.text or message.caption or "")
                                    cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, [current_video_index])
                                    logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                    playlist_indices.append(current_video_index)
                                    playlist_msg_ids.append(video_msg.id)
                                else:
                                    # For single videos, save to regular cache
                                    save_to_video_cache(url, quality_key, [video_msg.id], original_text=message.text or message.caption or "")
                        except Exception as e:
                            logger.error(f"Error forwarding video to logger: {e}")
                            logger.info(f"down_and_up: saving to cache with video_msg.id after error: {video_msg.id}")
                            if is_playlist:
                                # For playlists, save to playlist cache with video index
                                current_video_index = x + video_start_with
                                save_to_playlist_cache(get_clean_playlist_url(url), quality_key, [current_video_index], [video_msg.id], original_text=message.text or message.caption or "")
                                cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, [current_video_index])
                                logger.info(f"Checking the cache immediately after writing: {cached_check}")
                                playlist_indices.append(current_video_index)
                                playlist_msg_ids.append(video_msg.id)
                            else:
                                # For single videos, save to regular cache
                                save_to_video_cache(url, quality_key, [video_msg.id], original_text=message.text or message.caption or "")
                        safe_edit_message_text(user_id, proc_msg_id,
                            f"{info_text}\n{full_bar}   100.0%\n\n**🎞 Video duration:** __{TimeFormatter(duration * 1000)}__\n\n1 file uploaded.")
                        send_mediainfo_if_enabled(user_id, after_rename_abs_path, message)
                        os.remove(after_rename_abs_path)
                        if thumb_dir and os.path.exists(thumb_dir):
                            os.remove(thumb_dir)
                        threading.Event().wait(2)
                    except Exception as e:
                        logger.error(f"Error sending video: {e}")
                        send_to_all(message, f"❌ Error sending video: {str(e)}")
                        continue
        if successful_uploads == len(indices_to_download):
            success_msg = f"**✅ Upload complete** - {video_count} files uploaded.\n\n{Config.CREDITS_MSG}"
            safe_edit_message_text(user_id, proc_msg_id, success_msg)
            send_to_logger(message, success_msg)

        if is_playlist and quality_key:
            total_sent = len(cached_videos) + successful_uploads
            app.send_message(user_id, f"✅ Playlist videos sent: {total_sent}/{len(requested_indices)} files.", reply_to_message_id=message.id)
            send_to_logger(message, f"Playlist videos sent: {total_sent}/{len(requested_indices)} files (quality={quality_key}) to user {user_id}")

    except Exception as e:
        if "Download timeout exceeded" in str(e):
            send_to_user(message, "⏰ Download cancelled due to timeout (2 hours)")
            send_to_logger(message, "Download cancelled due to timeout")
        else:
            logger.error(f"Error in video download: {e}")
            send_to_user(message, f"❌ Failed to download video: {e}")
        
        # Clean up temporary files on error
        try:
            cleanup_user_temp_files(user_id)
        except Exception as cleanup_error:
            logger.error(f"Error cleaning up temp files after error for user {user_id}: {cleanup_error}")
    finally:
        set_active_download(user_id, False)
        clear_download_start_time(user_id)  # Clear the download start time
        if playlist_name:
            with playlist_errors_lock:
                error_key = f"{user_id}_{playlist_name}"
                if error_key in playlist_errors:
                    del playlist_errors[error_key]

        # Clean up temporary files
        try:
            cleanup_user_temp_files(user_id)
        except Exception as e:
            logger.error(f"Error cleaning up temp files for user {user_id}: {e}")

        try:
            if status_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[status_msg_id], revoke=True)
            if hourglass_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[hourglass_msg_id], revoke=True)
        except Exception as e:
            logger.error(f"Error deleting status messages: {e}")

        # --- ADDED: summary of cache after cycle ---
        if is_playlist and playlist_indices and playlist_msg_ids:
            save_to_playlist_cache(get_clean_playlist_url(url), quality_key, playlist_indices, playlist_msg_ids, original_text=message.text or message.caption or "")
            cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, playlist_indices)
            summary = "\n".join([f"Index {idx}: msg_id={cached_check.get(idx, '-')}" for idx in playlist_indices])
            logger.info(f"[SUMMARY] Playlist cache (quality {quality_key}):\n{summary}")

def down_and_audio(app, message, url, tags, quality_key=None, playlist_name=None, video_count=1, video_start_with=1):
    """
    Now if part of the playlist range is already cached, we first repost the cached indexes, then download and cache the missing ones, without finishing after reposting part of the range.
    """
    playlist_indices = []
    playlist_msg_ids = []  
        
    user_id = message.chat.id
    logger.info(f"down_and_audio called: url={url}, quality_key={quality_key}, video_count={video_count}, video_start_with={video_start_with}")
    
    # Import needed functions from other modules
    from magic.processing.tags import is_playlist_with_range, generate_final_tags, save_user_tags
    from magic.download.cache import get_cached_playlist_videos, get_cached_message_ids, save_to_video_cache, save_to_playlist_cache, get_clean_playlist_url
    from magic.utils.filesystem import create_directory, cleanup_user_temp_files, check_disk_space, sanitize_filename
    from magic.utils.communication import safe_send_message, safe_forward_messages, safe_edit_message_text, safe_delete_messages, start_hourglass_animation, send_to_logger, send_to_user, send_to_all
    from magic.database.firebase import write_logs, check_user
    from magic.user.settings import send_mediainfo_if_enabled
    from magic.utils.filesystem import set_active_download, clear_download_start_time, check_download_timeout
    
    # We define a playlist not only by the number of videos, but also by the presence of a range in the URL
    original_text = message.text or message.caption or ""
    is_playlist = video_count > 1 or is_playlist_with_range(original_text)
    requested_indices = list(range(video_start_with, video_start_with + video_count)) if is_playlist else []
    cached_videos = {}
    uncached_indices = []
    if quality_key and is_playlist:
        cached_videos = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, requested_indices)
        uncached_indices = [i for i in requested_indices if i not in cached_videos]
        # First, repost the cached ones
        if cached_videos:
            for index in requested_indices:
                if index in cached_videos:
                    try:
                        app.forward_messages(
                            chat_id=user_id,
                            from_chat_id=Config.LOGS_ID,
                            message_ids=[cached_videos[index]]
                        )
                    except Exception as e:
                        logger.error(f"down_and_audio: error reposting cached audio index={index}: {e}")
            if len(uncached_indices) == 0:
                app.send_message(user_id, f"✅ Playlist audio sent from cache ({len(cached_videos)}/{len(requested_indices)} files).", reply_to_message_id=message.id)
                send_to_logger(message, f"Playlist audio sent from cache (quality={quality_key}) to user{user_id}")
                return
            else:
                app.send_message(user_id, f"♻️ {len(cached_videos)}/{len(requested_indices)} audio sent from cache, downloading missing ones...", reply_to_message_id=message.id)
    elif quality_key and not is_playlist:
        cached_ids = get_cached_message_ids(url, quality_key)
        if cached_ids:
            try:
                app.forward_messages(
                    chat_id=user_id,
                    from_chat_id=Config.LOGS_ID,
                    message_ids=cached_ids
                )
                app.send_message(user_id, "✅ Audio sent from cache.", reply_to_message_id=message.id)
                send_to_logger(message, f"Audio sent from cache (quality={quality_key}) to user{user_id}")
                return
            except Exception as e:
                logger.error(f"Error reposting audio from cache: {e}")
                save_to_video_cache(url, quality_key, [], clear=True)
                app.send_message(user_id, "⚠️ Failed to get audio from cache, starting new download...", reply_to_message_id=message.id)
    else:
        logger.info(f"down_and_audio: quality_key is None, skipping cache check")

    anim_thread = None
    stop_anim = threading.Event()
    proc_msg = None
    proc_msg_id = None
    status_msg = None
    status_msg_id = None
    hourglass_msg = None
    hourglass_msg_id = None
    audio_files = []
    try:
        # Check if there is a saved waiting time
        user_dir = os.path.join("users", str(user_id))
        flood_time_file = os.path.join(user_dir, "flood_wait.txt")

        # We send the initial message
        if os.path.exists(flood_time_file):
            with open(flood_time_file, 'r') as f:
                wait_time = int(f.read().strip())
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = wait_time % 60
                time_str = f"{hours}h {minutes}m {seconds}s"
                proc_msg = app.send_message(user_id, f"⚠️ Telegram has limited message sending.\n\n⏳ Please wait: {time_str}\n\nTo update timer send URL again 2 times.")
        else:
            proc_msg = app.send_message(user_id, "⚠️ Telegram has limited message sending.\n\n⏳ Please wait: \n\nTo update timer send URL again 2 times.")

        # We are trying to replace with "Download started"
        try:
            app.edit_message_text(
                chat_id=user_id,
                message_id=proc_msg.id,
                text="Download started"
            )
            if os.path.exists(flood_time_file):
                os.remove(flood_time_file)
        except FloodWait as e:
            wait_time = e.value
            os.makedirs(user_dir, exist_ok=True)
            with open(flood_time_file, 'w') as f:
                f.write(str(wait_time))
            return
        except Exception as e:
            logger.error(f"Error editing message: {e}")
            return

        # If there is no flood error, send a normal message (only once)
        proc_msg = app.send_message(user_id, "Processing... ♻️", reply_to_message_id=message.id)
        proc_msg_id = proc_msg.id
        status_msg = app.send_message(user_id, "🎧 Audio is processing...")
        hourglass_msg = app.send_message(user_id, "⏳ Please wait...")
        status_msg_id = status_msg.id
        hourglass_msg_id = hourglass_msg.id
        anim_thread = start_hourglass_animation(user_id, hourglass_msg_id, stop_anim)

        # Check if there's enough disk space (estimate 500MB per audio file)
        user_folder = os.path.abspath(os.path.join("users", str(user_id)))
        create_directory(user_folder)

        if not check_disk_space(user_folder, 500 * 1024 * 1024 * video_count):
            send_to_user(message, "❌ Not enough disk space to download the audio files.")
            return

        check_user(message)

        # Reset of the flag of errors for the new launch of the playlist
        if playlist_name:
            with playlist_errors_lock:
                error_key = f"{user_id}_{playlist_name}"
                if error_key in playlist_errors:
                    del playlist_errors[error_key]

        cookie_file = os.path.join(user_folder, os.path.basename(Config.COOKIE_FILE_PATH))
        last_update = 0
        current_total_process = ""
        successful_uploads = 0

        def progress_hook(d):
            nonlocal last_update
            # Check the timeout
            if check_download_timeout(user_id):
                raise Exception(f"Download timeout exceeded ({Config.DOWNLOAD_TIMEOUT // 3600} hours)")
            current_time = time.time()
            if current_time - last_update < 0.2:
                return
            if d.get("status") == "downloading":
                downloaded = d.get("downloaded_bytes", 0)
                total = d.get("total_bytes", 0)
                percent = (downloaded / total * 100) if total else 0
                blocks = int(percent // 10)
                bar = "🟩" * blocks + "⬜️" * (10 - blocks)
                try:
                    safe_edit_message_text(user_id, proc_msg_id, f"{current_total_process}\nDownloading audio:\n{bar}   {percent:.1f}%")
                except Exception as e:
                    logger.error(f"Error updating progress: {e}")
                last_update = current_time
            elif d.get("status") == "finished":
                try:
                    full_bar = "🟩" * 10
                    safe_edit_message_text(user_id, proc_msg_id,
                        f"{current_total_process}\nDownloading audio:\n{full_bar}   100.0%\nDownload finished, processing audio...")
                except Exception as e:
                    logger.error(f"Error updating progress: {e}")
                last_update = current_time
            elif d.get("status") == "error":
                try:
                    safe_edit_message_text(user_id, proc_msg_id, "Error occurred during audio download.")
                except Exception as e:
                    logger.error(f"Error updating progress: {e}")
                last_update = current_time

        def try_download_audio(url, current_index):
            nonlocal current_total_process
            ytdl_opts = {
                'format': 'ba',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'prefer_ffmpeg': True,
                'extractaudio': True,
                'playlist_items': str(current_index + video_start_with),
                'cookiefile': cookie_file,
                'outtmpl': os.path.join(user_folder, "%(title)s.%(ext)s"),
                'progress_hooks': [progress_hook],
            }
            try:
                with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=False)
                if "entries" in info_dict:
                    entries = info_dict["entries"]
                    if len(entries) > 1:  # If the video in the playlist is more than one
                        actual_index = current_index + video_start_with - 1  # -1 because indexes in entries start from 0
                        if actual_index < len(entries):
                            info_dict = entries[actual_index]
                        else:
                            raise Exception(f"Audio index {actual_index + 1} out of range (total {len(entries)})")
                    else:
                        # If there is only one video in the playlist, just download it
                        info_dict = entries[0]  # Just take the first video

                try:
                    safe_edit_message_text(user_id, proc_msg_id,
                        f"{current_total_process}\n\n> __Downloading audio using format: ba...__ 📥")
                except Exception as e:
                    logger.error(f"Status update error: {e}")
                
                with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                    ydl.download([url])
                
                try:
                    full_bar = "🟩" * 10
                    safe_edit_message_text(user_id, proc_msg_id, f"{current_total_process}\n{full_bar}   100.0%")
                except Exception as e:
                    logger.error(f"Final progress update error: {e}")
                return info_dict
            except yt_dlp.utils.DownloadError as e:
                error_text = str(e)
                send_to_user(message, f"❌ Error downloading: {error_text}\n\nPerhaps cookie authorization is required. More information: https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp")
                logger.error(f"DownloadError: {error_text}")
                return None
            except Exception as e:
                logger.error(f"Audio download attempt failed: {e}")
                send_to_user(message, f"❌ Unknown error: {e}")
                return None

        if is_playlist and quality_key:
            indices_to_download = uncached_indices
        else:
            indices_to_download = range(video_count)
        for idx, current_index in enumerate(indices_to_download):
            current_index = current_index - video_start_with  # for numbering/display
            total_process = f"""
**📶 Total Progress**
> **Audio:** {idx + 1} / {len(indices_to_download)}
"""

            current_total_process = total_process

            # Determine rename_name based on the incoming playlist_name:
            if playlist_name and playlist_name.strip():
                # A new name for the playlist is explicitly set - let's use it
                rename_name = sanitize_filename(f"{playlist_name.strip()} - Part {idx + video_start_with}")
            else:
                # No new name set - extract name from metadata
                rename_name = None

            info_dict = try_download_audio(url, current_index)

            if info_dict is None:
                with playlist_errors_lock:
                    error_key = f"{user_id}_{playlist_name}"
                    if error_key not in playlist_errors:
                        playlist_errors[error_key] = True
                        send_to_all(
                            message,
                            f"❌ Failed to download audio: Check if your site is supported\n"
                            "> You may need `cookie` for downloading this audio. First, clean your workspace via **/clean** command\n"
                            "> For Youtube - get `cookie` via **/download_cookie** command. For any other supported site - send your own cookie and after that send your audio link again."
                        )
                break

            successful_uploads += 1

            audio_title = info_dict.get("title", "audio")
            audio_title = sanitize_filename(audio_title)
            
            # If rename_name is not set, set it equal to audio_title
            if rename_name is None:
                rename_name = audio_title

            # Find the downloaded audio file
            allfiles = os.listdir(user_folder)
            files = [fname for fname in allfiles if fname.endswith('.mp3')]
            files.sort()
            if not files:
                send_to_all(message, f"Skipping unsupported file type in playlist at index {idx + video_start_with}")
                continue

            downloaded_file = files[0]
            write_logs(message, url, downloaded_file)

            if rename_name == audio_title:
                caption_name = audio_title  # Original title for caption
                # Sanitize filename for disk storage while keeping original title for caption
                final_name = sanitize_filename(downloaded_file)
                if final_name != downloaded_file:
                    old_path = os.path.join(user_folder, downloaded_file)
                    new_path = os.path.join(user_folder, final_name)
                    try:
                        if os.path.exists(new_path):
                            os.remove(new_path)
                        os.rename(old_path, new_path)
                    except Exception as e:
                        logger.error(f"Error renaming file from {old_path} to {new_path}: {e}")
                        final_name = downloaded_file
            else:
                ext = os.path.splitext(downloaded_file)[1]
                # Sanitize filename for disk storage while keeping original title for caption
                final_name = sanitize_filename(rename_name + ext)
                caption_name = rename_name  # Original title for caption
                old_path = os.path.join(user_folder, downloaded_file)
                new_path = os.path.join(user_folder, final_name)

                if os.path.exists(new_path):
                    try:
                        os.remove(new_path)
                    except Exception as e:
                        logger.error(f"Error removing existing file {new_path}: {e}")

                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    logger.error(f"Error renaming file from {old_path} to {new_path}: {e}")
                    final_name = downloaded_file
                    caption_name = audio_title  # Original title for caption

            audio_file = os.path.join(user_folder, final_name)
            if not os.path.exists(audio_file):
                send_to_user(message, "Audio file not found after download.")
                continue

            audio_files.append(audio_file)

            try:
                full_bar = "🟩" * 10
                safe_edit_message_text(user_id, proc_msg_id, f"{current_total_process}\nUploading audio file...\n{full_bar}   100.0%")
            except Exception as e:
                logger.error(f"Error updating upload status: {e}")

            # We form a text with tags and a link for audio
            tags_for_final = tags if isinstance(tags, list) else (tags.split() if isinstance(tags, str) else [])
            tags_text_final = generate_final_tags(url, tags_for_final, info_dict)
            tags_block = (tags_text_final.strip() + '\n') if tags_text_final and tags_text_final.strip() else ''
            bot_name = getattr(Config, 'BOT_NAME', None) or 'bot'
            bot_mention = f' @{bot_name}' if not bot_name.startswith('@') else f' {bot_name}'
            # Use original audio_title for caption, not sanitized caption_name
            caption_with_link = f"{audio_title}\n\n{tags_block}[🔗 Audio URL]({url}){bot_mention}"
            
            try:
                audio_msg = app.send_audio(chat_id=user_id, audio=audio_file, caption=caption_with_link, reply_to_message_id=message.id)
                forwarded_msg = safe_forward_messages(Config.LOGS_ID, user_id, [audio_msg.id])
                
                # Save to cache after sending audio
                if quality_key and forwarded_msg:
                    if isinstance(forwarded_msg, list):
                        msg_ids = [m.id for m in forwarded_msg]
                    else:
                        msg_ids = [forwarded_msg.id]
                    
                    if is_playlist:
                        # For playlists, save to playlist cache with index
                        current_video_index = idx + video_start_with
                        logger.info(f"down_and_audio: saving to playlist cache: index={current_video_index}, msg_ids={msg_ids}")
                        save_to_playlist_cache(get_clean_playlist_url(url), quality_key, [current_video_index], msg_ids, original_text=message.text or message.caption or "")
                        cached_check = get_cached_playlist_videos(get_clean_playlist_url(url), quality_key, [current_video_index])
                        logger.info(f"Checking the cache immediately after writing: {cached_check}")
                        playlist_indices.append(current_video_index)
                        playlist_msg_ids.extend(msg_ids)  # We use msg_ids instead of forwarded_msgs
                    else:
                        # For single audios, save to regular cache
                        logger.info(f"down_and_audio: saving to video cache: msg_ids={msg_ids}")
                        save_to_video_cache(url, quality_key, msg_ids, original_text=message.text or message.caption or "")
            except Exception as send_error:
                logger.error(f"Error sending audio: {send_error}")
                send_to_user(message, f"❌ Failed to send audio: {send_error}")
                continue

            # Clean up the audio file after sending
            try:
                send_mediainfo_if_enabled(user_id, audio_file, message)
                os.remove(audio_file)
            except Exception as e:
                logger.error(f"Failed to delete audio file {audio_file}: {e}")

            # Add delay between uploads for playlists
            if idx < len(indices_to_download) - 1:
                threading.Event().wait(2)

        if successful_uploads == len(indices_to_download):
            success_msg = f"✅ Audio successfully downloaded and sent - {len(indices_to_download)} files uploaded.\n\n{Config.CREDITS_MSG}"
        else:
            success_msg = f"⚠️ Partially completed - {successful_uploads}/{len(indices_to_download)} audio files uploaded.\n\n{Config.CREDITS_MSG}"
            
        try:
            safe_edit_message_text(user_id, proc_msg_id, success_msg)
        except Exception as e:
            logger.error(f"Error updating final status: {e}")

        send_to_logger(message, success_msg)

        if is_playlist and quality_key:
            total_sent = len(cached_videos) + successful_uploads
            app.send_message(user_id, f"✅Playlist audio sent: {total_sent}/{len(requested_indices)} files.", reply_to_message_id=message.id)
            send_to_logger(message, f"Playlist audio sent: {total_sent}/{len(requested_indices)} files (quality={quality_key}) to user{user_id}")

    except Exception as e:
        if "Download timeout exceeded" in str(e):
            send_to_user(message, "⏰ Download cancelled due to timeout (2 hours)")
            send_to_logger(message, "Download cancelled due to timeout")
        else:
            logger.error(f"Error in audio download: {e}")
            send_to_user(message, f"❌ Failed to download audio: {e}")
    finally:
        # Always clean up resources
        stop_anim.set()
        if anim_thread:
            anim_thread.join(timeout=1)  # Wait for animation thread with timeout

        try:
            if status_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[status_msg_id], revoke=True)
            if hourglass_msg_id:
                safe_delete_messages(chat_id=user_id, message_ids=[hourglass_msg_id], revoke=True)
        except Exception as e:
            logger.error(f"Error deleting status messages: {e}")

        # Clean up any remaining audio files
        for audio_file in audio_files:
            try:
                if os.path.exists(audio_file):
                    os.remove(audio_file)
            except Exception as e:
                logger.error(f"Failed to delete file {audio_file}: {e}")

        set_active_download(user_id, False)
        clear_download_start_time(user_id)  # Cleaning the start time

        # Clean up temporary files
        try:
            cleanup_user_temp_files(user_id)
        except Exception as e:
            logger.error(f"Error cleaning up temp files for user {user_id}: {e}")

        # Reset playlist errors if this was a playlist
        if playlist_name:
            with playlist_errors_lock:
                error_key = f"{user_id}_{playlist_name}"
                if error_key in playlist_errors:
                    del playlist_errors[error_key]


def ytdlp_hook(d):
    """YT-DLP hook"""
    if d['status'] == 'downloading':
        logger.info(f"Downloading: {d.get('_percent_str', 'N/A')}")
    elif d['status'] == 'finished':
        logger.info(f"Downloaded: {d['filename']}")
