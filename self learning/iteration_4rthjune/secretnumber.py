# Accept secret code
code = int(input("Enter 6 Digit Secret Code: "))

# Count digits
temp = code
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

# Check length
if count != 6:
    print("Invalid Code")

else:

    # Extract first 3 digits
    first = code // 1000

    # Extract last 3 digits
    last = code % 1000

    sum1 = 0
    sum2 = 0

    # Sum of first 3 digits
    while first > 0:
        sum1 = sum1 + first % 10
        first = first // 10

    # Sum of last 3 digits
    while last > 0:
        sum2 = sum2 + last % 10
        last = last // 10

    # Check validity
    if sum1 == sum2:
        print("Valid Code")
    else:
        print("Invalid Code")

