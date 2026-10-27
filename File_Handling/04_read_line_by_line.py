# 04 - Read a text file line by line and display each line
def read_line_by_line(filename):
    try:
        with open(filename, "r") as f:
            print(f"Reading '{filename}' line by line:\n")
            for line_no, line in enumerate(f, start=1):
                print(f"Line {line_no}: {line}", end="")
        print()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

read_line_by_line("student.txt")
