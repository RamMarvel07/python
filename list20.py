books = ["Python", "Java", "C++"]

new_book = input("Enter new book: ")
books.append(new_book)

search = input("Enter book to search: ")

if search in books:
    print("Book found")
else:
    print("Book not found")

remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)

print("Books List:", books)
print("Total books:", len(books))