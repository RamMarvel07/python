# 02 - Open and display complete contents of student.txt
def display_file(filename):
    try:
        with open(filename, "r") as f:
            contents = f.read()
        print(f"--- Contents of '{filename}' ---")
        print(contents)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Run 01_create_student_file.py first.")

display_file("student.txt")
