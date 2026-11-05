"""Offline regression tests for /split without bot credentials or Pyrogram."""
import ast
import logging
import math
import os
import re
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[2]


def load_functions(path, names, env):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), env)
    return env


class SplitTests(unittest.TestCase):
    def setUp(self):
        self.env = load_functions("COMMANDS/split_sizer.py", {"parse_size_argument", "get_user_split_size"}, {
            "os": os, "re": re, "math": math, "MIN_SPLIT_SIZE": 100 * 1024**2,
            "MAX_SPLIT_SIZE": 2 * 1024**3, "DEFAULT_SPLIT_SIZE": 1950 * 1024**2,
        })

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
        env = {"os": os, "math": math, "logger": logging.getLogger(__name__),
               "safe_get_messages": lambda _: template, "ffmpeg_extract_subclip": Mock(return_value=False)}
        split = load_functions("DOWN_AND_UP/ffmpeg.py", {"split_video_2"}, env)["split_video_2"]
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RuntimeError):
                split(tmp, "v", "source", 200, 100, 20, 1)
            def make_part(_source, _start, _end, targetname):
                Path(targetname).write_bytes(b"a" * 101)
                return True
            env["ffmpeg_extract_subclip"] = make_part
            with self.assertRaises(RuntimeError):
                split(tmp, "v", "source", 200, 100, 20, 1)
            env["ffmpeg_extract_subclip"] = lambda *a, **kw: Path(kw["targetname"]).write_bytes(b"a" * 90) > 0
            result = split(tmp, "v", "source", 200, 100, 20, 1)
            self.assertEqual(len(result["path"]), 2)
            with self.assertRaises(ValueError):
                split(tmp, "v", "source", 200, 0, 20, 1)


if __name__ == "__main__":
    unittest.main()
