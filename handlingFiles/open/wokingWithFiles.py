with open("testing.txt", "w") as file:
    file.write("Hilo")
import os
# os.remove("testing.txt")#this deletes the file
os.rename("testing.txt","proven.txt")#renames the files
print(os.path.exists("proven.txt"))#checks if file is available and returns true/false
print(os.path.getsize("proven.txt"))#gets the file size
print(os.path.abspath("proven.txt"))#get absolute path of the file

import datetime
timestamp = os.path.getmtime("read.py")#get The date and time of file
print(datetime.datetime.fromtimestamp(timestamp))#formates the date-time in a readable manner

print(os.path.isfile("proven.txt"))
print(os.path.isdir("proven.txt"))
