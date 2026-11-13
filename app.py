"""FastAPI endpoints and the shared LangGraph RAG workflow."""

from typing import TypedDict

from fastapi import FastAPI, HTTPException
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field

from rag_config import (
    CHAT_MODEL,
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    RETRIEVAL_COUNT,
)


class RAGState(TypedDict):
    """Values passed between the retrieval and answer graph nodes."""

    question: str
    context: list[Document]
    answer: str


class QueryRequest(BaseModel):
    """Validated request body for POST /query."""

    question: str = Field(min_length=1, max_length=4000)


class QueryResponse(BaseModel):
    """Answer and source files returned to API clients."""

    answer: str
    sources: list[str]


def build_rag_graph():
    """Create the graph that retrieves passages and generates a grounded answer."""
    if not CHROMA_DIR.is_dir():
        raise RuntimeError(
            f"ChromaDB index not found at {CHROMA_DIR}. Run `python ingest.py` first."
        )

    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    chat_model = ChatOllama(model=CHAT_MODEL, temperature=0)

    def retrieve(state: RAGState) -> dict:
        documents = store.similarity_search(
            state["question"],
            k=RETRIEVAL_COUNT,
        )
        return {"context": documents}

    def generate_answer(state: RAGState) -> dict:
        context = "\n\n".join(
            f"Source: {document.metadata.get('source', 'unknown')}\n"
            f"{document.page_content}"
            for document in state["context"]
        )
        prompt = f"""Answer the question using only the supplied context.
If the context does not contain the answer, say you do not know.
Mention the source filename when useful.

Context:
{context}

Question:
{state["question"]}
"""
        response = chat_model.invoke(prompt)
        return {"answer": response.content}

    workflow = StateGraph(RAGState)
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate_answer", generate_answer)
    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "generate_answer")
    workflow.add_edge("generate_answer", END)
    return workflow.compile()


rag = build_rag_graph()
app = FastAPI(title="Local RAG API", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the API process is responding."""
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query_documents(request: QueryRequest) -> QueryResponse:
    """Answer a question using the indexed local documents."""
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=422, detail="Question cannot be blank.")

    result = rag.invoke({"question": question})
    sources = sorted(
        {
            document.metadata.get("source", "unknown")
            for document in result["context"]
        }
    )
    return QueryResponse(answer=result["answer"], sources=sources)
