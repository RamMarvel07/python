

file = open("student.txt", "r")

vowels = 0
consonants = 0

content = file.read()

for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

file.close()

print("Total vowels:", vowels)
print("Total consonants:", consonants)