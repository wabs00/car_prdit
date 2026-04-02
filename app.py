from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html", prediction_text=None, values={})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = {
            "Engine volume": float(request.form["engine"]),
            "Mileage": float(request.form["mileage"]),
            "Cylinders": float(request.form["cylinders"]),
            "Prod. year": float(request.form["year"]),
            "Levy": float(request.form["levy"]),
        }

        df = pd.DataFrame([data], columns=model.feature_names_in_)
        pred_value = max(0, np.ravel(model.predict(df))[0])

        return render_template(
            "index.html",
            prediction_text=f"Estimated Price: {pred_value:,.2f}",
            values=data,
        )
    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}",
            values={},
        )

if __name__ == "__main__":
    app.run(debug=True)