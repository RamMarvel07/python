s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
print("Uppercase =", upper)
print("Lowercase =", lower)