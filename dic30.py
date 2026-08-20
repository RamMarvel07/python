students = {
    "Rahul": "Computer Science",
    "Amit": "Mechanical",
    "Priya": "Computer Science",
    "Sneha": "Electronics",
    "Karan": "Mechanical"
}

groups = {}

for student, department in students.items():
    if department not in groups:
        groups[department] = []

    groups[department].append(student)

print(groups)
