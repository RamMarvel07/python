words = ["apple", "banana", "cherry", "avocado", "blueberry", "apricot", "cat", "dog", "elephant", "fig"]

word_length_dict = {}
for word in words:
    length = len(word)
    if length not in word_length_dict:
        word_length_dict[length] = []
    word_length_dict[length].append(word)

print("Words grouped by length:")
for length, word_list in word_length_dict.items():
    print(length, ":", word_list)
