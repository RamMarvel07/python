def create_file():
    file = open("employees.txt", "w")
    file.write("101,Amit,IT,50000\n")
    file.write("102,Priya,HR,60000\n")
    file.write("103,Rahul,Finance,55000\n")
    file.write("104,Neha,IT,75000\n")
    file.close()


def display_employees():
    file = open("employees.txt", "r")

    for line in file:
        data = line.strip().split(",")
        print(data[0], data[1], data[2], data[3])

    file.close()


def highest_paid():
    file = open("employees.txt", "r")
    highest = None

    for line in file:
        data = line.strip().split(",")
        salary = int(data[3])

        if highest is None or salary > highest[3]:
            highest = [data[0], data[1], data[2], salary]

    file.close()

    print("Highest Paid Employee:", highest[1])
    print("Salary:", highest[3])


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")
        total += int(data[3])
        count += 1

    file.close()

    print("Average Salary:", total / count)


def above_salary(salary):
    file = open("employees.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if int(data[3]) > salary:
            print(data[0], data[1], data[2], data[3])

    file.close()


create_file()

print("All Employees:")
display_employees()

print("\nHighest Paid Employee:")
highest_paid()

print("\nAverage Salary:")
average_salary()

salary = int(input("\nEnter salary: "))

print("Employees earning above", salary, ":")
above_salary(salary)