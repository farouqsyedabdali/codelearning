todolist = []

def mainMenu():
    while True:
        print("\nWhat would you like to do?\n")
        print("1. Read your list")
        print("2. Add an item to your list")
        print("3. Remove an item from your list")
        print("4. Return to main menu\n")

        while True:
            try:
                select = int(input("Select an option: "))
                break
            except:
                print("\nPlease select a valid option!")

        if select == 1:
            readList()
        elif select == 2:
            addToList()
        elif select == 3:
            removeFromList()
        elif select == 4:
            print("\nExiting...")
            break
        else:
            print("\nPlease make a valid selection!")

def readList():
    if len(todolist) != 0:
        print("-----------------------")
        print(*todolist, sep="\n")
        print("-----------------------")
    else:
        print("\nYou have nothing to do!")

def addToList():
    newItem = input("\nWhat do you need to do? ")
    todolist.append(newItem)

def removeFromList():
    removedItem = input("\nWhat do you want to remove? ")
    if removedItem in todolist:
        todolist.remove(removedItem)
        print("\nItem removed")
    else:
        print("\nItem not in list!")
