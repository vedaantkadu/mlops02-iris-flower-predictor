from src.data_processing import DataProcessing
from src.model_training import ModelTraining
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

def run_pipeline():
    try:
        logger.info("🚀 Starting the training pipeline...")
        
        # Step 1: Data Preprocessing
        data_preprocessor = DataProcessing(file_path="artifacts/raw/data.csv")
        data_preprocessor.run()

        # Step 2: Model Training
        model_trainer = ModelTraining()
        model_trainer.run()

        logger.info("✅ Training pipeline completed successfully.")

    except Exception as e:
        logger.error(f"❌ Pipeline failed due to: {e}")
        raise CustomException("Pipeline execution failed", e)

if __name__ == "__main__":
    run_pipeline()
