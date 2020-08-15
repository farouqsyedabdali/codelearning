contact_list = []

def mainMenu():

    while True: #Lists all of the available options until user quits
        print("\nWhat would you like to do?")
        print("1. Read all of your contacts")
        print("2. Add a new contact")
        print("3. Remove a contact")
        print("4. Search for a contact")
        print("5. Edit a contact")
        print("6. Return to the main menu\n")

        while True: #Error checks the input
            try:
              selection = int(input("Select an option: "))
              break
            except:
              print("Please make a valid selection!")
    
        if selection == 1:
            readContacts()
        elif selection == 2:
            addContact()
        elif selection == 3:
            removeContact()
        elif selection == 4:
            searchContact()
        elif selection == 5:
            editContact()
        elif selection == 6: #Returns to the home page
            print("\nExiting...\n")
            break
        else:
            print("\nPlease make a vaild selection!")

def readContacts():
    if len(contact_list) == 0:
        print("\nYou have no contacts")
    else:
        print("")
        print(*contact_list, sep=", ") #Prints contact list without brackets and seperates with comma

def addContact():
    add_name = input("\nWhat is the name of your contact? ")
    contact_list.append(add_name)
    print(f"\n{add_name} added to contacts")


def removeContact():
    removed_name = input("\nWho do you want to remove? ")
    double_check = input("\nAre you sure you want to remove this person? Y/N: ").lower()
    if double_check == "y": #Double checks with the user
        try: #Error checks the input
            contact_list.remove(removed_name)
            print(f"\n{removed_name} removed from contacts")
        except:
            print(f"There is no one named {removed_name} in your contacts")
    else:
        pass

def searchContact():
    find_name = input("\nWho do you want to look for? ")
    if find_name in contact_list:
        print(f"\n{find_name} is in your contacts")
    else:
        print("\nNo results found")

def editContact():
    while True:
        old_name = input("\nWho do you want to edit? ")
        new_name = input("\nWhat's their new name? ")
        try: #Error checks the input
            contact_list.remove(old_name)
            contact_list.append(new_name)
            break
        except:
            print(f"\nThere is no one named {old_name} in your contacts. Try again!")
