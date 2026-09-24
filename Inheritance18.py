class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        Person.__init__(self, name, age)
        self.specialization = specialization

    def display_doctor(self):
        print("Doctor:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        Person.__init__(self, name, age)
        self.disease = disease

    def display_patient(self):
        print("Patient:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display(self):
        print("Surgeon:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Doctor):
    def __init__(self, name, age, specialization, research):
        super().__init__(name, age, specialization)
        self.research = research

    def display(self):
        print("Researcher:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Research:", self.research)


d = Doctor("Dr. Amit", 40, "Cardiology")
d.display_doctor()

p = Patient("Rahul", 30, "Heart Problem")
p.display_patient()

s = Surgeon("Dr. Patil", 45, "Surgery", "Heart Disease")
s.display()

m = MedicalResearcher("Dr. Sharma", 50, "Medicine", "Cancer Research")
m.display()