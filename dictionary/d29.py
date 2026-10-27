books = {101: "Python Programming", 102: "Data Structures", 103: "Operating Systems"}

while True:
    print("\n1. Add book")
    print("2. Search book")
    print("3. Remove book")
    print("4. Display all books")
    print("5. Count total books")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        books[book_id] = title
        print("Book added.")

    elif choice == "2":
        book_id = int(input("Enter book ID to search: "))
        if book_id in books:
            print(book_id, "->", books[book_id])
        else:
            print("Book not found.")

    elif choice == "3":
        book_id = int(input("Enter book ID to remove: "))
        if book_id in books:
            del books[book_id]
            print("Book removed.")
        else:
            print("Book not found.")

    elif choice == "4":
        for book_id, title in books.items():
            print(book_id, "->", title)

    elif choice == "5":
        print("Total books:", len(books))

    elif choice == "6":
        break

    else:
        print("Invalid choice.")
