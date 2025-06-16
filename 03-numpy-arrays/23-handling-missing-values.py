import numpy as np

# nan -> Not a Number (missing data)
# inf -> Infinite value (e.g., divide by zero)

# np.isnan() -> Detect missing (NaN) values
# np.isinf() -> Detect infinite values
# np.nan_to_num() -> Replace NaN or inf with custom values

# --- Example 1: Handling NaN ---
arr = np.array([1, 2, np.nan, 4, 5])

print("Detect NaN values:")
print(np.isnan(arr))  # [False False  True False False]

cleaned_arr = np.nan_to_num(arr, nan=100)  # Replace NaN with 100
print("NaN replaced with 100:")
print(cleaned_arr)  # [  1.   2. 100.   4.   5.]


# --- Example 2: Handling inf and -inf ---
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

print("\nDetect inf values:")
print(np.isinf(arr))  # [False False  True False  True False]

cleaned_arr = np.nan_to_num(arr, nan=0, posinf=100, neginf=-100)
print("inf replaced with 100, -inf with -100:")
print(cleaned_arr)  # [   1.    2.  100.    4. -100.    6.]