file = open("text.txt")
print(file.readline())
print(file.read())
file.close()
print("Next")
#open read and close at once
with open("text.txt") as file:
    print(file.read())
