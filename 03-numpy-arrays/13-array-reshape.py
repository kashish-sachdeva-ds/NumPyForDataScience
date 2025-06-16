"""
The reshape() function changes the shape of the array 
without changing the data. It returns a view (not a copy), 
which means changes in the reshaped array can affect the original.
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into 2 rows and 3 columns
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)

# Output:
# [[1 2 3]
#  [4 5 6]]