"""Pick a representative still frame from a video (cover fallback) and make covers
that have the SAME aspect ratio as the video.

Fallback cover: the first seconds of a video are often a black screen or titles, so
the frame is taken from the middle; if the middle frame is dark or flat (fade, black
transition) a few other positions are tried and the most informative frame wins.
The result keeps the video's aspect ratio (Telegram thumbnails: JPEG, <= 320 px per
side, < 200 KB).

Service cover: `fit_cover_to_aspect` reshapes it to the video's displayed aspect
ratio (rotation and non-square pixels taken into account) without stretching.
"""
import os
import shutil
import subprocess
import time
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
MAX_THUMB_BYTES = 200_000  # strictly below 200 kB


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


def _extract(ffmpeg: str, video_path: str, seconds: float, dest: str, vfs: List[str], quality: int, deadline: float) -> bool:
    for vf in vfs:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return False
        try:
            if os.path.exists(dest):
                os.remove(dest)
            subprocess.run(
                [ffmpeg, '-y', '-v', 'error', '-ss', str(seconds), '-i', video_path,
                 '-frames:v', '1', '-vf', vf, '-q:v', str(quality), dest],
                capture_output=True, timeout=min(5, remaining))
        except subprocess.TimeoutExpired:
            return False
        except OSError:
            return False
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
        deadline = time.monotonic() + 15
        best_path, best_score = None, -1.0
        tmp_paths = []
        for idx, sec in enumerate(frame_times(duration)):
            cand = f"{dest}.cand{idx}.jpg"
            tmp_paths.append(cand)
            if not _extract(ffmpeg, video_path, sec, cand, vfs, quality, deadline):
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
            if os.path.getsize(best_path) > MAX_THUMB_BYTES and max(max_w, max_h) <= 320:
                # re-encode smaller (Telegram rejects thumbs over 200 KB)
                small = best_path + '.small.jpg'
                if _extract(ffmpeg, best_path, 0, small, vfs, 5, deadline):
                    os.replace(small, best_path)
            # ffmpeg may retain non-square pixels in its scale calculation; JPEG
            # viewers do not reliably honor SAR. Normalize the extracted still to
            # the video's displayed dimensions before passing it to Telegram.
            display_w, display_h = video_display_size(video_path, timeout=max(0.1, min(3, deadline - time.monotonic())))
            if display_w and display_h:
                try:
                    from PIL import Image
                    with Image.open(best_path) as source:
                        im = source.convert('RGB')
                    target_ratio = display_w / display_h
                    if abs(im.width / im.height - target_ratio) > 0.01:
                        if target_ratio >= 1:
                            w, h = max_w, max(1, round(max_w / target_ratio))
                        else:
                            h, w = max_h, max(1, round(max_h * target_ratio))
                        im.resize((w, h), Image.Resampling.LANCZOS).save(
                            best_path, 'JPEG', quality=90, optimize=True)
                except Exception:
                    pass
            os.replace(best_path, dest)
            ok = os.path.getsize(dest) > 0 and (max(max_w, max_h) > 320 or os.path.getsize(dest) < MAX_THUMB_BYTES)
            if not ok:
                os.remove(dest)
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


def video_display_size(video_path: str, timeout: float = 30) -> Tuple[int, int]:
    """(width, height) the video is shown with: rotation metadata and non-square
    pixels (SAR) applied. (0, 0) if it cannot be probed."""
    try:
        import json
        r = subprocess.run(
            ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
             'stream=width,height,sample_aspect_ratio:stream_tags=rotate:stream_side_data=rotation',
             '-of', 'json', video_path],
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
        st = (json.loads(r.stdout).get('streams') or [{}])[0]
        w, h = int(st.get('width') or 0), int(st.get('height') or 0)
        if w <= 0 or h <= 0:
            return 0, 0
        sar = str(st.get('sample_aspect_ratio') or '1:1')
        try:
            n, d = sar.split(':')
            if int(n) > 0 and int(d) > 0 and n != d:
                w = max(1, round(w * int(n) / int(d)))
        except (ValueError, ZeroDivisionError):
            pass
        rot = (st.get('tags') or {}).get('rotate')
        for sd in st.get('side_data_list') or []:
            if 'rotation' in sd:
                rot = sd['rotation']
        try:
            if round(float(rot)) % 180 == 90:
                w, h = h, w
        except (TypeError, ValueError):
            pass
        return w, h
    except Exception:
        return 0, 0


