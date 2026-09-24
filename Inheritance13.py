class Printer:
    def print_document(self):
        print("Printing Document")


class Scanner:
    def scan_document(self):
        print("Scanning Document")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction Device")


m = MultifunctionDevice()
m.display()
m.print_document()
m.scan_document()