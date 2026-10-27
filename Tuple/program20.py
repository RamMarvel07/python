search_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
print("Tuple:", search_tuple)
user_num = int(input("Enter a number to search: "))
if user_num in search_tuple:
    print(f"{user_num} FOUND in the tuple.")
else:
    print(f"{user_num} NOT FOUND in the tuple.")
