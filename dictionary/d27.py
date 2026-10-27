products = {"Apples": 50, "Bananas": 8, "Mangoes": 15, "Grapes": 5, "Oranges": 20}

while True:
    print("\n1. Add product")
    print("2. Update quantity")
    print("3. Delete product")
    print("4. Search product")
    print("5. Display products with quantity below 10")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        products[name] = qty
        print("Product added.")

    elif choice == "2":
        name = input("Enter product name to update: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
            print("Quantity updated.")
        else:
            print("Product not found.")

    elif choice == "3":
        name = input("Enter product name to delete: ")
        if name in products:
            del products[name]
            print("Product deleted.")
        else:
            print("Product not found.")

    elif choice == "4":
        name = input("Enter product name to search: ")
        if name in products:
            print(name, "->", products[name])
        else:
            print("Product not found.")

    elif choice == "5":
        print("Products with quantity below 10:")
        for name, qty in products.items():
            if qty < 10:
                print(name, "->", qty)

    elif choice == "6":
        break

    else:
        print("Invalid choice.")
