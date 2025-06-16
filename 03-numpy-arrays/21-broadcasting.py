# Broadcasting in NumPy - Efficient way to apply operations on arrays of different shapes

# Without NumPy (using loops)
prices = [100, 200, 300]
discount = 10  # 10% discount

final_prices = []
for price in prices:
    final_price = price - (price * discount / 100)
    final_prices.append(final_price)

print("With loop:", final_prices)  # Output: [90.0, 180.0, 270.0]


# With NumPy Broadcasting
import numpy as np

prices = np.array([100, 200, 300])
discount = 10

final_prices = prices - (prices * discount / 100)
print("With NumPy:", final_prices)  # Output: [ 90. 180. 270.]



# ------------------------------
# Simple Broadcasting Example
arr = np.array([100, 200, 300])
result = arr * 2
print("Multiplied by scalar:", result)  # Output: [200 400 600]


# ------------------------------
# Broadcasting with 2D and 1D arrays
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])

result = matrix + vector
print("Matrix + Vector:\n", result)
# Output:
# [[11 22 33]
#  [14 25 36]]



# ------------------------------
# Broadcasting Error Example
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20])

# This will raise an error because shapes are not compatible
# result = arr1 + arr2

# Fix: Reshape arr2 if needed or use compatible shapes using .reshape


# ------------------------------
# Rules for Broadcasting

'''
1. If shapes are different, NumPy tries to stretch smaller arrays to match the bigger one.

2. If shapes cant match even after stretching, it throws an error.

3. Broadcasting makes array operations faster and more readable (no need for explicit loops).

'''