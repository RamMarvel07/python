class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self):
        return self.price - self.price * 0.10

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.discounted_price())


c = Car("Toyota", "Innova", "Petrol", 2000000)
c.display()