file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

identical = True

for i in range(max(len(lines1), len(lines2))):
    line1 = lines1[i].strip() if i < len(lines1) else ""
    line2 = lines2[i].strip() if i < len(lines2) else ""

    if line1 != line2:
        print("Files are different.")
        print("First difference is at line:", i + 1)
        print("File 1:", line1)
        print("File 2:", line2)
        identical = False
        break

if identical and len(lines1) == len(lines2):
    print("Files are identical.")
elif identical:
    print("Files are different.")
    print("First difference is at line:", min(len(lines1), len(lines2)) + 1)