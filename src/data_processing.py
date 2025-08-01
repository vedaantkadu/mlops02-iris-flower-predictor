import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
import os
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class DataProcessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.processed_data_path = "artifacts/processed"
        os.makedirs(self.processed_data_path, exist_ok=True)

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            logger.info("Read the data successfully...")

            # Drop 'Id' column if it exists
            if 'Id' in self.df.columns:
                self.df.drop(columns=['Id'], inplace=True)
                logger.info("Dropped 'Id' column successfully.")
            else:
                logger.info("'Id' column not found, skipping drop step.")

        except Exception as e:
            logger.error(f"Error while reading data: {e}")
            raise CustomException("Failed to read data", e)

    def handle_outliers(self, column):
        try:
            logger.info("Starting handle outlier operation...")
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_value = Q1 - 1.5 * IQR
            upper_value = Q3 + 1.5 * IQR
            median = np.median(self.df[column])

            self.df[column] = self.df[column].apply(lambda x: median if x < lower_value or x > upper_value else x)

            logger.info("Handled outliers successfully.")
        except Exception as e:
            logger.error(f"Error while handling outliers: {e}")
            raise CustomException("Failed to handle outliers", e)

    def split_data(self):
        try:
            X = self.df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
            y = self.df["Species"]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            logger.info("Data split successfully.")

            joblib.dump(X_train, os.path.join(self.processed_data_path, "X_train.pkl"))
            joblib.dump(X_test, os.path.join(self.processed_data_path, "X_test.pkl"))
            joblib.dump(y_train, os.path.join(self.processed_data_path, "y_train.pkl"))
            joblib.dump(y_test, os.path.join(self.processed_data_path, "y_test.pkl"))

            logger.info("Files saved successfully for data processing step.")
        except Exception as e:
            logger.error(f"Error while splitting data: {e}")
            raise CustomException("Failed to split data", e)

    def run(self):
        self.load_data()
        self.handle_outliers("SepalWidthCm")
        self.split_data()

if __name__ == "__main__":
    data_processor = DataProcessing("artifacts/raw/data.csv")
    data_processor.run()
