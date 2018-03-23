from ATM import *

# card initialization
file = open("account.txt","r")

bank = file.readline()

username = file.readline()

pin = int(file.readline())

balance = float(file.readline())

file.close()

x = ATM(bank,username,pin,balance)

# function to call the methods for basic operations on ATM
def transactions():
    time.sleep(1.0)
    print("1.Make a deposit.\n")
    time.sleep(1.0)
    print("2.Make a withdraw.\n")
    time.sleep(1.0)
    print("3.Check the current balance.\n")

    choice = int(input())
    clear_screen()
    if choice==1:
        x.deposit()
        print("\nTransaction ended.\n")
        balanceUpdate()
        time.sleep(1.5)
        transact_again()

    elif choice==2:
        x.withdraw()
        print("\nTransaction ended.\n")
        balanceUpdate()
        time.sleep(1.5)
        transact_again()

    elif choice==3:
        x.checkBalance()
        print("\nTransaction ended.\n")
        time.sleep(1.5)
        transact_again()

    else:
        print ("Invalid option\n")
        time.sleep(1.5)
        transact_again()

def transact_again():
    option = input("Would you like to do other transactions? (y/n)\n")

    if option == 'y':
        clear_screen()
        transactions()
    else:
        x.closeSession()

# function to update in the database the changes made during a transaction
def balanceUpdate():
    f = open("account.txt","w")
    f.write(x.bankName)
    f.write(x.username)
    f.write(str(x.pin))
    f.write("\n")
    f.write(str(x.balance))
    f.close()

print("\nInitializing card...\n")
time.sleep(2.0)
clear_screen()

x.openSession()

transactions()