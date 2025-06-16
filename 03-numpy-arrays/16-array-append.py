"""
NumPy Array Appending using np.append()

Syntax:
    np.append(array, values, axis=None)

- Appends values to the end of an array.
- If axis is None (default), array is flattened before appending.
"""

import numpy as np

arr = np.array([10, 20, 30])

# Append values to the end
new_arr = np.append(arr, [40, 50])

print("1D Append:")
print(new_arr)  # Output: [10 20 30 40 50]