student_records = (
    (1, "Alice",   "A"),
    (2, "Bob",     "B"),
    (3, "Charlie", "A+"),
    (4, "Diana",   "B+"),
)
print("{'Roll':<6} {'Name':<12} {'Grade'}")
print("-" * 25)
for record in student_records:
    print("{record[0]:<6} {record[1]:<12} {record[2]}")
