expenses = []
total_price = 0
average_price = 0
total_items = 0


def mainMenu():
    while True: #Runs options until user exits
        print("\nWhat would you like to do?\n")
        print("1. Read your expenses")
        print("2. Add expenses")
        print("3. Return to the main menu\n")
    
        while True: #Error checks the input
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
        for i in expenses: #Prints each expense in list seperated by a "-"
            print(*i, sep=" - ")

        print("-------------------------")

        print(f"Total items = {total_items}")
        print(f"Total price = {total_price}")
        print(f"Avereage price = {average_price}")


def addExpense():
    new_list = [] #Creates a new list to add to expenses
    global total_price #These three access the global variables using global function
    global average_price
    global total_items

    added_expense = input("What did you purchase? ")
    while True: #Error checks the input
        try:
            added_price = int(input("What is the price of the purchase after tax? "))
            added_count = int(input("How many did you purchase? "))
            break
        except:
            print("Please make a valid selection! ")

    new_list.append(added_expense)
    new_list.append(f"{added_price} dollars")
    new_list.append(f"{added_count} purchased")

    total_price += added_price*added_count #Runs functions to print out in readExpenses()
    total_items += 1
    average_price = total_price/total_items

    expenses.append(new_list)
