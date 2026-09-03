file = open("student.txt", "r")

content = file.read()
words = content.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

file.close()

print(word_count)