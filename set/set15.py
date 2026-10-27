set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("Set 1:", set1)
print("Set 2:", set2)
if set1.isdisjoint(set2):
    print("\nThe two sets have NO elements in common (Disjoint sets).")
else:
    print("\nThe two sets HAVE common elements (Not disjoint).")
