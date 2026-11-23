
from langchain_core.documents import Document


def build_document(transcript: list, video_details: dict) -> Document:
    """
    Convert transcript segments into a LangChain Document.
    """

    # Combine all transcript segments into one text
    full_text = " ".join(
        segment["text"] for segment in transcript
    )

    # Store video information as metadata
    metadata = {
        "video_id": video_details["video_id"],
        "title": video_details["title"],
        "channel": video_details["channel"],
        "url": f"https://www.youtube.com/watch?v={video_details['video_id']}"
    }

    # Create LangChain Document
    document = Document(
        page_content=full_text,
        metadata=metadata
    )

    return document
