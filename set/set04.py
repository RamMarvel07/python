numbers = {10, 20, 30, 40, 50, 60, 70}
print("Original set of numbers:")
print(numbers)
num = int(input("\nEnter the number to remove: "))
if num in numbers:
    numbers.discard(num)
    print(f"Number {num} has been removed.")
    print("Updated set:", numbers)
else:
    print(f"Number {num} was not found in the set.")
    print("Set remains unchanged:", numbers)
