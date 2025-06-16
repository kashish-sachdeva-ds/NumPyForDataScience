"""
Fancy Indexing in NumPy

Fancy indexing allows you to select multiple specific elements from an array
using a list or array of indices.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(arr[[0, 2, 4]])   # Output: [10 30 50]
print(arr[[1, 3, 5]])   # Output: [20 40 60]