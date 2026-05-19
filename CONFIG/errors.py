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
]


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
