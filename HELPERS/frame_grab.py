"""Pick a representative still frame from a video (cover fallback).

Used when the service gave no cover of its own. The first seconds of a video are
often a black screen or titles, so the frame is taken from the middle; if the
middle frame is dark or flat (fade, black transition) a few other positions are
tried and the most informative frame wins. The result keeps the video's aspect
ratio (Telegram thumbnails: JPEG, <= 320 px per side, < 200 KB).
"""
import os
import shutil
import subprocess
from typing import List, Optional, Tuple

try:
    from HELPERS.logger import logger
except Exception:  # standalone use (tests)
    import logging
    logger = logging.getLogger(__name__)

# fractions of the duration to try, in order of preference
FRAME_FRACTIONS = (0.5, 0.33, 0.67, 0.2, 0.8, 0.1, 0.9)
MIN_MEAN_LUMA = 22.0   # 0..255: below this the frame is practically black
MIN_STDDEV_LUMA = 12.0  # below this it is a flat colour (no picture)
MAX_THUMB_BYTES = 200 * 1024


def frame_times(duration) -> List[float]:
    """Seek positions (seconds) for a video of `duration` seconds, best first."""
    try:
        dur = float(duration or 0)
    except (TypeError, ValueError):
        dur = 0.0
    if dur <= 0:
        return [1.0, 0.0]
    if dur < 3:
        return [round(dur / 2, 2), 0.0]
    times = []
    for frac in FRAME_FRACTIONS:
        t = round(min(dur * frac, dur - 1.0), 2)
        if t < 0:
            t = 0.0
        if t not in times:
            times.append(t)
    # last resorts when the reported duration is longer than the file
    times.extend(x for x in (1.0, 0.0) if x not in times)
    return times


def frame_stats(path: str) -> Optional[Tuple[float, float]]:
    """(mean, stddev) of the luma of an image, or None if it cannot be read."""
    try:
        from PIL import Image, ImageStat
        with Image.open(path) as img:
            gray = img.convert('L')
            gray.thumbnail((64, 64))
            st = ImageStat.Stat(gray)
            return float(st.mean[0]), float(st.stddev[0])
    except Exception:
        return None


def is_informative(stats: Optional[Tuple[float, float]]) -> bool:
    return bool(stats) and stats[0] >= MIN_MEAN_LUMA and stats[1] >= MIN_STDDEV_LUMA


def _scale_filters(max_w: int, max_h: int) -> List[str]:
    # aspect ratio kept, never upscaled, even dimensions; plain fallback for old ffmpeg
    return [
        f"scale=w='min({max_w},iw)':h='min({max_h},ih)':force_original_aspect_ratio=decrease"
        f":force_divisible_by=2:flags=lanczos,unsharp=3:3:0.5:3:3:0.25",
        f"scale=w='min({max_w},iw)':h='min({max_h},ih)':force_original_aspect_ratio=decrease:flags=lanczos",
    ]


def _extract(ffmpeg: str, video_path: str, seconds: float, dest: str, vfs: List[str], quality: int) -> bool:
    for vf in vfs:
        try:
            if os.path.exists(dest):
                os.remove(dest)
            subprocess.run(
                [ffmpeg, '-y', '-v', 'error', '-ss', str(seconds), '-i', video_path,
                 '-frames:v', '1', '-vf', vf, '-q:v', str(quality), dest],
                capture_output=True, timeout=45)
        except (subprocess.TimeoutExpired, OSError):
            continue
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            return True
    return False


def grab_representative_frame(video_path: str, duration, dest: str, max_w: int = 320,
                              max_h: int = 320, ffmpeg_path: Optional[str] = None,
                              quality: int = 2) -> bool:
    """Write a JPEG still of `video_path` to `dest`. Never raises; True on success."""
    try:
        ffmpeg = ffmpeg_path or shutil.which('ffmpeg') or 'ffmpeg'
        vfs = _scale_filters(max_w, max_h)
        best_path, best_score = None, -1.0
        tmp_paths = []
        for idx, sec in enumerate(frame_times(duration)):
            cand = f"{dest}.cand{idx}.jpg"
            tmp_paths.append(cand)
            if not _extract(ffmpeg, video_path, sec, cand, vfs, quality):
                continue
            stats = frame_stats(cand)
            if stats is None or is_informative(stats):
                # Pillow unavailable/unreadable -> trust the first (middle) frame
                best_path = cand
                break
            score = stats[1] + 0.3 * stats[0]
            if score > best_score:
                best_path, best_score = cand, score
        ok = False
        if best_path and os.path.exists(best_path):
            if os.path.getsize(best_path) > MAX_THUMB_BYTES:
                # re-encode smaller (Telegram rejects thumbs over 200 KB)
                small = best_path + '.small.jpg'
                if _extract(ffmpeg, best_path, 0, small, vfs, 5):
                    os.replace(small, best_path)
            os.replace(best_path, dest)
            ok = os.path.getsize(dest) > 0
        for p in tmp_paths + [dest + '.cand0.jpg.small.jpg']:
            try:
                if p != dest and os.path.exists(p):
                    os.remove(p)
            except OSError:
                pass
        return ok
    except Exception as e:  # never break the upload because of a cover
        logger.warning(f"grab_representative_frame failed for {video_path}: {e}")
        return False
