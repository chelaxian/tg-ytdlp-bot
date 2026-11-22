"""Audio-path permanent errors must not be reported as "site unsupported".

Evidence (log audit 2026-11-22, DE CT108): after PR #573 the audio path
(down_and_audio.py) still sent the hardcoded "Check here if your site
supported / You may need cookie" blockquote for deterministic permanent
failures, e.g. YouTube "Video unavailable. This video is not available"
(deleted/private video, 3 user-visible cases in 24h) and "The downloaded
file is empty". The video path and the Always Ask menu already map these
to localized ALWAYS_ASK_* messages; this test pins the shared helper and
the audio call site's routing so parity holds.
"""
import unittest

from HELPERS.ytdlp_errors import audio_error_ask_category, PERMANENT_ASK_CATEGORIES


class AudioErrorAskCategoryTests(unittest.TestCase):
    def test_deleted_or_private_youtube_video(self):
        cases = (
            'ERROR: [youtube] r9wKkgSNp98: Video unavailable. This video is not available',
            'DownloadError: ERROR: [youtube] 1vvtDM6D2YM: Video unavailable. '
            'This video is not available',
            'ERROR: [youtube] abc123: Private video. Sign in if you have been '
            'granted access to this video',
        )
        for text in cases:
            with self.subTest(text=text[:60]):
                self.assertEqual(audio_error_ask_category(text), 'VIDEO_UNAVAILABLE')

    def test_empty_download(self):
        self.assertEqual(
            audio_error_ask_category('ERROR: The downloaded file is empty'),
            'EMPTY_DOWNLOAD',
        )

    def test_premiere_members_geo_age(self):
        cases = (
            ('ERROR: [youtube] xyz: Premieres in 2 hours. Watch the premiere on 11/23', 'PREMIERE_PENDING'),
            ('ERROR: [youtube] xyz: Join this channel to get access to '
             'members-only content', 'MEMBERS_ONLY'),
            ('ERROR: [youtube] xyz: The uploader has not made this video '
             'available in your country', 'GEO_RESTRICTED'),
            ('ERROR: [youtube] xyz: Sorry, you must verify your age to view '
             'this video', 'AGE_RESTRICTED'),
        )
        for text, expected in cases:
            with self.subTest(text=text[:60]):
                self.assertEqual(audio_error_ask_category(text), expected)

    def test_cookie_fixable_errors_stay_on_cookie_advice(self):
        """Bot-check/auth errors must NOT be routed away from the cookie hint."""
        cases = (
            "ERROR: [youtube] xyz: Sign in to confirm you're not a bot. "
            'This helps protect our community.',
            'ERROR: login required',
            'ERROR: HTTP Error 403: Forbidden',
        )
        for text in cases:
            with self.subTest(text=text[:60]):
                self.assertIsNone(audio_error_ask_category(text))

    def test_unknown_errors_return_none(self):
        for text in ('ERROR: Unsupported URL: https://example.com/x', '', None):
            with self.subTest(text=text):
                self.assertIsNone(audio_error_ask_category(text))

    def test_permanent_categories_map_to_ask_messages(self):
        """Every category the helper returns must have a localized message key."""
        _ASK_ERROR_CATEGORY_MESSAGES = {
            'MEMBERS_ONLY': 'ALWAYS_ASK_MEMBERS_ONLY_MSG',
            'LIVE_ENDED': 'ALWAYS_ASK_LIVE_ENDED_MSG',
            'PREMIERE_PENDING': 'ALWAYS_ASK_PREMIERE_PENDING_MSG',
            'GEO_RESTRICTED': 'ALWAYS_ASK_GEO_RESTRICTED_MSG',
            'AGE_RESTRICTED': 'ALWAYS_ASK_AGE_RESTRICTED_MSG',
            'VIDEO_UNAVAILABLE': 'ALWAYS_ASK_VIDEO_UNAVAILABLE_MSG',
            'EMPTY_DOWNLOAD': 'ALWAYS_ASK_EMPTY_DOWNLOAD_MSG',
        }
        for category in PERMANENT_ASK_CATEGORIES:
            with self.subTest(category=category):
                self.assertIn(category, _ASK_ERROR_CATEGORY_MESSAGES)

    def test_audio_path_routes_permanent_errors_before_cookie_blockquote(self):
        """The audio error block must consult the helper before the generic
        cookie-advice blockquote (offline source check, mirrors
        test_yt403_message.py)."""
        from pathlib import Path
        root = Path(__file__).resolve().parent.parent
        audio_src = (root / 'DOWN_AND_UP' / 'down_and_audio.py').read_text(encoding='utf-8')
        self.assertIn('audio_error_ask_category(error_text, url)', audio_src)
        generic_pos = audio_src.index('You may need <code>cookie</code> for downloading this audio')
        helper_pos = audio_src.index('audio_error_ask_category(error_text, url)')
        self.assertLess(
            helper_pos, generic_pos,
            'permanent-error routing must run before the generic cookie blockquote',
        )


if __name__ == '__main__':
    unittest.main()
