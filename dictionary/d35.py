paragraph = input("Enter a paragraph: ")
words = paragraph.split()

word_length_count = {}
for word in words:
    length = len(word)
    word_length_count[length] = word_length_count.get(length, 0) + 1

print("Word length frequencies:")
for length, count in sorted(word_length_count.items()):
    print("Length", length, ":", count, "word(s)")
