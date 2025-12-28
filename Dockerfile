FROM python:3.10-slim

ARG TZ=Europe/Moscow
ENV TZ="$TZ" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# System dependencies:
# - git, ffmpeg, mediainfo, rsync (README: base deps + FFmpeg)
# - font packages for Arabic/Asian and emoji support (README: optional fonts)
# - docker.io for dashboard container to manage Docker
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    mediainfo \
    rsync \
    docker.io \
    curl \
    iputils-ping \
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
COPY docker-entrypoint.sh /usr/local/bin/
RUN sed -i 's/\r$//' /usr/local/bin/docker-entrypoint.sh && \
    chmod +x /usr/local/bin/docker-entrypoint.sh && \
    # Clean up any Python cache that might have been copied
    find /app -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true && \
    find /app -type f -name "*.pyc" -delete 2>/dev/null || true

CMD ["/usr/local/bin/docker-entrypoint.sh"]