balance = 10000

while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter Deposit Amount: "))
        balance = balance + amount
        print("Amount Deposited Successfully")

    elif choice == 3:
        amount = int(input("Enter Withdrawal Amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")

