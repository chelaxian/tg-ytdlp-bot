#!/bin/bash

# Обновление образа bgutil-provider через docker pull
echo "🔄 Updating bgutil-provider image..."

if ! command -v docker &> /dev/null; then
    echo "❌ Error: docker not found"
    exit 1
fi

docker pull brainicism/bgutil-ytdlp-pot-provider:latest

echo "✅ bgutil-provider image updated successfully"
