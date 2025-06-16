"""
NumPy Array Properties

This script demonstrates basic properties of NumPy arrays:
- ndim     : number of dimensions
- shape    : dimensions of the array (rows, columns, etc.)
- size     : total number of elements
- dtype    : data type of each element
- astype   : convert array to a different data type
"""

import numpy as np

# 1. .ndim → Number of dimensions
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])

print(arr_1d.ndim)   # Output: 1
print(arr_2d.ndim)   # Output: 2
print(arr_3d.ndim)   # Output: 3


# 2. .shape → Tuple of shape (rows, columns)
arr_shape = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_shape.shape)   # Output: (2, 3)


# 3. .size → Total number of elements
arr_size = np.array([[10, 20, 30], [40, 50, 60]])

print(arr_size.size)     # Output: 6


# 4. .dtype → Data type of array elements
arr_dtype = np.array([10, 20, 30.5, 40])

print(arr_dtype.dtype)   # Output: float64


# 5. .astype() → Convert array to different data type
float_arr = np.array([1.2, 2.3, 3.8])
int_arr = float_arr.astype(int)

print(float_arr.dtype)    # Output: float64
print(int_arr)            # Output: [1 2 3]
print(int_arr.dtype)      # Output: int64