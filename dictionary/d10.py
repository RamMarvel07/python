students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)
