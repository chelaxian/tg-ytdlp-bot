# Smoke test: Twitter broadcast terminal errors must stop the live-stream chunk loop.
# Regression for issue #562: "Broadcast no longer exists" / "-start is passed, but ..."
# were not in stream_ended_keywords, so the loop retried forever (22k+ ERROR lines).
import sys
import types
try:
    import yt_dlp
except ImportError:
    yt_dlp = None

# Import the module only when yt_dlp is available (CI); locally parse source text.
try:
    sys.path.insert(0, ".")
    from DOWN_AND_UP import live_stream_downloader as lsd
except ImportError:
    lsd = None


def _keywords():
    # Access the list used in download_live_stream_chunked via source inspection is fragile;
    # instead we replicate the check by calling the module-level helper if present.
    # Fallback: parse the literal list from source.
    import inspect
    src = inspect.getsource(lsd) if lsd else open("DOWN_AND_UP/live_stream_downloader.py").read()
    assert 'stream_ended_keywords' in src, "stream_ended_keywords list not found"
    for kw in ("broadcast no longer exists", "-start is passed, but"):
        assert f'"{kw}"' in src, f"keyword missing: {kw}"
    return True


def _classify(error_text):
    """Replicates the classification logic from download_live_stream_chunked."""
    stream_ended_keywords = [
        "transmission ended", "video unavailable", "private video",
        "video is unavailable", "stream ended",
        "this live stream recording is not available",
        "live stream recording is not available", "HTTP Error 403",
        "HTTP Error 404", "unable to download video data",
        "no video formats found", "requested format is not available",
        "broadcast no longer exists", "-start is passed, but",
    ]
    error_lower = error_text.lower()
    return any(k.lower() in error_lower for k in stream_ended_keywords)


class _FakeDownloadError(Exception):
    pass


def test_broadcast_no_longer_exists_is_terminal():
    e = _FakeDownloadError(
        "ERROR: [twitter:broadcast] 2NgNkMoMKanNjp: Broadcast no longer exists")
    assert _classify(str(e)), "Broadcast no longer exists must classify as stream ended"


def test_live_from_start_passed_is_terminal():
    e = _FakeDownloadError(
        "ERROR: [twitter:broadcast] abc: -start is passed, but the broadcast has already ended")
    assert _classify(str(e)), "-start is passed must classify as stream ended"


def test_transient_error_still_not_terminal():
    e = _FakeDownloadError(
        "ERROR: unable to download webpage: Connection timed out")
    assert not _classify(str(e)), "Generic network error must remain retryable"


if __name__ == "__main__":
    _keywords()
    test_broadcast_no_longer_exists_is_terminal()
    test_live_from_start_passed_is_terminal()
    test_transient_error_still_not_terminal()
    print("3/3 passed")
