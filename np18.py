import numpy as np
a = np.arange(1, 25).reshape(2, 3, 4)
print("Array:")
print(a)
print("Number of dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)