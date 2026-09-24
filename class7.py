class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount_price(self):
        discount = self.price * 0.10
        return self.price - discount


m = MobilePhone("Samsung", "S24", "128GB", 50000)

m.display()
print("Price after Discount:", m.discount_price())