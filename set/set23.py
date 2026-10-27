available_books = {"Python Basics", "Data Structures", "AI Fundamentals", "Web Dev", "Clean Code"}
requested_books = {"Data Structures", "AI Fundamentals", "Networking", "Clean Code"}
print("Available books:", available_books)
print("Requested books:", requested_books)
books_that_can_be_issued = available_books.intersection(requested_books)
print("\nRequested books that are available:")
print(books_that_can_be_issued)
