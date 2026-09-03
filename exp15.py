file = open("program.py", "r")
new_file = open("program_without_comments.py", "w")

for line in file:
    if not line.strip().startswith("#"):
        new_file.write(line)

file.close()
new_file.close()

print("Single-line comments removed successfully.")