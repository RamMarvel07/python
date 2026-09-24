class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.marks, "%")


s1 = Student(1, "Sandesh", 85)
s2 = Student(2, "Rahul", 78)
s3 = Student(3, "Amit", 92)

s1.display()
s2.display()
s3.display()