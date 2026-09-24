class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill Including Tax:", self.total_bill())

    def __del__(self):
        print("Order Completed")


order = FoodOrder(101, "Sandesh", "Pizza", 2, 250)
order.display()