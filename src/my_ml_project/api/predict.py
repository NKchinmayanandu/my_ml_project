from fastapi import APIRouter
from my_ml_project.services.inference import predict_loan
from my_ml_project.api.schemas import LoanRequest

router = APIRouter()

@router.post("/predict")
def predict(data: LoanRequest):
    prediction, probability = predict_loan(data.dict())

    return {
        "prediction": prediction,
        "probability": probability
    }
