import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D array:")
print(a)
b = a.flatten()
print("Flattened array:")
print(b)