def _strip_black_bars(img, limit: int = 24):
    """Crop letterbox/pillarbox bars (near-black frame around the picture)."""
    try:
        bbox = img.convert('L').point(lambda p: 255 if p > limit else 0).getbbox()
        if not bbox:
            return img
        l, t, r, b = bbox
        w, h = img.size
        # only real bars: something is removed, and enough picture is left
        if (r - l) * (b - t) >= 0.4 * w * h and (r - l < w - 4 or b - t < h - 4):
            return img.crop(bbox)
    except Exception:
        pass
    return img


def fit_cover_to_aspect(src: str, dest: str, aspect_w: int, aspect_h: int,
                        max_w: int = 320, max_h: int = 320, max_crop: float = 0.35) -> bool:
    """Make `dest` (JPEG) from the image `src` with the aspect ratio aspect_w:aspect_h.

    Black bars of the source are removed first. A slightly different ratio is fixed by
    a centre crop (no padding); if that would cut away more than `max_crop` of the
    picture (square poster on a 16:9 video) the whole picture is kept on a blurred
    copy of itself. Never stretches. Never raises; False if Pillow cannot read `src`.
    """
    try:
        from PIL import Image, ImageFilter
        if aspect_w <= 0 or aspect_h <= 0:
            return False
        target = aspect_w / aspect_h
        with Image.open(src) as im:
            img = im.convert('RGB')
        img = _strip_black_bars(img)
        w, h = img.size
        cur = w / h
        # output size: longest allowed side, aspect ratio of the video, even sides
        if target >= 1:
            ow, oh = max_w, max_w / target
        else:
            oh, ow = max_h, max_h * target
        if ow > max_w or oh > max_h:
            k = min(max_w / ow, max_h / oh)
            ow, oh = ow * k, oh * k
        ow, oh = max(2, int(round(ow))), max(2, int(round(oh)))
        ow, oh = ow + ow % 2, oh + oh % 2

        lost = 1 - min(cur, target) / max(cur, target)
        if lost <= max_crop:
            # centre crop to the target ratio
            if cur > target:
                nw = int(round(h * target))
                box = ((w - nw) // 2, 0, (w - nw) // 2 + nw, h)
            else:
                nh = int(round(w / target))
                box = (0, (h - nh) // 2, w, (h - nh) // 2 + nh)
            out = img.crop(box).resize((ow, oh), Image.Resampling.LANCZOS)
        else:
            bg = img.resize((ow, oh), Image.Resampling.BILINEAR).filter(ImageFilter.GaussianBlur(12))
            k = min(ow / w, oh / h)
            fw, fh = max(1, int(round(w * k))), max(1, int(round(h * k)))
            fg = img.resize((fw, fh), Image.Resampling.LANCZOS)
            bg.paste(fg, ((ow - fw) // 2, (oh - fh) // 2))
            out = bg

        quality = 92
        out.save(dest, 'JPEG', quality=quality, optimize=True)
        if max(max_w, max_h) <= 320:
            while os.path.getsize(dest) >= MAX_THUMB_BYTES and quality > 50:
                quality -= 10
                out.save(dest, 'JPEG', quality=quality, optimize=True)
        size = os.path.getsize(dest)
        return size > 0 and (max(max_w, max_h) > 320 or size < MAX_THUMB_BYTES)
    except Exception as e:
        logger.warning(f"fit_cover_to_aspect failed for {src}: {e}")
        return False
