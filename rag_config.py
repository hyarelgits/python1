"""Shared paths and model settings for the local RAG application."""

import os
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
CHROMA_DIR = Path(
    os.environ.get("RAG_CHROMA_DIR", str(PROJECT_DIR / "chroma_db"))
).expanduser()

COLLECTION_NAME = os.environ.get("RAG_COLLECTION_NAME", "ubuntu_rag")
CHAT_MODEL = os.environ.get("RAG_CHAT_MODEL", "llama3.2:3b")
EMBEDDING_MODEL = os.environ.get("RAG_EMBEDDING_MODEL", "nomic-embed-text")
CHUNK_SIZE = int(os.environ.get("RAG_CHUNK_SIZE", "800"))
CHUNK_OVERLAP = int(os.environ.get("RAG_CHUNK_OVERLAP", "120"))
RETRIEVAL_COUNT = int(os.environ.get("RAG_RETRIEVAL_COUNT", "4"))
