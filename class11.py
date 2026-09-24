class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append((name, price))
        print("Product Added")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print("Product Removed")
                return
        print("Product Not Found")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]
        return total

    def __del__(self):
        print("Shopping Cart Object Destroyed")


cart = ShoppingCart("Sandesh", 101)

cart.add_product("Mobile", 20000)
cart.add_product("Headphones", 2000)

print("Total Bill:", cart.total_bill())

cart.remove_product("Headphones")

print("Total Bill:", cart.total_bill())