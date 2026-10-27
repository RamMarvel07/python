text = input("Enter a string: ")

printed = ""

for ch in text:
    count = 0
    for item in text:
        if item == ch:
            count += 1

    if count > 1 and ch not in printed:
        print(ch)
        printed += ch
