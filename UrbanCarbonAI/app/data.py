import pandas as pd
import numpy as np

def generate_mock_data(n_samples=500):
    np.random.seed(42)
    population_density = np.random.randint(1000, 10000, n_samples)
    public_transit = np.random.randint(30, 90, n_samples)
    green_spaces = np.random.randint(5, 30, n_samples)
    coal_energy = np.random.randint(10, 60, n_samples)
    renewable_energy = np.random.randint(10, 50, n_samples)
    vehicle_age = np.random.uniform(3, 12, n_samples)

    emissions = (
        0.0001 * population_density +
        0.5 * (100 - public_transit) +
        0.3 * (30 - green_spaces) +
        0.05 * coal_energy -
        0.03 * renewable_energy +
        0.1 * vehicle_age +
        np.random.normal(0, 0.5, n_samples)
    )

    emissions = np.abs(emissions)

    return pd.DataFrame({
        "city_id": range(1, n_samples + 1),
        "population_density": population_density,
        "public_transit_score": public_transit,
        "green_spaces": green_spaces,
        "energy_source_coal": coal_energy,
        "energy_source_renewable": renewable_energy,
        "avg_vehicle_age": vehicle_age,
        "carbon_emissions": emissions
    })
