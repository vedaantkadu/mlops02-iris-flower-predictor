from pipeline.predict_pipeline import PredictionPipeline

if __name__ == "__main__":
    input_data = {
        "SepalLengthCm": 5.1,
        "SepalWidthCm": 3.5,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2
    }

    pipeline = PredictionPipeline()
    result = pipeline.predict(input_data)
    print("🌸 Predicted Species:", result)
