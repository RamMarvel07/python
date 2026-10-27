students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 68
}

highest = max(students, key=students.get)
print("Student with highest marks:", highest, "->", students[highest])
