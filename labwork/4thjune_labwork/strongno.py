# Accept a number from user
num = int(input("Enter a Number: "))

# Store original number for comparison
original_num = num

# Variable to store sum of factorials
sum_factorial = 0

# Process each digit of the number
while num > 0:

    # Extract last digit
    digit = num % 10

    # Calculate factorial of the digit
    factorial = 1
    i = 1

    while i <= digit:
        factorial = factorial * i
        i = i + 1

    # Add factorial to sum
    sum_factorial = sum_factorial + factorial

    # Remove last digit
    num = num // 10

# Check whether number is Strong Number
if sum_factorial == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is not a Strong Number")

