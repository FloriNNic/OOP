from module2 import*

def menu(n):
    print("\nWhat would you like to do?\n")
    print("1.Generate the partitions of",n)
    print("2.Find the",n,"-th palindrome")
    print("3.Determine all the subsets of sum",n)
    print("4.Display a triangle of numbers",n)
    print("5.Enter another number")
    print("6.Exit")
    print('\n')
    choice = int(input("Enter your choice: "))

    if choice==1:
        x1 = Partitions()
        x1.generatePartitions(1,n)
        menu(n)

    elif choice ==2:
        x2 = Palindrome()
        print(x2.findPalindrome(n))
        menu(n)

    elif choice==3:
        x3 = Subsets(n)
        print(x3.generateSubsets(n))
        menu(n)

    elif choice==4:
        x4 = Display()
        x4.displayTriangle(n)
        menu(n)

    elif choice==5:
        n = int(input("Enter a number: "))
        menu(n)

    elif choice==6:
        return 0

    else:
        print("You don't have so many choices !")
        menu(n)

n = int(input("Enter a number: "))

menu(n)


