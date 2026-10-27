employee = {
    "name": "Bob",
    "age": 30,
    "designation": "Engineer",
    "salary": 55000
}

key = input("Enter key to search: ")
if key in employee:
    print(key, ":", employee[key])
else:
    print("Key not found.")
