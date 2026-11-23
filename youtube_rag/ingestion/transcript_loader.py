
# Import YouTube transcript API
from youtube_transcript_api import YouTubeTranscriptApi

# Import transcript-related exception
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound
)


def get_transcript(video_id: str) -> list:
    """
    Fetch transcript of a YouTube video.

    Returns a list containing transcript segments
    with their text, start time and duration.
    """

    try:
        # Initialize transcript API
        api = YouTubeTranscriptApi()

        # Fetch transcript for the given video ID
        fetched_transcript = api.fetch(video_id)

        # Convert transcript object into a list of dictionaries
        transcript = fetched_transcript.to_raw_data()

        return transcript

    except TranscriptsDisabled:
        raise ValueError("Transcripts are disabled for this video")

    except NoTranscriptFound:
        raise ValueError("No transcript available for this video")
