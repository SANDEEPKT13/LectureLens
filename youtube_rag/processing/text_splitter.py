from langchain.text_splitter import RecursiveCharacterTextSplitter
from youtube_rag.config import CHUNK_SIZE, CHUNK_OVERLAP

def split_document(document):

    # Initialize text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""]
    )

    # Split document into smaller Document objects
    chunks = splitter.split_documents([document])

    return chunks
