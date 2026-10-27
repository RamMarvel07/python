numbers = [45, 23, 89, 12, 67]
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest:", largest)
print("Smallest:", smallest)