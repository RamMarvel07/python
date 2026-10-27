s = input("Enter a string: ")
v = c = d = sp = sc = 0
for ch in s:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        v += 1
    elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        c += 1
    elif '0' <= ch <= '9':
        d += 1
    elif ch == ' ':
        sp += 1
    else:
        sc += 1
print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
print("Spaces =", sp)
print("Special Characters =", sc)