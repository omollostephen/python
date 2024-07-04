import os
print(os.getcwd())#current working directory
# print(os.mkdir("new_dir"))#creates directory
# print(os.rmdir("new_dir"))#deletes directory

# os.chdir("new_dir")#change directory
print(os.getcwd())
print(os.listdir("open"))


dir = "open"
for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

