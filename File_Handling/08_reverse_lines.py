# 08 - Read a text file and display lines in reverse order
def display_reverse(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        print(f"Lines of '{filename}' in reverse order:\n")
        for line in reversed(lines):
            print(line, end="")
        print()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

display_reverse("student.txt")
