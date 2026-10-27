students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 68
}

print("Students:", students)
name = input("Enter student name to update marks: ")
if name in students:
    new_marks = int(input("Enter new marks: "))
    students[name] = new_marks
    print("Updated marks:", students)
else:
    print("Student not found.")
