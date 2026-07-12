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
    "not available in your area",
    "not available from your location",
    "not available outside",
    "available only in",
    "geographically restricted",
    "geographic restriction",
    "geo-blocked",
    "region blocked",
    "rights restrictions",
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


# Specific, semantic yt-dlp error categories surfaced to the user with an
# actionable localized message (issues #352, #354, #356, #359, #360).
# Returns the category code or None when the error is unclassified (caller
# falls back to the generic handling).
def classify_yt_dlp_error(error_message, url=None):
    """Classify a yt-dlp/extractor error string into a semantic category.

    Returns one of: MEMBERS_ONLY, LIVE_ENDED, GEO_RESTRICTED, AGE_RESTRICTED,
    HTTP_500, EXTRACTOR_ERROR — or None if the error is not recognised (fall
    through to generic handling).

    Note: a geo/members/age error can still be actionable via cookies, so the
    caller keeps appending the cookie hint for those categories.
    """
    if not error_message:
        return None
    error_lower = error_message.lower()

    # Members-only content (issue #352)
    if "members-only" in error_lower or "join this channel" in error_lower:
        return "MEMBERS_ONLY"

    # Live stream ended / not started (issue #354)
    if "live event has ended" in error_lower or "live event has not started" in error_lower:
        return "LIVE_ENDED"
    # Regression #354: a /live/<ID> URL that returns "No video formats found" is
    # in practice an ended stream that yt-dlp reports before the LIVE_ENDED text.
    if "no video formats found" in error_lower and url and "/live/" in url.lower():
        return "LIVE_ENDED"

    # Geo restriction (issue #359) — reuse the existing geo pattern matcher
    if is_geo_block_error(error_message):
        return "GEO_RESTRICTED"

    # Age verification required (issue #360)
    if (
        "take a few minutes to verify your age" in error_lower
        or "sign in to confirm your age" in error_lower
        or "age verification required" in error_lower
    ):
        return "AGE_RESTRICTED"

    # Upstream server error (issue #356) — transient, show "try again later"
    if "http error 500" in error_lower or "internal server error" in error_lower:
        return "HTTP_500"

    # Extractor/parse failure (issue #328) — Facebook and other platforms change
    # page structure, breaking yt-dlp's extractor. Show a friendly message
    # suggesting yt-dlp update or cookies rather than the raw "Cannot parse data".
    if "cannot parse data" in error_lower or "unable to extract" in error_lower or "extractor error" in error_lower:
        return "EXTRACTOR_ERROR"

    return None
