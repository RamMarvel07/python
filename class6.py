class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = 100 * 5 + (self.units - 100) * 7
        else:
            bill = 100 * 5 + 100 * 7 + (self.units - 200) * 10
        return bill

    def display(self):
        print("Consumer No:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units:", self.units)
        print("Electricity Bill:", self.calculate_bill())


e = ElectricityBill(101, "Sandesh", 250)
e.display()