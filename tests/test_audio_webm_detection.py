"""Regression tests: audio-file detection misses .webm (pinned opus audio streams).

GROUP 1 defect (windows 24-26 Nov 2026, bot.log evidence):
When a user pins an audio stream in the Always Ask menu (askq|other_id|250-0 /
251-drc etc.), yt-dlp downloads an audio-only opus stream inside a .webm
container with format_override set, FFmpegExtractAudio is skipped
(_pinned_audio_stream=True), EmbedThumbnail raises "Supported filetypes for
thumbnail embedding are..." (cosmetic), and then DOWN_AND_UP.down_and_audio
finds NO audio file because .webm is in neither the standard nor the
additional audio-extension list. The user gets "unsupported file type" and the
downloaded file is discarded — a real user-visible data-loss defect.

The extension lists are parsed directly from the production source (no import
of down_and_audio: it pulls heavy runtime deps like yt_dlp).
"""
import re
import unittest

SRC_PATH = 'DOWN_AND_UP/down_and_audio.py'


def _audio_ext_lists():
    """Extract the standard+additional audio extension lists exactly as
    down_and_audio builds them in the 'if not files:' fallback branch."""
    with open(SRC_PATH, encoding='utf-8') as fh:
        src = fh.read()
    m_std = re.search(r"audio_extensions = (\[[^\]]*\])", src)
    m_add = re.search(r"additional_extensions = (\[[^\]]*\])", src)
    assert m_std and m_add, 'audio extension lists not found in down_and_audio.py'
    return eval(m_std.group(1)), eval(m_add.group(1))


class WebmAudioDetectionTests(unittest.TestCase):
    def test_webm_recognized_as_pinned_audio_container(self):
        """A .webm file produced by a pinned opus/opus-drc audio-only stream
        must be recognized by the audio-file fallback detection."""
        standard, additional = _audio_ext_lists()
        fname = "Miami 3і顺手.webm"  # typical sanitized yt-dlp output name
        recognized = any(fname.endswith(ext) for ext in standard) or \
            any(fname.endswith(ext) for ext in additional)
        self.assertTrue(recognized,
                        '.webm is in neither audio list: std=%r additional=%r' % (standard, additional))

    def test_weba_in_additional_list(self):
        """Guard: the additional list must still contain .weba (yt-dlp webm-audio alias)."""
        _, additional = _audio_ext_lists()
        self.assertIn('.weba', additional)


if __name__ == '__main__':
    unittest.main()
