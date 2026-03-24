import numpy as np
import pandas as pd

# Raw data in different Python formats
labels  = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr     = np.array(my_data)
d       = {'a': 10, 'b': 20, 'c': 30}


# Creating a Series

# From a list - auto integer index (0, 1, 2)
print(pd.Series(data=my_data))

# From a list + explicit labels
print(pd.Series(data=my_data, index=labels))
print(pd.Series(my_data, labels))   # positional args, same result

# From a NumPy array + labels
print(pd.Series(arr, labels))

# From a dict - keys become the index automatically
print(pd.Series(d))

# Series of strings
print(pd.Series(data=labels))

# A Series can hold any Python object, even functions
print(pd.Series(data=[sum, print, len]))


# Accessing values

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR',  'Japan'])
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
ser3 = pd.Series(labels)

# Access by label
print(ser1['USA'])

# Access by integer position (when index is integers)
print(ser3[0])


# Series arithmetic - Pandas aligns by index label before operating.
# Labels with no match in the other Series produce NaN (missing value).
print(ser1 + ser2)