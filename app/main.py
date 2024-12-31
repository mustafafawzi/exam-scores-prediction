from fastapi import FastAPI
from schemas import PredictionRequest
from models import get_model_prediction

# Create an instance of the FastAPI app
app = FastAPI()

# Endpoint for predictions
@app.post("/predict")
def predict(request: PredictionRequest):
    result = get_model_prediction(request)
    return result
