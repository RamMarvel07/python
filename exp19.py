def create_file():
    file = open("attendance.txt", "w")
    file.write("101,Amit,80,100\n")
    file.write("102,Priya,70,100\n")
    file.write("103,Rahul,60,100\n")
    file.write("104,Neha,90,100\n")
    file.close()


def calculate_attendance():
    file = open("attendance.txt", "r")

    for line in file:
        data = line.strip().split(",")
        roll_no = data[0]
        name = data[1]
        present = int(data[2])
        total = int(data[3])

        percentage = (present / total) * 100

        print(name, "Attendance:", percentage, "%")

    file.close()


def below_75():
    file = open("attendance.txt", "r")

    print("\nStudents having attendance below 75%:")

    for line in file:
        data = line.strip().split(",")
        present = int(data[2])
        total = int(data[3])

        percentage = (present / total) * 100

        if percentage < 75:
            print(data[0], data[1], percentage, "%")

    file.close()


create_file()

print("Attendance Percentage:")
calculate_attendance()

below_75()