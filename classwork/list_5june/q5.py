#To check booked and available seat
#list of seats 
seats=[1,0,1,1,0,0,1,1,1,0]
#count of booked seats 
booked_seat=0
#count of available seats
available_seat=1
#by count fuction counting the available nd booked seats
#printing the available nd bookes seats
print("Booked seats :",seats.count(booked_seat))
print("Available seats :",seats.count(available_seat))
# Find first available seat
for i in range(len(seats)):

    if seats[i] == 0:
        first_available = i + 1
        break
print("first available seat : ",first_available)




