#To check booked and available seat
#list of seats 
seats=[1,0,1,1,0,0,1,1,1,0]
available_seat_number=[]
#count of booked seats 
booked_seat=1
#count of available seats
available_seat=0
#by count fuction counting the available nd booked seats
#printing the available nd bookes seats
print("Booked seats :",seats.count(booked_seat))
print("Available seats :",seats.count(available_seat))
# Find first available seat
first_available = 0
for i in range(len(seats)):

    if seats[i] == 0:
        available_seat_number.append(i + 1)
    
        if first_available == 0:
           first_available = i + 1
        
print("first available seat : ",first_available)
print("Available Seat Numbers :", available_seat_number)

# Bus occupancy percentage
occupancy = (seats.count(booked_seat) * 100) / len(seats)

print("Bus Occupancy :", int(occupancy), "%", sep="")

if occupancy > 70:
    print("Status : More Than 70% Occupied")
else:
    print("Status : Not More Than 70% Occupied")



