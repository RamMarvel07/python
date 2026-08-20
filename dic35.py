paragraph = input("Enter a paragraph: ")

words = paragraph.split()
length_count = {}

for word in words:
    length = len(word)
    length_count[length] = length_count.get(length, 0) + 1

print("Word length : Number of words")

for length, count in sorted(length_count.items()):
    print(length, ":", count)
