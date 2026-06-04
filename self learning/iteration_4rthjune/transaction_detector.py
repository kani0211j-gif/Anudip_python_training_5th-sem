# Initialize counters
above = 0
below = 0
total = 0

while True:

    amount = float(input("Enter Transaction Amount (-1 to stop): "))

    if amount == -1:
        break

    if amount > 50000:
        above = above + 1

    if amount < 1000:
        below = below + 1

    total = total + amount

print("Transactions Above 50000 =", above)
print("Transactions Below 1000 =", below)
print("Total Transaction Amount =", total)

