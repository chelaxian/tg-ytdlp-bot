"""Offline regression tests for /split without bot credentials or Pyrogram."""
import ast
import logging
import math
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[2]


def load_functions(path, names, env):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    for node in nodes:
        node.decorator_list = []
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), env)
    return env


class SplitTests(unittest.TestCase):
    def setUp(self):
        self.env = load_functions("COMMANDS/split_sizer.py", {"parse_size_argument", "get_user_split_size"}, {
            "os": os, "re": re, "math": math, "MIN_SPLIT_SIZE": 100 * 1024**2,
            "MAX_SPLIT_SIZE": 2 * 1024**3, "DEFAULT_SPLIT_SIZE": 1950 * 1024**2,
        })

    def test_callback_validation_and_atomic_storage(self):
        msg = SimpleNamespace(SPLIT_INVALID_SIZE_CALLBACK_MSG="invalid", SPLIT_SIZE_SET_MSG="size {size}",
                              SPLIT_SIZE_SET_CALLBACK_LOG_MSG="size {size}")
        answered, edits = Mock(), Mock()
        env = {**self.env, "tempfile": tempfile, "create_directory": lambda p: os.makedirs(p, exist_ok=True),
               "safe_get_messages": lambda _: msg, "safe_callback_answer": answered,
               "safe_edit_message_text": edits, "send_to_logger": Mock(), "humanbytes": str,
               "logger": logging.getLogger(__name__)}
        load_functions("COMMANDS/split_sizer.py", {"_write_split_size", "split_size_callback"}, env)
        old = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            try:
                os.chdir(tmp)
                cb = SimpleNamespace(from_user=SimpleNamespace(id=1), message=SimpleNamespace(
                    chat=SimpleNamespace(id=1), id=42), data="split_size|1")
                env["split_size_callback"](None, cb)
                answered.assert_called_once_with(cb, "invalid")
                self.assertFalse(Path("users/1/split.txt").exists())
                answered.reset_mock()
                cb.data = "split_size|104857600"
                env["split_size_callback"](None, cb)
                self.assertEqual(Path("users/1/split.txt").read_text(), "104857600")
                self.assertEqual(os.listdir("users/1"), ["split.txt"])
                answered.assert_called_once_with(cb)
                edits.assert_called_once()
            finally:
                os.chdir(old)

    def test_arguments(self):
        parse = self.env["parse_size_argument"]
        self.assertEqual(parse("100mb"), 100 * 1024**2)
        self.assertEqual(parse("1.5GB"), 1536 * 1024**2)
        self.assertEqual(parse("2gb"), 2 * 1024**3)
        for value in ("0mb", "99mb", "2.01gb", "x", "9" * 400 + "mb"):
            self.assertIsNone(parse(value), value)

    def test_stored_bounds(self):
        old = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            try:
                os.chdir(tmp)
                path = Path("users/1/split.txt")
                path.parent.mkdir(parents=True)
                for value in ("0", "-1", "1", str(3 * 1024**3), "bad", ""):
                    path.write_text(value)
                    self.assertEqual(self.env["get_user_split_size"](1), 1950 * 1024**2)
                path.write_text(str(100 * 1024**2))
                self.assertEqual(self.env["get_user_split_size"](1), 100 * 1024**2)
            finally:
                os.chdir(old)

    def test_ffmpeg_results_fail_closed(self):
        template = SimpleNamespace(FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG="{rounds}",
            FFMPEG_SPLITTING_VIDEO_PART_MSG="{current}/{total} {start_time} {end_time}",
            FFMPEG_VIDEO_SPLIT_SUCCESS_MSG="{count}")
        env = {"os": os, "math": math, "tempfile": tempfile, "logger": logging.getLogger(__name__),
               "safe_get_messages": lambda _: template, "get_video_info_ffprobe": lambda _: (1, 1, 20),
               "_extract_split_part": Mock(return_value=False)}
        split = load_functions("DOWN_AND_UP/ffmpeg.py", {"split_video_2"}, env)["split_video_2"]
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RuntimeError):
                split(tmp, "v", "source", 200, 100, 20, 1)
            self.assertEqual(os.listdir(tmp), [])
            calls = []
            def variable_part(_source, start, end, target):
                calls.append((start, end))
                Path(target).write_bytes(b"a" * int((end - start) * (15 if start < 10 else 5)))
                return True
            env["_extract_split_part"] = variable_part
            result = split(tmp, "v", "source", 200, 100, 20, 1)
            self.assertEqual(len(result["path"]), 3)
            self.assertTrue(all(os.path.getsize(p) <= 100 for p in result["path"]))
            self.assertEqual(calls, [(0, 10), (0, 5), (5, 10), (10, 20)])
            with self.assertRaises(ValueError):
                split(tmp, "v", "source", 200, 0, 20, 1)

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg/ffprobe unavailable")
    def test_real_long_gop_video(self):
        ffmpeg = shutil.which("ffmpeg")
        ffprobe = shutil.which("ffprobe")
        def probe(path):
            duration = subprocess.check_output([ffprobe, "-v", "error", "-show_entries",
                "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)], text=True)
            return 160, 90, float(duration)
        template = SimpleNamespace(FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG="{rounds}",
            FFMPEG_VIDEO_SPLIT_SUCCESS_MSG="{count}")
        env = {"os": os, "math": math, "tempfile": tempfile, "subprocess": subprocess,
               "logger": logging.getLogger(__name__), "safe_get_messages": lambda _: template,
               "get_ffmpeg_path": lambda: ffmpeg, "get_video_info_ffprobe": probe}
        load_functions("DOWN_AND_UP/ffmpeg.py", {"split_video_2", "_extract_split_part"}, env)
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.mp4"
            subprocess.run([ffmpeg, "-y", "-v", "error", "-f", "lavfi", "-i",
                "testsrc2=size=160x90:rate=25:duration=8", "-f", "lavfi", "-i",
                "sine=frequency=440:duration=8", "-c:v", "libx264", "-c:a", "aac", "-g", "250",
                "-pix_fmt", "yuv420p", "-shortest", str(source)], check=True)
            limit = source.stat().st_size // 3
            result = env["split_video_2"](tmp, "v", str(source), source.stat().st_size, limit, 8, 1)
            self.assertGreaterEqual(len(result["path"]), 3)
            self.assertTrue(all(0 < os.path.getsize(p) <= limit for p in result["path"]))
            self.assertAlmostEqual(sum(probe(p)[2] for p in result["path"]), 8, delta=0.3)
            def frame_count(path):
                output = subprocess.check_output([ffprobe, "-v", "error", "-select_streams", "v:0", "-count_frames",
                    "-show_entries", "stream=nb_read_frames", "-of", "default=noprint_wrappers=1:nokey=1", str(path)], text=True)
                return int(output)
            # Bound encoder rounding to at most one frame per segment.
            self.assertLessEqual(abs(sum(frame_count(p) for p in result["path"]) - frame_count(source)),
                                 len(result["path"]))
            for path in result["path"]:
                audio = subprocess.check_output([ffprobe, "-v", "error", "-select_streams", "a:0", "-show_entries",
                    "stream=codec_name", "-of", "csv=p=0", str(path)], text=True).strip()
                self.assertEqual(audio, "aac")


if __name__ == "__main__":
    unittest.main()
