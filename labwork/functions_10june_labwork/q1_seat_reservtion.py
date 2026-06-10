'''Railway Reservation Seat Analyzer
Problem Statement
A railway coach has seats represented as follows:
seats = [
 "Booked", "Available", "Booked", "Booked",
 "Available", "Available", "Booked", "Available",
 "Booked", "Booked", "Available", "Booked"
]
Requirements
Create the following functions:
1. count_seats(seats)
Returns the number of booked and available seats.
2. first_available(seats)
Returns the seat number of the first available seat.
3. occupancy_percentage(seats)
Returns the percentage of occupied seats.
4. display_available_seats(seats)
Displays all available seat numbers.'''
#-----------------------------------------------------------------------
# List of seats
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]
#------------------------------------------------
# Function to count booked and available seats
def count_seats(seats):

    booked = 0
    available = 0

    for seat in seats:

        if seat == "Booked":
            booked += 1

        else:
            available += 1

    return booked, available


#------------------------------------------------
# Function to find first available seat
def first_available(seats):

    for i in range(len(seats)):

        if seats[i] == "Available":
            return i + 1      # seat number starts from 1

    return -1


#------------------------------------------------
# Function to calculate occupancy percentage
def occupancy_percentage(seats):

    booked = 0

    for seat in seats:

        if seat == "Booked":
            booked += 1

    percentage = (booked / len(seats)) * 100

    return percentage


#------------------------------------------------
# Function to display available seat numbers
def display_available_seats(seats):

    print("Available Seat Numbers : ")

    for i in range(len(seats)):

        if seats[i] == "Available":
            print(i + 1, end=" ")

    print()


#------------------------------------------------
# Main Program

booked, available = count_seats(seats)

print("Booked Seats :", booked)
print("Available Seats :", available)

print("First Available Seat :", first_available(seats))

print("Occupancy Percentage :",
      (occupancy_percentage(seats)),"%")

display_available_seats(seats)
#-------------------------------------------------------
#output will be
'''Booked Seats : 7
Available Seats : 5
First Available Seat : 2
Occupancy Percentage : 58.333333333333333336 %
Available Seat Numbers : 
2 5 6 8 11 '''

