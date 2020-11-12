users = {}


def mainMenu():
    oldOrNew = input("Are you already registered? Y/N: ").lower()

    if oldOrNew == "y":
        oldUser()
    elif oldOrNew == "n":
        newUser()
    else:
        pass


def oldUser():
    while True:
        oldName = input("What is your name? ")
        if oldName not in users:
            print("That name doesn't exist!")
        else:
            pass

        while True:
            oldPass = input("What is your password? ")
            if oldPass == users[oldName]:
                print("Logged in!")
                break
            else:
                print("That's not your password!")
                


def newUser():
    while True:
        newName = input("Enter a name: ")

        if newName in users:
            print("That name is taken!")
        else:
            break

    newPass = input("Enter a password: ")
    users[newName] = newPass
    
    print("Account created!")
    mainMenu()

mainMenu()