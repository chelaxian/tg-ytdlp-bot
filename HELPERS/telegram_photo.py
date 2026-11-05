"""Prepare still images for Telegram photos without changing the original."""
import os
import tempfile

from PIL import Image, ImageOps


def prepare_photo(path, max_bytes=10 * 1024 * 1024, max_sum=10000, max_ratio=20):
    """Return a temporary JPEG path, or None. The caller owns the returned file.

    Animated images are not flattened. Pillow's decompression-bomb protection
    remains enabled, and extreme aspect ratios are padded rather than cropped.
    """
    output = None
    success = False
    try:
        with Image.open(path) as source:
            if getattr(source, "is_animated", False):
                return None
            image = ImageOps.exif_transpose(source)
            image.load()
            if image.mode in ("RGBA", "LA") or "transparency" in image.info:
                rgba = image.convert("RGBA")
                image = Image.new("RGB", rgba.size, "white")
                image.paste(rgba, mask=rgba.getchannel("A"))
            else:
                image = image.convert("RGB")
            width, height = image.size
            if not width or not height:
                return None

            # Scale before padding: a huge, very narrow source must not create
            # a huge intermediate canvas merely to meet the aspect ratio limit.
            padded_width = max(width, (height + max_ratio - 1) // max_ratio)
            padded_height = max(height, (width + max_ratio - 1) // max_ratio)
            if padded_width + padded_height > max_sum - 4:
                scale = (max_sum - 4) / (padded_width + padded_height)
                image = image.resize(tuple(max(1, int(n * scale)) for n in image.size), Image.Resampling.LANCZOS)
            width, height = image.size
            size = (max(width, (height + max_ratio - 1) // max_ratio),
                    max(height, (width + max_ratio - 1) // max_ratio))
            if size != image.size:
                canvas = Image.new("RGB", size, "white")
                canvas.paste(image, ((size[0] - width) // 2, (size[1] - height) // 2))
                image = canvas

            fd, output = tempfile.mkstemp(prefix="tg-photo-", suffix=".jpg")
            os.close(fd)
            for _ in range(5):
                for quality in (95, 90, 85, 80, 70, 60, 50, 40):
                    image.save(output, "JPEG", quality=quality, optimize=True)
                    if os.path.getsize(output) <= max_bytes:
                        success = True
                        return output
                image = image.resize(tuple(max(1, int(n * 0.8)) for n in image.size), Image.Resampling.LANCZOS)
    except (OSError, ValueError, SyntaxError, Image.DecompressionBombError):
        return None
    finally:
        if output and not success:
            try:
                os.remove(output)
            except OSError:
                pass
    return None


def retry_invalid_photo_upload(send, media, is_photo, is_invalid, prepare, cleanup):
    """Retry an explicitly rejected upload once, using JPEG photo copies.

    Only definitive photo errors are retried: timeouts and network errors can be
    ambiguous about delivery and must not result in duplicate messages.
    """
    try:
        return send()
    except Exception as error:
        if not is_invalid(error):
            raise
        changed = False
        for item in media:
            if not is_photo(item):
                continue
            path = getattr(item, 'media', None)
            if not isinstance(path, (str, os.PathLike)):
                continue
            prepared = prepare(path)
            if prepared:
                cleanup.append(prepared)
                item.media = prepared
                changed = True
        if not changed:
            raise
        return send()
