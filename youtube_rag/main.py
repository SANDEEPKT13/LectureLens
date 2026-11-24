
# # from youtube_rag.config import (
# #     YOUTUBE_API_KEY,
# #     GROQ_API_KEY,
# #     EMBEDDING_MODEL,
# #     CHUNK_SIZE,
# #     CHUNK_OVERLAP
# # )

# # print("Configuration loaded successfully!")

# # print("YouTube API configured:", bool(YOUTUBE_API_KEY))
# # print("Groq API configured:", bool(GROQ_API_KEY))

# # print("Embedding Model:", EMBEDDING_MODEL)
# # print("Chunk Size:", CHUNK_SIZE)
# # print("Chunk Overlap:", CHUNK_OVERLAP)



# # from youtube_rag.ingestion.youtube_client import (
# #     extract_video_id,
# #     get_video_details
# # )

# # url = input("Enter YouTube video URL: ")

# # try:
# #     video_id = extract_video_id(url)

# #     print("\nVideo ID:", video_id)

# #     details = get_video_details(video_id)

# #     print("\n========== VIDEO DETAILS ==========")

# #     for key, value in details.items():
# #         print(f"{key}: {value}")

# # except Exception as error:
# #     print("\nError:", error)




# from youtube_rag.ingestion.youtube_client import extract_video_id
# from youtube_rag.ingestion.transcript_loader import get_transcript


# url = input("Enter YouTube URL: ")

# try:
#     # Extract video ID
#     video_id = extract_video_id(url)

#     print("\nVideo ID:", video_id)

#     # Fetch transcript
#     transcript = get_transcript(video_id)

#     print("\nTranscript fetched successfully!")

#     print("\nTotal segments:", len(transcript))

#     # Display first 5 segments
#     print("\n========== TRANSCRIPT ==========")

#     for segment in transcript[:5]:

#         print(
#             f"[{segment['start']:.2f}s] "
#             f"{segment['text']}"
#         )

# except Exception as error:

#     print("\nError:", error)




# ==========================================
# 1. IMPORTS
# ==========================================

from youtube_rag.ingestion.youtube_client import (
    extract_video_id,
    get_video_details
)

from youtube_rag.ingestion.transcript_loader import get_transcript

from youtube_rag.processing.document_builder import build_document
from youtube_rag.processing.text_splitter import split_document

from youtube_rag.embeddings.embedder import get_embedding_model

from youtube_rag.vectorstore.chroma_store import create_vector_store

from youtube_rag.rag.retriever import (
    get_retriever,
    retrieve_documents
)

from youtube_rag.rag.chain import (
    create_rag_chain,
    generate_answer
)


# ==========================================
# 2. MAIN FUNCTION
# ==========================================

def main():

    print("\n===== YOUTUBE AI RESEARCH ASSISTANT =====")

    try:

        # ----------------------------------
        # STEP 1: GET YOUTUBE VIDEO
        # ----------------------------------

        url = input("\nEnter YouTube URL: ")

        video_id = extract_video_id(url)

        print("\nVideo ID:", video_id)


        # ----------------------------------
        # STEP 2: FETCH VIDEO DETAILS
        # ----------------------------------

        video_details = get_video_details(video_id)

        print("\nVideo Title:", video_details["title"])
        print("Channel:", video_details["channel"])


        # ----------------------------------
        # STEP 3: FETCH TRANSCRIPT
        # ----------------------------------

        transcript = get_transcript(video_id)

        print("\nTranscript fetched successfully!")
        print("Total transcript segments:", len(transcript))


        # ----------------------------------
        # STEP 4: BUILD DOCUMENT
        # ----------------------------------

        document = build_document(
            transcript,
            video_details
        )

        print("\nDocument created successfully!")


        # ----------------------------------
        # STEP 5: SPLIT INTO CHUNKS
        # ----------------------------------

        chunks = split_document(document)

        print("\nTotal chunks created:", len(chunks))


        # ----------------------------------
        # STEP 6: GENERATE EMBEDDINGS
        # ----------------------------------

        embedding_model = get_embedding_model()

        print("\nEmbedding model initialized!")


        # ----------------------------------
        # STEP 7: STORE IN CHROMADB
        # ----------------------------------

        vector_store = create_vector_store(
            chunks,
            embedding_model
        )

        print("\nVector database created!")
        print(
            "Stored chunks:",
            vector_store._collection.count()
        )


        # ----------------------------------
        # STEP 8: CREATE RETRIEVER
        # ----------------------------------

        retriever = get_retriever(
            vector_store,
            k=4
        )

        print("\nRetriever initialized!")


        # ----------------------------------
        # STEP 9: CREATE RAG CHAIN
        # ----------------------------------

        rag_chain = create_rag_chain()

        print("\nLLM chain initialized!")


        # ----------------------------------
        # STEP 10: QUESTION-ANSWER LOOP
        # ----------------------------------

        while True:

            question = input(
                "\nAsk a question about the video "
                "(type 'exit' to quit): "
            )

            if question.lower().strip() == "exit":
                print("\nExiting YouTube AI Research Assistant.")
                break

            if not question.strip():
                print("Please enter a valid question.")
                continue

            # Retrieve relevant chunks
            results = retrieve_documents(
                retriever,
                question
            )

            # Generate answer using retrieved context
            answer = generate_answer(
                results,
                question,
                rag_chain
            )

            print("\n========== AI ANSWER ==========")
            print(answer)


    except Exception as error:

        print("\nAn error occurred:", error)


# ==========================================
# 3. APPLICATION ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()
