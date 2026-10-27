# 01 - Create student.txt and write student details
def create_student_file():
    with open("student.txt", "w") as f:
        f.write("Name      : Alice Johnson\n")
        f.write("Roll No   : 101\n")
        f.write("Branch    : Computer Science\n")
        f.write("Semester  : 3\n")
    print("student.txt created successfully.")
    print("Contents written:")
    print("  Name      : Alice Johnson")
    print("  Roll No   : 101")
    print("  Branch    : Computer Science")
    print("  Semester  : 3")

create_student_file()
