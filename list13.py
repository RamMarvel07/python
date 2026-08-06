numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)