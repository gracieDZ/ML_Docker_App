from flask import Flask, request, jsonify
import pandas as pd
import xgboost as xgb
import joblib

app = Flask(__name__)

# Load a pre-trained model (you can train and save it with joblib)
model = joblib.load("model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
