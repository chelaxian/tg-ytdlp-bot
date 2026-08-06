FROM python:3.11-slim

ARG TZ=Europe/Moscow
ENV TZ="$TZ" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# System dependencies:
# - git, ffmpeg, mediainfo, rsync (README: base deps + FFmpeg)
# - font packages for Arabic/Asian and emoji support (README: optional fonts)
# - docker.io for dashboard container to manage Docker
# - gnupg + curl for adding the NodeSource apt repo (Node.js installed separately below)
# - phantomjs removed: deprecated and no longer available in Debian repos
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    mediainfo \
    rsync \
    docker.io \
    curl \
    iputils-ping \
    gnupg \
    fonts-noto-core \
    fonts-noto-extra \
    fonts-kacst-one \
    fonts-noto-cjk \
    fonts-indic \
    fonts-noto-color-emoji \
    fontconfig \
    libass9 \
    ca-certificates \
    && \
    # Install Amiri Arabic font and clean up in one layer
    git clone --depth 1 https://github.com/aliftype/amiri.git /tmp/amiri \
    && mkdir -p /usr/share/fonts/truetype/amiri \
    && cp /tmp/amiri/fonts/*.ttf /usr/share/fonts/truetype/amiri/ \
    && fc-cache -fv \
    && rm -rf /tmp/amiri \
    && \
    # Clean up apt cache and temporary files
    apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* /var/tmp/*

# Node.js 22 for yt-dlp's EJS (the YouTube n-challenge / nsig solver). Debian's apt
# nodejs is < 22, but EJS requires node >= 22 — otherwise every JS challenge provider
# reports "unavailable" and adaptive formats (720p+/4K) are dropped.
# https://github.com/yt-dlp/ejs — added the canonical way (GPG key in keyrings +
# signed-by source list, not the piped setup script).
RUN mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_22.x nodistro main" > /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Copy application code
COPY . .

# Копируем и делаем исполняемым entrypoint скрипт
# Конвертируем Windows окончания строк (CRLF) в Unix (LF) и делаем исполняемым
COPY scripts/docker-entrypoint.sh /usr/local/bin/
RUN sed -i 's/\r$//' /usr/local/bin/docker-entrypoint.sh && \
    chmod +x /usr/local/bin/docker-entrypoint.sh && \
    # Clean up any Python cache that might have been copied
    find /app -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true && \
    find /app -type f -name "*.pyc" -delete 2>/dev/null || true

CMD ["/usr/local/bin/docker-entrypoint.sh"]