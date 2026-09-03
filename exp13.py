file = open("student.txt", "r")

word = input("Enter the word to search: ")
count = 0
line_numbers = []

for line_no, line in enumerate(file, 1):
    words = line.split()
    for w in words:
        if w == word:
            count += 1
            if line_no not in line_numbers:
                line_numbers.append(line_no)

file.close()

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)