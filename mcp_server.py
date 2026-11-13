"""MCP Streamable HTTP server exposing the local RAG workflow as a tool."""

from mcp.server import MCPServer

from app import rag


mcp = MCPServer("Local RAG")


@mcp.tool()
def ask_documents(question: str) -> str:
    """Answer a question using local documents and include source filenames."""
    question = question.strip()
    if not question:
        raise ValueError("Question cannot be blank.")

    result = rag.invoke({"question": question})
    sources = sorted(
        {
            document.metadata.get("source", "unknown")
            for document in result["context"]
        }
    )
    source_text = ", ".join(sources) if sources else "none"
    return f"{result['answer']}\nSources: {source_text}"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8001,
    )
