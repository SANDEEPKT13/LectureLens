
# ==========================================
# 1. IMPORTING REQUIRED LIBRARIES
# ==========================================

import re

# Used to connect and communicate with YouTube Data API
from googleapiclient.discovery import build

# Used to handle errors returned by Google's API
from googleapiclient.errors import HttpError

# Import our YouTube API key from config.py
from youtube_rag.config import YOUTUBE_API_KEY


# ==========================================
# 2. EXTRACT VIDEO ID FROM YOUTUBE URL
# ==========================================

def extract_video_id(url: str) -> str:
    """
    Extract YouTube video ID from different URL formats.
    """

    # Different formats in which YouTube URLs can appear
    patterns = [
        r"(?:youtube\.com/watch\?v=)([^&]+)",
        r"(?:youtu\.be/)([^?&]+)",
        r"(?:youtube\.com/shorts/)([^?&]+)",
        r"(?:youtube\.com/embed/)([^?&]+)",
        r"(?:youtube\.com/live/)([^?&]+)"
    ]

    # Try each pattern against the provided URL
    for pattern in patterns:

        # Search for the matching URL pattern
        match = re.search(pattern, url)

        # If a match is found, extract the video ID
        if match:
            return match.group(1)

    # If no pattern matches, raise an error
    raise ValueError("Invalid YouTube URL")


# ==========================================
# 3. INITIALIZE YOUTUBE API CLIENT
# ==========================================

def get_youtube_client():
    """
    Initialize YouTube API client.
    """

    # Check whether API key exists
    if not YOUTUBE_API_KEY:
        raise ValueError("YouTube API key not found in .env")

    # Build and return the YouTube API client
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_API_KEY
    )

    return youtube


# ==========================================
# 4. FETCH VIDEO METADATA
# ==========================================

def get_video_details(video_id: str) -> dict:
    """
    Fetch video metadata using YouTube Data API.
    """

    # Initialize YouTube API client
    youtube = get_youtube_client()

    try:

        # Prepare API request to fetch video details
        request = youtube.videos().list(
            part="snippet,contentDetails",
            id=video_id
        )

        # Execute API request and receive JSON response
        response = request.execute()

        # Check whether YouTube returned any video
        if not response.get("items"):
            raise ValueError("Video not found or unavailable")

        # Extract the first video from API response
        video = response["items"][0]

        # Extract video snippet information
        snippet = video["snippet"]

        # Extract video duration information
        content = video["contentDetails"]

        # Return only the information we need
        return {
            "video_id": video_id,
            "title": snippet["title"],
            "description": snippet["description"],
            "channel": snippet["channelTitle"],
            "published_at": snippet["publishedAt"],
            "duration": content["duration"]
        }

    # Handle errors returned by YouTube API
    except HttpError as error:

        raise RuntimeError(
            f"YouTube API request failed: {error}"
        ) from error
