students = ["Rahul", "Priya", "Amit", "Sneha"]

print("Total students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

new_student = input("Enter new student name: ")
students.append(new_student)

absent = input("Enter absent student name: ")

if absent in students:
    students.remove(absent)

print("Updated Student List:", students)