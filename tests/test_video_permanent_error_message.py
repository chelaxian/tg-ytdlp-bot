"""Video-path permanent errors must not be reported as "site unsupported".

Evidence (log audit 2026-11-23, DE CT108): the non-YouTube video path
(down_and_up.py) still sent the hardcoded "Check here if your site
supported / You may need cookie" blockquote for deterministic permanent
failures, e.g. "The downloaded file is empty" from HLS proxies (3
user-visible cases in 24h, LOG_EXCEPTION ids 99991-99993). The audio path
(PR #574) and the Always Ask menu already route these to localized
ALWAYS_ASK_* messages; this test pins the video call site's routing so
parity holds.
"""
import unittest

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class VideoPathPermanentErrorRoutingTests(unittest.TestCase):
    def test_video_path_routes_permanent_errors_before_cookie_blockquote(self):
        """The non-YouTube error block must consult the shared classifier
        before the generic cookie-advice blockquote (offline source check,
        mirrors test_audio_permanent_error_message.py)."""
        video_src = (ROOT / 'DOWN_AND_UP' / 'down_and_up.py').read_text(encoding='utf-8')
        self.assertIn('audio_error_ask_category(error_message, url)', video_src)
        generic_pos = video_src.index('ERROR_CHECK_SUPPORTED_SITES_MSG}</blockquote>')
        helper_pos = video_src.index('audio_error_ask_category(error_message, url)')
        self.assertLess(
            helper_pos, generic_pos,
            'permanent-error routing must run before the generic cookie blockquote',
        )

    def test_video_path_guard_is_non_youtube_only(self):
        """The routing must live inside the `not is_youtube_url(url)` guard
        (the block that starts `if not error_message_sent and not
        is_youtube_url(url):`): YouTube failures have their own localized
        handling upstream."""
        video_src = (ROOT / 'DOWN_AND_UP' / 'down_and_up.py').read_text(encoding='utf-8')
        helper_pos = video_src.index('audio_error_ask_category(error_message, url)')
        generic_pos = video_src.index('ERROR_CHECK_SUPPORTED_SITES_MSG}</blockquote>')
        guard_pos = video_src.index('not error_message_sent and not is_youtube_url(url)')
        self.assertLess(
            guard_pos, helper_pos,
            'permanent-error routing must live inside the non-YouTube guard',
        )
        self.assertLess(helper_pos, generic_pos)


if __name__ == '__main__':
    unittest.main()
