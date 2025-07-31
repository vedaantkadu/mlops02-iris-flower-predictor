import pandas as pd
import joblib
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class PredictionPipeline:
    def __init__(self):
        try:
            model_path = "artifacts/models/model.pkl"
            self.model = joblib.load(model_path)
            logger.info("Model loaded successfully from model.pkl")
        except Exception as e:
            logger.exception("Failed to load the model.")
            raise CustomException("Error in loading model", e)

    def predict(self, input_data: dict):
        try:
            # Convert input data dictionary to DataFrame
            df = pd.DataFrame([input_data])
            logger.info(f"Input DataFrame: \n{df}")

            # Run prediction
            prediction = self.model.predict(df)[0]
            logger.info(f"Prediction: {prediction}")
            return prediction

        except Exception as e:
            logger.exception("Prediction failed.")
            raise CustomException("Error in prediction", e)
