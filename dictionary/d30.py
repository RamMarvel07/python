students = {
    "Alice": "Computer Science",
    "Bob": "Electronics",
    "Charlie": "Computer Science",
    "Diana": "Mechanical",
    "Eve": "Electronics",
    "Frank": "Computer Science"
}

grouped = {}
for student, dept in students.items():
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(student)

print("Students grouped by department:")
for dept, names in grouped.items():
    print(dept, ":", names)
