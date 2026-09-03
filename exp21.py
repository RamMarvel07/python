def create_file():
    file = open("books.txt", "w")
    file.write("101,Python Programming,John,Available\n")
    file.write("102,Data Structures,Robert,Available\n")
    file.write("103,Computer Networks,James,Issued\n")
    file.close()


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    file = open("books.txt", "a")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

    print("Book added successfully.")


def search_book():
    book_id = input("Enter Book ID to search: ")
    file = open("books.txt", "r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[0] == book_id:
            print("Book ID:", data[0])
            print("Title:", data[1])
            print("Author:", data[2])
            print("Status:", data[3])
            found = True
            break

    file.close()

    if not found:
        print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    file = open("books.txt", "r")
    books = []

    for line in file:
        data = line.strip().split(",")

        if data[0] == book_id:
            if data[3] == "Available":
                data[3] = "Issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")

        books.append(data)

    file.close()

    file = open("books.txt", "w")

    for book in books:
        file.write(",".join(book) + "\n")

    file.close()


def return_book():
    book_id = input("Enter Book ID to return: ")

    file = open("books.txt", "r")
    books = []

    for line in file:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"
            print("Book returned successfully.")

        books.append(data)

    file.close()

    file = open("books.txt", "w")

    for book in books:
        file.write(",".join(book) + "\n")

    file.close()


def display_available():
    file = open("books.txt", "r")

    print("Available Books:")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data[0], data[1], data[2])

    file.close()


create_file()

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")