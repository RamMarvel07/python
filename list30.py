names = ["Rahul", "Priya", "Amit"]
ages = [25, 30, 40]

name = input("Enter patient name: ")
age = int(input("Enter age: "))

names.append(name)
ages.append(age)

delete = input("Enter patient name to delete: ")

if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)

search = input("Enter patient name to search: ")

if search in names:
    index = names.index(search)
    print("Patient:", names[index], "Age:", ages[index])
else:
    print("Patient not found")

print("Patient List:")
for i in range(len(names)):
    print(names[i], "-", ages[i])

print("Total Patients:", len(names))