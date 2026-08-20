words = ["cat", "dog", "apple", "bat", "orange", "sun"]

groups = {}

for word in words:
    length = len(word)

    if length not in groups:
        groups[length] = []

    groups[length].append(word)

print(groups)
words = ["cat", "dog", "apple", "bat", "orange", "sun"]

groups = {}

for word in words:
    length = len(word)

    if length not in groups:
        groups[length] = []

    groups[length].append(word)

print(groups)
