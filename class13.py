class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("Total Marks:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("Student Result Object Destroyed")


s = StudentResult("Sandesh", [85, 90, 78, 88, 92])
s.display()