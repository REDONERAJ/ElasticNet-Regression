from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the pre-trained model once
print("Loading model...")
model = joblib.load("elasticnet_carprice_model.pkl")
print("✅ Model loaded successfully.")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print("Received request:", request.method)
    prediction = None
    if request.method == "POST":
        try:
            # Get form inputs
            values = [
                float(request.form["carwidth"]),
                float(request.form["curbweight"]),
                float(request.form["enginesize"]),
                float(request.form["horsepower"]),
                float(request.form["citympg"])
            ]
            # Predict
            prediction = model.predict(np.array([values]))[0]
            prediction = round(prediction, 2)
            print(f"Prediction: {prediction}")
        except Exception as e:
            prediction = "Invalid input"
            print("Error:", e)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=5001)
