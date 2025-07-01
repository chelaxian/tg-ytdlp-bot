"""
Thumbnail processing for videos
"""
import os
import requests
from ..database.firebase import logger


def download_thumbnail(video_id: str, dest: str) -> None:
    """Download YouTube thumbnail by video ID"""
    try:
        # YouTube thumbnail URLs
        urls = [
            f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
            f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
            f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg",
            f"https://img.youtube.com/vi/{video_id}/default.jpg"
        ]
        
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200 and len(response.content) > 1000:  # Valid image
                    with open(dest, 'wb') as f:
                        f.write(response.content)
                    logger.info(f"Downloaded thumbnail from {url} to {dest}")
                    return
            except Exception as e:
                logger.warning(f"Failed to download from {url}: {e}")
                continue
        
        logger.warning(f"Failed to download any thumbnail for video_id: {video_id}")
        
    except Exception as e:
        logger.error(f"Error downloading thumbnail for {video_id}: {e}") 