
import os
import math
import hashlib
import subprocess
import shutil
import logging
import time
import re
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize
from HELPERS.app_instance import get_app
from HELPERS.logger import logger, send_to_all, send_to_logger
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from HELPERS.safe_messeger import safe_forward_messages
from COMMANDS.format_cmd import get_user_mkv_preference
from pyrogram import enums

# Get app instance for decorators
app = get_app()

def get_ffmpeg_path():
    messages = safe_get_messages(None)
    """Get FFmpeg path - first try system PATH, then fallback to local binary"""
    import shutil
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # First try to find ffmpeg in system PATH
    ffmpeg_path = shutil.which('ffmpeg')
    if not ffmpeg_path:
        # Fallback to local binary
        if os.name == 'nt':  # Windows
            ffmpeg_path = os.path.join(project_root, "ffmpeg.exe")
        else:  # Linux/Unix
            ffmpeg_path = os.path.join(project_root, "ffmpeg")
        
        if not os.path.exists(ffmpeg_path):
            logger.error(safe_get_messages(None).FFMPEG_NOT_FOUND_MSG)
            return None
    
    return ffmpeg_path

def normalize_path_for_ffmpeg(path, for_ffmpeg=True):
    """Normalize path for FFmpeg compatibility across platforms"""
    if os.name == 'nt':  # Windows
        # For Windows, normalize the path first
        normalized = os.path.normpath(path)
        
        # Convert to forward slashes for FFmpeg compatibility
        normalized = normalized.replace('\\', '/')
        
        # Only add quotes if this is for FFmpeg command line
        if for_ffmpeg and (' ' in normalized or any(char in normalized for char in ['(', ')', '[', ']', '{', '}', '&', '|', ';', '"', "'"])):
            # For Windows, use double quotes and escape internal quotes
            escaped_path = normalized.replace('"', '\\"')
            normalized = f'"{escaped_path}"'
        return normalized
    else:  # Linux/Unix
        # For Linux, normalize the path and use absolute path
        normalized = os.path.normpath(path)
        return os.path.abspath(normalized)

def create_safe_filename(original_path, prefix="safe", extension=None):
    """Create a safe filename for cross-platform compatibility"""
    import hashlib
    import time
    import re
    
    # Get original filename and extension
    base_name = os.path.basename(original_path)
    if extension is None:
        name, ext = os.path.splitext(base_name)
    else:
        name = os.path.splitext(base_name)[0]
        ext = extension
    
    # Create safe name using hash and timestamp
    file_hash = hashlib.md5(original_path.encode('utf-8')).hexdigest()[:8]
    timestamp = int(time.time())
    
    # Clean the original name - remove or replace problematic characters
    # Keep only alphanumeric characters, spaces, dots, and common punctuation
    safe_chars = re.sub(r'[^\w\s\-\.\(\)]', '_', name)
    # Limit length to avoid path issues
    safe_chars = safe_chars[:50] if len(safe_chars) > 50 else safe_chars
    
    # Use cleaned name + hash + timestamp for maximum compatibility
    safe_name = f"{prefix}_{safe_chars}_{file_hash}_{timestamp}{ext}"
    
    # Ensure no double underscores
    safe_name = re.sub(r'_+', '_', safe_name)
    
    return safe_name

def test_path_handling():
    """Test function to verify path handling with special characters"""
    # Use universal path format
    test_path = os.path.join("users", "7360853", "Ценам приказано не расти _ Послушаются ли они (Eng.en.srt")
    
    logger.info(f"Testing path: {test_path}")
    logger.info(f"Path exists: {os.path.exists(test_path)}")
    logger.info(f"Platform: {os.name}")
    
    # Test universal path handling
    normalized_path = os.path.normpath(test_path)
    logger.info(f"Normalized path: {normalized_path}")
    
    return True

def get_ytdlp_path():
    messages = safe_get_messages(None)
    """Get yt-dlp binary path - first try system PATH, then fallback to local binary.
    This is used only for functions that need the binary directly (like /cookies_from_browser)"""
    import shutil
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # First try to find yt-dlp in system PATH
    ytdlp_path = shutil.which('yt-dlp')
    if not ytdlp_path:
        # Fallback to local binary
        if os.name == 'nt':  # Windows
            ytdlp_path = os.path.join(project_root, "yt-dlp.exe")
        else:  # Linux/Unix
            ytdlp_path = os.path.join(project_root, "yt-dlp")
        
        if not os.path.exists(ytdlp_path):
            logger.error(safe_get_messages(None).YTDLP_NOT_FOUND_MSG)
            return None
    
    return ytdlp_path

def split_video_2(dir, video_name, video_path, video_size, max_size, duration, user_id):
    messages = safe_get_messages(None)
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
        if rounds and rounds > 20:
            logger.warning(safe_get_messages(user_id).FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG.format(rounds=rounds))

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
                logger.info(safe_get_messages(user_id).FFMPEG_SPLITTING_VIDEO_PART_MSG.format(current=x+1, total=rounds, start_time=start_time, end_time=end_time))
                ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=target_name)

                # Verify the split was successful
                if not os.path.exists(target_name) or os.path.getsize(target_name) == 0:
                    logger.error(safe_get_messages(user_id).FFMPEG_FAILED_CREATE_SPLIT_PART_MSG.format(part=x+1, target_name=target_name))
                else:
                    logger.info(safe_get_messages(user_id).FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG.format(part=x+1, target_name=target_name, size=os.path.getsize(target_name)))

            except Exception as e:
                logger.error(safe_get_messages(user_id).FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG.format(part=x+1, error=e))
                # If a part fails, we continue with the others

        split_vid_dict = {
            "video": caption_lst,
            "path": path_lst
        }

        logger.info(safe_get_messages(user_id).FFMPEG_VIDEO_SPLIT_SUCCESS_MSG.format(count=len(path_lst)))
        return split_vid_dict

    except Exception as e:
        logger.error(safe_get_messages(user_id).FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG.format(error=e))
        # Return what we have so far
        split_vid_dict = {
            "video": caption_lst,
            "path": path_lst,
            "duration": duration
        }
        return split_vid_dict


def get_duration_thumb_(dir, video_path, thumb_name):
    messages = safe_get_messages(None)
    # Generate a short unique name for the thumbnail
    thumb_hash = hashlib.md5(thumb_name.encode()).hexdigest()[:10]
    thumb_dir = os.path.abspath(os.path.join(dir, thumb_hash + ".jpg"))
    try:
        width, height, duration = get_video_info_ffprobe(video_path)
        duration = int(duration)
        orig_w = width if width and width > 0 else 1920
        orig_h = height if height and height > 0 else 1080
    except Exception as e:
        logger.error(safe_get_messages(None).FFMPEG_FFPROBE_BYPASS_ERROR_MSG.format(video_path=video_path, error=e))
        import traceback
        logger.error(traceback.format_exc())
        duration = 0
        orig_w, orig_h = 1920, 1080  # Default dimensions
    
    # Determine optimal thumbnail size based on video aspect ratio
    aspect_ratio = orig_w / orig_h
    max_dimension = 640  # Maximum width or height
    
    if aspect_ratio and aspect_ratio > 1.5:  # Wide/horizontal video (16:9, etc.)
        thumb_w = max_dimension
        thumb_h = int(max_dimension / aspect_ratio)
    elif aspect_ratio and aspect_ratio < 0.75:  # Tall/vertical video (9:16, etc.)
        thumb_h = max_dimension
        thumb_w = int(max_dimension * aspect_ratio)
    else:  # Square-ish video (1:1, 4:3, etc.)
        if orig_w >= orig_h:
            thumb_w = max_dimension
            thumb_h = int(max_dimension / aspect_ratio)
        else:
            thumb_h = max_dimension
            thumb_w = int(max_dimension * aspect_ratio)
    
    # Ensure minimum size
    thumb_w = max(thumb_w, 240)
    thumb_h = max(thumb_h, 240)
    
    # Create thumbnail using FFmpeg instead of moviepy
    try:
        # Get FFmpeg path using the common function
        ffmpeg_path = get_ffmpeg_path()
        if not ffmpeg_path:
            logger.error(safe_get_messages(None).FFMPEG_NOT_FOUND_MSG)
            create_default_thumbnail(thumb_dir, thumb_w, thumb_h)
            return duration, thumb_dir
        
        ffmpeg_command = [
            ffmpeg_path,
            "-y",
            "-i", video_path,
            "-ss", "2",         # Seek to 2 Seconds
            "-vframes", "1",    # Capture 1 Frame
            "-vf", f"scale={thumb_w}:{thumb_h}",  # Scale to exact thumbnail size
            thumb_dir
        ]
        subprocess.run(ffmpeg_command, check=True, capture_output=True, encoding='utf-8', errors='replace')
    except Exception as e:
        logger.error(safe_get_messages(None).FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG.format(error=e))
        # Create default thumbnail as fallback
        create_default_thumbnail(thumb_dir, thumb_w, thumb_h)
    
    return duration, thumb_dir

