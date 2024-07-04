with open('text2.txt','r+') as file:
    file.write("It's been 4 years honey1")
with open("text2.txt") as file:
    print(file.read())
with open("text.txt", "a") as file:
    file.write("and its been 4 years baby\n")
file = open("text.txt")
print(file.read())