# Python List vs NumPy Array – What's the Difference?

python_list = [1, 2, 3, 4, 5]
print(python_list)

# Output: [1, 2, 3, 4, 5]


#NumPy array
import numpy as np

numpy_array = np.array(python_list)
print(numpy_array)

# Output: [1 2 3 4 5]



'''Note:
- NumPy arrays display without commas
- They support powerful operations like vectorized math, broadcasting, etc.

    Why Use NumPy Arrays Instead of Lists?
- Faster performance on large data
- Supports element-wise operations directly
- Uses less memory
- Has built-in functions for statistics, math, etc.'''