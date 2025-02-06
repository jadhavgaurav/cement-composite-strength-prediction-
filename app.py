from flask import Flask, render_template, request, redirect
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        features = [
            float(request.form["cement"]),
            float(request.form["blast_furnace_slag"]),
            float(request.form["fly_ash"]),
            float(request.form["water"]),
            float(request.form["superplasticizer"]),
            float(request.form["coarse_aggregate"]),
            float(request.form["fine_aggregate"]),
            float(request.form["age"]),
        ]

        # Reshape and predict
        prediction = model.predict([np.array(features)])[0]
        return render_template(
            "index.html",
            prediction=round(prediction, 2)
        )
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