def get_duration_thumb(message, dir_path, video_path, thumb_name):
    user_id = message.chat.id
    messages = safe_get_messages(user_id)
    """
    Captures a thumbnail at 2 seconds into the video and retrieves video duration.
    Creates thumbnail with same aspect ratio as video (no black bars).

    Args:
        message: The message object
        dir_path: Directory path for the thumbnail
        video_path: Path to the video file
        thumb_name: Name for the thumbnail

    Returns:
        tuple: (duration, thumbnail_path) or None if error
    """
    # Generate a short unique name for the thumbnail
    thumb_hash = hashlib.md5(thumb_name.encode()).hexdigest()[:10]
    thumb_dir = os.path.abspath(os.path.join(dir_path, thumb_hash + ".jpg"))

    # FFPROBE COMMAND to GET Video Dimensions and Duration
    ffprobe_size_command = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-of", "csv=s=x:p=0",
        video_path
    ]
    
    ffprobe_duration_command = [
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
            logger.error(safe_get_messages(user_id).FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG.format(video_path=video_path))
            send_to_all(message, safe_get_messages(user_id).VIDEO_FILE_NOT_FOUND_MSG.format(filename=os.path.basename(video_path)))
            return None

        # Get video dimensions
        try:
            size_result = subprocess.check_output(ffprobe_size_command, stderr=subprocess.STDOUT, universal_newlines=True, encoding='utf-8', errors='replace').strip()
        except UnicodeDecodeError:
            # Fallback with error handling
            size_result = subprocess.check_output(ffprobe_size_command, stderr=subprocess.STDOUT, encoding='utf-8', errors='replace').decode('utf-8', errors='replace').strip()
        # Robust parse of dimensions like "1920x1080"; tolerate any trailing garbage
        dims_match = re.search(r"(\d+)\s*x\s*(\d+)", size_result)
        if dims_match:
            try:
                orig_w = int(dims_match.group(1))
                orig_h = int(dims_match.group(2))
            except Exception as e:
                logger.error(safe_get_messages(user_id).FFMPEG_ERROR_PARSING_DIMENSIONS_MSG.format(size_result=size_result, error=e))
                orig_w, orig_h = 1920, 1080
        else:
            # Fallback to default horizontal orientation
            orig_w, orig_h = 1920, 1080
            logger.warning(safe_get_messages(user_id).FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG.format(size_result=size_result, width=orig_w, height=orig_h))
        
        # Determine optimal thumbnail size based on video aspect ratio
        aspect_ratio = orig_w / orig_h
        max_dimension = 640  # Maximum width or height
        
        if aspect_ratio and aspect_ratio > 1.5:  # Wide/horizontal video (16:9, etc.)
            thumb_w = max_dimension
            thumb_h = int(max_dimension / aspect_ratio)
        elif aspect_ratio and aspect_ratio < 0.75:  # Tall/vertical video (9:16, etc.)
            thumb_h = max_dimension
            thumb_w = int(max_dimension * aspect_ratio)
        else:  # Square-ish video (1:1, 4:3, etc.)
            if orig_w >= orig_h:
                thumb_w = max_dimension
                thumb_h = int(max_dimension / aspect_ratio)
            else:
                thumb_h = max_dimension
                thumb_w = int(max_dimension * aspect_ratio)
        
        # Ensure minimum size
        thumb_w = max(thumb_w, 240)
        thumb_h = max(thumb_h, 240)
        
        # FFMPEG Command to create thumbnail with calculated dimensions
        ffmpeg_command = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-ss", "2",         # Seek to 2 Seconds
            "-vframes", "1",    # Capture 1 Frame
            "-vf", f"scale={thumb_w}:{thumb_h}",  # Scale to exact thumbnail size
            thumb_dir
        ]

        # Run ffmpeg command to create thumbnail
        ffmpeg_result = subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
        if ffmpeg_result.returncode != 0:
            logger.error(safe_get_messages(user_id).FFMPEG_ERROR_CREATING_THUMBNAIL_MSG.format(stderr=ffmpeg_result.stderr))

        # Run ffprobe command to get duration
        try:
            result = subprocess.check_output(ffprobe_duration_command, stderr=subprocess.STDOUT, universal_newlines=True, encoding='utf-8', errors='replace')
        except UnicodeDecodeError:
            # Fallback with error handling
            result = subprocess.check_output(ffprobe_duration_command, stderr=subprocess.STDOUT, encoding='utf-8', errors='replace').decode('utf-8', errors='replace')

        try:
            # Extract duration robustly from any stdout (handle proxychains noise)
            text = str(result)
            # Prefer last numeric in the output as ffprobe prints duration alone
            matches = re.findall(r"(\d+(?:\.\d+)?)", text)
            if matches:
                duration = int(float(matches[-1]))
            else:
                raise ValueError("No numeric duration found in ffprobe output")
        except (ValueError, TypeError) as e:
            logger.error(safe_get_messages(user_id).FFMPEG_ERROR_PARSING_DURATION_MSG.format(error=e, result=result))
            duration = 0

        # Verify thumbnail was created
        if not os.path.exists(thumb_dir):
            logger.warning(safe_get_messages(user_id).FFMPEG_THUMBNAIL_NOT_CREATED_MSG.format(thumb_dir=thumb_dir))
            # Create a blank thumbnail as fallback
            create_default_thumbnail(thumb_dir, thumb_w, thumb_h)

        return duration, thumb_dir
    except subprocess.CalledProcessError as e:
        logger.error(safe_get_messages(user_id).FFMPEG_COMMAND_EXECUTION_ERROR_MSG.format(error=e.stderr if hasattr(e, 'stderr') else e))
        send_to_all(message, safe_get_messages(user_id).VIDEO_PROCESSING_ERROR_MSG.format(error=str(e)))
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing video: {e}")
        send_to_all(message, safe_get_messages(user_id).VIDEO_PROCESSING_ERROR_MSG.format(error=str(e)))
        return None

def create_default_thumbnail(thumb_path, width=480, height=480):
    """Create a default thumbnail when normal thumbnail creation fails"""
    try:
        # Get FFmpeg path using the common function
        ffmpeg_path = get_ffmpeg_path()
        if not ffmpeg_path:
            logger.error("ffmpeg not found in PATH or project directory.")
            return
        
        # Create a black image with specified dimensions (square by default)
        ffmpeg_cmd = [
            ffmpeg_path, "-y",
            "-f", "lavfi",
            "-i", f"color=c=black:s={width}x{height}",
            "-frames:v", "1",
            thumb_path
        ]
        subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
        logger.info(f"Created default {width}x{height} thumbnail at {thumb_path}")
    except Exception as e:
        logger.error(f"Failed to create default thumbnail: {e}")


