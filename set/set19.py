morning   = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
afternoon = {"Charlie", "Diana", "Frank", "Grace", "Eve"}
print("Morning session students  :", morning)
print("Afternoon session students:", afternoon)
both          = morning.intersection(afternoon)
only_morning  = morning.difference(afternoon)
only_afternoon = afternoon.difference(morning)
at_least_one  = morning.union(afternoon)
print("\nStudents present in BOTH sessions         :", both)
print("Students present ONLY in the morning      :", only_morning)
print("Students present ONLY in the afternoon    :", only_afternoon)
print("Students present in AT LEAST one session  :", at_least_one)
