import random
import string


class Password():
    def __init__(self):
        self.length = 0 #Length of password
        self.sec_level = "" #Security level of password
    

    def create(self):
        while True:
            try: #Error checks the input
                self.length = int(input("How long do you want the password? "))
                break
            except:
                print("\nMake a valid selection!\n")
        
        while True:
            self.sec_level = input("\nWhat security level would you like? Low/Medium/High: ").lower()

            if self.sec_level == "low":
                self.generate("low")
                break
            elif self.sec_level == "medium":
                self.generate("medium")
                break
            elif self.sec_level == "high":
                self.generate("high")
                break
            else:
                print("\nMake a valid selection!\n")
    

    def generate(self, security): #Generates password based on security level
        new_pass = []

        print("\nGenerating...\n")

        if security == "low":
            for i in range(self.length):
                new_pass.append(random.choice(string.ascii_letters))
        elif security == "medium":
            for i in range(self.length):
                new_pass.append(random.choice(string.hexdigits))
        elif security == "high":
            for i in range(self.length):
                new_pass.append(random.choice(string.printable))

        print(*new_pass, sep="")

            

print("Welcome to the Password Generator!\n")

p = Password() #Creates password object
p.create() #Runs the program

while True:
    redo = input("Would you like to create a new password? ").lower()
    if redo == "y":
        p.create()
    elif redo == "n":
        print("\nExiting...")
        break
    else:
        print("\nPlease make a valid selection!")