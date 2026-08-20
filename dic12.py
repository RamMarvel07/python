students = {
    "Rahul": 80,
    "Amit": 95,
    "Sneha": 65,
    "Priya": 92
}

lowest = min(students.values())

for name, marks in students.items():
    if marks == lowest:
        print("Lowest marks:", name, marks)
