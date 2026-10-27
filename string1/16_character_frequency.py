text = input("Enter a string: ")

checked = ""

for ch in text:
    if ch not in checked:
        count = 0
        for item in text:
            if item == ch:
                count += 1

        print(ch, ":", count)
        checked += ch
