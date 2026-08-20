marks = {
    "Rahul": 80,
    "Amit": 75,
    "shreyash": 90
}

student = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if student in marks:
    marks[student] = new_marks

print(marks)
