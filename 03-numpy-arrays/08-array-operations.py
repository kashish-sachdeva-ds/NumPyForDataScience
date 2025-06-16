"""
NumPy Array Operations

This script covers all essential NumPy operations:
1. Arithmetic operations
2. Comparison operations
3. Aggregate functions (min, max, sum, mean, std - standard deviation, var - variance)
4. Vectorized operations between arrays
"""

import numpy as np

# 1. Arithmetic Operations (element-wise)
arr = np.array([10, 20, 30])

print(arr + 5)    # [15 25 35]
print(arr - 5)    # [ 5 15 25]
print(arr * 2)    # [20 40 60]
print(arr / 2)    # [ 5. 10. 15.]
print(arr % 7)    # [3 6 2]
print(arr ** 2)   # [100 400 900]


# 2. Comparison Operations (returns boolean arrays)
print(arr > 15)    # [False  True  True]
print(arr == 20)   # [False  True  False]
print(arr <= 25)   # [ True  True False]


# 3. Aggregate Functions
print(np.sum(arr))     # 60
print(np.mean(arr))    # 20.0
print(np.min(arr))     # 10
print(np.max(arr))     # 30
print(np.std(arr))     # 7.637626158259412
print(np.var(arr))     # 58.666666666666664


# 4. Vectorized Operations Between Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])

print(arr1 + arr2)     # [11 22 33]
print(arr2 - arr1)     # [ 9 18 27]
print(arr1 * arr2)     # [10 40 90]
print(arr2 / arr1)     # [10. 10. 10.]


# Optional: Broadcasting example (different shapes)
scalar = 3
print(arr1 + scalar)   # [4 5 6]