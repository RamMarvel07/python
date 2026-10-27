string = input("Enter a string: ")
freq = {}

for char in string:
    freq[char] = freq.get(char, 0) + 1

result = None
for char in string:
    if freq[char] == 1:
        result = char
        break

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")
