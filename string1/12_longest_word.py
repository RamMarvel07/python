sentence = input("Enter a sentence: ")

words = sentence.split()

if len(words) == 0:
    print("No words found")
else:
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)
