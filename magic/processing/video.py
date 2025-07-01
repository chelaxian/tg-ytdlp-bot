"""
Video processing module for video splitting, thumbnail creation, and video sending
"""
import os
import math
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from config import Config
from pyrogram import enums


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
    from ..database.firebase import logger
    
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
    """Legacy function for getting duration and thumbnail"""
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
    from ..database.firebase import logger
    from ..utils.communication import send_to_all
    from ..utils.filesystem import create_directory
    
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
    from ..database.firebase import logger
    
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
    """Send video to user with proper formatting and information"""
    from ..database.firebase import logger
    from ..utils.formatters import humanbytes, TimeFormatter
    from ..user.settings import is_mediainfo_enabled
    from ..utils.communication import send_mediainfo_if_enabled
    
    try:
        # Get file size
        file_size = os.path.getsize(video_abs_path)
        file_size_str = humanbytes(file_size)
        
        # Format duration
        duration_str = TimeFormatter(duration * 1000)  # Convert to milliseconds
        
        # Create final caption with video info
        video_info = f"📁 {file_size_str} | ⏱ {duration_str}"
        final_caption = f"{caption}\n\n{video_info}"
        
        if info_text:
            final_caption += f"\n\n{info_text}"
            
        # Truncate if too long
        if len(final_caption) > 1024:
            final_caption = final_caption[:1021] + "..."
        
        # Send video
        app = message._client  # Get the pyrogram client
        sent_message = app.send_video(
            chat_id=message.chat.id,
            video=video_abs_path,
            caption=final_caption,
            duration=duration,
            thumb=thumb_file_path if thumb_file_path and os.path.exists(thumb_file_path) else None,
            parse_mode=enums.ParseMode.HTML,
            reply_to_message_id=message.id
        )
        
        # Send mediainfo if enabled
        if is_mediainfo_enabled(message.chat.id):
            send_mediainfo_if_enabled(message.chat.id, video_abs_path, message)
        
        logger.info(f"Video sent successfully: {full_video_title}")
        return sent_message
        
    except Exception as e:
        logger.error(f"Error sending video: {e}")
        from ..utils.communication import send_to_all
        send_to_all(message, f"❌ Error sending video: {e}")
        return None 