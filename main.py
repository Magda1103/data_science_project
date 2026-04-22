from fastapi import FastAPI
import joblib

app = FastAPI()

try:
    model_pipline = joblib.load("models/final_pipline.pkl")
except Exception as e:
    print(f"Model pipline not found, trying to load model from {e}")

@app.get("/")
def home():
    return {"message": "Model loaded"}