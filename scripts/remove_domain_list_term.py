#!/usr/bin/env python3
"""
Remove a single term from a list in CONFIG/domains.py.
Safe to run over SSH on each server (IT, FR, UK, UAE).

Usage (from repo root):
  python3 scripts/remove_domain_list_term.py WHITE_KEYWORDS pinterest.com
  python3 scripts/remove_domain_list_term.py WHITE_KEYWORDS "pinterest.com" --no-backup

Fixes the remote script SyntaxError: "if fWHITE_KEYWORDS" -> proper list edit without
generating inline Python (this script is the correct way to remove a term).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    do_backup = "--no-backup" not in sys.argv

    if len(args) < 2:
        print("Usage: python3 scripts/remove_domain_list_term.py <LIST_NAME> <TERM> [--no-backup]", file=sys.stderr)
        return 1

    list_name = args[0]
    term = args[1].strip()
    if not term:
        print("Error: term is empty", file=sys.stderr)
        return 1

    base = Path(__file__).resolve().parent.parent
    domains_path = base / "CONFIG" / "domains.py"
    if not domains_path.exists():
        print(f"Error: {domains_path} not found", file=sys.stderr)
        return 1

    try:
        content = domains_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {domains_path}: {e}", file=sys.stderr)
        return 1

    # Create backup
    if do_backup:
        from datetime import datetime
        backup_path = domains_path.parent / f"domains.py.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        try:
            backup_path.write_text(content, encoding="utf-8")
            print(f"Backup: {backup_path}")
        except Exception as e:
            print(f"Failed to create backup: {e}", file=sys.stderr)
            return 1

    # Find list block: LIST_NAME = [ ... ]
    escaped_name = re.escape(list_name)
    match = re.search(rf'^(\s*){escaped_name}\s*=\s*\[', content, re.MULTILINE)
    if not match:
        print(f"Error: list '{list_name}' not found in {domains_path}", file=sys.stderr)
        return 1

    indent = match.group(1)
    start = match.start()
    bracket_count = 0
    found_open = False
    end = -1
    for i, char in enumerate(content[start:], start=start):
        if char == "[":
            bracket_count += 1
            found_open = True
        elif char == "]":
            bracket_count -= 1
            if found_open and bracket_count == 0:
                end = i
                break
    if end == -1:
        print("Error: could not find end of list", file=sys.stderr)
        return 1

    list_block = content[start:end + 1]
    # Extract all quoted strings from the list block (handles 'x', "y", and inline comments)
    items = re.findall(r"['\"]([^'\"]*)['\"]", list_block)
    # Remove duplicates preserving order
    seen = set()
    unique = []
    for x in items:
        x = x.strip()
        if x and x not in seen:
            seen.add(x)
            unique.append(x)

    term_lower = term.lower()
    new_items = [x for x in unique if x.lower() != term_lower]
    if len(new_items) == len(unique):
        print(f"Term '{term}' not in list '{list_name}' (no change)")
        return 0

    # Rebuild list block
    new_lines = [f"{indent}{list_name} = [\n"]
    for item in new_items:
        # Escape backslash and quote for Python string
        escaped = item.replace("\\", "\\\\").replace('"', '\\"')
        new_lines.append(f'{indent}    "{escaped}",\n')
    new_lines.append(f"{indent}]\n")

    new_content = content[:start] + "".join(new_lines) + content[end + 1:]
    try:
        domains_path.write_text(new_content, encoding="utf-8")
    except Exception as e:
        print(f"Error writing {domains_path}: {e}", file=sys.stderr)
        return 1

    print(f"Removed '{term}' from {list_name}. {len(unique) - len(new_items)} term(s) removed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
