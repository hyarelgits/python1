from fastapi import FastAPI
import pickle

app = FastAPI()
model = pickle.load(open('loan_model.pkl', 'rb'))

@app.get("/")
def home():
    return {"message": "Loan AI is running"}

@app.get("/predict/{cibil}")
def predict(cibil: int):
    result = model.predict([[cibil]])
    return {"cibil": cibil, "approved": int(result[0])}
