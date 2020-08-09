events = []

def mainMenu():
    print("Welcome to your Schedule!")
    while True:
        print("\nWhat would you like to do?\n")
        print("1. Read all of your events")
        print("2. Add an event")
        print("3. Quit\n")

        selection = int(input("Select an option: "))
        if selection == 1:
            readEvents()
        elif selection == 2:
            addEvent()
        elif selection == 3:
            break

def readEvents():
    if len(events) == 0:
        print("\nYou have no events")
    else:
        for i in events:
            print(*i, sep=", ")

def addEvent():
    new_list = []

    added_event = input("What is the name of this event? ")
    added_time = input("What time will this event be? ")
    new_list.append(added_event)
    new_list.append(added_time)
    events.append(new_list)



mainMenu()