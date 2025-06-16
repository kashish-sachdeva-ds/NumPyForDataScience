import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vertical Stack (row-wise)
v_stack = np.vstack((arr1, arr2))
print("Vertical Stack:\n", v_stack)
# [[1 2 3]
#  [4 5 6]]

# Horizontal Stack (column-wise)
h_stack = np.hstack((arr1, arr2))
print("\nHorizontal Stack:\n", h_stack)
# [1 2 3 4 5 6]