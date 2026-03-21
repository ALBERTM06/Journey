import numpy as np

#
# #INDEXING 1D ARRAYS (works like Python lists)
# arr = np.arange(0, 11)

# print("Array:", arr)         # [ 0  1  2  3  4  5  6  7  8  9 10]
#
# print(arr[0])                # First element → 0
# print(arr[-1])               # Last element  → 10
# print(arr[3])                # Index 3       → 3
#
# #SLICING 1D ARRAYS  →  arr[start:stop:step]
# #stop is EXCLUSIVE (not included)
# print(arr[1:5])              # [1 2 3 4]      — index 1 up to (not including) 5
# print(arr[:4])               # [0 1 2 3]      — from start up to index 4
# print(arr[5:])               # [5 6 7 8 9 10] — from index 5 to end
# print(arr[::2])              # [0 2 4 6 8 10] — every 2nd element
# print(arr[::-1])             # [10 9 8 ... 0] — reversed!
#
# #BROADCAST ASSIGNMENT (unique to NumPy!)
# for i in range(0,5):
#     arr[i] = 99
# print(arr)

# #Slices are VIEWS, not copies — changes affect original

# arr_copy = arr.copy()        # Always .copy() if you want independence
# arr_copy[0:5] = 99           # Sets indices 0-4 to 99 at once
# print(arr_copy)              # [99 99 99 99 99  5  6  7  8  9 10]
# # Original arr is untouched because we used .copy()
#
# #INDEXING 2D ARRAYS  →  arr[row, col]
# #    Think of it as a spreadsheet: rows first, columns second
# matrix = np.array([
#     [10, 20, 30],   # row 0
#     [40, 50, 60],   # row 1
#     [70, 80, 90]    # row 2
# ])
#
# print(matrix[0])             # Entire row 0  → [10 20 30]
# print(matrix[1][2])          # Row 1, col 2  → 60  (Python-style)
# print(matrix[1, 2])          # Row 1, col 2  → 60  (NumPy-style, preferred)
# print(matrix[0, 0])          # Top-left      → 10
# print(matrix[-1, -1])        # Bottom-right  → 90
#
# # 5. SLICING 2D ARRAYS  →  arr[row_slice, col_slice]
# print(matrix[:2, 1:])        # Rows 0-1, columns 1-2:
#                              # [[20 30]
#                              #  [50 60]]
#
# print(matrix[:, 1])          # ALL rows, column 1 only → [20 50 80]
# print(matrix[1, :])          # Row 1, ALL columns     → [40 50 60]
#
# #FANCY INDEXING — select specific rows/cols by index list
# arr2d = np.arange(50).reshape(5, 10)
# print(arr2d)
# #Select rows 1, 3, and 0 (in that order):
# print(arr2d[[1, 3, 0]])
# # Select specific (row, col) pairs:
# rows = [0, 1, 2]
# cols = [0, 1, 2]
# print(arr2d[rows, cols])     # → diagonal: arr2d[0,0], arr2d[1,1], arr2d[2,2]
#
#BOOLEAN / CONDITIONAL INDEXING
#Returns elements that satisfy a condition
# scores = np.array([45, 82, 67, 91, 55, 78, 39, 88])
# mask = scores > 70           # array([F, T, F, T, F, T, F, T])
# print(scores[mask])          # [82 91 78 88] — only scores above 70
# print(scores[scores < 50])   # [45 55 39]   — inline version
#
# Useful for data filtering (you'll use this a LOT in data science):
ndvi_values = np.array([0.1, 0.65, 0.3, 0.8, -0.1, 0.72])
vegetation = ndvi_values[ndvi_values > 0.5]   # Only green areas
#print("Vegetation pixels:", vegetation)        # [0.65 0.8  0.72]

print(np.unique(ndvi_values))

