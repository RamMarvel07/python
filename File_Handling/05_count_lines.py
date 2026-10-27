# 05 - Count and display the total number of lines in a text file
def count_lines(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        print(f"Total number of lines in '{filename}': {len(lines)}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

count_lines("student.txt")
