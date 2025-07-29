
from HELPERS.app_instance import get_app_lazy

# Get app instance for decorators
app = get_app_lazy()

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
            "path": path_lst,
            "duration": video_duration
        }
        return split_vid_dict


def get_duration_thumb_(dir, video_path, thumb_name):
    # Generate a short unique name for the thumbnail
    thumb_hash = hashlib.md5(thumb_name.encode()).hexdigest()[:10]
    thumb_dir = os.path.abspath(os.path.join(dir, thumb_hash + ".jpg"))
    try:
        _, _, duration = get_video_info_ffprobe(video_path)
        duration = int(duration)
    except Exception as e:
        logger.error(f"[FFPROBE BYPASS] Error while processing video {video_path}: {e}")
        import traceback
        logger.error(traceback.format_exc())
        duration = 0
    
    # Get original video dimensions
    # orig_w, orig_h = clip.w, clip.h
    orig_w = int(str(clip.w).strip().split()[0]) if clip.w else 1920
    orig_h = int(str(clip.h).strip().split()[0]) if clip.h else 1080
    # Determine optimal thumbnail size based on video aspect ratio
    aspect_ratio = orig_w / orig_h
    max_dimension = 640  # Maximum width or height
    
    if aspect_ratio > 1.5:  # Wide/horizontal video (16:9, etc.)
        thumb_w = max_dimension
        thumb_h = int(max_dimension / aspect_ratio)
    elif aspect_ratio < 0.75:  # Tall/vertical video (9:16, etc.)
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
    
    # Create thumbnail frame
    frame = clip.get_frame(2)
    from PIL import Image
    
    # Convert frame to PIL Image and resize to exact thumbnail size
    img = Image.fromarray(frame)
    img = img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
    
    # Save the thumbnail directly (no padding needed)
    img.save(thumb_dir, 'JPEG', quality=85)
    
    clip.close()
    return duration, thumb_dir

def get_duration_thumb(message, dir_path, video_path, thumb_name):
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
            logger.error(f"Video file does not exist: {video_path}")
            send_to_all(message, f"❌ Video file not found: {os.path.basename(video_path)}")
            return None

        # Get video dimensions
        size_result = subprocess.check_output(ffprobe_size_command, stderr=subprocess.STDOUT, universal_newlines=True).strip()
        # if 'x' in size_result:
            # orig_w, orig_h = map(int, size_result.split('x'))
        if 'x' in size_result:
            dimensions = size_result.split('x')
            orig_w = int(str(dimensions[0]).strip().split()[0]) if dimensions[0] else 1920
            orig_h = int(str(dimensions[1]).strip().split()[0]) if dimensions[1] else 1080            
        else:
            # Fallback to default horizontal orientation
            orig_w, orig_h = 1920, 1080
            logger.warning(f"Could not determine video dimensions, using default: {orig_w}x{orig_h}")
        
        # Determine optimal thumbnail size based on video aspect ratio
        aspect_ratio = orig_w / orig_h
        max_dimension = 640  # Maximum width or height
        
        if aspect_ratio > 1.5:  # Wide/horizontal video (16:9, etc.)
            thumb_w = max_dimension
            thumb_h = int(max_dimension / aspect_ratio)
        elif aspect_ratio < 0.75:  # Tall/vertical video (9:16, etc.)
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
        ffmpeg_result = subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        if ffmpeg_result.returncode != 0:
            logger.error(f"Error creating thumbnail: {ffmpeg_result.stderr}")

        # Run ffprobe command to get duration
        result = subprocess.check_output(ffprobe_duration_command, stderr=subprocess.STDOUT, universal_newlines=True)

        try:
            # duration = int(float(result))
            duration = int(float(str(result).strip().split()[0])) if result else 0
        except (ValueError, TypeError) as e:
            logger.error(f"Error parsing video duration: {e}, result was: {result}")
            duration = 0

        # Verify thumbnail was created
        if not os.path.exists(thumb_dir):
            logger.warning(f"Thumbnail not created at {thumb_dir}, using default")
            # Create a blank thumbnail as fallback
            create_default_thumbnail(thumb_dir, thumb_w, thumb_h)

        return duration, thumb_dir
    except subprocess.CalledProcessError as e:
        logger.error(f"Command execution error: {e.stderr if hasattr(e, 'stderr') else e}")
        send_to_all(message, f"❌ Error processing video: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing video: {e}")
        send_to_all(message, f"❌ Error processing video: {e}")
        return None

def create_default_thumbnail(thumb_path, width=480, height=480):
    """Create a default thumbnail when normal thumbnail creation fails"""
    try:
        # Create a black image with specified dimensions (square by default)
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi",
            "-i", f"color=c=black:s={width}x{height}",
            "-frames:v", "1",
            thumb_path
        ]
        subprocess.run(ffmpeg_cmd, check=True, capture_output=True)
        logger.info(f"Created default {width}x{height} thumbnail at {thumb_path}")
    except Exception as e:
        logger.error(f"Failed to create default thumbnail: {e}")


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
        ], capture_output=True, text=True)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            width = data['streams'][0]['width'] if data['streams'] else 0
            height = data['streams'][0]['height'] if data['streams'] else 0
            duration = float(data['format']['duration']) if 'format' in data and 'duration' in data['format'] else 0
            return width, height, duration
    except Exception as e:
        logger.error(f'ffprobe error: {e}')
    return 0, 0, 0


def embed_subs_to_video(video_path, user_id, tg_update_callback=None, app=None, message=None):
    """
    Burning (hardcode) subtitles in a video file, if there is any .SRT file and subs.txt
    tg_update_callback (Progress: Float, ETA: StR) - Function for updating the status in Telegram
    """
    try:
        if not video_path or not os.path.exists(video_path):
            logger.error(f"Video file not found: {video_path}")
            return False
        
        user_dir = os.path.join("users", str(user_id))
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
        
        # We get video parameters via FFPRobe
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
        if original_size_mb > Config.MAX_SUB_SIZE:
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
        
        # Field of subtitles with improved styling
        subs_path_escaped = subs_path.replace("'", "'\\''")
        # Add translucent black stroke like YouTube and an improved display of subtitles
        filter_arg = f"subtitles='{subs_path_escaped}':force_style='FontSize=16,PrimaryColour=&Hffffff,OutlineColour=&H000000,BackColour=&H80000000,Outline=2,Shadow=1,MarginV=25'"
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
                if progress > 0:
                    elapsed = time.time() - last_update
                    eta_sec = int((1.0 - progress) * (elapsed / progress)) if progress > 0 else 0
                    eta = f"{eta_sec//60}:{eta_sec%60:02d}"
                # Update every 10 seconds or with a change in progress> 1%
                if tg_update_callback and (time.time() - last_update > 10 or progress >= 1.0):
                    tg_update_callback(progress, eta)
                    last_update = time.time()
        
        proc.wait()
        
        if proc.returncode != 0:
            logger.error(f"FFmpeg error: process exited with code {proc.returncode}")
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
        if output_size < original_size * 0.5:
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
                        reply_to_message_id=message.id,
                        parse_mode=enums.ParseMode.HTML
                    )
                    safe_forward_messages(Config.LOGS_ID, user_id, [sent_msg.id])
                    send_to_logger(message, "💬 Subtitles SRT-file sent to user.") 
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
