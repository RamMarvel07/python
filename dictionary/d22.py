even_squares = {i: i**2 for i in range(1, 21) if i % 2 == 0}
for key, value in even_squares.items():
    print(key, ":", value)
