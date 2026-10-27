products = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 80,
    "Grapes": 60,
    "Orange": 40
}

new_product = input("Enter new product name: ")
new_price = float(input("Enter price: "))
products[new_product] = new_price

print("\nUpdated Products:")
for product, price in products.items():
    print(product, ":", price)
