#given data of passengers
passengers = [("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")]
#display of waiting passengers
for records in passengers:
    passenger_name = records[0]
    status=records[1]
if status == "Waiting":
   print(" Name:", passenger_name)  
# 2. Count confirmed and waiting passengers
confirmed_tickets_counter = 0
waiting_tickets_counter = 0
for record in passengers:
    if record[1] == "Confirmed":
        confirmed_tickets_counter = confirmed_tickets_counter + 1
    else:
        waiting_tickets_counter = waiting_tickets_counter + 1

print("\nConfirmed Tickets Total Count:", confirmed_tickets_counter)
print("Waiting List Tickets Total Count:", waiting_tickets_counter)
# 3. Find whether a specific passenger has a confirmed ticket
target_passenger_search = "Priya"
has_confirmed_status = False

for record in passengers:
    if record[0] == target_passenger_search and record[1] == "Confirmed":
        has_confirmed_status = True
        break

if has_confirmed_status == True:
    print("\nVerification: Is", target_passenger_search, "'s ticket confirmed?: Yes")
else:
    print("\nVerification: Is", target_passenger_search, "'s ticket confirmed?: No")

# 4. Create separate lists for confirmed and waiting passengers
confirmed_passengers_output_list = []
waiting_passengers_output_list = []

for record in passengers:
    if record[1] == "Confirmed":
        confirmed_passengers_output_list.append(record[0])
    else:
        waiting_passengers_output_list.append(record[0])

print("\nGenerated Separate Confirmed List:", confirmed_passengers_output_list)
print("Generated Separate Waiting List:", waiting_passengers_output_list)
print("-" * 40)

