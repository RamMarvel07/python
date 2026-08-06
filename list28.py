scores = []

for i in range(10):
    scores.append(int(input("Enter score: ")))

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

century = 0
half_century = 0

for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half_century += 1

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half-centuries:", half_century)