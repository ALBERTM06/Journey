import numpy as np
import pandas as pd

# ============================================================
# PANDAS EXERCISES
# Work through each exercise and write your answer below it.
# Run the setup code first before attempting any exercise.
# ============================================================


# SETUP - run this before all exercises
np.random.seed(42)

locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret',
             'Thika', 'Malindi', 'Nyeri', 'Garissa', 'Kitale']

weather = pd.DataFrame({
    'Temperature': [24.5, 30.1, 27.3, 19.8, 18.2, 23.1, 31.5, 20.4, 38.2, 21.3],
    'Humidity': [65, 82, 74, 60, 55, 68, 85, 63, 30, 58],
    'Rainfall': [45.2, 120.5, 98.3, 30.1, None, 55.4, 140.2, 42.0, None, 60.3],
    'Wind Speed': [12.3, 18.7, 10.2, 15.4, 22.1, 11.0, 20.5, 9.8, 25.3, 13.7],
    'Category': ['Inland', 'Coastal', 'Lakeside', 'Inland', 'Inland',
                 'Inland', 'Coastal', 'Inland', 'Arid', 'Inland']
}, index=locations)

population = pd.Series(
    [4500000, 1200000, 600000, 570000, 475000,
     350000, 120000, 160000, 190000, 210000],
    index=locations
)
