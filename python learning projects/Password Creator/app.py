import random
import string


class Password():
    def __init__(self):
        self.length = 0
        self.sec_level = ""
    

    def create(self):
        while True:
            try:
                self.length = int(input("How long do you want the password? "))
                break
            except:
                print("Make a valid selection!")
        
        while True:
            self.sec_level = input("What security level would you like? Low/Medium/High: ").lower()

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
                print("Make a valid selection!")
    

    def generate(self, security):
        new_pass = []

        print("Generating...")

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


        while True:
            redo = input("Would you like to create a new password?")
            if redo == "y":
                self.create()
            elif redo == "n":
                print("Exiting...")
                break
            else:
                print("Please make a valid selection!")
            

print("Welcome to the Password Generator!")

p = Password()
p.create()
