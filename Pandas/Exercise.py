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

# ============================================================
# EXERCISE 1 - Series: label and position access
# a) Retrieve the population of Garissa using its label.
# b) Retrieve the population of Kitale using its integer position.
# c) Retrieve the populations of Mombasa, Kisumu and Malindi
#    using a list of labels.
# ============================================================

# Your answer:
print(population['Garissa'])                        # a) by label
print(population.iloc[9])                           # b) by position
print(population[['Mombasa', 'Kisumu', 'Malindi']]) # c) list of labels

# ============================================================
# EXERCISE 2 - Series: arithmetic and broadcasting
# a) Create a new Series called pop_millions that expresses
#    population in millions, rounded to 2 decimal places.
# b) Create another Series called pop_share that shows each
#    city's population as a percentage of the total population.
#    Round to 2 decimal places.
# ============================================================

# Your answer:
pop_millions = (population / 1_000_000).round(2)
print(pop_millions)

pop_share = ((population / population.sum()) * 100).round(2)
print(pop_share)

# ============================================================
# EXERCISE 3 - Series: alignment
# Create two small Series:
#   s1 = pd.Series([100, 200, 300], index=['A', 'B', 'C'])
#   s2 = pd.Series([10, 20, 30], index=['B', 'C', 'D'])
# Add them together and explain in a comment what happens
# to index A and index D in the result.
# ============================================================

# Your answer:
s1 = pd.Series([100, 200, 300], index=['A', 'B', 'C'])
s2 = pd.Series([10, 20, 30],  index=['B', 'C', 'D'])
print(s1 + s2)
# Index A only exists in s1, D only exists in s2.
# Both produce NaN because pandas can't find a matching value
# in the other Series to add to them.

# ============================================================
# EXERCISE 4 - DataFrame basics: selecting columns
# a) Select just the Temperature column (should return a Series).
# b) Select Temperature, Humidity and Rainfall together
#    (should return a DataFrame).
# c) Confirm the type of each result using type().
# ============================================================

# Your answer:
print(type(weather['Temperature']))             # a) Series
print(type(weather[['Temperature',
                     'Humidity', 'Rainfall']])) # b) DataFrame

# ============================================================
# EXERCISE 5 - DataFrame basics: adding columns
# a) Add a column called 'Heat Index' calculated as:
#    Temperature + (Humidity / 10)
# b) Add a column called 'Arid Flag' that is True where
#    Category == 'Arid' and False everywhere else.
#    Do this without using np.where - just use a boolean condition.
# ============================================================

# Your answer:
weather['Heat Index'] = weather['Temperature'] + (weather['Humidity'] / 10)
weather['Arid Flag']  = weather['Category'] == 'Arid'
print(weather)

# ============================================================
# EXERCISE 6 - DataFrame basics: dropping
# a) Drop the 'Wind Speed' column. Make it permanent.
# b) Drop the rows for Garissa and Malindi. Make it permanent.
# c) Print the shape of the DataFrame before and after
#    to confirm the drops worked.
# ============================================================

# Your answer:
print("Before:", weather.shape)
weather.drop('Wind Speed', axis=1, inplace=True)
weather.drop(['Garissa', 'Malindi'], axis=0, inplace=True)
print("After: ", weather.shape)
print(weather)

# ============================================================
# EXERCISE 7 - Indexing: .loc and .iloc
# a) Use .loc to get the full row for Thika.
# b) Use .iloc to get the same row by position.
# c) Use .loc to get the Humidity value for Nyeri.
# d) Use .loc to get Temperature and Rainfall for
#    Nairobi, Kisumu and Nakuru.
# ============================================================

# Your answer:
print(weather.loc['Thika'])                                    # a)
print(weather.iloc[5])                                         # b) Thika is at position 5
print(weather.loc['Nyeri', 'Humidity'])                        # c)
print(weather.loc[['Nairobi','Kisumu','Nakuru'],               # d)
                  ['Temperature', 'Rainfall']])

# ============================================================
# EXERCISE 8 - Indexing: slicing with .iloc
# Use .iloc to select the first 4 rows and first 3 columns
# of the DataFrame. (No labels - integers only.)
# ============================================================

# Your answer:
print(weather.iloc[:4, :3])

# ============================================================
# EXERCISE 9 - Conditional filtering: single condition
# a) Filter to show only cities where Temperature > 25.
# b) Filter to show only cities where Humidity is
#    between 60 and 75 (inclusive).
# ============================================================

# Your answer:
print(weather[weather['Temperature'] > 25])                    # a)
print(weather[(weather['Humidity'] >= 60) &
              (weather['Humidity'] <= 75)])                     # b)

# ============================================================
# EXERCISE 10 - Conditional filtering: multiple conditions
# a) Show cities that are Coastal AND have Humidity > 83.
# b) Show cities that are either Arid OR have
#    Temperature below 20.
# c) Show all Inland cities with Temperature above 22,
#    displaying only their Temperature and Humidity columns.
# ============================================================

# Your answer:
print(weather[(weather['Category'] == 'Coastal') &
              (weather['Humidity'] > 83)])  # a)

print(weather[(weather['Category'] == 'Arid') |
              (weather['Temperature'] < 20)])  # b)

inland_warm = weather[(weather['Category'] == 'Inland') &
                      (weather['Temperature'] > 22)]
print(inland_warm[['Temperature', 'Humidity']])  # c)

# ============================================================
# EXERCISE 11 - Missing data
# a) Find how many missing values exist in each column.
# b) Drop any rows where Rainfall is missing.
#    Do not use inplace - assign back to the DataFrame.
# c) Confirm the missing values are gone.
# d) How many rows remain? Print the shape to confirm.
# ============================================================

# Your answer:


# ============================================================
# EXERCISE 12 - Missing data: filling
# Reset the DataFrame by re-running the setup, then:
# a) Fill missing Rainfall values with the median
#    of the Rainfall column (not the mean this time).
# b) Fill missing values in the entire DataFrame with 0
#    using a single line. Assign back - do not use inplace.
#    Print the result to confirm no NaNs remain.
# ============================================================

# Your answer:


# ============================================================
# EXERCISE 13 - GroupBy: basic aggregation
# a) Group by Category and calculate the mean of
#    Temperature, Humidity, and Rainfall.
# b) Group by Category and find the city with the
#    highest Temperature in each group.
#    (hint: use .idxmax() after groupby)
# ============================================================

# Your answer:


# ============================================================
# EXERCISE 14 - GroupBy: multiple aggregations
# Group by Category and compute the following for Temperature:
# mean, min, max, and count - all in one operation.
# (hint: use .agg() with a list)
# ============================================================

# Your answer:


# ============================================================
# EXERCISE 15 - Reading and writing CSVs
# a) Save the weather DataFrame to a CSV called
#    'kenya_weather.csv'. The index (city names) should
#    be saved as a column labelled 'City'.
# b) Read it back into a new variable called df_loaded,
#    with 'City' set as the index.
# c) Use .equals() to check if df_loaded matches weather.
#    Print the result and explain in a comment why they
#    might not be exactly equal even if the data looks the same.
# ============================================================

# Your answer:
