list1 = [1,2,3,4]
list2 = [3,4,5,6]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)