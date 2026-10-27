sentence = input("Enter a sentence: ")

result = ""
capitalize_next = True

for ch in sentence:
    if ch == " ":
        result += ch
        capitalize_next = True
    elif capitalize_next and "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
        capitalize_next = False
    else:
        result += ch
        capitalize_next = False

print("Title case:", result)
