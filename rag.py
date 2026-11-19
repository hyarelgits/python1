import chromadb

# 1. Store - Put loan data in ChromaDB
client = chromadb.Client()
collection = client.create_collection(name="loan_data")

collection.add(
    documents=[
        "Hyarel CIBIL 750 Approved Yes, Bought Sugar 90 and Oil 150",
        "Priya CIBIL 680 Approved Yes, Bought Rice 250",
        "Rahul CIBIL 550 Approved No, Bought Tea 50",
    ],
    ids=["1", "2", "3"]
)

# 2. Retrieve - User asks question
question = "What is Hyarel CIBIL and what did he buy?"
results = collection.query(query_texts=[question], n_results=1)

print("Question:", question)
print("Retrieved:", results['documents'][0][0])

# 3. Generate - Simple answer (In real project, LLM makes this nice)
print("Answer: Hyarel CIBIL 750, Approved Yes, Bought Sugar 90 and Oil 150")
