import joblib
import pandas as pd

from my_ml_project.utils.logger import get_logger


logger = get_logger(__name__)

logger.info("Loading ML model...")
model = joblib.load("src/my_ml_project/models/loan_model.pkl")
logger.info("Model loaded successfully.")


def predict_loan(data: dict):
    logger.info(f"Incoming prediction request: {data}")

    df = pd.DataFrame([data])

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    logger.info(
        f"Prediction complete | prediction={prediction} | probability={probability}"
    )

    return prediction, probability
