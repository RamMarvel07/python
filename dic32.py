numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}

for num in numbers:
    required = target - num

    if required in seen:
        print("Numbers:", required, "and", num)
        break

    seen[num] = True
else:
    print("No pair found")
