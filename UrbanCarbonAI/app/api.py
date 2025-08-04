from flask import Flask, request, jsonify
import pandas as pd
import joblib

def create_app(model_path="carbon_emission_model.pkl"):
    app = Flask(__name__)
    model = joblib.load(model_path)

    @app.route("/")
    def home():
        return """
        <h1>Carbon Emission Prediction API</h1>
        <p>Send POST requests to /predict with JSON data:</p>
        <pre>{
            "population_density": 5000,
            "public_transit_score": 75,
            "green_spaces": 20,
            "energy_source_coal": 30,
            "energy_source_renewable": 40,
            "avg_vehicle_age": 6.5
        }</pre>
        """

    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            data = request.get_json()
            required = [
                "population_density", "public_transit_score", "green_spaces",
                "energy_source_coal", "energy_source_renewable", "avg_vehicle_age"
            ]
            for field in required:
                if field not in data:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            df = pd.DataFrame([data])
            prediction = model.predict(df)[0]
            return jsonify({
                "predicted_emissions": round(prediction, 2),
                "units": "tons CO₂ per capita"
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app
