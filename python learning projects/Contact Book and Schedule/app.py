import contacts
import schedule
import expensestrack

def mainMenu():
    print("Welcome to your contact book and schedule!")
    name = input("What is your name? ")

    print(f"Hello, {name}!")

    while True: #Runs function until user quits
        print("\nWhat would you like to do? ")
        print("\n1. Go to your contact book")
        print("2. Go to your schedule")
        print("3. Read your expenses")
        print("4. Quit\n")

        while True:
            try: #Error checks the input
                select = int(input("Select an option: "))
                break
            except:
                print("Please make a valid selection!")


        if select == 1: #Runs Contacts.py main menu function
            contacts.mainMenu()
        elif select == 2: #Runs Schedule.py main menu function
            schedule.mainMenu()
        elif select == 3:
            expensestrack.mainMenu()
        elif select == 4:
            print("\nExiting...")
            break
        else:
            print("Please make a valid selection!")

mainMenu() #Runs main menu function which runs the whole program