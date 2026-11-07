"""Smoke test: HELPERS/telegram_media prepares gallery-dl files as Telegram media.

Needs ffmpeg/ffprobe and Pillow. Run: python tests/smoke/test_y_telegram_media.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

from PIL import Image  # noqa: E402

from HELPERS import telegram_media as tm  # noqa: E402

HAVE_FFMPEG = bool(shutil.which("ffmpeg") and shutil.which("ffprobe"))


def photo_problem(path):
    """Same limits as COMMANDS.image_cmd._photo_send_problem (10 MB, w+h<=10000, ratio<=20)."""
    if os.path.getsize(path) > 10 * 1024 * 1024:
        return "size"
    with Image.open(path) as img:
        w, h = img.size
        if img.format not in ("JPEG", "PNG"):
            return "format"
    if w + h > 10000 or max(w, h) / min(w, h) > 20:
        return "dimensions"
    return None


def streams(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,codec_name",
                          "-of", "json", path], capture_output=True, check=True).stdout
    return {s["codec_type"]: s["codec_name"] for s in json.loads(out)["streams"]}


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def make_video(path, vcodec, acodec, extra=()):
    cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
           "-f", "lavfi", "-i", "testsrc=size=160x120:rate=10:duration=1",
           "-f", "lavfi", "-i", "sine=frequency=440:duration=1",
           "-c:v", vcodec, "-c:a", acodec, *extra, path]
    subprocess.run(cmd, capture_output=True, check=True)


@unittest.skipUnless(HAVE_FFMPEG, "ffmpeg/ffprobe not installed")
class VideoLadderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def path(self, name):
        return os.path.join(self.tmp, name)

    def check_ok(self, src, vcodec):
        before = read_bytes(src)
        kind, out, temps, how = tm.prepare_media(src, photo_problem)
        self.assertEqual(kind, "video", how)
        self.assertTrue(out.endswith(".mp4"), out)
        self.assertTrue(os.path.getsize(out) > 0)
        self.assertEqual(streams(out)["video"], vcodec, how)
        self.assertEqual(streams(out).get("audio"), "aac")
        self.assertEqual(read_bytes(src), before, "original must stay untouched")
        self.assertIn(out, temps)
        return how

    def test_webm_vp9_opus_is_remuxed_not_reencoded(self):
        src = self.path("clip.webm")
        make_video(src, "libvpx-vp9", "libopus")
        how = self.check_ok(src, "vp9")
        self.assertIn("remux", how)
        self.assertNotIn("video re-encode", how)

    def test_webm_vp8_vorbis_reencodes_video_only_as_last_resort(self):
        src = self.path("old.webm")
        make_video(src, "libvpx", "libvorbis")
        how = self.check_ok(src, "h264")
        self.assertEqual(how, "video re-encode")

    def test_mkv_h264_aac_is_pure_remux(self):
        src = self.path("movie.mkv")
        make_video(src, "libx264", "aac")
        how = self.check_ok(src, "h264")
        self.assertEqual(how, "remux")

    def test_avi_mpeg4_mp3_is_remuxed(self):
        src = self.path("old.avi")
        make_video(src, "mpeg4", "libmp3lame")
        kind, out, _temps, how = tm.prepare_media(src, photo_problem)
        self.assertEqual(kind, "video", how)
        self.assertEqual(streams(out)["video"], "mpeg4")

    def test_ready_mp4_only_gets_faststart(self):
        src = self.path("ok.mp4")
        make_video(src, "libx264", "aac")
        kind, out, temps, how = tm.prepare_media(src, photo_problem)
        self.assertEqual(kind, "video")
        self.assertTrue(out.endswith("._fast.mp4"))
        self.assertEqual(how, "faststart remux")

    def test_existing_mp4_is_never_overwritten(self):
        src = self.path("clip.webm")
        make_video(src, "libvpx-vp9", "libopus")
        taken = self.path("clip.mp4")
        with open(taken, "wb") as f:
            f.write(b"keep me")
        kind, out, _temps, _how = tm.prepare_media(src, photo_problem)
        self.assertEqual(kind, "video")
        self.assertNotEqual(os.path.abspath(out), os.path.abspath(taken))
        self.assertEqual(read_bytes(taken), b"keep me")

    def test_matroska_as_is_costs_nothing_and_changes_nothing(self):
        for name, vcodec, acodec in (("clip.webm", "libvpx-vp9", "libopus"),
                                     ("movie.mkv", "libx264", "aac")):
            src = self.path(name)
            make_video(src, vcodec, acodec)
            before = read_bytes(src)
            self.assertEqual(tm.prepare_media(src, photo_problem, matroska_as_is=True),
                             ("video", src, [], "matroska as is"))
            self.assertEqual(read_bytes(src), before)
        self.assertEqual(sorted(os.listdir(self.tmp)), ["clip.webm", "movie.mkv"])

    def test_matroska_as_is_audio_only_is_not_a_video(self):
        src = self.path("sound.webm")
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "lavfi",
                        "-i", "sine=frequency=440:duration=1", "-c:a", "libopus", src],
                       capture_output=True, check=True)
        self.assertEqual(tm.prepare_media(src, photo_problem, matroska_as_is=True)[0], "document")

    def test_as_is_does_not_touch_other_containers(self):
        src = self.path("old.avi")
        make_video(src, "mpeg4", "libmp3lame")
        kind, out, _temps, _how = tm.prepare_media(src, photo_problem, matroska_as_is=True)
        self.assertEqual(kind, "video")
        self.assertTrue(out.endswith(".mp4"))

    def test_broken_video_falls_back_to_document_without_leftovers(self):
        src = self.path("broken.webm")
        with open(src, "wb") as f:
            f.write(b"this is not a video" * 10)
        kind, out, temps, _how = tm.prepare_media(src, photo_problem)
        self.assertEqual((kind, out, temps), ("document", src, []))
        self.assertEqual(os.listdir(self.tmp), ["broken.webm"])

    def test_ffmpeg_timeout_falls_back_and_cleans_partial_output(self):
        src = self.path("slow.webm")
        make_video(src, "libvpx-vp9", "libopus")
        real_run = tm._run

        def fake_run(cmd, timeout):
            if cmd[0] == "ffmpeg":
                with open(cmd[-1], "wb") as partial:  # ffmpeg leaves a truncated file when killed
                    partial.write(b"partial")
                return None
            return real_run(cmd, timeout)

        with patch.object(tm, "_run", fake_run):
            kind, out, temps, _how = tm.prepare_media(src, photo_problem)
        self.assertEqual((kind, out, temps), ("document", src, []))
        self.assertEqual(os.listdir(self.tmp), ["slow.webm"])


class PhotoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def path(self, name):
        return os.path.join(self.tmp, name)

    def test_compliant_png_and_jpeg_are_sent_as_is(self):
        for name, fmt in (("a.png", "PNG"), ("b.jpg", "JPEG")):
            src = self.path(name)
            Image.new("RGB", (200, 100), "red").save(src, fmt)
            self.assertEqual(tm.prepare_media(src, photo_problem), ("photo", src, [], "as is"))

    def test_extreme_aspect_becomes_compliant_jpeg(self):
        src = self.path("wide.png")
        Image.new("RGB", (11000, 100), "red").save(src)
        kind, out, temps, _how = tm.prepare_media(src, photo_problem)
        self.addCleanup(lambda: [os.path.exists(t) and os.remove(t) for t in temps])
        self.assertEqual(kind, "photo")
        self.assertIsNone(photo_problem(out))

    def test_static_webp_bmp_tiff_become_jpeg_photos(self):
        for name in ("s.webp", "s.bmp", "s.tiff"):
            src = self.path(name)
            Image.new("RGB", (64, 64), "blue").save(src)
            kind, out, temps, _how = tm.prepare_media(src, photo_problem)
            self.addCleanup(lambda t=temps: [os.path.exists(x) and os.remove(x) for x in t])
            self.assertEqual(kind, "photo", name)
            self.assertEqual(Image.open(out).format, "JPEG")

    def test_corrupt_image_becomes_document(self):
        src = self.path("bad.jpg")
        with open(src, "wb") as f:
            f.write(b"not an image")
        kind, out, temps, _how = tm.prepare_media(src, photo_problem)
        self.assertEqual((kind, out, temps), ("document", src, []))
        self.assertEqual(os.listdir(self.tmp), ["bad.jpg"])

    @unittest.skipUnless(HAVE_FFMPEG, "ffmpeg not installed")
    def test_animated_gif_becomes_mp4_not_a_still_photo(self):
        src = self.path("anim.gif")
        frames = [Image.new("RGB", (40, 40), c) for c in ("red", "green", "blue")]
        frames[0].save(src, save_all=True, append_images=frames[1:], duration=100, loop=0)
        kind, out, _temps, _how = tm.prepare_media(src, photo_problem)
        self.assertEqual(kind, "video")
        self.assertEqual(streams(out)["video"], "h264")

    def test_non_media_extension_is_a_plain_document(self):
        src = self.path("notes.pdf")
        with open(src, "wb") as f:
            f.write(b"%PDF")
        self.assertEqual(tm.prepare_media(src, photo_problem)[0], "document")


if __name__ == "__main__":
    unittest.main(verbosity=2)
