
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API keys
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Text splitting configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector database path
CHROMA_DB_PATH = "data/chroma_db"


GROQ_MODEL = "openai/gpt-oss-20b"