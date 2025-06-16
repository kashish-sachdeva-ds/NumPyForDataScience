"""
NumPy Array Slicing

Slicing is used to extract a portion of an array using the format:
    arr[start:stop:step]

Notes:
- Start index is **inclusive**
- Stop index is **exclusive**
- Step is optional (default is 1)
- Negative step reverses the array
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(arr[2:5])     # Output: [30 40 50]
print(arr[:4])      # Output: [10 20 30 40]
print(arr[4:])      # Output: [50 60 70 80 90]
print(arr[1:7:2])   # Output: [20 40 60]
print(arr[::3])     # Output: [10 40 70]
print(arr[::-1])    # Output: [90 80 70 60 50 40 30 20 10]