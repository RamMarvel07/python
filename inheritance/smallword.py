s = input("Enter a sentence: ")
word = ""
shortest = ""
for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        if shortest == "" or len(word) < len(shortest):
            shortest = word
        word = ""
print("Shortest word =", shortest)