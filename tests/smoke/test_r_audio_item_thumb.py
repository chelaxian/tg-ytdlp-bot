"""Smoke test: /audio playlist items get their own cover, not a neighbour's (offline).

down_and_audio.find_item_thumbnail is extracted with ast, so the bot's runtime
(pyrogram app, config) is not needed.
Run: python tests/smoke/test_r_audio_item_thumb.py
"""
import ast
import os
import re
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = os.path.join(ROOT, "DOWN_AND_UP", "down_and_audio.py")

tree = ast.parse(open(SRC, encoding="utf-8").read())
wanted = []
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name == "find_item_thumbnail":
        wanted.append(node)
    elif isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id in ("_THUMB_EXTS", "_THUMB_ID_RE") for t in node.targets):
        wanted.append(node)
ns = {"os": os, "re": re}
exec(compile(ast.Module(body=wanted, type_ignores=[]), SRC, "exec"), ns)
find_item_thumbnail = ns["find_item_thumbnail"]

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


def touch(folder, name, data=b"x"):
    with open(os.path.join(folder, name), "wb") as f:
        f.write(data)


with tempfile.TemporaryDirectory() as d:
    # the folder as seen on DE: covers of earlier items + our telegram thumbs
    for name in ("Meditation Being Fully Yourself - Ep 79.webp", "Meditation Being Fully Yourself - Ep 79.mp3",
                 "telegram_thumb_0.jpg", "telegram_thumb_1.jpg", "yt_thumb_abc.jpg", "universal_thumb.jpg",
                 "Breathing from the Center.mp3", "Transforming Belief. 83, #Lion Goodman.mp3",
                 "Transforming Belief. 83, #Lion Goodman.jpg", "Ep.mp3", "Ep. 2 longer title.jpg",
                 "Multi.mp3", "Multi.maxresdefault.jpg"):
        touch(d, name)
    touch(d, "Empty.mp3")
    touch(d, "Empty.jpg", b"")

    got = find_item_thumbnail(d, os.path.join(d, "Breathing from the Center.mp3"))
    check("no own cover -> None (not a neighbour's / telegram_thumb)", got is None)
    got = find_item_thumbnail(d, os.path.join(d, "Meditation Being Fully Yourself - Ep 79.mp3"))
    check("own .webp cover", got and got.endswith("Meditation Being Fully Yourself - Ep 79.webp"))
    got = find_item_thumbnail(d, os.path.join(d, "Transforming Belief. 83, #Lion Goodman.mp3"))
    check("dots in title", got and got.endswith("Transforming Belief. 83, #Lion Goodman.jpg"))
    got = find_item_thumbnail(d, os.path.join(d, "Ep.mp3"))
    check("longer title with same prefix is not taken", got is None)
    got = find_item_thumbnail(d, os.path.join(d, "Multi.mp3"))
    check("<stem>.<thumb id>.jpg", got and got.endswith("Multi.maxresdefault.jpg"))
    got = find_item_thumbnail(d, os.path.join(d, "Empty.mp3"))
    check("empty thumbnail ignored", got is None)
    check("missing folder -> None", find_item_thumbnail(os.path.join(d, "nope"), "a.mp3") is None)

print(f"\n{ok} passed, {fail} failed")
sys.exit(1 if fail else 0)
