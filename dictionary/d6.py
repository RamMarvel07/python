employees = {
    1001: "Alice",
    1002: "Bob",
    1003: "Charlie",
    1004: "Diana",
    1005: "Eve"
}

emp_id = int(input("Enter employee ID to check: "))
if emp_id in employees:
    print("Employee found:", employees[emp_id])
else:
    print("Employee ID not found.")
