"""Проверки классификации ошибок без сети и конфигурации бота."""
import unittest

from HELPERS.ytdlp_errors import (
    AUTH_REQUIRED, CLIENT_HTTP_ERROR, FORMAT_UNAVAILABLE, LOCAL_FILE_ERROR,
    PERMANENT, RATE_LIMITED, TRANSIENT, classify_retryability,
    is_permanent_unavailable, should_abort_retries,
)


class RetryabilityTests(unittest.TestCase):
    def test_reported_errors(self):
        cases = (
            ('Video unavailable. This video has been removed', PERMANENT),
            ('Join this channel to get access to members-only content', PERMANENT),
            ('Sign in to confirm your age', PERMANENT),
            ('The page needs to be reloaded', PERMANENT),
            ("KeyError('INNERTUBE_CONTEXT')", PERMANENT),
            ('[Douyin] Fresh cookies are needed', AUTH_REQUIRED),
            ('HTTP Error 400: Bad Request', CLIENT_HTTP_ERROR),
            ('HTTP Error 429: Too Many Requests', RATE_LIMITED),
            ('[Errno 2] No such file or directory', LOCAL_FILE_ERROR),
            ('Disk quota exceeded', LOCAL_FILE_ERROR),
            ('Requested format is not available', FORMAT_UNAVAILABLE),
            ('Read timed out', TRANSIENT),
        )
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(classify_retryability(text), expected)

    def test_geo_prefix_does_not_disable_proxy_recovery(self):
        text = ('Video unavailable. The uploader has not made this video '
                'available in your country')
        self.assertFalse(is_permanent_unavailable(text))
        self.assertFalse(should_abort_retries(text))

    def test_explicit_removal_remains_terminal(self):
        text = 'Video unavailable. It has been removed. Not available in your country'
        self.assertTrue(should_abort_retries(text))

    def test_conditional_and_unknown_errors_remain_recoverable(self):
        for text in ('HTTP Error 403: Forbidden', 'Unrecognised extractor response', ''):
            with self.subTest(text=text):
                self.assertFalse(should_abort_retries(text))


if __name__ == '__main__':
    unittest.main()
