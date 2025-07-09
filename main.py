from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the second best model and label encoder
model = joblib.load("RidgeModel.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():

    if request.method == "POST":
        # Collect form data - fixed variable names to match house price prediction
        location = request.form["location"]
        bhk = request.form["bhk"]
        total_sqft = request.form["total_sqft"]
        bath = request.form["bath"]

        # Debug: print received input
        print(f"Received input:")
        print(f"  location: {location}")
        print(f"  bhk: {bhk}")
        print(f"  total_sqft: {total_sqft}")
        print(f"  bath: {bath}")

        # Prepare input as DataFrame for pipeline
        input_df = pd.DataFrame({
            'location': [location],
            'bhk': [bhk],
            'total_sqft': [float(total_sqft) if total_sqft else 0],
            'bath': [int(bath) if bath else 0]
        })

        # Debug: print prepared DataFrame
        print(f"Prepared DataFrame:")
        print(input_df)

        # Predict using the loaded model (pipeline)
        prediction = model.predict(input_df)[0]
        
        # Debug: print the prediction to console
        print(f"Predicted price: {prediction}")
        
        return render_template(
            "index.html",
            prediction=f"₹{prediction:,.2f} Lakhs",
            location=location,
            bhk=bhk,
            total_sqft=total_sqft,
            bath=bath
        )

    # For GET, set all fields to empty strings
    return render_template(
        "index.html",
        prediction=None,
        area_type="",
        availability="",
        location="",
        size="",
        society="",
        total_sqft="",
        bath="",
        balcony=""
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
