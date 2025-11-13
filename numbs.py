import numpy as np
arr = np.array([[1, 2, 3, 4, 5],[6,7,8,9,10]])
# Generating a single random float
random_float = np.random.rand()
print("random_float:",random_float)

# Generating a 1D array of random floats
array_1d = np.random.rand(4)
print("array_1d:",array_1d)

# Generating a 2D array of random floats
array_2d = np.random.rand(2, 4)
print("array_2d:",array_2d)

# Generating a 3D array of random floats
array_3d = np.random.rand(2, 3, 4)
print("array_3d:",array_3d)
print(arr)