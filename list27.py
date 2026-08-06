salaries = []

n = int(input("Enter number of employees: "))

for i in range(n):
    salaries.append(int(input("Enter salary: ")))

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above50000 = 0
below30000 = 0

for i in salaries:
    if i > 50000:
        above50000 += 1
    if i < 30000:
        below30000 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees Above 50000:", above50000)
print("Employees Below 30000:", below30000)