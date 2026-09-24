class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle Rented Successfully")
        else:
            print("Vehicle Not Available")

    def return_vehicle(self, days):
        self.available = True
        print("Vehicle Returned Successfully")
        print("Rental Charges:", self.rental_rate * days)

    def display(self):
        print("Vehicle No:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.available)


v = Vehicle("MH12AB1234", "Swift", 1000)

v.display()
v.rent()
v.return_vehicle(3)