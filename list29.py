temp = []

for i in range(30):
    temp.append(float(input("Enter temperature: ")))
highest = max(temp)
lowest = min(temp)
average = sum(temp) / len(temp)
above = 0
below = 0

for i in temp:
    if i > average:
        above += 1
    elif i < average:
        below += 1
print("Hottest Day Temperature:", highest)
print("Coldest Day Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)