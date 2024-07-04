with open("text.txt") as file:
    for line in file:
        print(line.strip().upper())
print("Next 2\n")
file1 = open("text.txt")
lines = file1.readlines()
file1.close()
lines.sort()
print(lines)