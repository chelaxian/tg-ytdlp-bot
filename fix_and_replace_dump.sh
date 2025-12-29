#!/bin/bash
# Скрипт для исправления проблемных путей и замены dump.json во всей истории Git
# ⚠️ ВНИМАНИЕ: Это перепишет историю Git и потребует force push!

set -e

echo "========================================"
echo "ИСПРАВЛЕНИЕ ПУТЕЙ И ЗАМЕНА dump.json"
echo "========================================"
echo ""

# Проверяем наличие dump.json
if [ ! -f "dump.json" ]; then
    echo "❌ Файл dump.json не найден в рабочей директории!"
    exit 1
fi

echo "⚠️  ВАЖНО:"
echo "   - Это перепишет всю историю Git"
echo "   - Исправит проблемные пути с пробелами"
echo "   - Заменит содержимое dump.json на заглушку во ВСЕХ коммитах"
echo "   - Потребуется force push"
echo ""

read -p "Вы уверены, что хотите продолжить? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "Отменено."
    exit 0
fi

echo ""
echo "Шаг 0: Проверка рабочей директории..."
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Обнаружены незакоммиченные изменения:"
    git status --short
    echo ""
    read -p "Что делать? (commit/stash/discard/abort): " handleChanges
    case "$handleChanges" in
        commit)
            git add -A
            read -p "Введите сообщение коммита: " commitMsg
            [ -z "$commitMsg" ] && commitMsg="Temporary commit before history rewrite"
            git commit -m "$commitMsg"
            ;;
        stash)
            git stash push -m "Stashed before history rewrite"
            ;;
        discard)
            read -p "Вы уверены? (yes/no): " confirmDiscard
            [ "$confirmDiscard" = "yes" ] && git restore . && git clean -fd || exit 0
            ;;
        *)
            exit 0
            ;;
    esac
fi

echo ""
echo "Шаг 1: Создание резервной копии..."
BACKUP_PATH="../tg-ytdlp-NEW-backup-$(date +%Y%m%d_%H%M%S)"
git clone --mirror . "$BACKUP_PATH"
echo "✅ Резервная копия создана: $BACKUP_PATH"
echo ""

echo "Шаг 2: Подготовка заглушки dump.json..."
STUB_FILE=$(mktemp)
cp dump.json "$STUB_FILE"
STUB_CONTENT=$(cat "$STUB_FILE")
echo "✅ Заглушка подготовлена"
echo ""

echo "Шаг 3: Создание скрипта замены..."
REPLACE_SCRIPT=$(mktemp)
cat > "$REPLACE_SCRIPT" << PYTHON_SCRIPT
import sys
import os
import json

# Читаем заглушку
stub_file = r"$STUB_FILE"
with open(stub_file, 'r', encoding='utf-8') as f:
    stub_content = f.read()

# Исправляем проблемные пути с пробелами
# Удаляем файлы с пробелами в путях (они некорректны)
problem_paths = [
    'etc/systemd/system /tg-ytdlp-bot.service',
    'etc/systemd/system /tg-ytdlp-dashboard.service',
]

for path in problem_paths:
    if os.path.exists(path):
        os.remove(path)

# Заменяем dump.json если он существует
if os.path.exists('dump.json'):
    with open('dump.json', 'w', encoding='utf-8') as f:
        f.write(stub_content)
PYTHON_SCRIPT

chmod +x "$REPLACE_SCRIPT"
echo "✅ Скрипт замены создан"
echo ""

echo "Шаг 4: Выполнение замены (это может занять много времени)..."
export FILTER_BRANCH_SQUELCH_WARNING=1

FILTER_CMD="python3 \"$REPLACE_SCRIPT\" 2>/dev/null || python \"$REPLACE_SCRIPT\" 2>/dev/null"

git filter-branch --force --tree-filter "$FILTER_CMD" --prune-empty --tag-name-filter cat -- --all

FILTER_EXIT=$?
unset FILTER_BRANCH_SQUELCH_WARNING

if [ $FILTER_EXIT -ne 0 ]; then
    echo ""
    echo "❌ Ошибка при выполнении filter-branch!"
    rm -f "$STUB_FILE" "$REPLACE_SCRIPT"
    exit 1
fi

echo ""
echo "Шаг 5: Очистка..."
rm -f "$STUB_FILE" "$REPLACE_SCRIPT"
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin 2>/dev/null || true
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo ""
echo "Шаг 6: Проверка результата..."
SAMPLE_COMMIT=$(git log --all --oneline | head -1 | cut -d' ' -f1)
if git show "$SAMPLE_COMMIT":dump.json >/dev/null 2>&1; then
    SAMPLE_CONTENT=$(git show "$SAMPLE_COMMIT":dump.json | head -5)
    if echo "$SAMPLE_CONTENT" | grep -q '"0"'; then
        echo "✅ dump.json успешно заменен на заглушку!"
    else
        echo "⚠️  Проверьте содержимое вручную"
    fi
else
    echo "⚠️  dump.json не найден в коммите $SAMPLE_COMMIT"
fi

echo ""
echo "========================================"
echo "ОПЕРАЦИЯ ЗАВЕРШЕНА"
echo "========================================"
echo ""
echo "Резервная копия: $BACKUP_PATH"
echo ""
echo "Для применения изменений выполните:"
echo "  git push origin --force --all"
echo "  git push origin --force --tags"
echo ""

