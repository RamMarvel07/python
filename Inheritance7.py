class Shape:
    def display(self, name):
        print("Shape:", name)


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth


class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height


c = Circle()
c.display("Circle")
print("Area:", c.area(7))

r = Rectangle()
r.display("Rectangle")
print("Area:", r.area(10, 5))

t = Triangle()
t.display("Triangle")
print("Area:", t.area(10, 8))