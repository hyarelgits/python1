# Local RAG API with FastAPI and MCP

A ready-to-run local Retrieval-Augmented Generation (RAG) starter using
LangChain, LangGraph, ChromaDB, FastAPI, and the official MCP Python SDK.
Ollama runs the chat and embedding models locally. The API has a Swagger UI,
and an MCP server exposes the same question-answering graph as a tool.

The sample knowledge file is fictional. Add your own `.txt` documents under
`data/`; additional data files are ignored by Git so private documents are not
uploaded accidentally.

## Requirements

- Ubuntu 24.04 or another system with Python 3.11 or newer. The MCP SDK needs
  Python 3.11+.
- 8 GB RAM recommended for `llama3.2:3b`; use `llama3.2:1b` on smaller VMs.
- About 10 GB of free disk space for Python packages and Ollama models.
- Internet access for the initial software and model downloads.

## Download from GitHub

Run on the Ubuntu VM. This branch is the project branch; `main` may not contain
this work until it is merged.

```bash
git clone --branch hyarelgits-small-business-website https://github.com/hyarelgits/python1.git ubuntu-rag
cd ubuntu-rag
```

## Install Ubuntu prerequisites

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip curl ca-certificates
python3 --version
```

Python must be 3.11 or newer. Ubuntu 22.04 may include Python 3.10; use a
Python 3.12 environment managed by `uv` in that case, as described in
`ubuntu_rag_fastapi_mcp_guide.txt`.

## Create the Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
```

Keep the virtual environment active in each terminal where you run the app.

## Install and start Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
sudo systemctl enable --now ollama
```

Download the embedding model and one chat model:

```bash
ollama pull nomic-embed-text
ollama pull llama3.2:3b
```

For a lower-memory VM, use `ollama pull llama3.2:1b` instead of downloading
the 3B model. Set the chat model before starting either app process:

```bash
export RAG_CHAT_MODEL=llama3.2:1b
```

The default chat model is `llama3.2:3b`. The embedding model defaults to
`nomic-embed-text`.

## Add documents and build the index

The repository includes `data/knowledge.txt` as a small example. Add your
own plain UTF-8 `.txt` files under `data/`, then run:

```bash
python ingest.py
```

This creates the local `chroma_db/` folder. It is generated data and is not
tracked by Git. Run `python ingest.py` again after changing the documents.

## Run FastAPI

In a terminal with the virtual environment active:

```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` for Swagger UI. Use **POST /query** with:

```json
{
  "question": "When is the bakery open?"
}
```

The response contains the answer and source filenames. `GET /health` checks
that FastAPI is responding.

## Run the MCP server

Keep FastAPI running. Open a second terminal, activate the same virtual
environment, and run:

```bash
cd ~/ubuntu-rag
source .venv/bin/activate
python mcp_server.py
```

MCP clients connect to `http://127.0.0.1:8001/mcp` using Streamable HTTP. The
tool is named `ask_documents`. FastAPI and MCP are separate processes, and
both use the same local Chroma index and RAG graph.

To access either endpoint from your own computer, use SSH port forwarding
instead of exposing the VM ports to the public internet:

```bash
ssh -L 8000:127.0.0.1:8000 -L 8001:127.0.0.1:8001 USERNAME@VM_IP
```

## Project files

- `ingest.py`: loads, splits, embeds, and indexes `.txt` files.
- `app.py`: LangGraph workflow and FastAPI endpoints.
- `mcp_server.py`: MCP tool server using the same workflow.
- `rag_config.py`: shared model, collection, and path settings.
- `data/knowledge.txt`: fictional sample document.
- `ubuntu_rag_fastapi_mcp_guide.txt`: detailed step-by-step guide with
  troubleshooting instructions.

## Learning guides

The `learning/` folder contains separate beginner-to-expert guides:

- [Python](learning/python_learning.txt)
- [Machine Learning](learning/machine_learning_learning.txt)
- [Deep Learning](learning/deep_learning_learning.txt)
- [RAG](learning/rag_learning.txt)
- [ChromaDB](learning/chromadb_learning.txt)
- [PostgreSQL](learning/postgresql_learning.txt)
- [LangChain](learning/langchain_learning.txt)
- [LangGraph](learning/langgraph_learning.txt)
- [MCP](learning/mcp_learning.txt)
- [FastAPI](learning/fastapi_learning.txt)

Stop each running server with Ctrl+C in its terminal. Never commit private
documents, model files, or `chroma_db/`.
