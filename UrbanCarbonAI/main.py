from app.data import generate_mock_data
from app.model import train_model
from app.api import create_app

import os

if __name__ == "__main__":
    print("Training model and launching API...")
    df = generate_mock_data()
    X = df.drop(["city_id", "carbon_emissions"], axis=1)
    y = df["carbon_emissions"]

    model = train_model(X, y)

    app = create_app()
    app.run(debug=True, port=5000)
