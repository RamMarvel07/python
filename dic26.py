employees = {
    "Rahul": 45000,
    "Amit": 60000,
    "Priya": 75000,
    "Sneha": 40000,
    "Karan": 55000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than ₹50,000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)
