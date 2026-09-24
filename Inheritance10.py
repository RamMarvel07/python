class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, engine):
        super().__init__(brand)
        self.engine = engine


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed)


class ElectricBike(Bike):
    def __init__(self, brand, engine, battery):
        super().__init__(brand, engine)
        self.battery = battery

    def display(self):
        print("Brand:", self.brand)
        print("Engine:", self.engine)
        print("Battery:", self.battery)


s = SportsCar("BMW", "M4", 280)
s.display()

e = ElectricBike("Ola", "Electric", "5 kWh")
e.display()