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
from magic.utils.formatters import humanbytes

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
    """
    Function to send video with all necessary parameters
    """
    try:
        # Import here to avoid circular import
        from magic.utils.communication import send_to_all, send_to_logger

        # First check if the video file actually exists and is valid
        if not os.path.exists(video_abs_path):
            logger.error(f"Video file does not exist: {video_abs_path}")
            send_to_all(message, f"❌ Video file not found: {os.path.basename(video_abs_path)}")
            return False

        # Check if file size is reasonable (not 0 bytes)
        file_size = os.path.getsize(video_abs_path)
        if file_size == 0:
            logger.error(f"Video file is empty (0 bytes): {video_abs_path}")
            send_to_all(message, f"❌ Video file is empty: {os.path.basename(video_abs_path)}")
            return False

        # Import app here to avoid circular import
        from magic.handlers.commands import app
        
        # Send the video to user
        user_id = message.chat.id
        
        # Build the full caption with info
        full_caption = caption
        if tags_text:
            full_caption += f"\n\n{tags_text}"
        if info_text:
            full_caption += f"\n\n{info_text}"

        # Try to send the video
        try:
            video_msg = app.send_video(
                chat_id=user_id,
                video=video_abs_path,
                duration=duration,
                thumb=thumb_file_path if thumb_file_path and os.path.exists(thumb_file_path) else None,
                caption=full_caption[:1024],  # Telegram caption limit
                reply_to_message_id=message.id
            )
            
            # Also send to logs channel if configured
            if hasattr(Config, 'LOGS_ID') and Config.LOGS_ID:
                try:
                    log_msg = app.send_video(
                        chat_id=Config.LOGS_ID,
                        video=video_abs_path,
                        duration=duration,
                        thumb=thumb_file_path if thumb_file_path and os.path.exists(thumb_file_path) else None,
                        caption=f"📹 {full_video_title}\n👤 User: {user_id}\n📊 {humanbytes(file_size)}"[:1024]
                    )
                except Exception as e:
                    logger.warning(f"Failed to send video to logs channel: {e}")

            send_to_logger(message, f"Video sent successfully: {full_video_title} ({humanbytes(file_size)})")
            return True

        except Exception as e:
            logger.error(f"Failed to send video: {e}")
            send_to_all(message, f"❌ Failed to send video: {e}")
            return False

    except Exception as e:
        logger.error(f"Error in send_videos function: {e}")
        return False
    finally:
        # Always try to clean up temporary files
        try:
            if os.path.exists(video_abs_path):
                os.remove(video_abs_path)
                logger.info(f"Cleaned up video file: {video_abs_path}")
        except Exception as e:
            logger.warning(f"Failed to clean up video file {video_abs_path}: {e}")
        
        try:
            if thumb_file_path and os.path.exists(thumb_file_path):
                os.remove(thumb_file_path)
                logger.info(f"Cleaned up thumbnail file: {thumb_file_path}")
        except Exception as e:
            logger.warning(f"Failed to clean up thumbnail file {thumb_file_path}: {e}")

        # Clean up temp description file
        temp_desc_path = os.path.join(os.path.dirname(video_abs_path), "description.txt")
        if os.path.exists(temp_desc_path):
            try:
                os.remove(temp_desc_path)
            except Exception as e:
                logger.error(f"Error removing temporary description file: {e}")




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
            from magic.utils.communication import send_to_all
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
        from magic.utils.communication import send_to_all
        send_to_all(message, f"❌ Error processing video: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing video: {e}")
        from magic.utils.communication import send_to_all
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
    except Exception as e:
        logger.error(f"Failed to create default thumbnail: {e}")
