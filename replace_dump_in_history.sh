#!/bin/bash
# Скрипт для замены содержимого dump.json во всей истории Git на безопасную заглушку
# ⚠️ ВНИМАНИЕ: Это перепишет историю Git и потребует force push!

set -e

echo "========================================"
echo "ЗАМЕНА dump.json В ИСТОРИИ GIT"
echo "На безопасную заглушку"
echo "========================================"
echo ""

# Проверяем наличие dump.json
if [ ! -f "dump.json" ]; then
    echo "❌ Файл dump.json не найден в рабочей директории!"
    echo "   Убедитесь, что файл с заглушкой находится в корне проекта"
    exit 1
fi

echo "⚠️  ВАЖНО:"
echo "   - Это перепишет всю историю Git"
echo "   - Содержимое dump.json будет заменено на заглушку во ВСЕХ коммитах"
echo "   - Потребуется force push"
echo "   - Все, кто клонировал репозиторий, должны переклонировать"
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
            echo "Коммитим изменения..."
            git add -A
            read -p "Введите сообщение коммита (или Enter для автоматического): " commitMsg
            if [ -z "$commitMsg" ]; then
                commitMsg="Temporary commit before history rewrite"
            fi
            git commit -m "$commitMsg"
            ;;
        stash)
            echo "Сохраняем изменения в stash..."
            git stash push -m "Stashed before history rewrite"
            ;;
        discard)
            echo "⚠️  Отменяем все незакоммиченные изменения..."
            read -p "Вы уверены? (yes/no): " confirmDiscard
            if [ "$confirmDiscard" = "yes" ]; then
                git restore .
                git clean -fd
                echo "✅ Изменения отменены"
            else
                echo "Отменено."
                exit 0
            fi
            ;;
        *)
            echo "Отменено."
            exit 0
            ;;
    esac
    echo ""
else
    echo "✅ Рабочая директория чиста"
    echo ""
fi

echo "Шаг 1: Создание резервной копии..."
BACKUP_PATH="../tg-ytdlp-NEW-backup-$(date +%Y%m%d_%H%M%S)"
echo "Копирование в: $BACKUP_PATH"
git clone --mirror . "$BACKUP_PATH"
if [ $? -ne 0 ]; then
    echo "❌ Ошибка при создании резервной копии!"
    exit 1
fi
echo "✅ Резервная копия создана"
echo ""

echo "Шаг 2: Создание временного файла с заглушкой..."
STUB_FILE=$(mktemp)
cp dump.json "$STUB_FILE"
echo "✅ Заглушка сохранена: $STUB_FILE"
echo ""

echo "Шаг 3: Замена dump.json во всей истории..."
echo "Это может занять некоторое время..."
echo ""

# Создаем скрипт для замены
REPLACE_SCRIPT=$(mktemp)
cat > "$REPLACE_SCRIPT" << PYTHON_SCRIPT
import sys
import os
import shutil

# Читаем заглушку
stub_file = r"$STUB_FILE"
if not os.path.exists(stub_file):
    sys.exit(1)

with open(stub_file, 'r', encoding='utf-8') as f:
    stub_content = f.read()

# Заменяем dump.json если он существует
if os.path.exists('dump.json'):
    with open('dump.json', 'w', encoding='utf-8') as f:
        f.write(stub_content)
PYTHON_SCRIPT

export FILTER_BRANCH_SQUELCH_WARNING=1

# Выполняем замену через git filter-branch
FILTER_CMD="python3 \"$REPLACE_SCRIPT\" 2>/dev/null || python \"$REPLACE_SCRIPT\" 2>/dev/null"

# Используем --index-filter вместо --tree-filter для лучшей производительности
# Но для замены содержимого нужен tree-filter
git filter-branch --force --tree-filter "$FILTER_CMD" --prune-empty --tag-name-filter cat -- --all

FILTER_EXIT_CODE=$?
unset FILTER_BRANCH_SQUELCH_WARNING
unset STUB_FILE

# Удаляем временные файлы
rm -f "$STUB_FILE" "$REPLACE_SCRIPT"

if [ $FILTER_EXIT_CODE -ne 0 ]; then
    echo ""
    echo "❌ Ошибка при выполнении filter-branch!"
    exit 1
fi

echo ""
echo "Шаг 4: Очистка резервных ссылок..."
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin || true
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo ""
echo "Шаг 5: Проверка результата..."
# Проверяем несколько коммитов
TEST_COMMITS=$(git log --all --oneline | head -5)
ALL_REPLACED=true
for commit in $TEST_COMMITS; do
    COMMIT_HASH=$(echo "$commit" | cut -d' ' -f1)
    CONTENT=$(git show "$COMMIT_HASH":dump.json 2>/dev/null || echo "")
    if [ -n "$CONTENT" ]; then
        if ! echo "$CONTENT" | grep -q '"0"'; then
            echo "⚠️  Коммит $COMMIT_HASH : содержимое может быть не заменено"
            ALL_REPLACED=false
        fi
    fi
done

if [ "$ALL_REPLACED" = true ]; then
    echo "✅ Содержимое dump.json заменено на заглушку во всех коммитах!"
else
    echo "⚠️  Проверьте результат вручную"
fi

echo ""
echo "========================================"
echo "ЗАМЕНА ЗАВЕРШЕНА"
echo "========================================"
echo ""
echo "Следующие шаги:"
echo "1. Проверьте результат: git show <commit>:dump.json"
echo "2. Убедитесь, что dump.json в .gitignore (уже есть)"
echo "3. Force push во все ветки:"
echo "   git push origin --force --all"
echo "   git push origin --force --tags"
echo ""
echo "⚠️  ВАЖНО: После force push уведомите всех разработчиков"
echo "   о необходимости переклонировать репозиторий!"
echo ""
echo "Резервная копия сохранена в: $BACKUP_PATH"
echo ""

read -p "Выполнить force push сейчас? (yes/no): " pushNow
if [ "$pushNow" = "yes" ]; then
    echo ""
    echo "Выполнение force push..."
    git push origin --force --all
    if [ $? -eq 0 ]; then
        git push origin --force --tags
        if [ $? -eq 0 ]; then
            echo "✅ Force push выполнен успешно!"
        else
            echo "⚠️  Ошибка при push тегов"
        fi
    else
        echo "❌ Ошибка при force push!"
    fi
else
    echo "Force push пропущен. Выполните его вручную позже."
fi

