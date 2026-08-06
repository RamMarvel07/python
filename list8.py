numbers = []

for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)