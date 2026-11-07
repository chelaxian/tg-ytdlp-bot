"""Prepare gallery-dl downloads so Telegram shows them as media, not as files.

prepare_media() walks a cost ladder and stops at the first rung that works:

  video   webm / mkv (matroska_as_is)   -> sent unmodified as a video: zero cost, the client
                                           decides how to play it (e.g. the Telegram iOS
                                           experimental player); the mp4 rungs below are
                                           the fallback if Telegram rejects the upload
          already playable mp4          -> faststart remux (stream copy)
          any other container           -> remux to mp4 with stream copy
          incompatible audio only       -> re-encode audio only (cheap)
          incompatible video codec      -> re-encode video (last resort)
          nothing worked                -> document (original file)
  photo   JPEG/PNG within limits        -> as is
          anything Pillow can read      -> JPEG copy within Telegram limits
          anything ffmpeg can read      -> JPEG copy via ffmpeg
          nothing worked                -> document (original file)
  animated GIF / WebP / APNG            -> short mp4 (Telegram has no animated
          photos; a photo would lose the animation)

Originals are never modified; every generated file is returned so the caller
can register and clean it up.
"""
import json
import logging
import os
import subprocess

logger = logging.getLogger(__name__)

PHOTO_EXTS = frozenset({
    '.jpg', '.jpeg', '.jpe', '.jfif', '.pjpeg', '.pjp', '.png', '.apng', '.gif',
    '.webp', '.bmp', '.tif', '.tiff', '.avif', '.heic', '.heif', '.jxl', '.jp2',
    '.ico',
})
VIDEO_EXTS = frozenset({
    '.mp4', '.m4v', '.mov', '.mkv', '.webm', '.avi', '.flv', '.wmv', '.asf',
    '.mpg', '.mpeg', '.ts', '.m2ts', '.mts', '.ogv', '.3gp', '.3g2',
})

# What the mp4 muxer accepts by stream copy (anything else forces a re-encode).
MP4_COPY_VIDEO = frozenset({'h264', 'hevc', 'vp9', 'av1', 'mpeg4'})
# Audio that every Telegram client plays inside mp4; opus/vorbis/ac3 are
# re-encoded to AAC (audio is ~100x cheaper to encode than video).
MP4_COPY_AUDIO = frozenset({'aac', 'mp3'})
# Already mp4-native: only a faststart remux is wanted.
NATIVE_VIDEO = frozenset({'h264', 'hevc'})

# Containers that Telegram clients with an extended player can open unchanged.
MATROSKA_EXTS = frozenset({'.webm', '.mkv'})

_ANIMATED_PHOTO_EXTS = frozenset({'.gif', '.webp', '.apng', '.png'})
# Pillow keeps formats that Telegram accepts as a photo unchanged.
_PHOTO_AS_IS_FORMATS = frozenset({'JPEG', 'PNG'})


