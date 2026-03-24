import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# Creating a DataFrame - pd.DataFrame(data, row_labels, col_labels)
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])
print(df)

# Selecting columns
# Single column returns a Series
print(df['W'])
print(type(df['W']))

# Multiple columns - pass a list, returns a smaller DataFrame
print(df[['W', 'Z']])

# Adding and dropping columns
# New column from an operation on existing ones
df['AA'] = df['W'] + df['Y']
print(df)

# drop() doesn't modify df by default - use inplace=True to make it stick
df.drop('AA', axis=1, inplace=True)

# Dropping a row - axis=0 is default so you can omit it
df.drop('E')    # not inplace, just showing the result

# Selecting rows
# .loc[] uses the row label
print(df.loc['C'])

# .iloc[] uses the integer position
print(df.iloc[2])

# Selecting specific values and subsets
# Single value - row then column
print(df.loc['B', 'Y'])
print(df.iloc[1, 2])
# Subset using lists of labels or positions
print(df.loc[['A','B'], ['W','Y']])
print(df.iloc[[0,1], [0,2]])