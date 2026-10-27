# 12 - Count word frequencies and display as a dictionary
import re

def word_frequency(filename):
    try:
        freq = {}
        with open(filename, "r") as f:
            content = f.read()
        words = re.findall(r"[A-Za-z]+", content.lower())
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        print(f"Word frequencies in '{filename}':")
        for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            print(f"  '{word}': {count}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

word_frequency("student.txt")
