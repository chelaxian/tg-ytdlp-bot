"""Offline checks for the 2026-11-05 DE error-log triage.

Run: python tests/smoke/test_t_log_errors_audit.py
Pure-function checks load code via ast, so they need no bot dependencies.
"""
import ast
import os
import pathlib
import re
import sys
import unicodedata
import unittest
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
NAME_MAX = 255


def load_functions(path, names, namespace):
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
    nodes = [n for n in tree.body
             if (isinstance(n, ast.FunctionDef) and n.name in names)
             or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in names for t in n.targets))]
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


def filesystem_namespace():
    ns = {"os": os, "re": re, "unicodedata": unicodedata}
    load_functions("HELPERS/filesystem_hlp.py",
                   {"_SAFE_CHARS", "_byte_len", "_truncate_name", "_REAL_EXT_RE", "_split_name_ext",
                    "_clean_unicode_name", "sanitize_filename", "sanitize_filename_strict"}, ns)
    return ns


# Facebook reel caption from the DE log: ends with ". #hashtags ... | Farsi Persian Song"
FB_TITLE = (
    "27K views · 618 reactions | Top Persian Music 2026 | بهترین موسیقی فارسی ۲۰۲۶ | "
    "بهترین موسیقی و آهنگ های فارسی Welcome to a Persian music collection filled with beautiful "
    "songs, memorable melodies, and a rich musical atmosphere. This 2026 selection brings together "
    "Persian music for listeners who appreciate expressive vocals. "
    "#PersianMusic #PersianSongs #TopPersianMusic #PersianMusic2026 #FarsiMusic #IranianMusic "
    "#موسیقی_فارسی #آهنگ_فارسی #موزیک_ایرانی #آهنگ_های_فارسی #بهترین_موسیقی #PersianMelodies "
    "#PersianMix #FarsiSongsMusic #PersianPlaylist | Farsi Persian Song"
)


class FilenameTests(unittest.TestCase):
    def setUp(self):
        self.ns = filesystem_namespace()

    def test_caption_with_dot_is_not_an_extension(self):
        out = self.ns["sanitize_filename"](FB_TITLE)
        self.assertLessEqual(len(out.encode("utf-8")) + len(".jpg"), NAME_MAX)
        self.assertLessEqual(len(out.encode("utf-8")), 100)
        for bad in "#|":
            self.assertNotIn(bad, out)
        self.assertFalse(out.startswith("."))

    def test_strict_variant(self):
        out = self.ns["sanitize_filename_strict"](FB_TITLE)
        self.assertLessEqual(len(out.encode("utf-8")), 100)
        self.assertNotIn("#", out)

    def test_real_extension_kept(self):
        self.assertEqual(self.ns["sanitize_filename"]("My video.mp4"), "My video.mp4")
        self.assertEqual(self.ns["sanitize_filename"]("Song.webm"), "Song.webm")
        long_name = "ä" * 200 + ".mp4"
        out = self.ns["sanitize_filename"](long_name)
        self.assertTrue(out.endswith(".mp4"))
        self.assertLessEqual(len(out.encode("utf-8")), 100)

    def test_split_name_ext(self):
        split = self.ns["_split_name_ext"]
        self.assertEqual(split("a.mp4"), ("a", ".mp4"))
        self.assertEqual(split("Mr. Smith #tag | x"), ("Mr. Smith #tag | x", ""))
        self.assertEqual(split("no dots"), ("no dots", ""))

    def test_oversized_extension_is_never_returned_raw(self):
        out = self.ns["_truncate_name"]("x", "." + "q" * 300, 100)
        self.assertLessEqual(len(out.encode("utf-8")), 100)


class UrlExtractorTests(unittest.TestCase):
    def test_manifest_paths(self):
        ns = {"urlparse": urlparse}
        load_functions("URL_PARSERS/url_extractor.py", {"_is_downloadable_manifest"}, ns)
        fn = ns["_is_downloadable_manifest"]
        self.assertTrue(fn("https://cdn.example/a.mpd?token=redacted"))
        self.assertTrue(fn("https://cdn.example/a.m3u8?token=redacted"))
        self.assertTrue(fn("https://cdn.example/a.m3u8/"))
        self.assertFalse(fn("https://cdn.example/a.mpd.jpg"))
        self.assertFalse(fn("https://cdn.example/a.ts?file=a.m3u8"))
        self.assertFalse(fn("https://i.ytimg.com/vi/abc/maxresdefault.jpg"))


class SourceTests(unittest.TestCase):
    def read(self, rel):
        return (ROOT / rel).read_text(encoding="utf-8")

    def test_geo_branch_in_video_and_audio(self):
        for rel in ("DOWN_AND_UP/down_and_up.py", "DOWN_AND_UP/down_and_audio.py"):
            src = self.read(rel)
            self.assertIn('"GEO_RESTRICTED"', src, rel)
            self.assertIn("[:600]", src, rel)

    def test_httponly_not_a_tag(self):
        self.assertIn("startswith('HttpOnly_')", self.read("URL_PARSERS/tags.py"))

    def test_gallery_unsupported_url_is_classified(self):
        src = self.read("COMMANDS/image_cmd.py")
        self.assertIn("is_gallery_dl_no_extractor_error", src)

    def test_gallery_markers(self):
        ns = {}
        load_functions("HELPERS/fallback_helper.py",
                       {"_GALLERY_DL_NO_EXTRACTOR_MARKERS", "is_gallery_dl_no_extractor_error"}, ns)
        fn = ns["is_gallery_dl_no_extractor_error"]
        self.assertTrue(fn("[gallery-dl][error] Unsupported URL 'https://x/y.m3u8'"))
        self.assertFalse(fn("403 Forbidden"))


if __name__ == "__main__":
    unittest.main()
