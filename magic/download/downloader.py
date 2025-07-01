"""
Main download functions for video and audio
"""
import os
import time
import yt_dlp
from pyrogram import enums
from config import Config
from ..utils.formatters import humanbytes, sanitize_filename, TimeFormatter
from ..utils.filesystem import create_directory, cleanup_user_temp_files, set_active_download, get_active_download, cleanup_temp_files
from ..utils.communication import send_to_all, send_to_logger, progress_bar
from ..database.firebase import logger, write_logs
from ..processing.tags import extract_url_range_tags, generate_final_tags, is_playlist_with_range
from ..processing.video import get_duration_thumb, split_video_2, send_videos
from .cache import save_to_video_cache, get_cached_message_ids, save_to_playlist_cache, get_cached_playlist_videos, get_clean_playlist_url
from .quality import get_video_formats
from ..user.settings import get_user_split_size


def down_and_audio(app, message, url, tags, quality_key=None, playlist_name=None, video_count=1, video_start_with=1):
    """Download audio from URL with caching support"""
    user_id = message.chat.id
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    set_active_download(user_id, "downloading_audio")
    
    try:
        # Check cache first
        if quality_key:
            cached_msg_ids = get_cached_message_ids(url, quality_key)
            if cached_msg_ids:
                app.forward_messages(user_id, Config.CACHE_CHANNEL, cached_msg_ids)
                send_to_logger(message, f"Reposted cached audio: {url}")
                return
        
        # Download audio
        ydl_opts = {
            'outtmpl': os.path.join(user_dir, '%(title)s.%(ext)s'),
            'extractaudio': True,
            'audioformat': 'mp3',
            'audioquality': '192',
        }
        
        if Config.COOKIES_FILE_PATH and os.path.exists(Config.COOKIES_FILE_PATH):
            ydl_opts['cookiefile'] = Config.COOKIES_FILE_PATH
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            
            # Find audio file
            title = sanitize_filename(info_dict.get('title', 'audio'))
            for ext in ['mp3', 'm4a', 'opus']:
                audio_file = os.path.join(user_dir, f"{title}.{ext}")
                if os.path.exists(audio_file):
                    break
            
            if os.path.exists(audio_file):
                # Send audio
                caption = f"🎵 <b>{title}</b>"
                sent_message = app.send_audio(
                    user_id, audio_file, caption=caption,
                    parse_mode=enums.ParseMode.HTML,
                    reply_to_message_id=message.id
                )
                
                # Cache result
                if quality_key:
                    save_to_video_cache(url, quality_key, [sent_message.id])
                
                write_logs(message, url, title)
                os.remove(audio_file)
                
    except Exception as e:
        logger.error(f"Audio download error: {e}")
        send_to_all(message, f"❌ Audio download error: {e}")
    
    finally:
        set_active_download(user_id, None)


def down_and_up(app, message, url, playlist_name, video_count, video_start_with, tags_text, force_no_title=False, format_override=None, quality_key=None):
    """Main video download function with caching support"""
    user_id = message.chat.id
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    set_active_download(user_id, "downloading_video")
    
    try:
        # Check cache first
        if quality_key:
            cached_msg_ids = get_cached_message_ids(url, quality_key)
            if cached_msg_ids:
                app.forward_messages(user_id, Config.CACHE_CHANNEL, cached_msg_ids)
                send_to_logger(message, f"Reposted cached video: {url}")
                return
        
        # Download video
        ydl_opts = {
            'outtmpl': os.path.join(user_dir, '%(title)s.%(ext)s'),
            'format': format_override or 'best[ext=mp4]/best',
        }
        
        if Config.COOKIES_FILE_PATH and os.path.exists(Config.COOKIES_FILE_PATH):
            ydl_opts['cookiefile'] = Config.COOKIES_FILE_PATH
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            
            # Find video file
            title = sanitize_filename(info_dict.get('title', 'video'))
            video_file = None
            for ext in ['mp4', 'mkv', 'webm']:
                potential_file = os.path.join(user_dir, f"{title}.{ext}")
                if os.path.exists(potential_file):
                    video_file = potential_file
                    break
            
            if not video_file:
                raise Exception("Video file not found after download")
            
            file_size = os.path.getsize(video_file)
            duration_result = get_duration_thumb(message, user_dir, video_file, "thumb")
            duration, thumb_file = duration_result if duration_result else (0, None)
            
            # Handle splitting
            split_size = get_user_split_size(user_id)
            split_msg_ids = []
            
            if split_size and file_size > split_size:
                split_result = split_video_2(user_dir, title, video_file, file_size, split_size, duration)
                for i, part_path in enumerate(split_result.get('path', [])):
                    if os.path.exists(part_path):
                        sent_msg = send_videos(message, part_path, f"<b>{title} - Part {i+1}</b>", 
                                             duration//len(split_result['path']), thumb_file, "", message.id, title)
                        if sent_msg:
                            split_msg_ids.append(sent_msg.id)
                        try:
                            os.remove(part_path)
                        except:
                            pass
            else:
                sent_msg = send_videos(message, video_file, f"<b>{title}</b>", duration, thumb_file, "", message.id, title)
                if sent_msg:
                    split_msg_ids.append(sent_msg.id)
            
            # Cache result - FIXED: save all message IDs at once
            if quality_key and split_msg_ids:
                save_to_video_cache(url, quality_key, split_msg_ids)
            
            write_logs(message, url, title)
            
            # Cleanup
            try:
                os.remove(video_file)
                if thumb_file and os.path.exists(thumb_file):
                    os.remove(thumb_file)
            except:
                pass
                
    except Exception as e:
        logger.error(f"Video download error: {e}")
        send_to_all(message, f"❌ Video download error: {e}")
    
    finally:
        set_active_download(user_id, None)


def ytdlp_hook(d):
    """Hook for yt-dlp progress"""
    try:
        if d['status'] == 'downloading':
            # Basic logging for debugging
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            logger.debug(f"Download progress: {percent}, Speed: {speed}")
    except Exception as e:
        logger.error(f"ytdlp_hook error: {e}") 