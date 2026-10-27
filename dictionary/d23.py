numbers = [1, 2, 3, 2, 4, 1, 5, 3, 2, 1]
freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print("Numbers:", numbers)
print("Frequency:")
for num, count in freq.items():
    print(num, ":", count)
