
from langchain_chroma import Chroma

from youtube_rag.config import CHROMA_DB_PATH


def create_vector_store(chunks, embedding_model):
    """
    Store document chunks and their embeddings in ChromaDB.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH,
        collection_name="youtube_transcripts"
    )

    return vector_store
