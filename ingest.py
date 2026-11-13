"""Build or refresh the local ChromaDB index from UTF-8 text files."""

import hashlib

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag_config import (
    CHROMA_DIR,
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    COLLECTION_NAME,
    DATA_DIR,
    EMBEDDING_MODEL,
    PROJECT_DIR,
)


def load_documents() -> list[Document]:
    """Load non-empty .txt files and retain their relative source paths."""
    documents = []
    for path in sorted(DATA_DIR.rglob("*.txt")):
        text = path.read_text(encoding="utf-8").strip()
        if text:
            source = path.relative_to(PROJECT_DIR).as_posix()
            documents.append(Document(page_content=text, metadata={"source": source}))
    return documents


def main() -> None:
    """Split, embed, and save all documents in the persistent vector store."""
    if not DATA_DIR.is_dir():
        raise SystemExit(f"Document folder not found: {DATA_DIR}")

    documents = load_documents()
    if not documents:
        raise SystemExit(f"No non-empty .txt files found under {DATA_DIR}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(documents)
    if not chunks:
        raise SystemExit("No text passages were created from the documents.")

    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    # Clear this app's collection first so removed documents do not stay searchable.
    existing_ids = store.get()["ids"]
    if existing_ids:
        store.delete(ids=existing_ids)

    ids = [
        hashlib.sha256(
            f"{chunk.metadata['source']}:{index}".encode("utf-8")
        ).hexdigest()
        for index, chunk in enumerate(chunks)
    ]
    store.add_documents(chunks, ids=ids)

    print(
        f"Indexed {len(chunks)} passages from {len(documents)} text file(s) "
        f"into {CHROMA_DIR}."
    )


if __name__ == "__main__":
    main()