def _run(cmd, timeout):
    """Run a tool; None on timeout or a missing binary (never raises)."""
    try:
        return subprocess.run(cmd, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        logger.error("Timed out after %ss: %s", timeout, os.path.basename(cmd[0]))
    except OSError as exc:
        logger.error("Cannot run %s: %s", cmd[0], exc)
    return None


def probe(path, timeout=20):
    """ffprobe summary: format, first real video stream, first audio stream, duration."""
    result = _run(['ffprobe', '-v', 'error', '-show_streams', '-show_format',
                   '-of', 'json', os.path.abspath(path)], timeout)
    if result is None or result.returncode != 0:
        return None
    try:
        data = json.loads(result.stdout.decode('utf-8', 'replace') or '{}')
    except ValueError:
        return None
    streams = data.get('streams') or []
    video = next((s for s in streams if s.get('codec_type') == 'video'
                  and not (s.get('disposition') or {}).get('attached_pic')), None)
    audio = next((s for s in streams if s.get('codec_type') == 'audio'), None)
    fmt = data.get('format') or {}
    try:
        duration = float(fmt.get('duration') or 0)
    except (TypeError, ValueError):
        duration = 0.0
    return {
        'format': fmt.get('format_name') or '',
        'video': video,
        'audio': audio,
        'duration': duration,
    }


def _output_path(src, suffix):
    """A fresh sibling path; never overwrites the source or another file."""
    base = os.path.splitext(src)[0]
    candidate = base + suffix
    number = 1
    while os.path.exists(candidate):
        number += 1
        candidate = f"{base} ({number}){suffix}"
    return candidate


def _unlink_quiet(path):
    try:
        if path and os.path.exists(path):
            os.remove(path)
    except OSError:
        pass


def _ffmpeg(src, out, extra, timeout):
    """Run ffmpeg into out; True only if a non-empty file was produced."""
    cmd = ['ffmpeg', '-nostdin', '-hide_banner', '-loglevel', 'error', '-y',
           '-i', os.path.abspath(src), *extra, out]
    result = _run(cmd, timeout)
    if result is not None and result.returncode == 0 and os.path.exists(out) \
            and os.path.getsize(out) > 0:
        return True
    if result is not None and result.returncode != 0:
        logger.warning("ffmpeg failed for %s: %s", os.path.basename(src),
                       result.stderr.decode('utf-8', 'replace')[-300:])
    _unlink_quiet(out)  # a killed/failed ffmpeg leaves a truncated file behind
    return False


def _copy_timeout(path):
    try:
        size_mb = os.path.getsize(path) / (1024 * 1024)
    except OSError:
        size_mb = 0
    return int(min(900, 120 + size_mb * 2))


def _encode_timeout(info):
    return int(min(900, max(180, (info.get("duration") or 0) * 2 + 60)))


def _video_args(video_copy, audio_mode, hevc):
    args = ['-map', '0:v:0', '-map', '0:a:0?', '-sn', '-dn']
    if video_copy:
        args += ['-c:v', 'copy']
        if hevc:
            args += ['-tag:v', 'hvc1']  # Apple/Telegram iOS only plays hvc1
    else:
        args += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '24',
                 '-pix_fmt', 'yuv420p', '-threads', '2',
                 '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2']
    if audio_mode == 'copy':
        args += ['-c:a', 'copy']
    elif audio_mode == 'aac':
        args += ['-c:a', 'aac', '-b:a', '128k', '-ac', '2']
    return args + ['-movflags', '+faststart']


def prepare_video(path):
    """Return (mp4_path or None, temp_files, how). None means: send as a document."""
    info = probe(path)
    if not info or not info['video']:
        return None, [], 'no video stream'
    video = info['video'].get('codec_name') or ''
    audio = (info['audio'] or {}).get('codec_name')
    ext = os.path.splitext(path)[1].lower()
    mp4_family = bool({'mp4', 'mov'} & set(info['format'].split(',')))

    audio_mode = 'none' if audio is None else 'copy' if audio in MP4_COPY_AUDIO else 'aac'

    if ext in ('.mp4', '.m4v', '.mov') and mp4_family and video in NATIVE_VIDEO \
            and audio_mode in ('none', 'copy'):
        if ext == '.mp4':
            out = _output_path(path, '._fast.mp4')
            if _ffmpeg(path, out, _video_args(True, audio_mode, video == 'hevc'),
                       _copy_timeout(path)):
                return out, [out], 'faststart remux'
            return path, [], 'original mp4'
        # .mov/.m4v: same streams, only the container/extension changes
        out = _output_path(path, '.mp4')
        if _ffmpeg(path, out, _video_args(True, audio_mode, video == 'hevc'),
                   _copy_timeout(path)):
            return out, [out], 'remux to mp4'
        return None, [], 'remux failed'

    video_copy = video in MP4_COPY_VIDEO
    out = _output_path(path, '.mp4')
    if not video_copy:
        timeout = _encode_timeout(info)
    elif audio_mode == 'aac':
        timeout = max(_copy_timeout(path), 180)
    else:
        timeout = _copy_timeout(path)
    if _ffmpeg(path, out, _video_args(video_copy, audio_mode, video == 'hevc'), timeout):
        how = 'remux' if video_copy and audio_mode != 'aac' else \
            'remux + audio re-encode' if video_copy else 'video re-encode'
        return out, [out], how
    if video_copy:
        # the muxer refused the stream copy: last resort, re-encode the video
        out = _output_path(path, '.mp4')
        if _ffmpeg(path, out, _video_args(False, audio_mode, False), _encode_timeout(info)):
            return out, [out], 'video re-encode'
    return None, [], 'conversion failed'


