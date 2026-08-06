numbers = list(map(int, input("Enter list elements: ").split()))

for i in numbers:
    print(i, ":", numbers.count(i))