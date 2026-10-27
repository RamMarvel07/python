class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class Employee(person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        super().display()
        print("emp_id:",self.emp_id)
        print("salary:",self.salary)
e=Employee("pratham",21,11,20000)
e.display()
