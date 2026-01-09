# Limits Configuration

class LimitsConfig(object):
    #######################################################
    # Limits and restrictions
    TURN_OFF_LIMITS_FOR_ADMINS = True
    #######################################################
    MAX_FILE_SIZE_GB = 8  # GiB
    # Download timeout in seconds (2 hours = 7200 seconds)
    DOWNLOAD_TIMEOUT = 7200 # in seconds
    MAX_SUB_QUALITY = 720 # 720p
    MAX_SUB_DURATION = 5400 # in seconds
    MAX_SUB_SIZE = 500 # in MB      
    MAX_PLAYLIST_COUNT = 50
    MAX_TIKTOK_COUNT = 500        
    # Max number of media files to download/send for /img
    MAX_IMG_FILES = 1000
    # Max single video duration in seconds for yt-dlp downloads (default 12 hours)
    MAX_VIDEO_DURATION = 43200
    #######################################################
    # Image download timeouts (in seconds)
    # Maximum wait time for one range (30 minutes) - for large videos
    # Increase this if you have very large video files that take longer to download
    MAX_IMG_RANGE_WAIT_TIME = 1800  # 30 minutes
    
    # Maximum total wait time (4 hours) - for very large collections
    # Increase this if you download very large Instagram accounts with thousands of posts
    MAX_IMG_TOTAL_WAIT_TIME = 14400  # 4 hours
    
    # Maximum inactivity time (5 minutes) - if no new files found
    # If no new files are found for this time, download stops (prevents infinite waiting)
    MAX_IMG_INACTIVITY_TIME = 300  # 5 minutes
    
    # Example configurations for different scenarios:
    # For fast internet and small files: MAX_IMG_RANGE_WAIT_TIME = 600 (10 min), MAX_IMG_TOTAL_WAIT_TIME = 3600 (1 hour)
    # For slow internet and large files: MAX_IMG_RANGE_WAIT_TIME = 3600 (1 hour), MAX_IMG_TOTAL_WAIT_TIME = 28800 (8 hours)
    # For very large accounts: MAX_IMG_TOTAL_WAIT_TIME = 43200 (12 hours)
    ENABLE_LIVE_STREAM_BLOCKING = False
    SPLIT_LIVE_STREAM_BY_HOURS = 1
    MAX_LIVE_STREAM_DURATION = 36000 # 10 hours
    #######################################################
    # Animation and HTTP connection limits (prevents hanging)
    #######################################################
    # Maximum animation duration (4 hours) - after this time animation is forcefully stopped
    MAX_ANIMATION_DURATION = 14400  # 4 hours
    
    # Maximum HTTP connection lifetime (4 hours) - connections are forcefully closed after this time
    MAX_HTTP_CONNECTION_LIFETIME = 14400  # 4 hours
    
    # HTTP session timeout for individual requests 
    HTTP_REQUEST_TIMEOUT = 60  # 60 seconds
    #######################################################
    # Cookie cache configuration
    #######################################################
    # Cookie cache duration in seconds (30 seconds for quick operations)
    COOKIE_CACHE_DURATION = 30
    # Maximum cookie cache lifetime in seconds (2 hours) - forced deactivation
    COOKIE_CACHE_MAX_LIFETIME = 7200  # 2 hours
    # Cookie cache timeout for individual requests in seconds
    COOKIE_CACHE_REQUEST_TIMEOUT = 60  # 60 seconds
    
    # YouTube cookie retry limits per user
    # Maximum number of YouTube cookie retry attempts per user per hour
    YOUTUBE_COOKIE_RETRY_LIMIT_PER_HOUR = 8  # 8 attempts per hour per user
    # Time window for retry limit in seconds (1 hour)
    YOUTUBE_COOKIE_RETRY_WINDOW = 3600  # 1 hour
    
    #######################################################
    # Rate limiting configuration for URLs
    #######################################################
    # Maximum URLs per minute
    RATE_LIMIT_PER_MINUTE = 5
    # Maximum URLs per hour
    RATE_LIMIT_PER_HOUR = 60
    # Maximum URLs per day
    RATE_LIMIT_PER_DAY = 1000
    # Cooldown durations in seconds
    RATE_LIMIT_COOLDOWN_MINUTE = 300  # 5 minutes
    RATE_LIMIT_COOLDOWN_HOUR = 3600   # 1 hour
    RATE_LIMIT_COOLDOWN_DAY = 86400   # 1 day
    #######################################################
    # Command spam protection
    #######################################################
    # Maximum commands per minute
    COMMAND_LIMIT_PER_MINUTE = 20
    # Initial cooldown for command spam (in seconds)
    COMMAND_COOLDOWN_INITIAL = 60  # 1 minute
    # Cooldown multiplier for repeated violations (exponential backoff)
    COMMAND_COOLDOWN_MULTIPLIER = 2
    #######################################################
    # Group multipliers (applied in groups/channels) - except quality
    GROUP_MULTIPLIER = 2
    #######################################################
    # Multiple URLs in one message limits (for non-Always Ask mode)
    # Maximum number of URLs per message for regular users
    MAX_MULTI_URL_LIMIT = 10
    # For groups, the limit is MAX_MULTI_URL_LIMIT * GROUP_MULTIPLIER (20)
    # Admins have no limit (0 means unlimited)
    #######################################################
    NSFW_STAR_COST = 1
    #######################################################
    # Anti-bot protection limits
    #######################################################
    # Включить/выключить защиту от ботов
    ANTI_BOT_PROTECTION_ENABLED = True
    # Защита от повторяющихся ссылок
    # Проверка 1: Максимальное количество одинаковых ссылок в течение периода
    ANTI_BOT_DUPLICATE_URL_LIMIT = 11 # 11 одинаковых ссылок
    # Период для проверки повторяющихся ссылок (в секундах)
    ANTI_BOT_DUPLICATE_URL_WINDOW = 3600  # 1 час
    
    # Проверка 2: Защита от отправки по таймеру (одинаковый интервал между сообщениями)
    # Период для проверки таймера (в секундах)
    ANTI_BOT_TIMER_INTERVAL_WINDOW = 3600  # 1 час
    # Погрешность для определения одинакового интервала (в секундах)
    ANTI_BOT_TIMER_INTERVAL_TOLERANCE = 3  # 3 секунды погрешности
    # Минимальное количество сообщений с одинаковым интервалом для блокировки
    ANTI_BOT_TIMER_INTERVAL_MIN_COUNT = 11  # минимум 11 сообщений с одинаковым интервалом
    # Минимальный интервал между сообщениями для проверки таймера (в секундах)
    # Используется для избежания ложных срабатываний на быстрый перебор команд
    ANTI_BOT_TIMER_INTERVAL_MIN_INTERVAL = 60  # 1 минута
    
    # Защита от повторяющихся команд
    # Максимальное количество одинаковых команд в течение периода
    ANTI_BOT_DUPLICATE_COMMAND_LIMIT = 50  # 50 одинаковых команд
    # Период для проверки повторяющихся команд (в секундах)
    ANTI_BOT_DUPLICATE_COMMAND_WINDOW = 300  # 5 минут
    
    # Защита от активности 24/7 (не спят)
    # Максимальное количество разных часов в течение 23 часов с момента запуска, когда пользователь проявлял активность
    ANTI_BOT_24H_ACTIVITY_LIMIT = 23  # активность в каждый из 23 часов с момента запуска
    # Период для проверки активности 24/7 (в секундах) - 23 часа с момента запуска
    ANTI_BOT_24H_WINDOW = 82800  # 23 часа (23 * 3600)
    
    # Дополнительные защиты от ботов
    # Защита от флуда (слишком быстрые сообщения)
    # Максимальное количество сообщений в секунду
    ANTI_BOT_FLOOD_MESSAGES_PER_SECOND = 5  # 5 сообщений в секунду
    # Период для проверки флуда (в секундах) - проверяем каждую секунду в течение этого периода
    ANTI_BOT_FLOOD_WINDOW = 10  # 10 секунд
    
    # Защита от повторяющихся одинаковых сообщений (любой текст)
    # Максимальное количество одинаковых сообщений в течение периода
    ANTI_BOT_DUPLICATE_MESSAGE_LIMIT = 50  # 50 одинаковых сообщений
    # Период для проверки повторяющихся сообщений (в секундах)
    ANTI_BOT_DUPLICATE_MESSAGE_WINDOW = 300  # 5 минут
    
    # Защита от подозрительных паттернов
    # Блокировать сообщения, состоящие только из цифр
    ANTI_BOT_BLOCK_NUMBERS_ONLY = True
    # Блокировать сообщения, состоящие только из спецсимволов
    ANTI_BOT_BLOCK_SPECIAL_ONLY = True
    # Минимальная длина сообщения для проверки паттернов
    ANTI_BOT_PATTERN_MIN_LENGTH = 10
    