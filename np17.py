import numpy as np
marks = np.array([55, 70, 85, 60, 90, 45, 78, 88, 92, 67,72, 50, 81, 95, 63, 76, 84, 58, 69, 87])
average = np.mean(marks)
print("Class average:", average)
print("Marks above average:")
print(marks[marks > average])