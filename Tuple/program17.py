values = (34, 7, 23, 32, 5, 62, 78, 19, 45, 11)
print("Tuple:", values)
largest  = values[0]
smallest = values[0]
for v in values:
    if v > largest:
        largest = v
    if v < smallest:
        smallest = v
print("Largest  :", largest)
print("Smallest :", smallest)
