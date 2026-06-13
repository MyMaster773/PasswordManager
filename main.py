import sys
import os
ui = "x"
us = "x"
up = "x"

def sel():
    global ui
    if(ui == 4):
        print("Are you sure you want to exit? y/n" )
        ui = input()
        if (ui == "y"):
          sys.exit(0)
        else:
            print("\n\n")
            mainmenu()
    elif (ui == 1):
        ap()
    elif (ui == 2):
        vp()
    else:
        print("\nSorry, this section is under construction\n")
        mainmenu()


def mainmenu():

    global ui
    print("===Password Manager=== v0.5")

    print("1. Add Password\n2. View Password\n3. Deleat Password\n4. Exit")

    ui = int(input("What would like to do? \n"))
    sel()

def ap():
    f = open("database.txt", "a")
    
    global us,ui
    print("Enter the name of Website")
    us = input()
    print(f"Whats the password for {us}")
    up = input()
    print(f"The password for \n{us} : {up}")
    print("Is this correct? y/n")
    ui = input()
    while ui not in ("y","n"):
        print("Enter a valid option! That is \"y\" or \"n\"")
        ui = input()
    if (ui == "n"):
        ap()
    elif (ui == "y"):
        f.write(f"{us} : {up}\n")
        f.close
        print("Database sucessfully updated!\n\n")
        mainmenu()
        
def vp():
    if not os.path.exists("database.txt"):
        print("\nNo passwords saved.\n")
        mainmenu()
    f = open("database.txt", "r")
    pd = f.read()
    print("The saved passwords are the following: \n")
    print(pd)
    f.close()
    print("\n\n")
    mainmenu()



mainmenu()

