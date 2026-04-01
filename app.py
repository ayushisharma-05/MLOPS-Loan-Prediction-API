from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Loan Prediction API"}

@app.post("/predict")
def predict(income: float, loan_amount: float):
    features = np.array([[income, loan_amount]])
    prediction = model.predict(features)[0]
    
    return {
        "approved": int(prediction)
    }