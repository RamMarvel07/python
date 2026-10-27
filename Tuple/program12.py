user_list = []
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"  Number {i + 1}: "))
    user_list.append(num)
user_tuple = tuple(user_list)
print("List  :", user_list)
print("Tuple :", user_tuple)
