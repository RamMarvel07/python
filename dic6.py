employees = {
    101: "Rahul",
    102: "Aditya",
    81: "Sachin",
    87: "harshal"
}

id = int(input("Enter employee ID: "))

if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")
