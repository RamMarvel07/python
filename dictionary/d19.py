data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2, "f": 4}
print("Original dictionary:", data)

seen = set()
result = {}
for key, value in data.items():
    if value not in seen:
        seen.add(value)
        result[key] = value

print("Dictionary after removing duplicate values:", result)
