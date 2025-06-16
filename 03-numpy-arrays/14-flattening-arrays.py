"""
- ravel(): returns a view (if possible) → original array can be affected
- flatten(): returns a copy → completely independent from the original
"""

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.ravel())     # Output: [1 2 3 4 5 6]
print(arr_2d.flatten())   # Output: [1 2 3 4 5 6]



#checking the difference between ravel() and flatten()

a = np.array([[10, 20], [30, 40]])
r = a.ravel()
f = a.flatten()

r[0] = 99
f[1] = 88

print("Original:", a)  # Only ravel() changed the original