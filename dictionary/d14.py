string = input("Enter a string: ")
freq = {}

for char in string:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:")
for char, count in freq.items():
    print(repr(char), ":", count)
