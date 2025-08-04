# UrbanCarbonAI

A simple carbon emissions predictor for urban environments using mock data. Supports Flask API interaction.

## Run Locally

```bash
pip install -r requirements.txt
python main.py
```

## Run the API

After running the script, visit: http://localhost:5000


## API Example

### POST `/predict`

Send a JSON payload to get a carbon emission prediction:

**Request Example:**

```json
{
  "population_density": 5000,
  "public_transit_score": 75,
  "green_spaces": 20,
  "energy_source_coal": 30,
  "energy_source_renewable": 40,
  "avg_vehicle_age": 6.5
}
```

## Response Example:

```json
{
  "predicted_emissions": 3.25
}
```