def _animated(path, ext):
    """True when a still-image container actually holds several frames."""
    if ext not in _ANIMATED_PHOTO_EXTS:
        return False
    try:
        from PIL import Image
        with Image.open(path) as img:
            return bool(getattr(img, 'is_animated', False)) and getattr(img, 'n_frames', 1) > 1
    except Exception:
        return False


def prepare_animation(path):
    """Animated image -> silent mp4 (returns path or None)."""
    out = _output_path(path, '.mp4')
    extra = ['-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '26',
             '-pix_fmt', 'yuv420p', '-threads', '2',
             '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', '-movflags', '+faststart']
    return out if _ffmpeg(path, out, extra, 180) else None


def prepare_image(path, photo_problem):
    """Return (photo_path or None, temp_files, how)."""
    try:
        from PIL import Image
        with Image.open(path) as img:
            fmt = (img.format or '').upper()
    except Exception:
        fmt = ''
    if fmt in _PHOTO_AS_IS_FORMATS and not photo_problem(path):
        return path, [], 'as is'

    from HELPERS.telegram_photo import prepare_photo
    if fmt:
        copy = prepare_photo(path)
        if copy:
            if not photo_problem(copy):
                return copy, [copy], 'jpeg copy'
            _unlink_quiet(copy)
    # Pillow cannot read it (AVIF/HEIC/JXL without a decoder plugin): let ffmpeg try
    frame = _output_path(path, '.__tgframe.jpg')
    if _ffmpeg(path, frame, ['-frames:v', '1', '-q:v', '2'], 60):
        if not photo_problem(frame):
            return frame, [frame], 'ffmpeg jpeg'
        copy = prepare_photo(frame)
        if copy and not photo_problem(copy):
            return copy, [frame, copy], 'ffmpeg jpeg copy'
        _unlink_quiet(copy)
        _unlink_quiet(frame)
    return None, [], 'cannot convert'


def prepare_media(path, photo_problem=lambda _path: None, matroska_as_is=False):
    """Decide how to deliver path. Returns (kind, send_path, temp_files, how).

    kind is 'photo', 'video' or 'document'; for 'document' send_path is the
    untouched original. With matroska_as_is a real webm/mkv video is returned
    unchanged (cost: one ffprobe).
    """
    ext = os.path.splitext(path)[1].lower()
    try:
        if matroska_as_is and ext in MATROSKA_EXTS:
            info = probe(path)
            if info and info['video']:
                return 'video', path, [], 'matroska as is'
            return 'document', path, [], 'no video stream'
        if ext in PHOTO_EXTS:
            if _animated(path, ext):
                clip = prepare_animation(path)
                if clip:
                    return 'video', clip, [clip], 'animation to mp4'
                return 'document', path, [], 'animation conversion failed'
            image, temps, how = prepare_image(path, photo_problem)
            if image:
                return 'photo', image, temps, how
            return 'document', path, [], how
        if ext in VIDEO_EXTS:
            clip, temps, how = prepare_video(path)
            if clip and clip != path:
                return 'video', clip, temps, how
            if clip:
                return 'video', path, temps, how
            return 'document', path, [], how
    except Exception as exc:  # never lose a file because preparation crashed
        logger.exception("Media preparation crashed for %s: %s", path, exc)
    return 'document', path, [], 'not a photo/video'
