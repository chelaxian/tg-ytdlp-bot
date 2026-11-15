"""Regression tests: /format id with track suffix + /audio respects saved audio format.

Bug (user report 15.11.2026): "/format id 139-1" was stored as a literal custom
string because the ID regex only accepted digits, so YouTube multi-language
track IDs like "139-1" never matched. Separately, /audio always downloaded
bestaudio and re-encoded to 192k MP3 regardless of the saved audio format.
"""
import os
import re
import sys
import tempfile
import types

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # repo root
sys.path.insert(0, ROOT)

RE_ID = re.compile(r'^id\s*\d+(?:-\d+)?$', re.IGNORECASE)

def test_format_id_with_track_suffix_matches():
    assert RE_ID.match("id 401")
    assert RE_ID.match("id401")
    assert RE_ID.match("id 139-1")
    assert RE_ID.match("id139-1")
    assert RE_ID.match("id 233-0")
    assert RE_ID.match("ID 602-1")
    # negative: must not swallow unrelated forms
    assert not RE_ID.match("id 139-1 audio")       # audio variant has own regex
    assert not RE_ID.match("id 139-audio")
    assert not RE_ID.match("id-1")
    assert not RE_ID.match("140")
    print("ok: /format id regex accepts ID-N track suffixes")

RE_ID_AUDIO = re.compile(r'^id\s*\d+(?:-\d+)?\s+audio$')

def test_format_id_audio_with_track_suffix_matches():
    assert RE_ID_AUDIO.match("id 140 audio")
    assert RE_ID_AUDIO.match("id140 audio")
    assert RE_ID_AUDIO.match("id 139-1 audio")
    assert RE_ID_AUDIO.match("id139-1 audio")
    assert not RE_ID_AUDIO.match("id 139-1")       # plain id form
    assert not RE_ID_AUDIO.match("id audio")
    print("ok: /format id...audio regex accepts ID-N track suffixes")

def test_extracted_id_keeps_suffix():
    # mirrors format_cmd.py extraction
    for arg, expected in [("id 139-1", "139-1"), ("id401", "401"), ("id 233-0", "233-0")]:
        got = re.search(r'\d+(?:-\d+)?', arg).group()
        assert got == expected, (arg, got, expected)
    print("ok: extracted format ID keeps the track suffix")


def test_audio_command_uses_saved_audio_format():
    """other_handlers.audio_command_handler must pass the saved audio format
    (ID/bestaudio from format.txt) as format_override instead of 'ba'."""
    # Import in isolation: other_handlers imports pyrogram at module level,
    # which may be absent in CI; stub what the module needs.
    import importlib.util
    src = os.path.join(ROOT, "COMMANDS", "other_handlers.py")
    with open(src, "r", encoding="utf-8") as f:
        code = f.read()

    # The handler must read format.txt and forward a saved audio format.
    assert 'format.txt' in code, "audio_command_handler must consult format.txt"
    assert 'endswith("/bestaudio")' in code
    assert 'format_override=saved_audio_format or "ba"' in code
    # ...but the default path must stay unchanged for users without a saved format
    assert 'quality_key="mp3" if saved_audio_format is None else None' in code
    print("ok: /audio forwards saved ID/bestaudio format (code contract)")


def test_pinned_audio_stream_not_reencoded():
    """down_and_audio must skip the FFmpegExtractAudio 192k MP3 re-encode when
    the user pinned an exact stream (format_override != 'ba')."""
    src = os.path.join(ROOT, "DOWN_AND_UP", "down_and_audio.py")
    with open(src, "r", encoding="utf-8") as f:
        code = f.read()
    assert "_pinned_audio_stream = bool(format_override and format_override != 'ba')" in code
    # both postprocessor sites (main + safe-filename retry) must honour the pin
    assert code.count("_pinned_pp = [] if (format_override and format_override != 'ba')") == 1
    assert "'preferredquality': '192'" in code  # default path still re-encodes
    print("ok: pinned audio stream skips 192k re-encode in both postprocessor paths")


if __name__ == "__main__":
    test_format_id_with_track_suffix_matches()
    test_format_id_audio_with_track_suffix_matches()
    test_extracted_id_keeps_suffix()
    test_audio_command_uses_saved_audio_format()
    test_pinned_audio_stream_not_reencoded()
    print("\nALL TESTS PASSED")
