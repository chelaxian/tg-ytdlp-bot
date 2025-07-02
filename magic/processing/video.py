"""
Video processing functions
"""
import os
import re
import math
import time
import subprocess
import logging
from typing import Tuple
from pyrogram import enums
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from config import Config

logger = logging.getLogger(__name__)

def send_videos(
    message,
    video_abs_path: str,
    caption: str,
    duration: int,
    thumb_file_path: str,
    info_text: str,
    msg_id: int,
    full_video_title: str,
    tags_text: str = '',
):
    """Send video with proper caption formatting"""
    # Import needed functions
    from magic.utils.communication import safe_forward_messages, progress_bar
    from magic.utils.formatters import truncate_caption, TimeFormatter
    
    user_id = message.chat.id
    text = message.text or ""
    m = re.search(r'https?://[^\s\*]+', text)
    video_url = m.group(0) if m else ""
    temp_desc_path = os.path.join(os.path.dirname(video_abs_path), "full_description.txt")
    was_truncated = False
    try:
        # Logic simplified: use tags that were already generated in down_and_up.
        # Use original title for caption, but truncated description
        title_html, pre_block, blockquote_content, tags_block, link_block, was_truncated = truncate_caption(
            title=caption,  # Original title for caption
            description=full_video_title,  # Full description to be truncated
            url=video_url,
            tags_text=tags_text, # Use final tags for calculation
            max_length=1000  # Reduced for safety
        )
        # Form HTML caption: title outside the quote, timecodes outside the quote, description in the quote, tags and link outside the quote
        cap = ''
        if title_html:
            cap += title_html + '\n\n'
        if pre_block:
            cap += pre_block + '\n'
        cap += f'<blockquote expandable>{blockquote_content}</blockquote>\n'
        if tags_block:
            cap += tags_block
        cap += link_block
        
        # Import app from main
        from magic.handlers.commands import app
        
        video_msg = app.send_video(
            chat_id=user_id,
            video=video_abs_path,
            caption=cap,
            duration=duration,
            width=640,
            height=360,
            supports_streaming=True,
            thumb=thumb_file_path,
            progress=progress_bar,
            progress_args=(
                user_id,
                msg_id,
                f"{info_text}\n**Video duration:** __{TimeFormatter(duration*1000)}__\n\n__Uploading Video... 📤__"
            ),
            reply_to_message_id=message.id,
            parse_mode=enums.ParseMode.HTML
        )
        if was_truncated and full_video_title:
            with open(temp_desc_path, "w", encoding="utf-8") as f:
                f.write(full_video_title)
        if was_truncated and os.path.exists(temp_desc_path):
            try:
                user_doc_msg = app.send_document(
                    chat_id=user_id,
                    document=temp_desc_path,
                    caption="<blockquote>📝 if you want to change video caption - reply to video with new text</blockquote>",
                    reply_to_message_id=message.id,
                    parse_mode=enums.ParseMode.HTML
                )
                safe_forward_messages(Config.LOGS_ID, user_id, [user_doc_msg.id])
            except Exception as e:
                logger.error(f"Error sending full description file: {e}")
        return video_msg
    finally:
        if os.path.exists(temp_desc_path):
            try:
                os.remove(temp_desc_path)
            except Exception as e:
                logger.error(f"Error removing temporary description file: {e}")


def humanbytes(size):
    """Convert bytes to human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    # 2 ** 10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    """Format time from milliseconds to human readable"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") +\
        ((str(hours) + "h, ") if hours else "") +\
        ((str(minutes) + "m, ") if minutes else "") +\
        ((str(seconds) + "s, ") if seconds else "") +\
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]


