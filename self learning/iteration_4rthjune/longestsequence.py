# Accept number of inputs
n = int(input("Enter Number of Values: "))

# Accept first number
prev = int(input("Enter Number: "))

current_length = 1
max_length = 1

count = 1

while count < n:

    # Accept next number
    num = int(input("Enter Number: "))

    # Check increasing sequence
    if num > prev:
        current_length = current_length + 1

    else:
        current_length = 1

    # Update maximum length
    if current_length > max_length:
        max_length = current_length

    prev = num
    count = count + 1

# Display result
print("Longest Sequence Length =", max_length)

