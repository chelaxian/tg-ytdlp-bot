#!/usr/bin/env python3
"""Запуск изолированных проверок без сети, Firebase и Telegram-сессии.

Каждый smoke-скрипт запускается отдельно: его заглушки sys.modules не должны
попадать в другие тесты. Для проверок изображений нужен Pillow.
"""
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    commands = [('unittest', [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'])]
    for script in sorted((root / 'tests' / 'smoke').glob('test_*.py')):
        args = [] if script.name.startswith('test_a2_') else [str(root)]
        commands.append((script.name, [sys.executable, str(script), *args]))
    failures = 0
    for name, command in commands:
        try:
            result = subprocess.run(command, cwd=root, capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', timeout=120)
        except subprocess.TimeoutExpired:
            print(f'FAIL {name}: timeout')
            failures += 1
            continue
        if result.returncode:
            failures += 1
            print(f'FAIL {name} (exit {result.returncode})')
            print(result.stdout)
            print(result.stderr)
        else:
            print(f'PASS {name}')
    print(f'{len(commands) - failures}/{len(commands)} suites passed')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
