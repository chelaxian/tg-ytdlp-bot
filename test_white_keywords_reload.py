import unittest


class TestWhiteKeywordsRuntimeConfig(unittest.TestCase):
    def test_is_porn_respects_config_white_keywords_for_url(self):
        from HELPERS import porn as porn_mod
        from CONFIG.config import Config

        url = "https://x.com/dilf_minseok/status/2041560678788665575?s=52"

        old_white = getattr(Config, "WHITE_KEYWORDS", None)
        try:
            Config.WHITE_KEYWORDS = ["dilf_minseok"]
            self.assertFalse(porn_mod.is_porn(url, "", "", None))
        finally:
            if old_white is None:
                try:
                    delattr(Config, "WHITE_KEYWORDS")
                except Exception:
                    pass
            else:
                Config.WHITE_KEYWORDS = old_white

    def test_check_porn_detailed_respects_config_white_keywords(self):
        from HELPERS import porn as porn_mod
        from HELPERS.porn import check_porn_detailed
        from CONFIG.config import Config

        url = "https://x.com/dilf_minseok/status/2041560678788665575?s=52"

        old_white = getattr(Config, "WHITE_KEYWORDS", None)
        old_keywords = set(getattr(porn_mod, "PORN_KEYWORDS", set()) or set())
        try:
            Config.WHITE_KEYWORDS = ["dilf_minseok"]
            porn_mod.PORN_KEYWORDS = {"dilf"}
            is_nsfw, explanation = check_porn_detailed(url, "", "", None, uploader="dilf")
            self.assertFalse(is_nsfw)
            self.assertTrue(isinstance(explanation, str) and explanation)
        finally:
            porn_mod.PORN_KEYWORDS = old_keywords
            if old_white is None:
                try:
                    delattr(Config, "WHITE_KEYWORDS")
                except Exception:
                    pass
            else:
                Config.WHITE_KEYWORDS = old_white


if __name__ == "__main__":
    unittest.main()

import unittest


class TestWhiteKeywordsRuntimeConfig(unittest.TestCase):
    def test_is_porn_respects_config_white_keywords_for_url(self):
        # Import inside test to avoid side effects at module import time
        from HELPERS import porn as porn_mod
        from CONFIG.config import Config

        url = "https://x.com/dilf_minseok/status/2041560678788665575?s=52"

        old = getattr(Config, "WHITE_KEYWORDS", None)
        try:
            Config.WHITE_KEYWORDS = ["dilf_minseok"]
            # Should be clean because whitelist keyword appears in URL path
            self.assertFalse(porn_mod.is_porn(url, "", "", None))
        finally:
            if old is None:
                try:
                    delattr(Config, "WHITE_KEYWORDS")
                except Exception:
                    pass
            else:
                Config.WHITE_KEYWORDS = old

    def test_check_porn_detailed_respects_config_white_keywords(self):
        from HELPERS import porn as porn_mod
        from HELPERS.porn import check_porn_detailed
        from CONFIG.config import Config

        url = "https://x.com/dilf_minseok/status/2041560678788665575?s=52"

        old_white = getattr(Config, "WHITE_KEYWORDS", None)
        old_keywords = set(getattr(porn_mod, "PORN_KEYWORDS", set()) or set())
        try:
            Config.WHITE_KEYWORDS = ["dilf_minseok"]
            # Ensure the porn keyword list contains 'dilf' so this test stays meaningful
            porn_mod.PORN_KEYWORDS = {"dilf"}
            is_nsfw, explanation = check_porn_detailed(url, "", "", None, uploader="dilf")
            self.assertFalse(is_nsfw)
            self.assertTrue(isinstance(explanation, str) and explanation)
        finally:
            porn_mod.PORN_KEYWORDS = old_keywords
            if old_white is None:
                try:
                    delattr(Config, "WHITE_KEYWORDS")
                except Exception:
                    pass
            else:
                Config.WHITE_KEYWORDS = old_white


if __name__ == "__main__":
    unittest.main()

