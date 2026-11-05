"""HELPERS.log_redact masks credentials in log records (offline).

Run: python tests/smoke/test_q_log_redact.py
"""
import io
import logging
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from HELPERS import log_redact  # noqa: E402

JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEyMzQ1fQ.c2lnbmF0dXJlLXZhbHVlLWhlcmU"
SECRET_BITS = ("eyJhbGci", "c2lnbmF0dXJl", "s3cr3tpass", "sess=abc123", "k-9f8e7d6c")


class Redact(unittest.TestCase):
    def assertClean(self, text):
        out = log_redact.redact(text)
        for bit in SECRET_BITS:
            self.assertNotIn(bit, out, out)
        return out

    def test_args_loaded_dict(self):
        line = "User 1 args loaded: {'http_headers': '{\n  \"Authorization\": \"Bearer %s\",\n  \"origin\": \"https://x.cloud\"\n}'}" % JWT
        out = self.assertClean(line)
        self.assertIn("Bearer ***", out)
        self.assertIn("https://x.cloud", out)

    def test_message_text_and_escaped_json(self):
        self.assertClean('"text": "{\n  \\"Authorization\\": \\"Bearer %s\\",\n}"' % JWT)
        self.assertClean("[HANDLER-START] url_distractor chat=1 text='Bearer %s'" % JWT)

    def test_cookie_and_api_key_headers(self):
        out = self.assertClean("http_headers: {'Cookie': 'sess=abc123; uid=7', 'X-Api-Key': 'k-9f8e7d6c'}")
        self.assertIn("'Cookie': '***", out)

    def test_bare_jwt_and_proxy_url(self):
        self.assertClean("token is %s now" % JWT)
        out = self.assertClean("proxy socks5://bob:s3cr3tpass@1.2.3.4:1080 failed")
        self.assertIn("socks5://***:***@1.2.3.4:1080", out)

    def test_netscape_cookie_lines(self):
        value = "AFmmF2swRQIhAKsecretcookievalue"
        cases = (
            # real tabs (file content), escaped \t (repr/JSON), spaces (Telegram paste)
            ".youtube.com\tTRUE\t/\tTRUE\t1790000000\tLOGIN_INFO\t" + value,
            "text='/save_as_cookie\\n.youtube.com\\tTRUE\\t/\\tFALSE\\t0\\tSID\\t" + value + "\\n'",
            '"text": "/save_as_cookie\\n.youtube.com  TRUE  /  FALSE  1790000000  SID  ' + value + '",',
            "/save_as_cookie .youtube.com TRUE / TRUE 1790000000 SID " + value,
            "#HttpOnly_.instagram.com\tTRUE\t/\tTRUE\t1790000000\tsessionid\t" + value,
        )
        for line in cases:
            with self.subTest(line=line):
                out = log_redact.redact(line)
                self.assertNotIn(value, out)
                self.assertIn("***", out)
        out = log_redact.redact(cases[0])
        self.assertTrue(out.startswith(".youtube.com\tTRUE\t/\tTRUE\t1790000000\tLOGIN_INFO\t"), out)

    def test_ordinary_lines_untouched(self):
        for line in (
            "Copied cookies to download directory: users/1/downloads/x/cookie.txt",
            "[YTDLP DEBUG] Using cookies for https://youtu.be/x: users/1/cookie.txt",
            "opts keys: ['cookiefile', 'format']",
            "Add PO token provider for YouTube domains",
            "Downloading https://videos.example.cloud/content_store_412/master.m3u8",
            "[CHANNEL_CHECK] User 7 is member of channel @mychannel",
            "[debug] params: {'quiet': True, 'noplaylist': True, 'skip_download': True}",
            "is_true TRUE FALSE flags: TRUE / FALSE",
        ):
            with self.subTest(line=line):
                self.assertEqual(log_redact.redact(line), line)


class RecordFactory(unittest.TestCase):
    def test_installed_factory_masks_args(self):
        log_redact.install()
        self.assertFalse(log_redact.install())  # idempotent
        stream = io.StringIO()
        logger = logging.getLogger("redact-test")
        handler = logging.StreamHandler(stream)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        logger.info("User %s final ytdlp_args: %s", 5, {"http_headers": {"Authorization": "Bearer " + JWT}})
        logger.info("plain %s line", "ok")
        out = stream.getvalue()
        self.assertNotIn("eyJhbGci", out)
        self.assertIn("Bearer ***", out)
        self.assertIn("plain ok line", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
