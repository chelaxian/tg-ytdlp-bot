"""Смоук-тесты локалей с синтетическим Config, без секретов и сети."""
from concurrent.futures import ThreadPoolExecutor
import sys
import types
import unittest
from unittest.mock import patch

from CONFIG.LANGUAGES.language_router import LanguageRouter


class LanguageLoadingTests(unittest.TestCase):
    def setUp(self):
        stub = types.ModuleType('CONFIG.config')
        stub.Config = type('Config', (), {'ADMIN_USERNAME': '@example'})
        self.config_patch = patch.dict(sys.modules, {'CONFIG.config': stub})
        self.config_patch.start()
        self.addCleanup(self.config_patch.stop)

    def test_all_declared_locales_load(self):
        router = LanguageRouter()
        for code in router.available_languages:
            with self.subTest(language=code):
                self.assertGreater(len(router.load_messages(code)), 1000)

    def test_concurrent_farsi_load(self):
        router = LanguageRouter()
        with ThreadPoolExecutor(max_workers=30) as pool:
            results = list(pool.map(lambda _: router.load_messages('fa'), range(60)))
        self.assertTrue(all(len(messages) > 1000 for messages in results))
        self.assertTrue(all(messages is results[0] for messages in results))

    def test_missing_key_falls_back_to_english(self):
        from CONFIG.messages import Messages
        messages = Messages(None, 'fa')
        messages._messages = {'LOCAL_KEY': 'local'}
        english = {'NEW_KEY': 'English text'}
        with patch('CONFIG.messages.get_messages', return_value=english):
            self.assertEqual(messages.LOCAL_KEY, 'local')
            self.assertEqual(messages.NEW_KEY, 'English text')
            self.assertEqual(messages.UNKNOWN_KEY, '[UNKNOWN_KEY]')


if __name__ == '__main__':
    unittest.main()
