#parking slots represented as :
slots = [1, 0, 1, 1, 0, 0, 1, 0]
available=0
occupied=1
#printing available nd occupied slots
print("occupied slots are : ",slots.count(occupied))
print("available slots are : ",slots.count(available))
#first available slot
first_available_slot = 0
for i in range(len(slots)):
    if slots[i] == 0:
        first_available_slot = i + 1
        break
print("First available slot number: Slot", first_available_slot)

# 3. Display all available slot numbers
print("All available slot numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print("Slot", i + 1)
# 4. Check whether parking occupancy exceeds 75%
total_slots_count = len(slots)
occupancy_percentage = (slots.count(occupied)/ total_slots_count) * 100
print("Occupancy Percentage:", occupancy_percentage, "%")

if occupancy_percentage > 75:
    print("Alert: Parking occupancy exceeds 75%!")
else:
    print("Status: Occupancy is under control.")
print("\n")

