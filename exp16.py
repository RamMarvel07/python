file = open("student.txt", "r")

content = file.read()

file.close()

file = open("uppercase.txt", "w")
file.write(content.upper())

file.close()

print("File created successfully.")