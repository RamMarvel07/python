employee = {
    "id": 88,
    "name": "Prathmesh",
    "department": "IT",
    "salary": 50000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")
