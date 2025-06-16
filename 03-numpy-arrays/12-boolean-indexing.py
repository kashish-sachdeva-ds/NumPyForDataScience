"""
Boolean Indexing in NumPy

Boolean indexing lets you filter elements based on conditions.
It returns a new array containing only the elements where the condition is True.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 30])   # Output: [40 50]
print(arr[arr < 30])   # Output: [10 20]