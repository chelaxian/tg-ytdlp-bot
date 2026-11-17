"""Exercise the real /img loop's range gate and empty-search termination offline."""
import ast
from pathlib import Path
from typing import Any


SOURCE = Path(__file__).resolve().parent / 'COMMANDS' / 'image_cmd.py'


def run_ranges(ranges, cap):
    tree = ast.parse(SOURCE.read_text(encoding='utf-8'))
    loop = next(n for n in ast.walk(tree) if isinstance(n, ast.While)
                and any(isinstance(x, ast.If) and 'photos_videos_buffer' in ast.unparse(x.test)
                        for x in n.body))
    gate = next(x.test for x in loop.body if isinstance(x, ast.If)
                and 'photos_videos_buffer' in ast.unparse(x.test))
    empty_check = next(x for x in loop.body if isinstance(x, ast.If)
                       and ast.unparse(x.test) == 'files_found_in_this_search == 0')
    # Use production conditions and termination statements; fake I/O keeps the
    # complete run deterministic, including paths reused in later ranges.
    gate_code = compile(ast.Expression(gate), str(SOURCE), 'eval')
    wrapper = ast.Module(body=[ast.While(test=ast.Constant(True), body=[empty_check, ast.Break()], orelse=[])], type_ignores=[])
    empty_code = compile(ast.fix_missing_locations(wrapper), str(SOURCE), 'exec')
    class Logger:
        def info(self, *_): pass
    env: dict[str, Any] = dict(photos_videos_buffer=[], batch_size=10, files_found_in_this_search=0,
               consecutive_empty_searches=0, max_consecutive_empty_searches=3, logger=Logger())
    seen, sent, calls = set(), [], []
    start = 1
    for _ in range(30):
        if not eval(gate_code, env):
            # This is the original bug: no new request while partial buffer exists.
            found = []
        elif start > cap:
            break
        else:
            calls.append(start)
            found = ranges.get(start, [])
            start += 10
        fresh = [p for p in found if p not in seen]
        seen.update(fresh)
        env['photos_videos_buffer'].extend(fresh)
        while len(env['photos_videos_buffer']) >= 10:
            sent.extend(env['photos_videos_buffer'][:10])
            del env['photos_videos_buffer'][:10]
        env['files_found_in_this_search'] = len(fresh)
        exec(empty_code, env)
        if env['consecutive_empty_searches'] >= 3:
            break
    sent.extend(env['photos_videos_buffer'])
    return calls, sent


def test_partial_album_advances_and_flushes_without_duplicates():
    first = [f'{i}.jpg' for i in range(9)]
    calls, sent = run_ranges({1: first, 11: [first[0], 'new.jpg'], 21: ['last.jpg']}, 21)
    assert calls == [1, 11, 21]
    assert sent == first + ['new.jpg', 'last.jpg']


def test_three_empty_ranges_stop_even_with_partial_buffer():
    calls, sent = run_ranges({1: ['one.jpg']}, 100)
    assert calls == [1, 11, 21, 31]
    assert sent == ['one.jpg']
