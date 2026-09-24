class Camera:
    def take_photo(self):
        print("Photo Taken")


class Phone:
    def make_call(self, number):
        print("Calling:", number)


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone")


s = Smartphone()
s.display()
s.take_photo()
s.make_call("9876543210")