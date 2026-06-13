#PASSWORD MANAGER V0.7
# sel = selection  :  ap = add password  :  vp = view password  :  dp = delete password

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
    elif(ui == 1):
        ap()
    elif(ui == 2):
        vp()
    elif(ui == 3):
        dp()
    else:
        print("\nSorry, this section is under construction\n")
        mainmenu()


def mainmenu():

    global ui
    print("===Password Manager=== v0.7")

    print("1. Add Password\n2. View Password\n3. Delete Password\n4. Exit")

    ui = int(input("What would like to do? \n"))
    sel()

def ap():
    f = open("database.txt", "a")
    
    global us,ui
    print("Enter the name of Website")
    us = input()
    print(f"What's the password for {us}")
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
        f.close()
        print("Database successfully updated!\n\n")
        mainmenu()
        
def vp():
    if not os.path.exists("database.txt"):
        print("\nNo passwords saved.\n")
        mainmenu()
        return()
    f = open("database.txt", "r")
    pd = f.read()
    print("The saved passwords are the following: \n")
    print(pd)
    f.close()
    print("\n\n")
    mainmenu()

def dp():
    print("Are you sure that you would like to delete all the saved passwords?? y/n")
    ui = input()
    if(ui != "y" and ui != "n"):
        print("Please enter a valid option  \"y\" or \"n\"")
        dp()
    elif(ui == "n"):
        print("\n")
        mainmenu()



mainmenu()

