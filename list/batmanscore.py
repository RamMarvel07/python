scores = [45,67,120,89,150,33,76,102,15,58]
print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
print("Average:", sum(scores)/len(scores))
century = 0
half = 0
for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1
print("Centuries:", century)
print("Half Centuries:", half)