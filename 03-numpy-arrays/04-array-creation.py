import numpy as np

# -----------------------------------
# 1. Creating arrays using np.array()
# -----------------------------------

arr = np.array([1, 2, 3])
print(arr)

# Output: Manual array: [1 2 3]

# -----------------------------------
# 2. Creating arrays using np.zeros()
# -----------------------------------

zeros_1d = np.zeros(5)
zeros_2d = np.zeros((2, 3))
print(zeros_1d)
print(zeros_2d)

# Output:
# Zeros 1D: [0. 0. 0. 0. 0.]
# Zeros 2D: [[0. 0. 0.]
#              [0. 0. 0.]]


# -----------------------------------
# 3. Creating arrays using np.ones()
# -----------------------------------

ones_1d = np.ones(4)
ones_2d = np.ones((3, 2))
print(ones_1d)
print(ones_2d)

# Output: [ 1. 1. 1. 1.]
# Ones 2D: [[1. 1.]
#            [1. 1.]
#            [1. 1.]]



# ----------------------------------------
# 4. Creating arrays using np.full()
# ----------------------------------------

# 1D array with value 9
full_1d = np.full(5, 9)
full_2d = np.full((2, 3), 7)
print(full_1d)
print(full_2d)



'''Covered Methods:
1. np.array()     - Create arrays manually with custom values
2. np.zeros()     - Create arrays filled with zeros
3. np.ones()      - Create arrays filled with ones
4. np.full()      - Create arrays filled with any specified value'''