events = [] #List of events

def mainMenu():

    while True: #Runs the whole function until user quits
        print("\nWhat would you like to do?\n")
        print("1. Read all of your events")
        print("2. Add an event")
        print("3. Remove an event")
        print("4. Search for an event")
        print("5. Edit an event")
        print("6. Return to the main menu\n")

        while True:
            try: #Error checks the input
                selection = int(input("Select an option: "))
                break
            except:
                print("\nNot a valid selection!\n")

        if selection == 1:
            readEvents()
        elif selection == 2:
            addEvent()
        elif selection == 3:
            removeEvent()
        elif selection == 4:
            searchEvent()
        elif selection == 5:
            editEvent()
        elif selection == 6: #Returns to the home page
            print("\nExiting...\n")
            break
        else:
            print("\nNot a valid selection!")

def readEvents():
    if len(events) == 0:
        print("\nYou have no events")
    else:
        for i in events: #Prints the events in the list of events seperated by a hyphen
            print("")
            print(*i, sep=" - ")

def addEvent():
    new_list = [] #Creates a new list to add list inside of event list

    added_event = input("\nWhat is the name of this event? ")
    added_time = input("\nWhat time will this event be? ")
    added_date = input("\nWhat date? ")
    added_location = input("\nWhere is this event? ")
    new_list.append(added_event)
    new_list.append(added_time)
    new_list.append(added_date)
    new_list.append(added_location)
    events.append(new_list) #Adds the new list to events list after everything is added to new list

def removeEvent():
    removed_event = input("\nWhich event do you want to remove? ")
    double_check = input(f"\nAre you sure you want to remove {removed_event}? Y/N: ").lower()
    if double_check == "y": #Double checks with user
        for i in events:
            if removed_event in i:
                events.remove(i)
                print(f"\n{removed_event} has been removed from your schedule")
            else:
                print(f"\nThere is no event named {removed_event}")
    else:
        print("Operation cancelled")

def searchEvent():
    search = input("What do you want to look for? ")
    for i in events:
        if search in i:
            print(f"{search} is in your schedule")
            break
    else:
        print(f"{search} is not in your schedule")

def editEvent():
    new_events = []

    old_event = input("What event do you want to edit? ")
    
    for i in events:
        if old_event in i:
            new_event = input("What is this event called? ")
            new_time = input("What time will this event be? ")
            new_date = input("What date? ")
            new_place = input("Where will this event be? ")
            
            events.remove(i)
            new_events.append(new_event)
            new_events.append(new_time)
            new_events.append(new_date)
            new_events.append(new_place)

            events.append(new_events)
    else:
        print(f"{old_event} not in schedule")
