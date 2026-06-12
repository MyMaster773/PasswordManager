import sys
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
    else:
        print("Sorry, this section is under construction")


def mainmenu():

    global ui
    print("===Password Manager=== v0.2")

    print("1. Add Password\n2. View Password\n3. Deleat Password\n4. Exit")

    ui = int(input("What would like to do? \n"))
    sel()

def ap():
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
        print("Database sucessfully updated!")
        mainmenu()
        


mainmenu()

