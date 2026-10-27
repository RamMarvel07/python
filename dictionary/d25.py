students = {"Alice": 85, "Bob": 72, "Charlie": 90}

while True:
    print("\n1. Add student")
    print("2. Update marks")
    print("3. Delete student")
    print("4. Search student")
    print("5. Display all students")
    print("6. Highest marks")
    print("7. Average marks")
    print("8. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added.")

    elif choice == "2":
        name = input("Enter name to update: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
            print("Marks updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter name to search: ")
        if name in students:
            print(name, "->", students[name])
        else:
            print("Student not found.")

    elif choice == "5":
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "6":
        highest = max(students, key=students.get)
        print("Highest:", highest, "->", students[highest])

    elif choice == "7":
        avg = sum(students.values()) / len(students)
        print("Average marks:", avg)

    elif choice == "8":
        break

    else:
        print("Invalid choice.")
