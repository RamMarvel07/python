employees = {
    "Alice": 45000,
    "Bob": 62000,
    "Charlie": 38000,
    "Diana": 75000,
    "Eve": 52000
}

print("Highest salary:", max(employees, key=employees.get), "->", max(employees.values()))
print("Lowest salary:", min(employees, key=employees.get), "->", min(employees.values()))
print("Average salary:", sum(employees.values()) / len(employees))
print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, "->", salary)
