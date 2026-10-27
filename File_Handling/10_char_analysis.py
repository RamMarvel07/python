# 10 - Count alphabets, digits, spaces, and special characters in a text file
def analyze_characters(filename):
    try:
        alphabets = digits = spaces = special = 0
        with open(filename, "r") as f:
            content = f.read()
        for ch in content:
            if ch.isalpha():
                alphabets += 1
            elif ch.isdigit():
                digits += 1
            elif ch == " ":
                spaces += 1
            else:
                special += 1
        print(f"Character Analysis of '{filename}':")
        print(f"  Alphabets          : {alphabets}")
        print(f"  Digits             : {digits}")
        print(f"  Spaces             : {spaces}")
        print(f"  Special Characters : {special}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

analyze_characters("student.txt")
