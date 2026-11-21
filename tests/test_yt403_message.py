"""YouTube media-download 403 must not be reported as "site unsupported".

Evidence (log audit 2026-11-21): yt-dlp extracts metadata fine, then the
googlevideo.com media request is throttled with HTTP 403; the audio path
(down_and_audio.py) used to send the hardcoded "Check here if your site
supported / You may need cookie" blockquote, misleading users. The video
path already guards with is_youtube_url(url); this test pins the shared
predicate and both call sites' guard conditions offline.
"""
import unittest

from HELPERS.ytdlp_errors import is_temporary_access_block


class TemporaryAccessBlockTests(unittest.TestCase):
    def test_matches_youtube_download_403(self):
        cases = (
            'ERROR: unable to download video data: HTTP Error 403: Forbidden',
            'DownloadError: unable to download video data: HTTP Error 403: Forbidden',
            'HTTP error 403: forbidden',
        )
        for text in cases:
            with self.subTest(text=text):
                self.assertTrue(is_temporary_access_block(text))

    def test_matches_try_again_later(self):
        self.assertTrue(is_temporary_access_block('Please try again in a few minutes'))
        self.assertTrue(is_temporary_access_block('HTTP Error 429: Too Many Requests. Try again later'))

    def test_does_not_match_unrelated_errors(self):
        cases = (
            'ERROR: Unsupported URL: https://example.com/x',
            'ERROR: [youtube] xyz: Sign in to confirm you\'re not a bot',
            'ERROR: [generic] 123: No video formats found!',
            'HTTP Error 404: Not Found',
            'HTTP Error 401: Unauthorized',
            '',
            None,
        )
        for text in cases:
            with self.subTest(text=text):
                self.assertFalse(is_temporary_access_block(text))

    def test_audio_and_video_paths_guard_with_is_youtube_url(self):
        """Both error-sending blocks must be gated on a YouTube-URL check."""
        import re as _re
        from pathlib import Path

        root = Path(__file__).resolve().parent.parent
        audio_src = (root / 'DOWN_AND_UP' / 'down_and_audio.py').read_text(encoding='utf-8')
        self.assertIn(
            'is_youtube_url(url) and is_temporary_access_block(error_text)',
            audio_src,
            'audio path must route YouTube download 403 to the rate-limit message',
        )
        self.assertIn(
            'ALWAYS_ASK_YT_RATE_LIMITED_MSG',
            audio_src,
            'audio path must use the localized YT_RATE_LIMITED message',
        )
        # The video path keeps its existing guard: generic blockquote advice is
        # only sent for non-YouTube URLs (issue: YouTube 403 used to leak there
        # before the not is_youtube_url(url) guard).
        up_src = (root / 'DOWN_AND_UP' / 'down_and_up.py').read_text(encoding='utf-8')
        guard_re = _re.compile(
            r'if not error_message_sent and not is_youtube_url\(url\):'
        )
        self.assertTrue(
            guard_re.search(up_src),
            'video path generic error blockquote must stay behind not is_youtube_url(url)',
        )


if __name__ == '__main__':
    unittest.main()
