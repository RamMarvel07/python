numbers = [2, 7, 11, 15, 4, 6, 8, 3]
target = int(input("Enter target sum: "))

seen = {}
found = False

for num in numbers:
    complement = target - num
    if complement in seen:
        print("Pair found:", complement, "+", num, "=", target)
        found = True
        break
    seen[num] = True

if not found:
    print("No pair found with the given target.")
