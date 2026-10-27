day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {103, 104, 105, 106, 107}
print("Day 1 visitor IDs:", day1_visitors)
print("Day 2 visitor IDs:", day2_visitors)
unique_across_both = day1_visitors.union(day2_visitors)
returning_visitors  = day1_visitors.intersection(day2_visitors)
only_day1           = day1_visitors.difference(day2_visitors)
only_day2           = day2_visitors.difference(day1_visitors)
print("\nUnique visitors across both days:", unique_across_both)
print("Returning visitors (both days)  :", returning_visitors)
print("Visitors only on Day 1          :", only_day1)
print("Visitors only on Day 2          :", only_day2)
electronics = {"Laptop", "Phone", "Tablet", "Camera"}
portable    = {"Phone", "Tablet", "Earphones", "Smartwatch"}
print("\nElectronics category   :", electronics)
print("Portable category      :", portable)
both_categories = electronics.intersection(portable)
print("Products in both categories:", both_categories)
