#!/bin/bash
# Version 1.0.0

# Updater script for tg-ytdlp-bot
# Run from the bot folder (where magic.py is located)
# Note: backups created with minute-level timestamp (.backup_YYYYMMDD_HHMM)

# Опция сохранения docker-compose.yml при обновлении
PRESERVE_DOCKER_COMPOSE=True

echo "🚀 tg-ytdlp-bot updater"
echo "=================================="

# Sanity check: correct working directory
if [ ! -f "magic.py" ]; then
    echo "❌ Error: magic.py not found"
    echo "Make sure you run this script from the bot folder"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 not found"
    exit 1
fi

# Check Git
if ! command -v git &> /dev/null; then
    echo "❌ Error: git not found"
    echo "Install Git to use this updater:"
    echo "  Ubuntu/Debian: sudo apt install git"
    echo "  CentOS/RHEL:   sudo yum install git"
    exit 1
fi

# Сохраняем docker-compose.yml перед обновлением, если опция включена
if [ "$PRESERVE_DOCKER_COMPOSE" = "True" ] || [ "$PRESERVE_DOCKER_COMPOSE" = "true" ]; then
    if [ -f "docker-compose.yml" ]; then
        echo "💾 Preserving docker-compose.yml..."
        cp docker-compose.yml ../
        echo "✅ docker-compose.yml backed up to parent directory"
    else
        echo "⚠️  docker-compose.yml not found, skipping backup"
    fi
fi

# Run update
echo "📥 Starting update..."
python3 update_from_repo.py
update_status=$?

# Восстанавливаем docker-compose.yml после обновления, если опция включена
if [ "$PRESERVE_DOCKER_COMPOSE" = "True" ] || [ "$PRESERVE_DOCKER_COMPOSE" = "true" ]; then
    if [ -f "../docker-compose.yml" ]; then
        echo "🔄 Restoring docker-compose.yml..."
        cp ../docker-compose.yml .
        echo "✅ docker-compose.yml restored from backup"
    else
        echo "⚠️  Backup docker-compose.yml not found in parent directory"
    fi
fi

# Final status
if [ $update_status -eq 0 ]; then
    echo ""
    echo "✅ Update completed successfully!"
    echo "🔄 It's recommended to restart the bot"
else
    echo ""
    echo "❌ Update finished with errors"
    echo "Please check the logs above"
fi
