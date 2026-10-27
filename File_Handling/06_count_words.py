# 06 - Count the total number of words in a text file
def count_words(filename):
    try:
        word_count = 0
        with open(filename, "r") as f:
            for line in f:
                words = line.split()
                word_count += len(words)
        print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

count_words("student.txt")
