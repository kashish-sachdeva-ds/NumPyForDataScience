import numpy as np

# Split 1D array into 2 equal parts
arr = np.array([10, 20, 30, 40, 50, 60])
print("Split into 2 parts:", np.split(arr, 2))
# [array([10, 20, 30]), array([40, 50, 60])]



# 2D Array
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Horizontal Split (split columns)
print("\nHorizontal Split:\n", np.hsplit(arr_2d, 2))

# Vertical Split (split rows)
print("\nVertical Split:\n", np.vsplit(arr_2d, 2))