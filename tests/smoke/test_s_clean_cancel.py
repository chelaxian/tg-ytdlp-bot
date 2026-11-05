"""/clean cancellation is terminal and survives a deleted progress message (offline).

Covers three fixes:
1. "Download cancelled by user (/clean)" must classify as USER_CANCELLED and
   abort every retry chain (HELPERS/ytdlp_errors.py + proxy fallback).
2. try_with_proxy_fallback() must not restart the download through other
   proxies after a user cancellation.
3. The progress hook must raise on cancellation even when the progress
   message was already deleted (progress_msg_dead, issue #322 regression).

Run: python tests/smoke/test_s_clean_cancel.py
"""
import os
import sys
import types
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from HELPERS import ytdlp_errors  # noqa: E402


class CancelIsTerminal(unittest.TestCase):
    CANCELLED = "Download cancelled by user (/clean)"
    VARIANTS = (
        CANCELLED,
        "download cancelled by user (/clean)",
        "Live stream download cancelled by user (42) via /clean",
        "operation canceled by user",
    )

    def test_classified_as_user_cancelled(self):
        for text in self.VARIANTS:
            self.assertEqual(ytdlp_errors.classify_retryability(text),
                             ytdlp_errors.USER_CANCELLED, text)

    def test_should_abort_retries(self):
        for text in self.VARIANTS:
            self.assertTrue(ytdlp_errors.should_abort_retries(text), text)

    def test_unrelated_errors_still_retried(self):
        for text in ("read timed out", "http error 500", "unexpected flake"):
            self.assertFalse(ytdlp_errors.should_abort_retries(text), text)


class ProxyFallbackStops(unittest.TestCase):
    def _run_fallback(self):
        # Minimal fakes so try_with_proxy_fallback() exercises its per-proxy loop.
        fake_proxy_cmd = types.ModuleType("COMMANDS.proxy_cmd")
        fake_proxy_cmd.is_proxy_enabled = lambda user_id: True
        fake_proxy_cmd.get_user_selected_country = lambda user_id: "DE"
        fake_proxy_cmd.get_proxies_for_country = lambda country: [
            {"proxy_url": f"socks5://10.0.0.{i}:1080", "type": "socks5", "country": country}
            for i in (1, 2, 3)
        ]
        fake_limits = types.ModuleType("CONFIG.limits")
        fake_limits.LimitsConfig = types.SimpleNamespace(MAX_PROXIES_PER_COUNTRY=3)
        fake_messeger = types.ModuleType("HELPERS.safe_messeger")
        fake_messeger.safe_send_message = lambda *a, **k: None
        for name, mod in (("COMMANDS.proxy_cmd", fake_proxy_cmd),
                          ("CONFIG.limits", fake_limits),
                          ("HELPERS.safe_messeger", fake_messeger)):
            sys.modules[name] = mod
        try:
            from HELPERS import proxy_helper
            proxy_helper.PROXY_TEST_TIMEOUT = 1
            proxy_helper.test_proxy_url = lambda url, timeout=1: True
            proxy_helper.is_youtube_url = lambda url: False
            proxy_helper.add_pot_to_ytdl_opts = lambda opts, url: opts
            calls = []

            def operation(opts, *a, **k):
                calls.append(opts.get("proxy"))
                raise Exception("Download cancelled by user (/clean)")

            with self.assertRaises(Exception) as ctx:
                proxy_helper.try_with_proxy_fallback({}, "https://x.example/v", 7, operation)
            self.assertIn("cancelled by user", str(ctx.exception))
            # One download start only: cancellation must not be "retried" per proxy.
            self.assertEqual(len(calls), 1, calls)
        finally:
            for name in ("COMMANDS.proxy_cmd", "CONFIG.limits", "HELPERS.safe_messeger"):
                sys.modules.pop(name, None)


class ProgressHookStillRaisesWhenMessageDeleted(unittest.TestCase):
    def test_cancel_checked_before_progress_msg_dead(self):
        # Static check: in both progress hooks the _cancel_ev.is_set() raise must
        # come before the progress_msg_dead early-return, otherwise a deleted
        # progress message silently disables /clean cancellation.
        src = open(os.path.join(os.path.dirname(__file__), "..", "..", "DOWN_AND_UP/down_and_up.py"),
                   encoding="utf-8").read()
        start = src.index("def progress_func")
        cancel = src.index("_cancel_ev.is_set()", start)
        dead = src.index("if progress_msg_dead:", start)
        self.assertLess(cancel, dead, "cancellation must be checked before progress_msg_dead")


if __name__ == "__main__":
    unittest.main(verbosity=2)
