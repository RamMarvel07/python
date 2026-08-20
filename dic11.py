students = {
    "Rahul": 80,
    "Amit": 95,
    "Sneha": 88,
    "Priya": 92
}

highest = max(students.values())

for name, marks in students.items():
    if marks == highest:
        print("Highest marks:", name, marks)
