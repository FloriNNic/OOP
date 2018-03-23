from datetime import datetime # used to know when the balance was checked
import time

class ATM:
    def __init__(self, bankName, username, pin, balance):
        self.bankName = bankName
        self.username = username
        self.pin = pin
        self.balance = balance

    def checkBalance(self):
        self.processing()
        now = datetime.now()
        print("Your account balance at %s/%s/%s %s:%s was $%.4f" % (now.day,now.month,now.year,now.hour,now.minute, self.balance))

    def withdraw(self):
        amount = float(input("\nPlease enter the amount to withdraw:\n"))
        self.processing()
        if amount > self.balance:
            print("Your balance is insufficient.")
        else:
            self.balance -= amount

    def deposit(self):
        amount = float(input("\nPlease enter the amount to deposit:\n"))
        self.processing()
        self.balance += amount

    def processing(self):
        print("Processing...\n"),
        time.sleep(1.5)

    def PINcheck(self):
        pin = int(input("Please, enter your PIN:\n\n"))
        tries = 3
        while pin != self.pin:
            self.processing()
            tries -= 1
            if tries == 0:
                print("Your memory is playing tricks on you. Try again later...")
                exit(0)
            clear_screen()
            print("Wrong PIN,", end=' ')
            print("You have {} tries left.\n".format(tries))
            pin = int(input("Please, enter your PIN:\n\n"))

    def openSession(self):
        print("\nWelcome to", self.bankName)
        print("*******************\n")

        self.PINcheck()
        self.processing()
        clear_screen()
        print("Good afternoon, {}".format(self.username))
        time.sleep(0.5)
        print("What would you like to do today?\n")

    def closeSession(self):
        clear_screen()
        time.sleep(0.5)
        print("****************************\n")
        print("Thank you for using {}\nHave a nice day!".format(self.bankName))
        print("\n****************************")

# a 'handmade' screen cleaner
def clear_screen():
    print('\n'*30)