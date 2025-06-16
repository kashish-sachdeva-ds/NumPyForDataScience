# Traditional List Addition (not efficient for large datasets)
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Element-wise addition using zip and list comprehension
result = [x + y for x, y in zip(list1, list2)]
print("List result:", result)  # Output: [5, 7, 9]


# -----------------------------------
# NumPy Vectorized Addition (fast and efficient)

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2  # Element-wise addition
print("NumPy result:", result)  # Output: [5 7 9]

# -----------------------------------
# NumPy Vectorized Multiplication

arr = np.array([10, 20, 30])
multiplied = arr * 3  # Each element multiplied by 3

print("Multiplied:", multiplied)  # Output: [30 60 90]