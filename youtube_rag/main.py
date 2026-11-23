
# from youtube_rag.config import (
#     YOUTUBE_API_KEY,
#     GROQ_API_KEY,
#     EMBEDDING_MODEL,
#     CHUNK_SIZE,
#     CHUNK_OVERLAP
# )

# print("Configuration loaded successfully!")

# print("YouTube API configured:", bool(YOUTUBE_API_KEY))
# print("Groq API configured:", bool(GROQ_API_KEY))

# print("Embedding Model:", EMBEDDING_MODEL)
# print("Chunk Size:", CHUNK_SIZE)
# print("Chunk Overlap:", CHUNK_OVERLAP)



# from youtube_rag.ingestion.youtube_client import (
#     extract_video_id,
#     get_video_details
# )

# url = input("Enter YouTube video URL: ")

# try:
#     video_id = extract_video_id(url)

#     print("\nVideo ID:", video_id)

#     details = get_video_details(video_id)

#     print("\n========== VIDEO DETAILS ==========")

#     for key, value in details.items():
#         print(f"{key}: {value}")

# except Exception as error:
#     print("\nError:", error)




from youtube_rag.ingestion.youtube_client import extract_video_id
from youtube_rag.ingestion.transcript_loader import get_transcript


url = input("Enter YouTube URL: ")

try:
    # Extract video ID
    video_id = extract_video_id(url)

    print("\nVideo ID:", video_id)

    # Fetch transcript
    transcript = get_transcript(video_id)

    print("\nTranscript fetched successfully!")

    print("\nTotal segments:", len(transcript))

    # Display first 5 segments
    print("\n========== TRANSCRIPT ==========")

    for segment in transcript[:5]:

        print(
            f"[{segment['start']:.2f}s] "
            f"{segment['text']}"
        )

except Exception as error:

    print("\nError:", error)
