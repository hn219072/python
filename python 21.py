#creation of bank account
bal = [80000]
while True:
    print("Welcome to Saitm bank!")
    print("1. Deposit")
    print("2. Withdrawl")
    print("3. Bank Summary")
    print("4. Exit")
    opt = int(input("Choose your option (1, 2, 3 or 4): "))

    if opt==1:
        print("Your balance is: Rs.", bal[-1])
        dep = int(input("Enter the amount to be deposited: "))
        total = bal[-1]+dep
        bal.append(total)
        print("Total balance: Rs.", bal[-1])
        
    elif opt ==2:
        print("Your balance is: Rs.", bal[-1])
        withdraw = int(input("Enter the amount to be withdrawl: "))
        total = bal[-1]-withdraw
        bal.append(total)
        print("Total balance: Rs.", bal[-1])

    elif opt==3:
        print("Your total bank summary is: ")
        for i in bal:
            print(i, end=" ")
        print("\r")

    elif opt ==4:
        print("Thank you for your service.")
        break
    else:
        print("Invalid option")

