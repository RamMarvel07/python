class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal:", self.name)


class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

    def behavior(self):
        print("Dog is Loyal")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

    def behavior(self):
        print("Cat is Friendly")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")

    def behavior(self):
        print("Cow is Calm")


d = Dog("Dog")
d.display()
d.sound()
d.behavior()

c = Cat("Cat")
c.display()
c.sound()
c.behavior()

w = Cow("Cow")
w.display()
w.sound()
w.behavior()