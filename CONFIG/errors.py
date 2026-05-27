import re

# Error patterns that indicate cookie/authentication issues
# These errors trigger the SAVE_AS_COOKIE_HINT message to the user

COOKIE_ERRORS = [
    "Sign in to confirm you're not a bot",
    "Sign in to confirm your age",
    "Use --cookies-from-browser or --cookies for the authentication",
    "SIGN_IN_REQUIRED",
    "Private video. Sign in if you've been granted access to this video",
    "Requested content is not available, rate-limit reached or login required",
    "This post may not be comfortable for some audiences. Log in for access",
    "TikTok is requiring login for access to this content",
    "AuthRequired: authenticated cookies needed to access this timeline",
    "unable to download video data: HTTP Error 403: Forbidden",
    "HTTP Error 403: Forbidden",
    "HTTP Error 401",
    "Login required",
    "Authentication required",
    "cookies needed",
    "cookie is required",
    "sign in to confirm",
    "not a bot",
    "rate-limit reached",
    "login required",
    "Sign in to confirm",
    # Twitter/X errors — cookie often needed to access tweets
    "No video could be found in this tweet",
    "[twitter][error]",
    "tweet is not available",
    "content is not available",
    # Gallery-dl errors — cookie/auth required
    "authentication failed",
    "http redirect to login page",
    "redirect to login",
    "login page",
    "account suspended",
    "account banned",
    "account private",
    "profile private",
    "captcha required",
    "verification required",
    "age verification required",
    "no media found",
    "no content available",
    # YouTube membership/private/restriction errors
    "this video is available to this channel's members on level",
    "video unavailable. this video is private",
    "video is not available or has been removed",
    "your account has been rate-limited",
    "content isn't available, try again later",
    "requires login for access to this content",
    "join this channel to get access to members-only content",
    # Instagram errors
    "[instagram][error]",
    # Geo-block errors (cookie may help bypass)
    "has blocked it in your country",
    "not made this video available in your country",
    "Video limitato geograficamente",
]


# Geo-block error patterns
GEO_BLOCK_PATTERNS = [
    "not made this video available in your country",
    "blocked it in your country",
    "blocked in your country",
    "not available in your country",
    "not available in your region",
    "video limitato geograficamente",
    "geographic restriction",
    "geo-blocked",
    "region blocked",
    "this video is available in",
]

# Pattern to detect country list in error messages
# Matches: "This video is available in India." or "Kuwait, Qatar, Algeria, ..."
_COUNTRY_LIST_PATTERN = re.compile(
    r"(?:available\s+in|available\s+to)\s+(.+?)(?:\.\s*(?:You might|Use)|$)",
    re.IGNORECASE | re.DOTALL,
)


def is_cookie_error(error_message: str) -> bool:
    """Check if the error message indicates a cookie/authentication issue.
    
    Args:
        error_message: The error message string from yt-dlp or other downloader
    
    Returns:
        True if the error matches any known cookie/auth pattern
    """
    if not error_message:
        return False
    error_lower = error_message.lower()
    return any(pattern.lower() in error_lower for pattern in COOKIE_ERRORS)


def is_geo_block_error(error_message: str) -> bool:
    """Check if the error indicates a geographic block/restriction.
    
    Args:
        error_message: The error message string from yt-dlp or other downloader
    
    Returns:
        True if the error matches any known geo-block pattern
    """
    if not error_message:
        return False
    error_lower = error_message.lower()
    return any(pattern.lower() in error_lower for pattern in GEO_BLOCK_PATTERNS)


def has_country_list_in_error(error_message: str) -> bool:
    """Check if the geo-block error message contains a list of allowed countries.
    
    Args:
        error_message: The error message string from yt-dlp or other downloader
    
    Returns:
        True if specific countries are mentioned in the error
    """
    if not error_message:
        return False
    return bool(_COUNTRY_LIST_PATTERN.search(error_message))
