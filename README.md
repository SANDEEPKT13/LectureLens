Understand what each folder will contain
This is important. Don't just memorize the filenames. Understand why each file exists.
A. Root directory
File	Responsibility
.env	Stores API keys (Groq, YouTube)
.env.example	Shows which environment variables are required, without real keys
.gitignore	Prevents secrets, virtual environments and generated data from going to GitHub
requirements.txt	All Python dependencies
README.md	Project documentation

B. ingestion/ — Getting data from YouTube
Phase 1 & 2
File	Responsibility
youtube_client.py	Connect to YouTube API and fetch video metadata
transcript_loader.py	Fetch video captions/transcript and timestamps

The output of this folder will be our raw video information and transcript.
C. processing/ — Preparing data for RAG
Phase 3
File	Responsibility
document_builder.py	Convert transcript segments into LangChain Documents with metadata
text_splitter.py	Split documents into smaller chunks using RecursiveCharacterTextSplitter

Example:

Original transcript:
Today we will learn about RAG.
RAG stands for Retrieval Augmented Generation.
It combines retrieval with an LLM...


After splitting:
Chunk 1:
Today we will learn about RAG.
RAG stands for Retrieval Augmented Generation.

Chunk 2:
It combines retrieval with an LLM...


We'll preserve timestamps and video information in metadata.
D. embeddings/ — Converting text into vectors
Phase 4
embedder.py
- Load the HuggingFace embedding model.
- Convert transcript chunks into numerical vectors.
- Prepare embeddings for vector storage.
E. vectorstore/ — Storing embeddings
Phase 5
chroma_store.py
- Initialize ChromaDB.
- Store embedded documents.
- Persist the vector database locally.
- Load previously stored documents.
F. rag/ — The actual intelligence
Phases 6–9
File	Responsibility
prompts.py	Define system and user prompt templates
retriever.py	Retrieve relevant transcript chunks
chain.py	Connect retriever, prompt, LLM and output parser

This is where our RAG pipeline comes together.
G. utils/ — Reusable helpers
helpers.py

Small utility functions such as extracting a YouTube video ID, formatting timestamps and validating URLs.
H. data/ — Generated project data
Folder	Contains
transcripts/	Saved transcript data for debugging and reuse
chroma_db/	Persistent ChromaDB storage

These are generated data, not Python source code.
I. main.py — Entry point
This is the file we'll execute:
python -m youtube_rag.main


It will coordinate everything:
1. Accept YouTube URL.
2. Call ingestion functions.
3. Process transcript.
4. Generate embeddings.
5. Store documents.
6. Accept user questions.
7. Run RAG chain.
8. Display answers.
Important: main.py coordinates the modules. It shouldn't contain all their implementation logic.