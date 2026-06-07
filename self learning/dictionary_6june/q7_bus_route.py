passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# variables to store counts and totals
few_passengers_count = 0
total_passengers = 0
busiest_stop = ""
max_passengers = 0

# lists to store filtered stops
heavy_traffic_stops = []
extra_bus_needed = []

# single loop to process everything
for stop, count in passengers.items():
    # 1. total for average
    total_passengers += count
    
    # 2. check for heavy traffic (> 20)
    if count > 20:
        heavy_traffic_stops.append(f"{stop} : {count}")
        
    # 3. count stops with fewer than 10
    if count < 10:
        few_passengers_count += 1
        
    # 4. find the busiest stop
    if count > max_passengers:
        max_passengers = count
        busiest_stop = stop
        
    # 5. check if extra bus is needed (> 25)
    if count > 25:
        extra_bus_needed.append(stop)

# calculate the average
avg_passengers = total_passengers / len(passengers)

# printing all results
print("--- Heavy Traffic Stops (>20) ---")
for item in heavy_traffic_stops:
    print(item)

print("\nStops with fewer than 10 passengers:", few_passengers_count)
print(f"Busiest stop: {busiest_stop} with {max_passengers} passengers")
print("Stops needing extra bus:", extra_bus_needed)
print("Average passengers per stop:", avg_passengers)