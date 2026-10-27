fifteen = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print("Tuple:", fifteen)
even_count = 0
odd_count  = 0
for num in fifteen:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers :", odd_count)
