"""
Syntax:
    np.delete(arr, index, axis=None)

- arr: input array
- index: position to delete
- axis: 
    - None (default) → flatten array before deletion
    - 0 → delete row
    - 1 → delete column
"""

import numpy as np

# 1D Array Deletion
arr = np.array([10, 20, 30, 40, 50])
print("Original 1D Array:")
print(arr)

new_arr = np.delete(arr, 2)  # Delete element at index 2
print("After deleting index 2:")
print(new_arr)  # Output: [10 20 40 50]



# 2D Array Deletion
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nOriginal 2D Array:")
print(arr_2d)

# Delete second row (index 1)
new_arr_2d_row = np.delete(arr_2d, 1, axis=0)
print("\nAfter deleting row at index 1:")
print(new_arr_2d_row)

# Output:
# [[1 2 3]]


# Delete second column (index 1)
new_arr_2d_col = np.delete(arr_2d, 1, axis=1)
print("\nAfter deleting column at index 1:")
print(new_arr_2d_col)

# Output:
# [[1 3]
#  [4 6]]