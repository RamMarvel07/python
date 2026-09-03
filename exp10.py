
file = open("student.txt", "r")

alphabets = 0
digits = 0
spaces = 0
special = 0

content = file.read()

for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

file.close()

print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special)