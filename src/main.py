from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

try:
    model_pipline = joblib.load("../models/final_pipeline.pkl")
except Exception as e:
    print(f"Model pipline not found, trying to load model from {e}")

@app.get("/")
def home():
    return {"message": "Model loaded"}

class Model_Input(BaseModel):
    Gender: str
    Customer_Type: str
    Age: int
    Type_of_Travel: str
    Class: str
    Flight_Distance: int
    Inflight_wifi_service: int
    Departure_Arrival_time_convenient: int
    Ease_of_Online_booking: int
    Gate_location: int
    Food_and_drink: int
    Online_boarding: int
    Seat_comfort: int
    Inflight_entertainment: int
    On_board_service: int
    Leg_room_service: int
    Baggage_handling: int
    Checkin_service: int
    Inflight_service: int
    Cleanliness: int
    Departure_Delay_in_Minutes: int
    Arrival_Delay_in_Minutes: float

class PredictionOutput(BaseModel):
    prediction: int
    satisfaction_label: str
    probability: float
    threshold: float