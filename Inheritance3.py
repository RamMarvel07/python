class Academic:
    def __init__(self, marks):
        self.marks = marks

    def academic_performance(self):
        return self.marks


class Sports:
    def __init__(self, points):
        self.points = points

    def sports_performance(self):
        return self.points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def overall_performance(self):
        return self.marks + self.points

    def display(self):
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", self.overall_performance())


s = Student(85, 10)
s.display()