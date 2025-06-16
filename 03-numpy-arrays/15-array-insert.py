"""
Syntax:
    np.insert(array, index, values, axis=None)

Parameters:
- array : original array
- index : index before which to insert
- values : value(s) to insert
- axis :
    - None → flatten the array before inserting
    - 0 → insert row-wise
    - 1 → insert column-wise
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Insert 100 at index 2
new_arr = np.insert(arr, 2, 100)

print("1D Insertion:")
print(new_arr)  # Output: [10 20 100 30 40 50]

# 2D Array Example (Row-wise Insertion)
arr_2d = np.array([[1, 2], [3, 4]])

# Insert a new row [5, 6] at index 1 (axis=0)
new_arr_2d_row = np.insert(arr_2d, 1, [5, 6], axis=0)

print("\n2D Row-wise Insertion:")
print(new_arr_2d_row)
# Output:
# [[1 2]
#  [5 6]
#  [3 4]]