# Limits Configuration

class LimitsConfig(object):
    #######################################################
    # Limits and restrictions
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
    
    #######################################################
    # Group multipliers (applied in groups/channels) - except quality
    GROUP_MULTIPLIER = 2
    #######################################################
    NSFW_STAR_COST = 1
    