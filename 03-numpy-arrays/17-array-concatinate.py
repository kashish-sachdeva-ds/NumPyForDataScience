# np.concatenate(arr1, arr2, axis = 0)

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.concatenate((arr1, arr2))
print("Concatenated Array:")
print(new_arr)  # Output: [1 2 3 4 5 6]