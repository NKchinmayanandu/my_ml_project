from fastapi import FastAPI
from my_ml_project.api.predict import router as predict_router

app = FastAPI()

app.include_router(predict_router)

@app.get("/")
def home():
    return {"message": "Loan Prediction API running"}

