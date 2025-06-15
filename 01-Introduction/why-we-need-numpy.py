# Example: Calculating average temperature using basic Python

temperatures = [32.5, 31.0, 30.5, 29.0, 28.5, 27.0, 26.5]

total = 0
for temp in temperatures:
    total += temp

average = total / len(temperatures)
print(average)

# Output: 29.287 approx


'''Note:
This works fine for small datasets like this list.
But if we have a huge dataset with thousands or millions of numbers,
using a loop like this becomes slower and less efficient.

That's where NumPy helps:
NumPy allows fast, optimized, and vectorized operations on large datasets.
Instead of using loops, we can use numpy arrays and functions like numpy.mean().
This makes code cleaner, faster, and more suitable for data science and ML tasks.'''



# Example: Calculating average temperature using NumPy

import numpy as np

temperatures_np = np.array([32.5, 31.0, 30.5, 29.0, 28.5, 27.0, 26.5])
average_np = np.mean(temperatures_np)
print(average_np)

# Output: 29.287 approx

'''it is fast, memory efficient, 
and optimized for numerical operations on large data.'''