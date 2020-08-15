expenses = []

def mainMenu():
    while True:
        print("\nWhat would you like to do?\n")
        print("1. Read your expenses")
        print("2. Add expenses")
        print("3. Return to the main menu\n")
    
        while True:
            try:
                selection = int(input("Select an option: "))
                break
            except:
                print("Make a valid selection!")
        
        if selection == 1:
            readExpenses()
        elif selection == 2:
            addExpense()
        elif selection == 3:
            print("\nExiting...\n")
            break


def readExpenses():
    if len(expenses) == 0:
        print("You have no expenses listed")
    else:
        print("-------------------------")
        for i in expenses:
            print(*i, sep=" - ")

        print("-------------------------")

def addExpense():
    new_list = []

    added_expense = input("What did you purchase? ")
    while True:
        try:
            added_price = int(input("What is the price of the purchase after tax? "))
            added_count = int(input("How many did you purchase? "))
            break
        except:
            print("Please make a valid selection! ")

    new_list.append(added_expense)
    new_list.append(f"{added_price} dollars")
    new_list.append(f"{added_count} purchased")

    expenses.append(new_list)
