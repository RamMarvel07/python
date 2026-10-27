# 11 - Find the longest word in a text file
import re

def find_longest_word(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
        words = re.findall(r"[A-Za-z]+", content)
        if not words:
            print("No words found in the file.")
            return
        longest = max(words, key=len)
        print(f"Longest word in '{filename}': '{longest}' (length = {len(longest)})")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

find_longest_word("student.txt")
