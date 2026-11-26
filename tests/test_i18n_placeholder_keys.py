"""Regression tests: non-ASCII placeholder keys in message templates crash .format().

GROUP 1 defect (window 2026-11-25 19:50 -> 2026-11-26 20:00 UTC):
proxy_option_callback crashed with KeyError: 'país' for ES users because
messages_ES.PROXY_COUNTRY_SELECTED_MSG uses {país} (non-ASCII key) while the
caller formats with country=/country_code=. Same class of defect in HA/KO/UR/KK.

Tests scan the REAL loaded message tables (LanguageRouter.load_messages) for
placeholder keys containing non-ASCII characters, so .format(**ascii_kwargs)
can never raise KeyError for a translated key.
"""
import re
import sys
import types
import unittest
from unittest.mock import patch

PLACEHOLDER_RE = re.compile(r'\{([^{}\n]+)\}')


def _stub_config():
    stub = types.ModuleType('CONFIG.config')
    stub.Config = type('Config', (), {'ADMIN_USERNAME': '@example'})
    return stub


def _iter_message_dicts():
    """Yield (lang_code, dict) for every locale the router can load."""
    from CONFIG.LANGUAGES.language_router import LanguageRouter
    router = LanguageRouter()
    for code in router.available_languages:
        messages = router.load_messages(code)
        if isinstance(messages, dict):
            yield code, messages
        else:
            yield code, {k: getattr(messages, k) for k in dir(messages)
                         if k.isupper() and isinstance(getattr(messages, k), str)}


class NonAsciiPlaceholderTests(unittest.TestCase):
    def setUp(self):
        self.config_patch = patch.dict(sys.modules, {'CONFIG.config': _stub_config()})
        self.config_patch.start()
        self.addCleanup(self.config_patch.stop)

    def test_no_non_ascii_placeholder_keys(self):
        """Every {placeholder} key in every loaded message template must be
        ASCII; non-ASCII keys make .format(ascii_kw=...) raise KeyError."""
        bad = []
        checked = 0
        for lang, messages in _iter_message_dicts():
            for key, template in messages.items():
                if not isinstance(template, str):
                    continue
                checked += 1
                for m in PLACEHOLDER_RE.finditer(template):
                    ph = m.group(1)
                    if not ph.isascii():
                        bad.append(f'{lang}.{key}: {{{ph}}}')
        self.assertGreater(checked, 5000, 'message tables did not load (checked=%d)' % checked)
        self.assertEqual(bad, [], 'non-ASCII placeholder keys found: ' + '; '.join(bad[:40]))

    def test_proxy_country_selected_msg_formats(self):
        """The exact production call from COMMANDS/proxy_cmd.py:
        PROXY_COUNTRY_SELECTED_MSG.format(country=..., country_code=...) must
        not raise for ANY language."""
        langs = 0
        for lang, messages in _iter_message_dicts():
            template = messages.get('PROXY_COUNTRY_SELECTED_MSG')
            if template is None:
                continue
            langs += 1
            with self.subTest(language=lang):
                try:
                    template.format(country='Australia', country_code='AU')
                except KeyError as exc:
                    self.fail(f'{lang}: KeyError {exc}: {template!r}')
        self.assertGreater(langs, 20, 'PROXY_COUNTRY_SELECTED_MSG not found in loaded locales')


if __name__ == '__main__':
    unittest.main()
