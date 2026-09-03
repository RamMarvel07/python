

file = open("student.txt", "r")

content = file.read()
count = len(content)

file.close()

print("Total number of characters:", count)