class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self):
        return self.price - self.price * 0.10

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price())


p = ElectronicProduct(101, "Laptop", 60000, "Lenovo", "2 Years")
p.display()