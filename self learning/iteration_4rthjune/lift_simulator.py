# Lift starts from floor 0
current = 0

# Store total travelled floors
total = 0

while True:

    print("Current Floor =", current)

    destination = int(input("Enter Destination (-1 to stop): "))

    if destination == -1:
        break

    # Calculate travelled floors
    if destination > current:
        travelled = destination - current

    else:
        travelled = current - destination

    print("Travelled =", travelled, "floors")

    total = total + travelled

    current = destination

print("Total Travelled =", total, "floors")

