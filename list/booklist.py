books = ["Python","Java","C"]
books.append("C++")
book = input("Search Book: ")
if book in books:
    print("Available")
else:
    print("Not Available")
books.remove("Java")
print(books)
print("Total Books:", len(books))