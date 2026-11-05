"""Smoke test: cover fallback takes a representative frame from the middle (needs ffmpeg + Pillow).

Run: python tests/smoke/test_w_frame_grab.py
"""
import ast
import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

from HELPERS import frame_grab as fg  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


def make_video(path, vf_parts, size="640x360", dur=10):
    """Video built from lavfi segments joined by concat (black / test pattern)."""
    inputs, labels = [], []
    for i, (kind, secs) in enumerate(vf_parts):
        src = f"color=c=black:s={size}:d={secs}" if kind == "black" else f"testsrc2=s={size}:d={secs}"
        inputs += ["-f", "lavfi", "-i", src + ":r=25" if kind == "black" else src + ":r=25"]
        labels.append(f"[{i}:v]")
    fc = "".join(labels) + f"concat=n={len(vf_parts)}:v=1:a=0[v]"
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", fc, "-map", "[v]",
                        "-pix_fmt", "yuv420p", path], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def dims(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height", "-of", "csv=s=x:p=0", path], capture_output=True, text=True)
    w, h = r.stdout.strip().split("x")
    return int(w), int(h)


# ---- pure helpers ----
t = fg.frame_times(100)
check("frame_times starts in the middle", t[0] == 50.0)
check("frame_times has fallbacks, all inside the video", len(t) > 3 and all(0 <= x <= 99 for x in t))
check("frame_times unknown duration", fg.frame_times(0) == [1.0, 0.0] and fg.frame_times(None) == [1.0, 0.0])
check("frame_times tiny video", fg.frame_times(2) == [1.0, 0.0])
check("frame_times float duration", fg.frame_times(61.4)[0] == 30.7)

# _thumb_box from ffmpeg.py (heavy imports, so extracted with ast)
src = open(os.path.join(ROOT, "DOWN_AND_UP", "ffmpeg.py"), encoding="utf-8").read()
node = next(n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == "_thumb_box")
ns = {}
exec(compile(ast.Module([node], []), "ffmpeg.py", "exec"), ns)
box = ns["_thumb_box"]
check("thumb box 16:9 keeps ratio (not stretched to 240)", box(1920, 1080) == (320, 180))
check("thumb box portrait", box(1080, 1920) == (180, 320))
check("thumb box square", box(500, 500) == (320, 320))
check("thumb box even sides", all(v % 2 == 0 for v in box(853, 480) + box(480, 853)))
check("thumb box bad input does not raise", box(0, 0) == (320, 180) or box(None, None) == (320, 180))

# ---- real ffmpeg ----
with tempfile.TemporaryDirectory() as d:
    # 1) normal video: middle frame, aspect ratio kept, JPEG < 200 KB
    v1 = os.path.join(d, "normal.mp4")
    make_video(v1, [("pattern", 10)])
    o1 = os.path.join(d, "normal.jpg")
    check("grab ok", fg.grab_representative_frame(v1, 10, o1))
    check("is JPEG", open(o1, "rb").read(3) == b"\xff\xd8\xff")
    check("640x360 -> 320x180", dims(o1) == (320, 180))
    check("under 200 KB", os.path.getsize(o1) < 200 * 1024)
    check("frame is informative", fg.is_informative(fg.frame_stats(o1)))

    # 2) black screen exactly in the middle: another position is used
    v2 = os.path.join(d, "blackmid.mp4")
    make_video(v2, [("pattern", 3), ("black", 4), ("pattern", 3)])
    o2 = os.path.join(d, "blackmid.jpg")
    check("grab ok (black middle)", fg.grab_representative_frame(v2, 10, o2))
    check("black middle skipped", fg.is_informative(fg.frame_stats(o2)))

    # 3) black intro + titles at the start: the cover is not the first frame
    v3 = os.path.join(d, "intro.mp4")
    make_video(v3, [("black", 4), ("pattern", 6)])
    o3 = os.path.join(d, "intro.jpg")
    check("grab ok (black intro)", fg.grab_representative_frame(v3, 10, o3))
    check("intro skipped", fg.is_informative(fg.frame_stats(o3)))

    # 4) portrait video, never upscaled beyond the source
    v4 = os.path.join(d, "portrait.mp4")
    make_video(v4, [("pattern", 4)], size="180x320", dur=4)
    o4 = os.path.join(d, "portrait.jpg")
    check("grab ok (portrait)", fg.grab_representative_frame(v4, 4, o4))
    check("portrait 180x320 kept", dims(o4) == (180, 320))

    # 5) bigger cover for paid media: 1280 limit, ratio kept
    v5 = os.path.join(d, "hd.mp4")
    make_video(v5, [("pattern", 3)], size="1920x1080", dur=3)
    o5 = os.path.join(d, "hd.jpg")
    check("grab ok (1280)", fg.grab_representative_frame(v5, 3, o5, 1280, 1280))
    check("1920x1080 -> 1280x720", dims(o5) == (1280, 720))

    # 6) wrong duration (longer than the file) still yields a frame; leftovers cleaned
    o6 = os.path.join(d, "baddur.jpg")
    check("duration larger than file", fg.grab_representative_frame(v1, 500, o6))
    # 7) unreadable input does not raise
    check("missing file returns False", fg.grab_representative_frame(os.path.join(d, "nope.mp4"), 10,
                                                                      os.path.join(d, "x.jpg")) is False)
    leftovers = [n for n in os.listdir(d) if ".cand" in n]
    check("no temporary candidates left", not leftovers)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
