from flask import Flask, render_template, request
from pipeline.predict_pipeline import PredictionPipeline  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            # Read and sanitize inputs (replace commas with dots)
            sepal_length = float(request.form['SepalLengthCm'].replace(',', '.'))
            sepal_width = float(request.form['SepalWidthCm'].replace(',', '.'))
            petal_length = float(request.form['PetalLengthCm'].replace(',', '.'))
            petal_width = float(request.form['PetalWidthCm'].replace(',', '.'))

            input_data = {
                "SepalLengthCm": sepal_length,
                "SepalWidthCm": sepal_width,
                "PetalLengthCm": petal_length,
                "PetalWidthCm": petal_width
            }

            predictor = PredictionPipeline()
            prediction = predictor.predict(input_data)

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
