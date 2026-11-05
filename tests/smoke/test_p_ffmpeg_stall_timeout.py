"""ffmpeg stall timeout added by HELPERS.cookie_file.validated_cookie_options (offline).

Run: python tests/smoke/test_p_ffmpeg_stall_timeout.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from HELPERS import cookie_file as cf  # noqa: E402

EXPECTED = ['-rw_timeout', str(cf.FFMPEG_STALL_TIMEOUT_US)]


class FfmpegStallTimeout(unittest.TestCase):
    def test_added_when_missing(self):
        opts = cf.validated_cookie_options({'format': 'best'})
        self.assertEqual(opts['external_downloader_args'], {'ffmpeg_i': EXPECTED})

    def test_caller_options_not_mutated(self):
        original = {'format': 'best', 'external_downloader_args': {'ffmpeg': ['-loglevel', 'error']}}
        opts = cf.validated_cookie_options(original)
        self.assertEqual(original['external_downloader_args'], {'ffmpeg': ['-loglevel', 'error']})
        self.assertEqual(opts['external_downloader_args'],
                         {'ffmpeg': ['-loglevel', 'error'], 'ffmpeg_i': EXPECTED})

    def test_explicit_input_args_win(self):
        for key in ('ffmpeg_i', 'ffmpeg_i1'):
            with self.subTest(key=key):
                opts = cf.validated_cookie_options({'external_downloader_args': {key: ['-x']}})
                self.assertEqual(opts['external_downloader_args'], {key: ['-x']})

    def test_plain_list_left_alone(self):
        opts = cf.validated_cookie_options({'external_downloader_args': ['-x']})
        self.assertEqual(opts['external_downloader_args'], ['-x'])

    def test_timeout_is_a_minute(self):
        self.assertEqual(cf.FFMPEG_STALL_TIMEOUT_US, 60_000_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
