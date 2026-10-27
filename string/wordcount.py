s = input("Enter a sentence: ")
count = 0
inword = False
for ch in s:
    if ch != " ":
        if inword == False:
            count += 1
            inword = True
    else:
        inword = False
print("Number of words =", count)