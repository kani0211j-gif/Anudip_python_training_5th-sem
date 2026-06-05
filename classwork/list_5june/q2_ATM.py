#list of atm transaction 
transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0
#creating empty list 
deposits = []
withdrawals = []

largest_deposit = 0
largest_withdrawal = transactions[1]

# Traverse list
for amount in transactions:

    # Calculate balance
    balance = balance + amount

    # Deposit amount checking
    if amount > 0:
        deposits.append(amount)

        if amount > largest_deposit:
            largest_deposit = amount

    # Withdrawal amount checking
    else:
        withdrawals.append(amount)

        if amount < largest_withdrawal:
            largest_withdrawal = amount

# Display results of final 
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
