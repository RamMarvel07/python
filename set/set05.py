students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
print("Set of student names:")
print(students)
name = input("\nEnter a student name to search: ")
if name in students:
    print(f"'{name}' EXISTS in the set of students.")
else:
    print(f"'{name}' does NOT exist in the set of students.")
