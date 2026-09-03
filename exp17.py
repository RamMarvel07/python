file = open("students.txt", "w")

file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()

file = open("students.txt", "r")

records = []

for line in file:
    data = line.strip().split(",")
    if data[0] != "RollNo":
        records.append([int(data[0]), data[1], int(data[2])])

file.close()

print("All Records:")
for record in records:
    print(record[0], record[1], record[2])

highest = max(records, key=lambda x: x[2])

print("\nStudent with Highest Marks:")
print(highest[1], highest[2])

total = sum(record[2] for record in records)
average = total / len(records)

print("\nAverage Marks:", average)

print("\nStudents who scored more than 80:")
for record in records:
    if record[2] > 80:
        print(record[0], record[1], record[2])