"""Regression: /image download dir must survive signed CDN URLs.

CloudflareStream links look like
    https://customer-<hash>.cloudflarestream.com/<800-char-JWT>/manifest/video.m3u8
create_unique_download_path() takes the first path component (the JWT) as the
profile directory name. It is already \\w-safe but exceeds NAME_MAX (255 bytes),
so os.makedirs() fails with OSError [Errno 36] File name too long before any
download starts (2026-11-16, 5 failures, 2 users).

image_cmd.py imports pyrogram at module level, which is not installable in the
test environment; the check is therefore a source-level text/AST check of the
sanitizing code path, in the same style as tests/test_chanban_until_date.py.
"""
import ast
import os
import re

TARGET = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "COMMANDS",
    "image_cmd.py",
)

JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." + "a" * 300 + ".sIgNaTuRe-0123456789abcdef0123456789abcdef"


def _function_source(fn_name):
    with open(TARGET, encoding="utf-8") as f:
        text = f.read()
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == fn_name:
            seg = ast.get_source_segment(text, node)
            assert seg is not None
            return seg
    raise AssertionError(f"{fn_name} not found in {TARGET}")


def _sanitize_jwt(profile_name):
    """Reimplement the sanitizing steps of create_unique_download_path."""
    profile_name = re.sub(r"[^\w\-_.]", "_", profile_name)
    src = _function_source("create_unique_download_path")
    assert "encode('utf-8')" in src or 'encode("utf-8")' in src, (
        "byte-length cap missing: JWT profile names exceed NAME_MAX"
    )
    m = re.search(r"profile_name_bytes\[:(\d+)\]", src)
    assert m, "no byte-prefix truncation of profile_name found"
    budget = int(m.group(1))
    b = profile_name.encode("utf-8")
    if len(b) > budget:
        profile_name = b[:budget].decode("utf-8", errors="ignore")
    return profile_name


def test_image_path_component_short_for_jwt_url():
    # the JWT as the first path component must be capped below NAME_MAX (255)
    component = _sanitize_jwt(JWT)
    assert len(component.encode("utf-8")) <= 255, component
    assert len(component) > 0


def test_image_path_component_normal_names_untouched():
    component = _sanitize_jwt("someuser")
    assert component == "someuser"
