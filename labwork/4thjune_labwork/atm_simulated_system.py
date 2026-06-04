# Initial Account Balance
balance = 10000

# Repeat until user selects Exit
while True:

    # Display ATM Menu
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Accept user choice
    choice = int(input("Enter Your Choice: "))

    # Check Balance
    if choice == 1:
        print("Available Balance: ₹", balance)

    # Deposit Money
    elif choice == 2:

        # Accept deposit amount
        amount = float(input("Enter Deposit Amount: ₹"))

        # Validate amount
        if amount <= 0:
            print("Invalid Amount! Amount must be positive.")

        else:
            balance = balance + amount
            print("₹", amount, "Deposited Successfully.")
            print("Updated Balance: ₹", balance)

    # Withdraw Money
    elif choice == 3:

        # Accept withdrawal amount
        amount = float(input("Enter Withdrawal Amount: ₹"))

        # Check positive amount
        if amount <= 0:
            print("Invalid Amount! Amount must be positive.")

        # ATM dispenses notes in multiples of 100
        elif amount % 100 != 0:
            print("Please Enter Amount in Multiples of 100.")

        # Check sufficient balance
        elif amount > balance:
            print("Insufficient Balance!")

        # Maintain minimum balance of ₹1000
        elif balance - amount < 1000:
            print("Minimum Balance of ₹1000 Must Be Maintained!")

        else:
            balance = balance - amount
            print("₹", amount, "Withdrawn Successfully.")
            print("Remaining Balance: ₹", balance)

    # Exit ATM
    elif choice == 4:
        print("Thank You For Using ATM.")
        break

    # Invalid Menu Choice
    else:
        print("Invalid Choice! Please Select Between 1 and 4.")

