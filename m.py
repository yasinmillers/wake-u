import numpy as np

# Creating a 2x3 array in row-major order
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:")
print(a)
print("Shape:", a.shape)
print("Strides:", a.strides)