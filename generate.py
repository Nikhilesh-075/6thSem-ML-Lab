import numpy as np
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 1000

longitude = np.random.uniform(-124, -113, n_samples)  # Longitude (West Coast of USA)
latitude = np.random.uniform(32, 42, n_samples)  # Latitude (West Coast of USA)

housing_median_age = np.random.randint(1, 52, n_samples)  # Housing median age (years)
total_rooms = np.random.randint(500, 5000, n_samples)  # Total rooms
total_bedrooms = np.random.randint(100, 1500, n_samples)  # Total bedrooms
population = np.random.randint(500, 10000, n_samples)  # Population of the area
households = np.random.randint(100, 3000, n_samples)  # Number of households

median_income = np.random.uniform(1, 15, n_samples)  # Median income (in $1000s)
median_house_value = (median_income * 50000 + total_rooms * 5 + population * 10 +
                      np.random.normal(0, 100000, n_samples))  # Median house value (target variable)

# Create a DataFrame
data = pd.DataFrame({
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income,
    'median_house_value': median_house_value
})

# Show the first few rows
data.head()
