# 03 - Append additional student information to student.txt
def append_student_info(filename):
    additional_info = {
        "Name"    : "Bob Smith",
        "Roll No" : "102",
        "Branch"  : "Electronics",
        "Semester": "3",
    }
    with open(filename, "a") as f:
        f.write("\n--- Additional Student ---\n")
        for key, value in additional_info.items():
            f.write(f"{key:<10}: {value}\n")
    print("Additional student information appended successfully.")

append_student_info("student.txt")

# Show updated contents
with open("student.txt", "r") as f:
    print("\nUpdated file contents:")
    print(f.read())