def split_video_2(dir, video_name, video_path, video_size, max_size, duration):
    """
    Split a video into multiple parts

    Args:
        dir: Directory path
        video_name: Name for the video
        video_path: Path to the video file
        video_size: Size of the video in bytes
        max_size: Maximum size for each part
        duration: Duration of the video

    Returns:
        dict: Dictionary with video parts information
    """
    rounds = (math.floor(video_size / max_size)) + 1
    n = duration / rounds
    caption_lst = []
    path_lst = []

    try:
        if rounds > 20:
            logger.warning(f"Video will be split into {rounds} parts, which may be excessive")

        for x in range(rounds):
            start_time = x * n
            end_time = (x * n) + n

            # Ensure end_time doesn't exceed duration
            end_time = min(end_time, duration)

            cap_name = video_name + " - Part " + str(x + 1)
            target_name = os.path.join(dir, cap_name + ".mp4")

            caption_lst.append(cap_name)
            path_lst.append(target_name)

            try:
                # Use progress logging
                logger.info(f"Splitting video part {x+1}/{rounds}: {start_time:.2f}s to {end_time:.2f}s")
                ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=target_name)

                # Verify the split was successful
                if not os.path.exists(target_name) or os.path.getsize(target_name) == 0:
                    logger.error(f"Failed to create split part {x+1}: {target_name}")
                else:
                    logger.info(f"Successfully created split part {x+1}: {target_name} ({os.path.getsize(target_name)} bytes)")

            except Exception as e:
                logger.error(f"Error splitting video part {x+1}: {e}")
                # If a part fails, we continue with the others

        split_vid_dict = {
            "video": caption_lst,
            "path": path_lst
        }

        logger.info(f"Video split into {len(path_lst)} parts successfully")
        return split_vid_dict

    except Exception as e:
        logger.error(f"Error in video splitting process: {e}")
        # Return what we have so far
        split_vid_dict = {
            "video": caption_lst,
            "path": path_lst
        }
        return split_vid_dict


def get_duration_thumb_(dir, video_path, thumb_name):
    """Get duration and thumbnail using moviepy"""
    thumb_dir = os.path.abspath(dir + "/" + thumb_name + ".jpg")
    clip = VideoFileClip(video_path)
    duration = (int(clip.duration))
    clip.save_frame(thumb_dir, t=2)
    clip.close()
    return duration, thumb_dir


def get_duration_thumb(message, dir_path, video_path, thumb_name):
    """
    Captures a thumbnail at 2 seconds into the video and retrieves video duration.
    Forces overwriting existing thumbnail with the '-y' flag.

    Args:
        message: The message object
        dir_path: Directory path for the thumbnail
        video_path: Path to the video file
        thumb_name: Name for the thumbnail

    Returns:
        tuple: (duration, thumbnail_path) or None if error
    """
    from magic.utils.communication import send_to_all
    
    thumb_dir = os.path.abspath(os.path.join(dir_path, thumb_name + ".jpg"))

    # FFMPEG Command with -y Flag to overwrite Thumbnail File
    ffmpeg_command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-ss", "2",         # Seek to 2 Seconds
        "-vframes", "1",    # Capture 1 Frame
        thumb_dir
    ]

    # FFPROBE COMMAND to GET Video Duration
    ffprobe_command = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_path
    ]

    try:
        # First check if video file exists
        if not os.path.exists(video_path):
            logger.error(f"Video file does not exist: {video_path}")
            send_to_all(message, f"❌ Video file not found: {os.path.basename(video_path)}")
            return None

        # Run ffmpeg command to create thumbnail
        ffmpeg_result = subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        if ffmpeg_result.returncode != 0:
            logger.error(f"Error creating thumbnail: {ffmpeg_result.stderr}")

        # Run ffprobe command to get duration
        result = subprocess.check_output(ffprobe_command, stderr=subprocess.STDOUT, universal_newlines=True)

        try:
            duration = int(float(result))
        except (ValueError, TypeError) as e:
            logger.error(f"Error parsing video duration: {e}, result was: {result}")
            duration = 0

        # Verify thumbnail was created
        if not os.path.exists(thumb_dir):
            logger.warning(f"Thumbnail not created at {thumb_dir}, using default")
            # Create a blank thumbnail as fallback
            create_default_thumbnail(thumb_dir)

        return duration, thumb_dir
    except subprocess.CalledProcessError as e:
        logger.error(f"Command execution error: {e.stderr if hasattr(e, 'stderr') else e}")
        send_to_all(message, f"❌ Error processing video: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing video: {e}")
        send_to_all(message, f"❌ Error processing video: {e}")
        return None


def create_default_thumbnail(thumb_path):
    """Create a default thumbnail when normal thumbnail creation fails"""
    try:
        # Create a 640x360 black image
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi",
            "-i", "color=c=black:s=640x360",
            "-frames:v", "1",
            thumb_path
        ]
        subprocess.run(ffmpeg_cmd, check=True, capture_output=True)
        logger.info(f"Created default thumbnail at {thumb_path}")
        return thumb_path
    except Exception as e:
        logger.error(f"Failed to create default thumbnail: {e}")
        return None
