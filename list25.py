numbers = list(map(int, input("Enter list elements: ").split()))

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("List without duplicates:", unique)