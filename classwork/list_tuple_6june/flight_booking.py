# Flight Booking Analysis

# Tuple containing passenger records
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

print("Confirmed Passengers:")

# Counters for different booking status
confirmed_count = 0
waiting_count = 0
cancelled_count = 0

# Counter for Delhi passengers
delhi_count = 0

# List to store waiting passengers
waiting_list = []

# List to store destinations
destination_list = []

# Traverse each passenger record
for passenger in bookings:

    # Extract values from tuple
    passenger_id = passenger[0]
    destination = passenger[1]
    status = passenger[2]

    # Store destination in list
    destination_list.append(destination)

    # Display confirmed passengers
    if status == "Confirmed":
        print(passenger_id, destination)

    # Count Delhi passengers
    if destination == "Delhi":
        delhi_count += 1

    # Count booking status
    if status == "Confirmed":
        confirmed_count += 1

    elif status == "Waiting":
        waiting_count += 1

        # Add waiting passenger id into list
        waiting_list.append(passenger_id)

    elif status == "Cancelled":
        cancelled_count += 1


print("\nPassengers Travelling to Delhi:", delhi_count)

print("\nConfirmed:", confirmed_count)
print("Waiting:", waiting_count)
print("Cancelled:", cancelled_count)

print("\nWaiting List:")
print(waiting_list)

# Count bookings for each destination using count() function
delhi_bookings = destination_list.count("Delhi")
mumbai_bookings = destination_list.count("Mumbai")
chennai_bookings = destination_list.count("Chennai")

print("\nMost Booked Destination:")

if delhi_bookings > mumbai_bookings and delhi_bookings > chennai_bookings:
    print("Delhi")

elif mumbai_bookings > delhi_bookings and mumbai_bookings > chennai_bookings:
    print("Mumbai")

else:
    print("Chennai")

