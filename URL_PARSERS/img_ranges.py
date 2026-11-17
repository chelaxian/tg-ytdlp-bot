"""Parsing and planning inclusive /img ranges in playlist order."""
import re


def parse_img_range(text):
    match = re.fullmatch(r'(-?\d+)-(-?\d*)', text)
    if not match:
        return None
    start = int(match.group(1))
    end = int(match.group(2)) if match.group(2) else None
    if start < 0 and end is not None and end > 0:
        end = -end
    if start == 0 or end == 0 or (start > 0 and end is not None and end < 0):
        return None
    return start, end


def plan_img_range(start, end, total, limit):
    if start < 0 or (end is not None and end < 0):
        reverse_tail = start < -1 and end == -1
        if not total or total < 1:
            raise ValueError('Cannot resolve negative image indices without a gallery count')
        if end is None:
            end = -total
        start = total + start + 1 if start < 0 else start
        end = total + end + 1 if end < 0 else end
        if start < 1 and end < 1:
            raise ValueError('Image range is outside the gallery')
        start, end = max(1, start), max(1, end)
        if reverse_tail:
            start, end = end, start
    if end is None:
        return start, None, False
    reverse = start > end
    if limit:
        end = max(end, start - limit + 1) if reverse else min(end, start + limit - 1)
    return start, end, reverse
