set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6}
print("Set 1:", set1)
print("Set 2:", set2)
if set1.issuperset(set2):
    print("\nSet 1 IS a superset of Set 2.")
else:
    print("\nSet 1 is NOT a superset of Set 2.")
