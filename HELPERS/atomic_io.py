"""Dependency-free atomic file writes (temp file in the same directory + os.replace).

A reader never observes a half-written file, and a failed write (disk quota
exceeded / ENOSPC, Errno 122 on DE - issues #316, #460, #478, or a value that
json cannot serialize mid-dump) leaves the previous file untouched instead of
a truncated one ("Expecting value: line 37 column 22").

Kept free of bot imports (no Pyrogram/app/logger) so that standalone scripts
such as DATABASE/download_firebase.py can use it too.
"""
import json
import os
import tempfile


def _replace_with_tmp(file_path, write_fn, mode):
    directory = os.path.dirname(os.path.abspath(file_path))
    os.makedirs(directory, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        dir=directory, prefix=f".{os.path.basename(file_path)}.", suffix=".tmp"
    )
    try:
        if 'b' in mode:
            fh = os.fdopen(fd, mode)
        else:
            fh = os.fdopen(fd, mode, encoding='utf-8')
        with fh:
            write_fn(fh)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_path, file_path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise


def atomic_write_bytes(file_path, data):
    """Atomically replace file_path with the given bytes."""
    _replace_with_tmp(file_path, lambda fh: fh.write(data), 'wb')


def atomic_write_text(file_path, text):
    """Atomically replace file_path with the given text (UTF-8)."""
    _replace_with_tmp(file_path, lambda fh: fh.write(text), 'w')


def atomic_write_json(file_path, data, **dump_kwargs):
    """Atomically write JSON. The payload is serialized in memory first, so a
    TypeError on a non-serializable value never touches the target file."""
    dump_kwargs.setdefault('ensure_ascii', False)
    text = json.dumps(data, **dump_kwargs)
    atomic_write_text(file_path, text)
