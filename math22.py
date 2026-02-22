import numpy as np


A = np.array([1, 2, 3])
B= np.array([4, 5, 6])
C= A + B# Element-wise addition of two arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
d = a.dot(b)  # Matrix multiplication
print(d)
print(C)