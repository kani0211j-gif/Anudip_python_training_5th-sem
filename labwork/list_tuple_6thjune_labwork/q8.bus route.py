# Given data
passengers = [12, 18, 25, 30, 28, 15, 8]
# 1. Find the busiest stop
max_passengers_value = passengers[0]
busiest_stop_number = 1

for i in range(len(passengers)):
    if passengers[i] > max_passengers_value:
        max_passengers_value = passengers[i]
        busiest_stop_number = i + 1

print("Busiest Stop Number: Stop", busiest_stop_number, "with", max_passengers_value, "passengers")

# 2. Display stops with fewer than 10 passengers
print("Stops with fewer than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop Number:", i + 1)

# 3. Calculate average passengers
total_passengers_sum = 0
for count in passengers:
    total_passengers_sum = total_passengers_sum + count
average_passengers_count = total_passengers_sum / len(passengers)
print("Average passengers per stop:", average_passengers_count)

# 4. Determine whether any stop exceeded 25 passengers
has_exceeded_25 = False
for count in passengers:
    if count > 25:
        has_exceeded_25 = True
        break

if has_exceeded_25 == True:
    print("Did any stop exceed 25 passengers?: Yes")
else:
    print("Did any stop exceed 25 passengers?: No")
print("\n")

