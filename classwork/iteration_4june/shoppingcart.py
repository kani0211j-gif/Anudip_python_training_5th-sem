# Variable to store total bill amount
total = 0

# Loop will continue until user enters 0
while True:

    # Taking item price as input
    price = int(input("Enter Item Price: "))

    # Check if user wants to stop entering prices
    if price == 0:
        break

    # Add current item price to total bill
    total = total + price

# Display final bill amount
print("\nTotal Bill Amount: ₹", total)

