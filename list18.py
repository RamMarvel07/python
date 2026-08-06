cart = ["Milk", "Bread", "Rice"]

cart.append("Sugar")
print("After adding:", cart)

cart.remove("Bread")
print("After removing:", cart)

item = input("Enter item to search: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")

print("Shopping Cart:", cart)
print("Total items:", len(cart))