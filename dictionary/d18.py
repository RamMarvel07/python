dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"x": 3, "y": 5, "z": 1}

common_values = set(dict1.values()) & set(dict2.values())
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Common values:", common_values)
