# Accept number of racers
n = int(input("Enter Number of Racers: "))

# Accept first racer's lap time
time = float(input("Enter Lap Time of Racer : "))

fastest = time
slowest = time

fastest_pos = 1
slowest_pos = 1

# Accept remaining racers
i = 2

while i <= n:

    time = float(input("Enter Lap Time of Racer: "))

    if time < fastest:
        fastest = time
        fastest_pos = i

    if time > slowest:
        slowest = time
        slowest_pos = i

    i = i + 1

# Calculate difference
difference = slowest - fastest

# Display result
print("Fastest Racer Position =", fastest_pos)
print("Slowest Racer Position =", slowest_pos)
print("Difference =", difference)

