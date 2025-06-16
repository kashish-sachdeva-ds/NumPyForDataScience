"""
NumPy Indexing (1D Arrays)

Indexing allows you to access specific elements in an array using their position.
Indexing starts from 0 (just like in Python lists).
You can also use negative indexing to access elements from the end.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])    # Output: 10 → first element
print(arr[2])    # Output: 30 → third element
print(arr[-1])   # Output: 50 → last element (negative indexing)