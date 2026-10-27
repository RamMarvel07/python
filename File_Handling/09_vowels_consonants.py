# 09 - Count vowels and consonants in a text file
def count_vowels_consonants(filename):
    try:
        vowels = set("aeiouAEIOU")
        vowel_count = 0
        consonant_count = 0
        with open(filename, "r") as f:
            content = f.read()
        for ch in content:
            if ch.isalpha():
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        print(f"File: '{filename}'")
        print(f"  Vowels     : {vowel_count}")
        print(f"  Consonants : {consonant_count}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

count_vowels_consonants("student.txt")
