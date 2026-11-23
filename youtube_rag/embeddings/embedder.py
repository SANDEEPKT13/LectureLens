from langchain_huggingface import HuggingFaceEmbeddings
from youtube_rag.config import EMBEDDING_MODEL

def get_embedding_model():
    """
    Initialize and return the embedding model.
    """

    # Create HuggingFace embeddings model
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    return embeddings



# - HuggingFaceEmbeddings: LangChain's integration for Hugging Face embedding models.
# - model_name: Specifies which pretrained model to load.
# - device="cpu": Runs the model on your CPU.
# - normalize_embeddings=True: Normalizes vectors, which makes similarity comparisons more consistent.
# - return embeddings: Gives us the embedding object to reuse in later stages.
# We are not manually writing vector-generation logic. LangChain handles that through the model integration.