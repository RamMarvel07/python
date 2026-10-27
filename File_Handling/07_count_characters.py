# 07 - Count the total number of characters (including spaces) in a text file
def count_characters(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
        print(f"Total characters (including spaces) in '{filename}': {len(content)}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

count_characters("student.txt")
