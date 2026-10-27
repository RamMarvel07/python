students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 68
}

lowest = min(students, key=students.get)
print("Student with lowest marks:", lowest, "->", students[lowest])
