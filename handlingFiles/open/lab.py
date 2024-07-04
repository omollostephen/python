guests = open("guests.txt","w") #creating a file guest
initial_guests = ["Omollo", "Miracle", "Anna","Daughter"]
# writing the guest list into the file
for number in range(1,len(initial_guests)+1):
    for i in initial_guests:
        guests.write(str(number)+". "+i+"\n")
        number +=1
    break
guests.close()

# displayguests
with open("guests.txt") as guest:
    print("List of guest is below:")
    for line in guest:
        print(line.strip())
# adding more guest
new_guests = ["Sam","Milton", "Pauline"]
with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i+"\n")
guests.close()
with open("guests.txt") as guests:
    print("New List of guests:")
    for g in guests:
        print(g.strip())
# guest checking out
checked_out = ["Anna","Omollo"]
temp_list=[]
with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())
with open('guests.txt', "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name+"\n")
with open("guests.txt") as guests:
    print("Remaining guests are:")
    for line in guests:
        print(line.strip())
# checking the guest in and checked_out
guest_to_check = ["Anna","Milton"]
checked_in =[]
with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guest_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked  in".format(check))