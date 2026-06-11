''' Problem Statement
The parking status of vehicles in a mall is maintained as follows.
Sample Data
parking_slots = [
 "Occupied", "Vacant", "Occupied", "Vacant",
 "Occupied", "Occupied", "Vacant", "Occupied",
 "Vacant", "Occupied"
]
Tasks
1. Display vacant parking slot numbers.
2. Count occupied and vacant slots.
3. Allocate the first vacant slot to a new vehicle.
4. Calculate parking occupancy percentage.
5. Store updated parking information in parking.txt.
Sample Output
Vacant Parking Slots:
2 4 7 9
Occupied Slots: 6
Vacant Slots: 4
Vehicle Allocated to Slot 2
Occupancy Percentage: 70.0%
Parking Details Saved Successfully.'''
#-------------------------------------------------------------------
# Smart Parking Management System
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]
#=-----------------------------------------------------------
# 1. Display vacant parking slot numbers

print("Vacant Parking Slots :")

for i in range(len(parking_slots)):

    if parking_slots[i] == "Vacant":

        print(i + 1, end=" ")
#------------------------------------------------------------------
# 2. Count occupied and vacant slots

occupied = 0
vacant = 0

for slot in parking_slots:

    if slot == "Occupied":
        occupied += 1

    else:
        vacant += 1

print("\n\nOccupied Slots :", occupied)
print("Vacant Slots :", vacant)
#-----------------------------------------------------------------
# 3. Allocate first vacant slot

for i in range(len(parking_slots)):

    if parking_slots[i] == "Vacant":

        parking_slots[i] = "Occupied"

        print("\nVehicle Allocated to Slot", i + 1)

        break
#-----------------------------------------------------------------
# 4. Occupancy Percentage

occupied = 0

for slot in parking_slots:

    if slot == "Occupied":
        occupied += 1

occupancy = (occupied / len(parking_slots)) * 100

print("Occupancy Percentage :", occupancy, "%")
#--------------------------------------------------------------------
# 5. Store updated parking information

file = open("parking.txt", "w")

for slot in parking_slots:

    file.write(slot + "\n")

file.close()

print("Parking Details Saved Successfully.")
#------------------------------------------------------------------
#output will be 
'''Vacant Parking Slots :
2 4 7 9 

Occupied Slots : 6
Vacant Slots : 4

Vehicle Allocated to Slot 2
Occupancy Percentage : 70.0 %
Parking Details Saved Successfully.'''

