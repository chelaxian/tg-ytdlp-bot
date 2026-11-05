import ast
import os
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image
from HELPERS.telegram_photo import prepare_photo, retry_invalid_photo_upload
from types import SimpleNamespace


class PhotoPreparationTests(unittest.TestCase):
    def test_dimensions_ratio_and_original(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = os.path.join(tmp, 'wide.png')
            Image.new('RGB', (11000, 100), 'red').save(original)
            with open(original, 'rb') as f:
                before = f.read()
            result = prepare_photo(original)
            self.assertIsNotNone(result)
            try:
                with Image.open(result) as image:
                    self.assertEqual(image.format, 'JPEG')
                    self.assertLessEqual(sum(image.size), 10000)
                    self.assertLessEqual(max(image.size) / min(image.size), 20)
                with open(original, 'rb') as f:
                    self.assertEqual(f.read(), before)
            finally:
                os.unlink(result)

    def test_transparency_and_byte_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = os.path.join(tmp, 'alpha.png')
            Image.new('RGBA', (500, 500), (0, 0, 0, 0)).save(original)
            result = prepare_photo(original, max_bytes=10000)
            self.assertIsNotNone(result)
            try:
                self.assertLessEqual(os.path.getsize(result), 10000)
                with Image.open(result) as image:
                    self.assertEqual(image.convert('RGB').getpixel((0, 0)), (255, 255, 255))
            finally:
                os.unlink(result)

    def test_invalid_and_animated_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            broken = os.path.join(tmp, 'bad.jpg')
            with open(broken, 'wb') as f:
                f.write(b'not a photo')
            self.assertIsNone(prepare_photo(broken))
            animated = os.path.join(tmp, 'animation.gif')
            frames = [Image.new('RGB', (10, 10), c) for c in ('red', 'blue')]
            frames[0].save(animated, save_all=True, append_images=frames[1:], duration=100)
            self.assertIsNone(prepare_photo(animated))

    def test_failure_cleans_temporary_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = os.path.join(tmp, 'input.png')
            Image.new('RGB', (100, 100)).save(original)
            with patch('HELPERS.telegram_photo.tempfile.tempdir', tmp):
                self.assertIsNone(prepare_photo(original, max_bytes=1))
            self.assertEqual(os.listdir(tmp), ['input.png'])


class RetryTests(unittest.TestCase):
    def test_only_definite_photo_rejection_is_retried(self):
        photo = SimpleNamespace(media='photo.png', kind='photo')
        video = SimpleNamespace(media='video.mp4', kind='video')
        calls, cleaned = [], []
        def send():
            calls.append((photo.media, video.media))
            if len(calls) == 1:
                raise ValueError('invalid photo')
            return 'album sent'
        result = retry_invalid_photo_upload(
            send, [photo, video], lambda x: x.kind == 'photo',
            lambda e: str(e) == 'invalid photo', lambda p: p + '.jpg', cleaned)
        self.assertEqual(result, 'album sent')
        self.assertEqual(calls, [('photo.png', 'video.mp4'), ('photo.png.jpg', 'video.mp4')])
        self.assertEqual(cleaned, ['photo.png.jpg'])

    def test_ambiguous_error_does_not_retry(self):
        calls = []
        def send():
            calls.append(1)
            raise TimeoutError('unknown delivery state')
        with self.assertRaises(TimeoutError):
            retry_invalid_photo_upload(send, [SimpleNamespace(media='a')], lambda _: True,
                                       lambda _: False, lambda _: 'copy', [])
        self.assertEqual(calls, [1])

    def test_conversion_failure_does_not_retry(self):
        calls = []
        def send():
            calls.append(1)
            raise ValueError('invalid photo')
        with self.assertRaises(ValueError):
            retry_invalid_photo_upload(send, [SimpleNamespace(media='a')], lambda _: True,
                                       lambda _: True, lambda _: None, [])
        self.assertEqual(calls, [1])


class AlbumFallbackTests(unittest.TestCase):
    def setUp(self):
        # Load the real isolated functions without starting the Telegram bot.
        class BadRequest(Exception):
            pass
        class Photo:
            def __init__(self, media, caption=None):
                self.media, self.caption, self.has_spoiler = media, caption, True
        self.BadRequest, self.Photo = BadRequest, Photo
        filename = os.path.join(os.path.dirname(__file__), 'COMMANDS', 'image_cmd.py')
        with open(filename, encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename)
        names = {'_is_invalid_photo_rpc_error', '_send_rejected_album_in_parts', '_PartialAlbumSendError'}
        functions = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names]
        env = {'BadRequest': BadRequest, 'InputMediaPhoto': Photo,
               'TG_INVALID_PHOTO_ERROR_IDS': ('PHOTO_INVALID',),
               'ReplyParameters': lambda **kw: kw, 'get_reply_message_id': lambda _: 9,
               'timed_upload': lambda operation: operation()}
        exec(compile(ast.fix_missing_locations(ast.Module(body=functions, type_ignores=[])), filename, 'exec'), env)
        self.fallback = env['_send_rejected_album_in_parts']
        self.PartialError = env['_PartialAlbumSendError']

    def test_only_bad_photo_becomes_original_document(self):
        bad_request = self.BadRequest
        class App:
            def __init__(self):
                self.delivered = []
            def send_media_group(self, chat, media, **kw):
                if any(x.media == 'bad' for x in media):
                    raise bad_request('PHOTO_INVALID')
                self.delivered.extend(('photo', x.media) for x in media)
                return [x.media for x in media]
            def send_photo(self, chat, photo, **kw):
                if photo == 'bad':
                    raise bad_request('PHOTO_INVALID')
                self.delivered.append(('photo', photo))
                return photo
            def send_document(self, chat, document, **kw):
                self.delivered.append(('document', document))
                return document
        app = App()
        items = [self.Photo('good1', 'caption'), self.Photo('good2'), self.Photo('bad'), self.Photo('good3')]
        result = self.fallback(app, 1, object(), items, ['o1', 'o2', 'original-bad', 'o3'], 5)
        self.assertEqual(result, ['good1', 'good2', 'original-bad', 'good3'])
        self.assertEqual(app.delivered, [('photo', 'good1'), ('photo', 'good2'),
                                         ('document', 'original-bad'), ('photo', 'good3')])

    def test_partial_delivery_is_reported_without_retry(self):
        class App:
            def send_media_group(self, chat, media, **kwargs):
                if media[0].media == 'a':
                    return ['a', 'b']
                raise TimeoutError('unknown delivery state')
        with self.assertRaises(self.PartialError) as caught:
            self.fallback(App(), 1, object(), [self.Photo(x) for x in 'abcd'], list('abcd'))
        self.assertEqual(caught.exception.sent, ['a', 'b'])
        self.assertIsInstance(caught.exception.__cause__, TimeoutError)

    def test_other_error_is_not_split(self):
        class App:
            def send_media_group(self, *args, **kwargs):
                raise TimeoutError('delivery unknown')
        with self.assertRaises(TimeoutError):
            self.fallback(App(), 1, object(), [self.Photo(x) for x in 'abcd'], list('abcd'))


if __name__ == '__main__':
    unittest.main()
