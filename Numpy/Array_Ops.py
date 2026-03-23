import numpy as np
#
# #ARRAY OPERATIONS — vectorized (no loops needed!)
# a = np.array([1, 2, 3, 4])
# b = np.array([10, 20, 30, 40])
#
# print(a + b)                 # [11 22 33 44]
# print(a * b)                 # [10 40 90 160]
# print(a ** 2)                # [ 1  4  9 16]
# print(np.sqrt(a))            # [1.  1.41 1.73 2. ]
#
# # Scalar operations (broadcast to every element):
# print(a * 3)                 # [ 3  6  9 12]
# print(a + 100)               # [101 102 103 104]
#
# #USEFUL ARRAY METHODS
# data = np.array([3, 1, 4, 1, 5, 9, 2, 6])
#
# print(data.sum())            # 31
# print(data.mean())           # 3.875
# print(data.std())            # Standard deviation
# print(data.var())            # Variance
# print(np.median(data))       # 3.5
# print(np.sort(data))         # [1 1 2 3 4 5 6 9] — sorted copy
# print(np.unique(data))       # [1 2 3 4 5 6 9]   — unique values
#
# # Axis-based operations on 2D arrays
# mat = np.array([[1,2,3],[4,5,6]])
# print(mat.sum(axis=0))       # Column sums → [5 7 9]
# print(mat.sum(axis=1))       # Row sums    → [6 15]
#
#
#
# #SHAPE MANIPULATION
# arr = np.arange(12)
# print(arr.reshape(3, 4))     # 3 rows, 4 cols
# print(arr.reshape(2, 6))     # 2 rows, 6 cols
# print(arr.reshape(3, 4).flatten())   # Back to 1D → [0 1 2 ... 11]
#
# # Stacking arrays
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.vstack([a, b]))     # Vertical stack → 2x3 matrix
# print(np.hstack([a, b]))     # Horizontal stack → [1 2 3 4 5 6]
#
# #np.where — conditional element selection
# #np.where(condition, value_if_true, value_if_false)v
# temps = np.array([22, 35, 18, 40, 28, 15])
# labels = np.where(temps > 30, "Hot", "OK")
# print(labels)                # ['OK' 'Hot' 'OK' 'Hot' 'OK' 'OK']
#
# # Real satellite data use case:
# ndvi = np.array([0.1, 0.6, -0.05, 0.75, 0.3])
# land_type = np.where(ndvi > 0.5, "Vegetation", "Non-vegetation")
# print(land_type)
#

a = np.array([1, 2])
b = np.array([4,5,6])

print(np.hstack([a,b]))

