"""Regression: Always Ask menu must not dump raw yt-dlp 'Requested format is
not available' at users (log audit 2026-11-25, DE CT108).

Evidence: 12 user-visible LOG_EXCEPTION cases in 24h (ids ~100085-100113,
DE window 2026-11-24 19:50 → 2026-11-25 20:00 UTC) showed the raw English
yt-dlp error in the Always Ask fallback path, because _classify_ask_error()
maps no category for FORMAT_UNAVAILABLE, so _ask_error_message() returned
None and the generic error_text (with the sanitized raw error) was sent.
The download path already shows the localized FORMAT_NOT_AVAILABLE_MSG +
advice, and CONFIG.LANGUAGES has FORMAT_NOT_AVAILABLE_MSG in every language.

Offline source-structure test (same pattern as
test_video_permanent_error_message.py from PR #575): no pyrogram import
needed.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


class AlwaysAskFormatUnavailableRoutingTests(unittest.TestCase):
    def test_classify_ask_error_maps_format_unavailable(self):
        """_classify_ask_error must route FORMAT_UNAVAILABLE retryability to
        the FORMAT_UNAVAILABLE ask category, mirroring the AUTH_REQUIRED /
        CLIENT_HTTP_ERROR / PERMANENT gap-filler branches."""
        src = _read('DOWN_AND_UP/always_ask_menu.py')
        self.assertIn(
            "retry_cat == ytdlp_errors.FORMAT_UNAVAILABLE",
            src,
            'FORMAT_UNAVAILABLE must be mapped in _classify_ask_error like '
            'the other retryability gap-filler branches',
        )

    def test_category_has_localized_message(self):
        """The mapped category must have a localized ALWAYS_ASK_* message and
        must not trigger the pointless cookie hint."""
        src = _read('DOWN_AND_UP/always_ask_menu.py')
        self.assertIn("'FORMAT_UNAVAILABLE':", src)
        no_hint = src.index('_ASK_ERROR_NO_COOKIE_HINT = frozenset({')
        no_hint_end = src.index('})', no_hint)
        hint_block = src[no_hint:no_hint_end]
        self.assertNotIn('FORMAT_UNAVAILABLE', hint_block)


if __name__ == '__main__':
    unittest.main()
