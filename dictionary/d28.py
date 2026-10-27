contacts = {"Alice": "9876543210", "Bob": "8765432109", "Charlie": "7654321098"}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, "->", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name] = input("Enter new phone number: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        for name, phone in contacts.items():
            print(name, "->", phone)

    elif choice == "6":
        break

    else:
        print("Invalid choice.")
