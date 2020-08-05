contact_list = []

def mainMenu():
  print("Welcome to your contact book!")
  name = input("What is your name? ")
    
  print(f"\nHello, {name}")

  while True: #Lists all of the available options until user quits
    print("\nWhat would you like to do?")
    print("1. Read all of your contacts")
    print("2. Add a new contact")
    print("3. Remove a contact")
    print("4. Quit\n")

    while True:
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
    elif selection == 4: #Quits the program
      print("\nExiting...\n")
      break

def readContacts():
  print(contact_list)

def addContact():
  add_name = input("What is the name of your contact? ")
  contact_list.append(add_name)
  print(f"{add_name} added to contacts")


def removeContact():
  removed_name = input("Who do you want to remove? ")
  double_check = input("Are you sure you want to remove this person? Y/N: ").lower()
  if double_check == "y": #Double checks with the user
    contact_list.remove(removed_name)
    print(f"{removed_name} removed from contacts")
  else:
    pass

mainMenu()