def ensure_utf8_srt(srt_path):
    """Ensure SRT file is in UTF-8 encoding"""
    try:
        with open(srt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return srt_path
    except UnicodeDecodeError:
        try:
            # Try to detect encoding and convert to UTF-8
            import chardet
            with open(srt_path, 'rb') as f:
                raw_data = f.read()
                detected = chardet.detect(raw_data)
                encoding = detected['encoding'] or 'cp1252'
            
            with open(srt_path, 'r', encoding=encoding) as f:
                content = f.read()
            
            # Write back as UTF-8
            with open(srt_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return srt_path
        except Exception as e:
            logger.error(f"Error converting SRT to UTF-8: {e}")
            return None


def force_fix_arabic_encoding(srt_path, lang):
    """Fix Arabic subtitle encoding issues"""
    try:
        with open(srt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply Arabic-specific fixes if needed
        if lang in {'ar', 'fa', 'ur', 'ps', 'iw', 'he'}:
            # Add any Arabic-specific text processing here
            pass
        
        with open(srt_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return srt_path
    except Exception as e:
        logger.error(f"Error fixing Arabic encoding: {e}")
        return None


def ffmpeg_extract_subclip(video_path, start_time, end_time, targetname):
    """Extract a subclip from video using FFmpeg"""
    try:
        # Get FFmpeg path using the common function
        ffmpeg_path = get_ffmpeg_path()
        if not ffmpeg_path:
            logger.error("ffmpeg not found in PATH or project directory.")
            return False
        
        # Check if video file exists first (without quotes)
        if not os.path.exists(video_path):
            logger.error(f"Video file not found: {video_path}")
            return False
        
        # Use absolute paths without quotes for Linux
        normalized_video_path = os.path.abspath(video_path)
        normalized_targetname = os.path.abspath(targetname)
        
        # First try with -c copy (fast, no re-encoding)
        # Use -ss after -i for more accurate seeking, then -t for duration
        # This ensures frame-accurate cutting
        duration = end_time - start_time
        cmd = [
            ffmpeg_path, '-y',
            '-i', normalized_video_path,
            '-ss', str(start_time),
            '-t', str(duration),
            '-c', 'copy',
            '-avoid_negative_ts', 'make_zero',
            '-fflags', '+genpts',
            '-f', 'mp4',
            normalized_targetname
        ]
        
        logger.info(f"Running ffmpeg extract command: {' '.join(cmd)}")
        logger.info(f"Video path: {normalized_video_path}")
        logger.info(f"Target path: {normalized_targetname}")
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=300)
            if os.path.exists(targetname) and os.path.getsize(targetname) > 0:
                # Verify trimmed file duration matches expected
                try:
                    _, _, trimmed_duration = get_video_info_ffprobe(targetname)
                    trimmed_duration = float(trimmed_duration) if trimmed_duration else 0
                    expected_duration = end_time - start_time
                    
                    # If duration doesn't match (more than 5 seconds difference), re-encode is needed
                    if abs(trimmed_duration - expected_duration) > 5:
                        logger.warning(f"FFmpeg extract with -c copy produced wrong duration ({trimmed_duration}s, expected {expected_duration}s), trying re-encode")
                        raise subprocess.CalledProcessError(1, cmd, f"Duration mismatch: {trimmed_duration}s vs {expected_duration}s")
                    
                    logger.info(f"FFmpeg extract completed successfully for {targetname}")
                    logger.info(f"Output file size: {os.path.getsize(targetname)} bytes")
                    logger.info(f"Trimmed duration: {trimmed_duration}s (expected {expected_duration}s)")
                    return True
                except Exception as verify_error:
                    logger.warning(f"Error verifying trimmed file duration: {verify_error}, trying re-encode")
                    raise subprocess.CalledProcessError(1, cmd, f"Duration verification failed: {verify_error}")
            else:
                logger.warning(f"FFmpeg extract completed but output file is missing or empty, trying re-encode")
                raise subprocess.CalledProcessError(1, cmd, "Output file missing or empty")
        except subprocess.CalledProcessError as e:
            # If -c copy fails, try with re-encoding (slower but more reliable)
            logger.warning(f"FFmpeg extract with -c copy failed (code {e.returncode}), trying with re-encoding")
            full_stderr = e.stderr if e.stderr else ""
            full_stdout = e.stdout if e.stdout else ""
            logger.error(f"FFmpeg stderr (full): {full_stderr}")
            logger.error(f"FFmpeg stdout (full): {full_stdout}")
            
            # Try with re-encoding using -ss after -i and -t for precise cutting
            # Explicitly specify output format with -f mp4
            duration = end_time - start_time
            cmd_reencode = [
                ffmpeg_path, '-y',
                '-i', normalized_video_path,
                '-ss', str(start_time),
                '-t', str(duration),
                '-c:v', 'libx264',
                '-c:a', 'aac',
                '-preset', 'fast',
                '-crf', '23',
                '-movflags', '+faststart',
                '-f', 'mp4',
                normalized_targetname
            ]
            
            logger.info(f"Trying re-encode: {' '.join(cmd_reencode)}")
            try:
                result = subprocess.run(cmd_reencode, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=600)
                if os.path.exists(targetname) and os.path.getsize(targetname) > 0:
                    # Verify trimmed file duration matches expected
                    try:
                        _, _, trimmed_duration = get_video_info_ffprobe(targetname)
                        trimmed_duration = float(trimmed_duration) if trimmed_duration else 0
                        expected_duration = end_time - start_time
                        
                        # If duration still doesn't match, log warning but return True (re-encoding should work)
                        if abs(trimmed_duration - expected_duration) > 5:
                            logger.warning(f"FFmpeg re-encode produced duration ({trimmed_duration}s) that doesn't match expected ({expected_duration}s)")
                        else:
                            logger.info(f"Trimmed duration verified: {trimmed_duration}s (expected {expected_duration}s)")
                    except Exception as verify_error:
                        logger.warning(f"Error verifying re-encoded file duration: {verify_error}")
                    
                    logger.info(f"FFmpeg extract with re-encoding completed successfully for {targetname}")
                    logger.info(f"Output file size: {os.path.getsize(targetname)} bytes")
                    return True
                else:
                    logger.error(f"FFmpeg re-encode completed but output file is missing or empty")
                    return False
            except subprocess.CalledProcessError as e2:
                error_details = ""
                if e2.stderr:
                    error_details = f"stderr: {e2.stderr}"
                if e2.stdout:
                    error_details += f"\nstdout: {e2.stdout}" if error_details else f"stdout: {e2.stdout}"
                logger.error(f"FFmpeg re-encode error (code {e2.returncode}): {error_details if error_details else str(e2)}")
                return False
            except subprocess.TimeoutExpired:
                logger.error(f"FFmpeg re-encode timed out after 600 seconds")
                return False
    except Exception as e:
        logger.error(f"Unexpected error during FFmpeg extract: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


# ####################################################################################
# ####################################################################################

def get_video_info_ffprobe(video_path):
    import json
    try:
        result = subprocess.run([
            'ffprobe', '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream=width,height',
            '-show_entries', 'format=duration',
            '-of', 'json', video_path
        ], capture_output=True, text=True, encoding='utf-8', errors='replace')
        if result.returncode == 0:
            data = json.loads(result.stdout)
            width = data['streams'][0]['width'] if data['streams'] else 0
            height = data['streams'][0]['height'] if data['streams'] else 0
            duration = float(data['format']['duration']) if 'format' in data and 'duration' in data['format'] else 0
            return width, height, duration
    except Exception as e:
        logger.error(f'ffprobe error: {e}')
        return 0, 0, 0



def embed_subs_to_video(video_path, user_id, tg_update_callback=None, app=None, message=None, subtitle_tracks=None):
    messages = safe_get_messages(user_id)
    """
    Burning (hardcode) subtitles in a video file, if there is any .SRT file and subs.txt
    tg_update_callback (Progress: Float, ETA: StR) - Function for updating the status in Telegram
    subtitle_tracks: Optional list of dicts with 'path' and 'language' keys for successfully downloaded subtitles
    """
    try:
        if not video_path or not os.path.exists(video_path):
            logger.error(f"Video file not found: {video_path}")
            return False
        
        user_dir = os.path.join("users", str(user_id))
        
        # If subtitle_tracks is provided, skip subs.txt check and use provided tracks
        if subtitle_tracks and len(subtitle_tracks) > 0:
            logger.info(f"Using provided subtitle_tracks ({len(subtitle_tracks)} tracks), skipping subs.txt check")
        else:
            # Old logic: check subs.txt file
            subs_file = os.path.join(user_dir, "subs.txt")
            if not os.path.exists(subs_file):
                logger.info(f"No subs.txt for user {user_id}, skipping embed_subs_to_video")
                return False
            
            with open(subs_file, "r", encoding="utf-8") as f:
                subs_lang = f.read().strip()
            if not subs_lang or subs_lang == "OFF":
                logger.info(f"Subtitles disabled for user {user_id}")
                return False
        
        video_dir = os.path.dirname(video_path)
        
        # Если контейнер MKV — выполняем «софт»-встраивание дорожки субтитров без прожига
        try:
            mkv_selected = bool(get_user_mkv_preference(user_id))
        except Exception:
            mkv_selected = False
        is_mkv_file = video_path.lower().endswith('.mkv')

        if is_mkv_file or mkv_selected:
            # If subtitle_tracks is provided, use only successfully downloaded tracks
            if subtitle_tracks and len(subtitle_tracks) > 0:
                # Use the list of successfully downloaded subtitle tracks
                subs_paths = []
                for track in subtitle_tracks:
                    track_path = track.get('path', '')
                    if track_path and os.path.exists(track_path) and os.path.getsize(track_path) > 0:
                        # Use full path from track_path
                        subs_paths.append(track_path)
                
                if not subs_paths:
                    logger.warning(f"No valid subtitle tracks found in provided list for soft-mux MKV")
                    return False
                
                logger.info(f"Using {len(subs_paths)} successfully downloaded subtitle tracks for MKV soft-mux")
                # Set filtered_srt_files to empty to skip old logic
                filtered_srt_files = []
            else:
                # Fallback: Check for multiple subtitle selection from Always Ask menu
                try:
                    from DOWN_AND_UP.always_ask_menu import get_filters
                    fstate = get_filters(user_id)
                    selected_subs_langs = fstate.get("selected_subs_langs", []) or []
                    subs_all_selected = fstate.get("subs_all_selected", False)
                except Exception:
                    selected_subs_langs = []
                    subs_all_selected = False
                
                # Get all SRT files
                srt_files = [f for f in os.listdir(video_dir) if f.lower().endswith('.srt')]
                if not srt_files:
                    logger.info(f"No .srt files found in {video_dir} for soft-mux MKV")
                    return False
                
                # Filter SRT files based on selection
                if subs_all_selected:
                    # Use all SRT files
                    filtered_srt_files = srt_files
                elif selected_subs_langs:
                    # Use only selected languages (match by filename pattern)
                    filtered_srt_files = []
                    for srt_file in srt_files:
                        # Check if filename contains any of the selected language codes
                        srt_lower = srt_file.lower()
                        for lang in selected_subs_langs:
                            if lang.lower() in srt_lower:
                                filtered_srt_files.append(srt_file)
                                break
                    if not filtered_srt_files:
                        # Fallback to all if no matches
                        filtered_srt_files = srt_files
                else:
                    # Single language mode - use first SRT file
                    filtered_srt_files = [srt_files[0]]
                
                if not filtered_srt_files:
                    logger.info(f"No matching .srt files found for soft-mux MKV")
                    return False

            # Подготавливаем путь вывода
            video_base = os.path.splitext(os.path.basename(video_path))[0]
            output_path = os.path.join(video_dir, f"{video_base}_with_subs_temp.mkv")

            # Собираем MKV: видео/аудио копируем, субтитры как srt
            ffmpeg_path = get_ffmpeg_path()
            if not ffmpeg_path:
                logger.error("ffmpeg not found for MKV soft-mux")
                return False
            
            # Build ffmpeg command with multiple subtitle inputs
            cmd = [ffmpeg_path, '-y', '-i', video_path]
            
            # Add all subtitle files as inputs
            if subtitle_tracks and len(subtitle_tracks) > 0:
                # Use full paths from subtitle_tracks - subs_paths already contains full paths
                final_subs_paths = []
                for subs_path in subs_paths:
                    # Ensure UTF-8 encoding
                    subs_path_utf8 = ensure_utf8_srt(subs_path)
                    if subs_path_utf8 and os.path.exists(subs_path_utf8) and os.path.getsize(subs_path_utf8) > 0:
                        cmd += ['-i', subs_path_utf8]
                        final_subs_paths.append(subs_path_utf8)
                subs_paths = final_subs_paths
            else:
                # Build paths from filenames (old logic)
                subs_paths = []
                for srt_file in filtered_srt_files:
                    subs_path = os.path.join(video_dir, srt_file)
                    subs_path = ensure_utf8_srt(subs_path)
                    if subs_path and os.path.exists(subs_path) and os.path.getsize(subs_path) > 0:
                        cmd += ['-i', subs_path]
                        subs_paths.append(subs_path)
            
            if not subs_paths:
                logger.error("No valid subtitle files for MKV soft-mux")
                return False
            
            # Map video and audio streams, then all subtitle streams
            cmd += ['-c', 'copy', '-c:s', 'srt', '-map', '0:v', '-map', '0:a']
            
            # Map all subtitle streams
            for i in range(len(subs_paths)):
                cmd += ['-map', f'{i+1}:0']
            
            # Add language metadata for each subtitle track
            if subtitle_tracks and len(subtitle_tracks) > 0:
                # Use language from subtitle_tracks
                for i, track in enumerate(subtitle_tracks):
                    track_lang = track.get('language', '')
                    if track_lang:
                        # Extract base language code (e.g., 'en' from 'en-US' or 'en-orig')
                        lang_code = track_lang.split('-')[0] if '-' in track_lang else track_lang
                        cmd += ['-metadata:s:s:' + str(i), f'language={lang_code}']
            else:
                # Use filename-based language detection (old logic)
                for i, srt_file in enumerate(filtered_srt_files):
                    # Try to extract language from filename
                    lang_code = None
                    srt_lower = srt_file.lower()
                    try:
                        from DOWN_AND_UP.always_ask_menu import get_filters
                        fstate = get_filters(user_id)
                        selected_subs_langs = fstate.get("selected_subs_langs", []) or []
                        subs_all_selected = fstate.get("subs_all_selected", False)
                    except Exception:
                        selected_subs_langs = []
                        subs_all_selected = False
                    
                    if subs_all_selected or selected_subs_langs:
                        # Try to match with selected languages
                        for lang in (selected_subs_langs if selected_subs_langs else []):
                            if lang.lower() in srt_lower:
                                lang_code = lang.split('-')[0] if '-' in lang else lang
                                break
                
                if not lang_code and subs_lang and subs_lang != 'OFF':
                    lang_code = subs_lang.split('-')[0] if '-' in subs_lang else subs_lang
                
                if lang_code:
                    cmd += ['-metadata:s:s:' + str(i), f'language={lang_code}']
            
            cmd += [output_path]

            try:
                logger.info(f"Running ffmpeg soft-mux (MKV) with {len(subs_paths)} subtitle tracks: {' '.join(cmd)}")
                subprocess.run(cmd, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
            except Exception as e:
                logger.error(f"FFmpeg soft-mux failed: {e}")
                return False

            if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
                logger.error("Soft-mux output missing or empty")
                return False

            # Безопасно заменяем исходный файл на результат (оставляем .mkv путь)
            backup_path = video_path + ".backup"
            try:
                os.rename(video_path, backup_path)
                os.rename(output_path, video_path)
                if os.path.exists(backup_path):
                    os.remove(backup_path)
            except Exception as e:
                logger.error(f"Error replacing MKV after soft-mux: {e}")
                # Откат
                try:
                    if os.path.exists(video_path):
                        os.remove(video_path)
                    if os.path.exists(backup_path):
                        os.rename(backup_path, video_path)
                except Exception:
                    pass
                if os.path.exists(output_path):
                    os.remove(output_path)
                return False

            logger.info(f"Soft subtitle mux into MKV completed successfully with {len(subs_paths)} tracks")
            return True

        # We get video parameters via FFPRobe (жёсткое прожигание для MP4 и прочих контейнеров)
        width, height, total_time = get_video_info_ffprobe(video_path)
        if width == 0 or height == 0:
            logger.error(f"Unable to determine video resolution via ffprobe: width={width}, height={height}")
            return False
        original_size = os.path.getsize(video_path)

        # Checking the duration of the video
        if total_time and total_time > Config.MAX_SUB_DURATION:
            logger.info(f"Video duration too long for subtitles: {total_time} sec")
            return False

        # Checking the file size
        original_size_mb = original_size / (1024 * 1024)
        if original_size_mb and original_size_mb > Config.MAX_SUB_SIZE:
            logger.info(f"Video file too large for subtitles: {original_size_mb:.2f} MB")
            return False

        # Video quality testing on the smallest side
        # Logue video parameters before checking quality
        logger.info(f"Quality check: width={width}, height={height}, min_side={min(width, height)}, limit={Config.MAX_SUB_QUALITY}")
        if min(width, height) > Config.MAX_SUB_QUALITY:
            logger.info(f"Video quality too high for subtitles: {width}x{height}, min side: {min(width, height)}p > {Config.MAX_SUB_QUALITY}p")
            return False

        # --- Simplified search: take any .SRT file in the folder ---
        srt_files = [f for f in os.listdir(video_dir) if f.lower().endswith('.srt')]
        if not srt_files:
            logger.info(f"No .srt files found in {video_dir}")
            return False
        
        subs_path = os.path.join(video_dir, srt_files[0])
        if not os.path.exists(subs_path):
            logger.error(f"Subtitle file not found: {subs_path}")
            return False

        # Always bring .SRT to UTF-8
        subs_path = ensure_utf8_srt(subs_path)
        if not subs_path or not os.path.exists(subs_path) or os.path.getsize(subs_path) == 0:
            logger.error(f"Subtitle file after ensure_utf8_srt is missing or empty: {subs_path}")
            return False

        # Forcibly correcting Arab cracies
        if subs_lang in {'ar', 'fa', 'ur', 'ps', 'iw', 'he'}:
            subs_path = force_fix_arabic_encoding(subs_path, subs_lang)
        if not subs_path or not os.path.exists(subs_path) or os.path.getsize(subs_path) == 0:
            logger.error(f"Subtitle file after force_fix_arabic_encoding is missing or empty: {subs_path}")
            return False
        
        video_base = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(video_dir, f"{video_base}_with_subs_temp.mp4")
        
        # We get the duration of the video via FFPRobe
        def get_duration(path):
            messages = safe_get_messages(user_id)
            try:
                import json
                result = subprocess.run([
                    'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                    '-of', 'json', path
                ], capture_output=True, text=True)
                if result.returncode == 0:
                    data = json.loads(result.stdout)
                    return float(data['format']['duration'])
            except Exception as e:
                logger.error(f"ffprobe error: {e}")
            return None
        
        # Field of subtitles with improved styling - using Arial Black font and black 75% background
        subs_path_escaped = subs_path.replace("'", "'\\''")
        # Use Arial Black font with black 75% background and white text
        filter_arg = f"subtitles='{subs_path_escaped}':force_style='FontName=Arial Black,FontSize=16,PrimaryColour=&Hffffff,OutlineColour=&H000000,BackColour=&H80000000,Outline=2,Shadow=1,MarginV=25'"
        cmd = [
            'ffmpeg',
            '-y',
            '-i', video_path,
            '-vf', filter_arg,
            '-c:a', 'copy',
            output_path
        ]
        
        logger.info(f"Running ffmpeg command: {' '.join(cmd)}")
        
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1
        )
        progress = 0.0
        last_update = time.time()
        eta = "?"
        time_pattern = re.compile(r'time=([0-9:.]+)')
        
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            logger.info(line.strip())
            match = time_pattern.search(line)
            if match and total_time:
                t = match.group(1)
                # Transform T (hh: mm: ss.xx) in seconds
                h, m, s = 0, 0, 0.0
                parts = t.split(':')
                if len(parts) == 3:
                    h, m, s = int(parts[0]), int(parts[1]), float(parts[2])
                elif len(parts) == 2:
                    m, s = int(parts[0]), float(parts[1])
                elif len(parts) == 1:
                    s = float(parts[0])
                cur_sec = h * 3600 + m * 60 + s
                progress = min(cur_sec / total_time, 1.0)
                # ETA
                if progress and progress > 0:
                    elapsed = time.time() - last_update
                    eta_sec = int((1.0 - progress) * (elapsed / progress)) if progress and progress > 0 else 0
                    eta = f"{eta_sec//60}:{eta_sec%60:02d}"
                # Update every 10 seconds or with a change in progress> 1%
                if tg_update_callback and (time.time() - last_update > 10 or progress >= 1.0):
                    tg_update_callback(progress, eta)
                    last_update = time.time()
        
        proc.wait()
        
        if proc.returncode != 0:
            # Try to read any remaining output for error details
            remaining_output = proc.stdout.read() if proc.stdout else ""
            error_details = remaining_output[:500] if remaining_output else "No error details available"
            
            logger.error(f"FFmpeg error: process exited with code {proc.returncode}")
            logger.error(f"FFmpeg error details: {error_details}")
            
            # Try to identify common error types
            error_lower = error_details.lower()
            if "invalid argument" in error_lower or "invalid data" in error_lower:
                logger.error("FFmpeg error: Invalid argument or data - video/subtitle format may be incompatible")
            elif "no such file" in error_lower or "cannot find" in error_lower:
                logger.error("FFmpeg error: File not found - check if video or subtitle file exists")
            elif "permission denied" in error_lower:
                logger.error("FFmpeg error: Permission denied - check file permissions")
            elif "codec" in error_lower and ("not found" in error_lower or "unsupported" in error_lower):
                logger.error("FFmpeg error: Codec not found or unsupported")
            elif "out of memory" in error_lower or "cannot allocate" in error_lower:
                logger.error("FFmpeg error: Out of memory - video may be too large")
            
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
        
        # Check that the file exists and is not empty
        if not os.path.exists(output_path):
            logger.error("Output file does not exist after ffmpeg")
            return False
        
        # We are waiting a little so that the file will definitely complete the recording
        time.sleep(1)
        
        output_size = os.path.getsize(output_path)
        original_size = os.path.getsize(video_path)
        
        if output_size == 0:
            logger.error("Output file is empty")
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
        
        # We check that the final file is not too small (there should be at least 50% of the original)
        if output_size and output_size < original_size * 0.5:
            logger.error(f"Output file too small: {output_size} bytes (original: {original_size} bytes)")
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
        
        # Safely replace the file
        backup_path = video_path + ".backup"
        try:
            os.rename(video_path, backup_path)   # Create a backup
            os.rename(output_path, video_path)   # Rename the result
            os.remove(backup_path)               # Delete backup
        except Exception as e:
            logger.error(f"Error replacing video file: {e}")
            # Restore the source file
            if os.path.exists(backup_path):
                os.rename(backup_path, video_path)
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
        
        # Send .SRT to the user before removing
        if os.path.exists(subs_path):
            try:
                if app is not None and message is not None:
                    sent_msg = app.send_document(
                        chat_id=user_id,
                        document=subs_path,
                        caption="<blockquote>💬 Subtitles SRT-file</blockquote>",
                        reply_parameters=enums.ReplyParameters(message_id=message.id) if hasattr(enums, 'ReplyParameters') else None,
                        parse_mode=enums.ParseMode.HTML
                    )
                    from HELPERS.logger import get_log_channel
                    safe_forward_messages(get_log_channel("video"), user_id, [sent_msg.id])
                    send_to_logger(message, safe_get_messages(user_id).SUBS_SENT_MSG) 
            except Exception as e:
                logger.error(f"Error sending srt file: {e}")
            try:
                os.remove(subs_path)
            except Exception as e:
                logger.error(f"Error deleting srt file: {e}")
        
        logger.info("Successfully burned-in subtitles")
        return True
        
    except Exception as e:
        logger.error(f"Error in embed_subs_to_video: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def download_all_audio_tracks(url, user_id, video_dir, available_langs=None, use_proxy=False, info_dict=None, downloaded_format=None):
    """
    Download all available audio tracks separately for MKV multi-track support.
    Returns list of downloaded audio file paths with language info.
    If info_dict is provided, uses it instead of fetching again.
    If downloaded_format is provided, uses its language as the original audio language.
    """
    try:
        import yt_dlp
        from COMMANDS.args_cmd import get_user_ytdlp_args
        from HELPERS.proxy_helper import add_proxy_to_ytdl_opts
        from HELPERS.pot_helper import add_pot_to_ytdl_opts
        
        # Get video info to find all audio formats
        # Define user_cookie_path early so it's available for downloads
        user_cookie_path = os.path.join("users", str(user_id), "cookie.txt")
        
        if info_dict:
            info = info_dict
            logger.info("Using provided info_dict for audio tracks discovery")
        else:
            info_opts = {
                'quiet': True,
                'no_warnings': True,
                'skip_download': True,
                'noplaylist': True,
            }
            
            # Add cookies
            if os.path.exists(user_cookie_path):
                info_opts['cookiefile'] = user_cookie_path
            
            # Add proxy
            info_opts = add_proxy_to_ytdl_opts(info_opts, url, user_id)
            
            # Add PO token
            info_opts = add_pot_to_ytdl_opts(info_opts, url)
            
            with yt_dlp.YoutubeDL(info_opts) as ydl:
                info = ydl.extract_info(url, download=False)
        
        # Find original audio language - use multiple methods for better accuracy
        original_audio_lang = None
        
        # Method 1: Use language from the actually downloaded format (most accurate)
        if downloaded_format:
            lang = downloaded_format.get('language')
            if lang:
                original_audio_lang = lang
                logger.info(f"Detected original audio language from downloaded format: {original_audio_lang}")
        
        # Method 2: Try to get from video metadata
        if not original_audio_lang:
            original_audio_lang = info.get('language') or info.get('original_language')
            if original_audio_lang:
                logger.info(f"Detected original audio language from video metadata: {original_audio_lang}")
        
        # Method 3: If not found, check which language appears most frequently in video+audio formats
        if not original_audio_lang:
            lang_counts = {}
            for fmt in info.get('formats', []):
                # Look for formats with both video and audio
                if fmt.get('vcodec') != 'none' and fmt.get('acodec'):
                    lang = fmt.get('language')
                    if lang:
                        # Count by base language (e.g., 'en' for 'en-US')
                        base_lang = lang.split('-')[0] if '-' in lang else lang
                        lang_counts[base_lang] = lang_counts.get(base_lang, 0) + 1
            
            if lang_counts:
                # Get the most common language
                original_audio_lang = max(lang_counts.items(), key=lambda x: x[1])[0]
                logger.info(f"Detected original audio language from format frequency: {original_audio_lang} (appeared {lang_counts[original_audio_lang]} times)")
        
        # Method 4: If still not found, use first video+audio format
        if not original_audio_lang:
            for fmt in info.get('formats', []):
                if fmt.get('vcodec') != 'none' and fmt.get('acodec'):
                    lang = fmt.get('language')
                    if lang:
                        original_audio_lang = lang
                        logger.info(f"Detected original audio language from first video format: {original_audio_lang}")
                        break
        
        # Find all audio-only formats with different languages
        # Collect all unique languages from audio-only formats
        all_audio_langs = set()
        audio_tracks = []
        formats_count = len(info.get('formats', []))
        logger.info(f"Scanning {formats_count} formats for audio tracks...")
        
        for fmt in info.get('formats', []):
            # Check for audio-only formats (vcodec == 'none' and has acodec)
            vcodec = fmt.get('vcodec', 'none')
            acodec = fmt.get('acodec')
            lang = fmt.get('language')
            
            if vcodec == 'none' and acodec:
                # Some formats might not have language tag, skip them
                if not lang:
                    logger.debug(f"Skipping audio format {fmt.get('format_id')} - no language tag")
                    continue
                
                # Skip original language - it's already in the main video
                # For Chinese, be more careful - zh-Hans and zh-Hant are different
                # For other languages, check both exact match and base match
                if original_audio_lang:
                    # Exact match
                    if lang == original_audio_lang:
                        logger.debug(f"Skipping original audio language {lang} - already in main video")
                        continue
                    
                    # For non-Chinese languages, check base match (e.g., 'en' matches 'en-US')
                    # But preserve Chinese variants (zh-Hans vs zh-Hant)
                    orig_base = original_audio_lang.split('-')[0] if '-' in original_audio_lang else original_audio_lang
                    lang_base = lang.split('-')[0] if '-' in lang else lang
                    
                    # Only skip if base matches AND it's not a Chinese variant
                    if orig_base == lang_base and not (orig_base == 'zh' and ('Hans' in original_audio_lang or 'Hant' in original_audio_lang or 'Hans' in lang or 'Hant' in lang)):
                        # Check if it's the same variant
                        orig_variant = original_audio_lang.split('-')[1] if '-' in original_audio_lang else None
                        lang_variant = lang.split('-')[1] if '-' in lang else None
                        if orig_variant == lang_variant or (orig_variant is None and lang_variant is None):
                            logger.debug(f"Skipping original audio language variant {lang} (matches {original_audio_lang}) - already in main video")
                            continue
                
                all_audio_langs.add(lang)
                # If available_langs is provided, filter by it; otherwise use all languages
                if available_langs is None or lang in available_langs:
                    audio_tracks.append({
                        'format_id': fmt.get('format_id'),
                        'language': lang,
                        'acodec': acodec,
                        'ext': fmt.get('ext', 'm4a')
                    })
        
        logger.info(f"Found {len(audio_tracks)} audio tracks to download (total available languages: {len(all_audio_langs)})")
        logger.info(f"Available languages: {sorted(all_audio_langs)}")
        if available_langs is not None:
            logger.info(f"Filtered by selected languages: {available_langs}")
            logger.info(f"Languages to download: {[t['language'] for t in audio_tracks]}")
        
        if not audio_tracks:
            logger.info("No audio tracks found for download")
            return []
        
        # Remove duplicates - for each language, keep the best quality format
        # Group tracks by language (preserve full language codes like zh-Hans, zh-Hant, en-US, en-GB)
        # Create a format lookup for quick access
        format_lookup = {fmt.get('format_id'): fmt for fmt in info.get('formats', [])}
        
        lang_tracks = {}
        for track in audio_tracks:
            lang = track['language']
            # Keep different variants of the same base language (e.g., en-US and en-GB are different)
            # But for same exact language code, keep only the best quality
            if lang not in lang_tracks:
                lang_tracks[lang] = track
            else:
                # Compare quality - prefer higher bitrate or better codec
                current = lang_tracks[lang]
                current_fmt = format_lookup.get(current.get('format_id'), {})
                new_fmt = format_lookup.get(track.get('format_id'), {})
                
                current_bitrate = current_fmt.get('abr', 0) or current_fmt.get('tbr', 0) or 0
                new_bitrate = new_fmt.get('abr', 0) or new_fmt.get('tbr', 0) or 0
                
                # Prefer higher bitrate, or if equal, prefer better codec (OPUS > AAC > others)
                codec_priority = {'opus': 3, 'aac': 2, 'mp3': 1, 'vorbis': 1}
                current_codec = current.get('acodec', '').lower()
                new_codec = track.get('acodec', '').lower()
                current_codec_priority = codec_priority.get(current_codec.split('.')[0] if '.' in current_codec else current_codec, 0)
                new_codec_priority = codec_priority.get(new_codec.split('.')[0] if '.' in new_codec else new_codec, 0)
                
                if new_bitrate > current_bitrate or (new_bitrate == current_bitrate and new_codec_priority > current_codec_priority):
                    lang_tracks[lang] = track
        
        unique_tracks = list(lang_tracks.values())
        
        logger.info(f"Downloading {len(unique_tracks)} unique audio tracks: {[t['language'] for t in unique_tracks]}")
        if original_audio_lang:
            logger.info(f"Original audio language '{original_audio_lang}' will be used from main video (not downloaded separately)")
        audio_tracks = unique_tracks
        
        # Download each audio track
        downloaded_tracks = []
        user_args = get_user_ytdlp_args(user_id, url)
        
        for track_info in audio_tracks:
            try:
                lang = track_info['language']
                format_id = track_info['format_id']
                ext = track_info['ext']
                
                # Create output filename
                audio_filename = f"audio_{lang}.{ext}"
                audio_path = os.path.join(video_dir, audio_filename)
                
                # Download options
                download_opts = {
                    'format': format_id,
                    'outtmpl': audio_path.replace(f'.{ext}', '.%(ext)s'),
                    'quiet': True,
                    'no_warnings': True,
                    'noplaylist': True,
                }
                
                # Add cookies
                if os.path.exists(user_cookie_path):
                    download_opts['cookiefile'] = user_cookie_path
                
                # Add proxy
                download_opts = add_proxy_to_ytdl_opts(download_opts, url, user_id)
                
                # Add PO token
                download_opts = add_pot_to_ytdl_opts(download_opts, url)
                
                # Download
                with yt_dlp.YoutubeDL(download_opts) as ydl:
                    ydl.download([url])
                
                # Check if file was downloaded
                if os.path.exists(audio_path):
                    downloaded_tracks.append({
                        'path': audio_path,
                        'language': lang
                    })
                    logger.info(f"Downloaded audio track: {lang} -> {audio_path}")
                else:
                    # Try to find file with any extension
                    import glob
                    pattern = audio_path.replace(f'.{ext}', '.*')
                    found_files = glob.glob(pattern)
                    if found_files:
                        downloaded_tracks.append({
                            'path': found_files[0],
                            'language': lang
                        })
                        logger.info(f"Downloaded audio track: {lang} -> {found_files[0]}")
            except Exception as e:
                logger.error(f"Failed to download audio track {track_info.get('language')}: {e}")
                continue
        
        # Return both downloaded tracks and original language info
        return {
            'tracks': downloaded_tracks,
            'original_lang': original_audio_lang
        }
    except Exception as e:
        logger.error(f"Error in download_all_audio_tracks: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return {'tracks': [], 'original_lang': None}


def embed_all_audio_tracks_to_mkv(video_path, audio_tracks, user_id, tg_update_callback=None, app=None, message=None, original_audio_lang=None):
    """
    Embed all audio tracks into MKV file as separate switchable tracks.
    audio_tracks: list of dicts with 'path' and 'language' keys
    original_audio_lang: language code of the original audio track (already in the video)
    """
    try:
        if not video_path or not os.path.exists(video_path):
            logger.error(f"Video file not found: {video_path}")
            return False
        
        if not video_path.lower().endswith('.mkv'):
            logger.error(f"Video file is not MKV: {video_path}")
            return False
        
        if not audio_tracks:
            logger.info("No audio tracks to embed")
            return False
        
        video_dir = os.path.dirname(video_path)
        video_base = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(video_dir, f"{video_base}_with_audio_temp.mkv")
        
        ffmpeg_path = get_ffmpeg_path()
        if not ffmpeg_path:
            logger.error("ffmpeg not found for audio mux")
            return False
        
        # Build ffmpeg command
        cmd = [ffmpeg_path, '-y', '-i', video_path]
        
        # Filter valid tracks
        valid_tracks = [t for t in audio_tracks if os.path.exists(t['path'])]
        if not valid_tracks:
            logger.warning("No valid audio tracks to embed")
            return False
        
        # Add all audio files as inputs
        for track in valid_tracks:
            cmd += ['-i', track['path']]
        
        # Map video and original audio from the main video file
        cmd += ['-map', '0:v']
        # Map original audio if it exists (it should, as we downloaded video+audio)
        cmd += ['-map', '0:a?']
        
        # Map all additional audio tracks from downloaded files
        for i in range(len(valid_tracks)):
            cmd += ['-map', f'{i+1}:a']
        
        # Copy video and audio codecs (no re-encoding)
        cmd += ['-c', 'copy', '-c:a', 'copy']
        
        # Add language metadata for each audio track
        # Original audio track (from the main video file)
        if original_audio_lang:
            # Use detected original language - preserve full language codes (e.g., zh-Hans, zh-Hant)
            # But for metadata, use ISO 639-1/639-2 codes (first part before hyphen)
            # For Chinese variants, we need to handle them specially
            if 'Hans' in original_audio_lang or 'Hant' in original_audio_lang:
                # For Chinese, use base code 'zh' but we'll preserve variant info in track name if needed
                orig_lang_code = 'zh'
            else:
                orig_lang_code = original_audio_lang.split('-')[0] if '-' in original_audio_lang else original_audio_lang
            cmd += ['-metadata:s:a:0', f'language={orig_lang_code}']
            logger.info(f"Setting original audio track language to: {orig_lang_code} (from {original_audio_lang})")
        else:
            # Try to detect from video file metadata using ffprobe
            try:
                import json
                ffprobe_result = subprocess.run([
                    'ffprobe', '-v', 'error',
                    '-select_streams', 'a:0',
                    '-show_entries', 'stream=tags:stream_tags=language',
                    '-of', 'json', video_path
                ], capture_output=True, text=True, encoding='utf-8', errors='replace')
                
                if ffprobe_result.returncode == 0:
                    probe_data = json.loads(ffprobe_result.stdout)
                    if 'streams' in probe_data and len(probe_data['streams']) > 0:
                        stream = probe_data['streams'][0]
                        if 'tags' in stream and 'language' in stream['tags']:
                            detected_lang = stream['tags']['language']
                            orig_lang_code = detected_lang.split('-')[0] if '-' in detected_lang else detected_lang
                            cmd += ['-metadata:s:a:0', f'language={orig_lang_code}']
                            logger.info(f"Detected original audio track language from video: {orig_lang_code}")
                        else:
                            cmd += ['-metadata:s:a:0', 'language=und']
                            logger.info("No language tag in original audio stream, using 'und'")
                    else:
                        cmd += ['-metadata:s:a:0', 'language=und']
                        logger.info("No audio stream found in video, using 'und'")
                else:
                    cmd += ['-metadata:s:a:0', 'language=und']
                    logger.info("Could not probe video for audio language, using 'und'")
            except Exception as e:
                logger.warning(f"Could not detect original audio language: {e}, using 'und'")
                cmd += ['-metadata:s:a:0', 'language=und']
        
        # Additional audio tracks (index starts from 1 because 0 is original)
        for i, track in enumerate(valid_tracks):
            lang = track['language']
            # For Chinese variants, use base code 'zh' for metadata
            # But preserve the full language code in the track info
            if 'Hans' in lang or 'Hant' in lang:
                lang_code = 'zh'
            else:
                # For other languages, use base code (ISO 639-1/639-2)
                lang_code = lang.split('-')[0] if '-' in lang else lang
            # Audio track index is i+1 because 0 is the original audio from video file
            cmd += ['-metadata:s:a:' + str(i+1), f'language={lang_code}']
            logger.debug(f"Setting additional audio track {i+1} language to: {lang_code} (from {lang})")
        
        cmd += [output_path]
        
        try:
            logger.info(f"Running ffmpeg to embed {len(valid_tracks)} audio tracks: {' '.join(cmd)}")
            # Add progress tracking if callback provided
            if tg_update_callback:
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    bufsize=1
                )
                progress = 0.0
                last_update = time.time()
                time_pattern = re.compile(r'time=([0-9:.]+)')
                duration_pattern = re.compile(r'Duration: (\d{2}):(\d{2}):(\d{2})\.(\d{2})')
                total_duration = 0
                
                for line in proc.stdout:
                    # Parse duration
                    dur_match = duration_pattern.search(line)
                    if dur_match:
                        hours, minutes, seconds, centiseconds = map(int, dur_match.groups())
                        total_duration = hours * 3600 + minutes * 60 + seconds + centiseconds / 100
                    
                    # Parse progress
                    time_match = time_pattern.search(line)
                    if time_match and total_duration > 0:
                        time_str = time_match.group(1)
                        try:
                            parts = time_str.split(':')
                            if len(parts) == 3:
                                hours, minutes, seconds = map(float, parts)
                                current_time = hours * 3600 + minutes * 60 + seconds
                                progress = min(current_time / total_duration, 1.0)
                                
                                # Update progress every 2 seconds
                                if time.time() - last_update >= 2.0:
                                    eta_seconds = (total_duration - current_time) / max(progress, 0.01) if progress > 0 else 0
                                    eta_minutes = int(eta_seconds / 60)
                                    tg_update_callback(progress, eta_minutes)
                                    last_update = time.time()
                        except Exception:
                            pass
                
                proc.wait()
                if proc.returncode != 0:
                    raise subprocess.CalledProcessError(proc.returncode, cmd)
            else:
                subprocess.run(cmd, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
        except Exception as e:
            logger.error(f"FFmpeg audio mux failed: {e}")
            return False
        
        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            logger.error("Audio mux output missing or empty")
            return False
        
        # Replace original file
        backup_path = video_path + ".backup"
        try:
            os.rename(video_path, backup_path)
            os.rename(output_path, video_path)
            if os.path.exists(backup_path):
                os.remove(backup_path)
        except Exception as e:
            logger.error(f"Error replacing MKV after audio mux: {e}")
            # Rollback
            try:
                if os.path.exists(video_path):
                    os.remove(video_path)
                if os.path.exists(backup_path):
                    os.rename(backup_path, video_path)
            except Exception:
                pass
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
        
        # Clean up downloaded audio files
        for track in audio_tracks:
            try:
                if os.path.exists(track['path']):
                    os.remove(track['path'])
            except Exception:
                pass
        
        logger.info(f"Successfully embedded {len(audio_tracks)} audio tracks into MKV")
        return True
    except Exception as e:
        logger.error(f"Error in embed_all_audio_tracks_to_mkv: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


def download_all_subtitles(url, user_id, video_dir, selected_langs=None, all_selected=False, available_dubs=None):
    """
    Download all selected subtitles for MKV multi-track support.
    Returns list of downloaded subtitle file paths with language info.
    
    Args:
        url: Video URL
        user_id: User ID
        video_dir: Directory to save subtitles
        selected_langs: List of specific languages to download
        all_selected: If True, download all available (or filtered by available_dubs if provided)
        available_dubs: If provided and all_selected=True, filter subtitles to only languages that have dubs
    """
    try:
        import yt_dlp
        from COMMANDS.subtitles_cmd import get_available_subs_languages, lang_match
        from COMMANDS.subtitles_cmd import get_user_subs_auto_mode
        from HELPERS.proxy_helper import add_proxy_to_ytdl_opts
        from HELPERS.pot_helper import add_pot_to_ytdl_opts
        from CONFIG.config import Config
        
        logger.info(f"[DEBUG] download_all_subtitles called: selected_langs={selected_langs}, all_selected={all_selected}, available_dubs={available_dubs}")
        
        # Get available languages
        auto_mode = get_user_subs_auto_mode(user_id)
        normal_langs = get_available_subs_languages(url, user_id, auto_only=False)
        auto_langs = get_available_subs_languages(url, user_id, auto_only=True)
        all_available = sorted(set(normal_langs) | set(auto_langs))
        
        logger.info(f"[DEBUG] download_all_subtitles: normal_langs={normal_langs}, auto_langs={auto_langs}, all_available={all_available}")
        
        if not all_available:
            logger.info("No subtitles available")
            return []
        
        # Determine which languages to download
        # Priority: selected_langs (if provided) > all_selected with available_dubs > all_selected > single language
        if selected_langs and len(selected_langs) > 0:
            # Use explicitly selected languages (from ALL DUBS or individual selection)
            langs_to_download = selected_langs
            logger.info(f"Using {len(langs_to_download)} explicitly selected subtitle languages: {langs_to_download}")
        elif all_selected:
            if available_dubs and len(available_dubs) > 0:
                # ALL DUBS mode: Select all subtitle types (orig, auto, trans) for specific languages
                # Languages to include: English, Arabic, Bengali, Chinese, Chinese (Traditional), Dutch, French, German, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malayalam, Polish, Portuguese, Punjabi, Romanian, Russian, Spanish, Swahili, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese
                target_dub_languages = ['en', 'ar', 'bn', 'zh', 'zh-Hans', 'zh-Hant', 'nl', 'fr', 'de', 'he', 'hi', 'id', 'it', 'ja', 'ko', 'ml', 'pl', 'pt', 'pa', 'ro', 'ru', 'es', 'sw', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'vi']
                
                # Filter to only languages from target_dub_languages (match by base code)
                # Include all types: orig, auto, trans
                langs_to_download = []
                for sub_lang in all_available:
                    sub_base = sub_lang.split('-')[0] if '-' in sub_lang else sub_lang
                    # Check if this subtitle language matches any target language
                    for target_lang in target_dub_languages:
                        target_base = target_lang.split('-')[0] if '-' in target_lang else target_lang
                        # Match exact or base match (e.g., 'zh-Hans' matches 'zh', 'zh-Hant' matches 'zh')
                        if sub_lang == target_lang or sub_base == target_base:
                            langs_to_download.append(sub_lang)
                            break
                
                # Remove duplicates while preserving order
                langs_to_download = sorted(list(dict.fromkeys(langs_to_download)))
                logger.info(f"ALL DUBS mode: filtering subtitles to {len(langs_to_download)} languages from target list (all types: orig, auto, trans)")
            else:
                # Download all available languages (ALL mode)
                langs_to_download = all_available
                logger.info(f"ALL mode: downloading all {len(langs_to_download)} available subtitle languages")
        else:
            # Single language mode - use existing logic
            return []
        
        if not langs_to_download:
            return []
        
        # Get video info
        info_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
            'noplaylist': True,
            'format': 'best',
            'ignore_no_formats_error': True,
        }
        
        # Add cookies
        user_cookie_path = os.path.join("users", str(user_id), "cookie.txt")
        if os.path.exists(user_cookie_path):
            info_opts['cookiefile'] = user_cookie_path
        
        # Add proxy
        info_opts = add_proxy_to_ytdl_opts(info_opts, url, user_id)
        
        # Add PO token
        info_opts = add_pot_to_ytdl_opts(info_opts, url)
        
        # Use tv client for reliability
        info_opts['extractor_args'] = {'youtube': {'player_client': ['tv']}}
        
        # Reuse the same ydl instance for both extract_info and urlopen
        # Reuse the same ydl instance for both extract_info and urlopen
        with yt_dlp.YoutubeDL(info_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                if not info:
                    logger.error("yt-dlp extract_info returned None")
                    return []
            except Exception as e:
                logger.error(f"Error extracting video info in download_all_subtitles: {e}")
                import traceback
                logger.error(traceback.format_exc())
                return []
        
            # Get subtitles dict
            subs_dict = {}
            if not auto_mode:
                subs_dict = info.get('subtitles', {}) or {}
                auto_dict = info.get('automatic_captions', {}) or {}
                for k, v in auto_dict.items():
                    subs_dict.setdefault(k, v)
            else:
                subs_dict = info.get('automatic_captions', {}) or {}
                normal_dict = info.get('subtitles', {}) or {}
                for k, v in normal_dict.items():
                    subs_dict.setdefault(k, v)
            
            # Download each subtitle language
            downloaded_subs = []
            preferred = ('srt', 'vtt', 'ttml', 'json3', 'srv3')
            
            for lang in langs_to_download:
                try:
                    # Find matching language
                    found_lang = lang_match(lang, list(subs_dict.keys()))
                    if not found_lang:
                        continue
                    
                    tracks = subs_dict.get(found_lang) or []
                    if not tracks:
                        alt = next((k for k in subs_dict if k.startswith(found_lang)), None)
                        tracks = subs_dict.get(alt, []) if alt else []
                    
                    if not tracks:
                        continue
                    
                    # Select best format
                    track = min(
                        tracks,
                        key=lambda t: preferred.index((t.get('ext') or '').lower())
                        if (t.get('ext') or '').lower() in preferred else 999
                    )
                    
                    ext = (track.get('ext') or 'txt').lower()
                    track_url = track.get('url', '')
                    
                    # Download subtitle using yt-dlp transport (with cookies, proxy, PO token)
                    # Reuse the same ydl instance that was used for extract_info
                    # Sanitize language code for filename (remove invalid characters)
                    import re
                    safe_lang = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', lang)
                    safe_lang = safe_lang.replace(' ', '_').strip('._')
                    # Limit length to avoid filesystem issues
                    if len(safe_lang) > 50:
                        safe_lang = safe_lang[:50]
                    subtitle_filename = f"subs_{safe_lang}.{ext}"
                    subtitle_path = os.path.join(video_dir, subtitle_filename)
                    
                    # Download subtitle - try all formats without delay, then try with proxy1 and proxy2
                    # No exponential backoff - we try different formats and different IPs immediately
                    from CONFIG.config import Config
                    from HELPERS.proxy_helper import build_proxy_url
                    
                    def _download_with_ydl_instance(ydl_instance, url_tt: str, dst_path: str) -> bool:
                        """Download using yt-dlp transport - no delays, just try once"""
                        try:
                            with ydl_instance.urlopen(url_tt) as resp:
                                data = resp.read()
                            if data and len(data) > 0:
                                with open(dst_path, "wb") as f:
                                    f.write(data)
                                return True
                        except Exception as e:
                            err_str = str(e)
                            if "429" in err_str or "Too Many Requests" in err_str:
                                logger.debug(f"timedtext 429 for {lang}, will try different format/proxy")
                            else:
                                logger.debug(f"timedtext download error for {lang}: {e}")
                        return False
                    
                    # Detect translated subs (tlang=)
                    is_translated = 'tlang=' in track_url
                    
                    # Strategy: Try all formats without delay, then try with proxy1 and proxy2
                    ok = False
                    
                    # Step 1: Try all available formats for this track (without delay)
                    preferred_formats = ['srt', 'vtt', 'ttml', 'json3', 'srv3']
                    if is_translated:
                        # For translated, prefer formats that are less rate-limited
                        preferred_formats = ['srv3', 'json3', 'vtt', 'ttml', 'srt']
                    
                    # Try current format first
                    if _download_with_ydl_instance(ydl, track_url, subtitle_path):
                        ok = True
                    else:
                        # Try other formats without delay
                        for fmt in preferred_formats:
                            if fmt == ext:
                                continue  # Already tried
                            q = '&' if '?' in track_url else '?'
                            fmt_url = track_url + q + f'fmt={fmt}'
                            if _download_with_ydl_instance(ydl, fmt_url, subtitle_path):
                                ok = True
                                break
                    
                    # Step 2: If failed, try with proxy1 (without delay)
                    if not ok:
                        try:
                            proxy_config = {
                                'type': Config.PROXY_TYPE,
                                'ip': Config.PROXY_IP,
                                'port': Config.PROXY_PORT,
                                'user': Config.PROXY_USER,
                                'password': Config.PROXY_PASSWORD
                            }
                            proxy_url = build_proxy_url(proxy_config)
                            if proxy_url:
                                # Create new ydl instance with proxy1
                                proxy_info_opts = {
                                    'quiet': True,
                                    'no_warnings': True,
                                    'skip_download': True,
                                    'noplaylist': True,
                                    'format': 'best',
                                    'ignore_no_formats_error': True,
                                    'cookiefile': user_cookie_path if os.path.exists(user_cookie_path) else None,
                                    'extractor_args': {'youtube': {'player_client': ['tv']}},
                                }
                                if proxy_info_opts['cookiefile'] is None:
                                    proxy_info_opts.pop('cookiefile')
                                proxy_info_opts['proxy'] = proxy_url
                                # Add PO token
                                from HELPERS.pot_helper import add_pot_to_ytdl_opts
                                proxy_info_opts = add_pot_to_ytdl_opts(proxy_info_opts, url)
                                with yt_dlp.YoutubeDL(proxy_info_opts) as proxy_ydl:
                                    # Try all formats with proxy1
                                    if _download_with_ydl_instance(proxy_ydl, track_url, subtitle_path):
                                        ok = True
                                    else:
                                        for fmt in preferred_formats:
                                            if fmt == ext:
                                                continue
                                            q = '&' if '?' in track_url else '?'
                                            fmt_url = track_url + q + f'fmt={fmt}'
                                            if _download_with_ydl_instance(proxy_ydl, fmt_url, subtitle_path):
                                                ok = True
                                                break
                        except Exception as e:
                            logger.debug(f"Failed to try proxy1 for {lang}: {e}")
                    
                    # Step 3: If still failed, try with proxy2 (without delay)
                    if not ok:
                        try:
                            proxy_config = {
                                'type': Config.PROXY_2_TYPE,
                                'ip': Config.PROXY_2_IP,
                                'port': Config.PROXY_2_PORT,
                                'user': Config.PROXY_2_USER,
                                'password': Config.PROXY_2_PASSWORD
                            }
                            proxy_url = build_proxy_url(proxy_config)
                            if proxy_url:
                                # Create new ydl instance with proxy2
                                proxy_info_opts = {
                                    'quiet': True,
                                    'no_warnings': True,
                                    'skip_download': True,
                                    'noplaylist': True,
                                    'format': 'best',
                                    'ignore_no_formats_error': True,
                                    'cookiefile': user_cookie_path if os.path.exists(user_cookie_path) else None,
                                    'extractor_args': {'youtube': {'player_client': ['tv']}},
                                }
                                if proxy_info_opts['cookiefile'] is None:
                                    proxy_info_opts.pop('cookiefile')
                                proxy_info_opts['proxy'] = proxy_url
                                # Add PO token
                                from HELPERS.pot_helper import add_pot_to_ytdl_opts
                                proxy_info_opts = add_pot_to_ytdl_opts(proxy_info_opts, url)
                                with yt_dlp.YoutubeDL(proxy_info_opts) as proxy_ydl:
                                    # Try all formats with proxy2
                                    if _download_with_ydl_instance(proxy_ydl, track_url, subtitle_path):
                                        ok = True
                                    else:
                                        for fmt in preferred_formats:
                                            if fmt == ext:
                                                continue
                                            q = '&' if '?' in track_url else '?'
                                            fmt_url = track_url + q + f'fmt={fmt}'
                                            if _download_with_ydl_instance(proxy_ydl, fmt_url, subtitle_path):
                                                ok = True
                                                break
                        except Exception as e:
                            logger.debug(f"Failed to try proxy2 for {lang}: {e}")
                    
                    if not ok:
                        try:
                            if os.path.exists(subtitle_path):
                                os.remove(subtitle_path)
                        except Exception:
                            pass
                        logger.warning(f"Could not download subtitle {lang}, skipping")
                        continue
                    
                    # Convert to SRT if needed
                    if ext == 'vtt':
                        try:
                            from COMMANDS.subtitles_cmd import _convert_vtt_to_srt
                            subtitle_path = _convert_vtt_to_srt(subtitle_path)
                        except Exception as e:
                            logger.error(f"Failed to convert VTT to SRT: {e}")
                            continue
                    elif ext in ('json3', 'srv3'):
                        try:
                            from COMMANDS.subtitles_cmd import _convert_json3_srv3_to_srt
                            subtitle_path = _convert_json3_srv3_to_srt(subtitle_path)
                        except Exception as e:
                            logger.error(f"Failed to convert JSON3/SRV3 to SRT: {e}")
                            continue
                    elif ext == 'ttml':
                        try:
                            from COMMANDS.subtitles_cmd import _convert_ttml_to_srt
                            subtitle_path = _convert_ttml_to_srt(subtitle_path)
                        except Exception as e:
                            logger.error(f"Failed to convert TTML to SRT: {e}")
                            continue
                    
                    # Ensure UTF-8
                    try:
                        from COMMANDS.subtitles_cmd import ensure_utf8_srt
                        subtitle_path = ensure_utf8_srt(subtitle_path)
                    except Exception as e:
                        logger.error(f"Failed to ensure UTF-8: {e}")
                        continue
                    
                    if subtitle_path and os.path.exists(subtitle_path) and os.path.getsize(subtitle_path) > 0:
                        downloaded_subs.append({
                            'path': subtitle_path,
                            'language': lang
                        })
                        logger.info(f"Downloaded subtitle: {lang} -> {subtitle_path}")
                except Exception as e:
                    logger.error(f"Failed to download subtitle {lang}: {e}")
                    continue
        
        return downloaded_subs
    except Exception as e:
        logger.error(f"Error in download_all_subtitles: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return []
