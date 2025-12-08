#!/usr/bin/env bash

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

find "$BASE_DIR" -type f | while IFS= read -r FILE; do
    # Skip binary files
    if ! grep -Iq . "$FILE"; then
        continue
    fi

    # Read file content safely (only text, trim)
    CONTENT="$(sed 's/[[:space:]]//g' "$FILE")"

    if [ "$CONTENT" = "REDACTED" ]; then
        echo "Удаляю: $FILE"
        rm -f "$FILE"
    fi
done
