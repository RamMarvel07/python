python_students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
java_students   = {"Charlie", "Diana", "Frank", "Grace"}
print("Python students:", python_students)
print("Java students  :", java_students)
both_courses   = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)
print("\nStudents enrolled in BOTH courses         :", both_courses)
print("Students enrolled in ONLY ONE course      :", only_one_course)
