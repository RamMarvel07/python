import numpy as np
a = np.array([10, 20, 60, 70, 30, 80, 40, 90, 50, 100])
a[a > 50] = 0
print(a)