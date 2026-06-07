units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# variables for counting and tracking
eco_houses_count = 0
max_usage_house = ""
highest_units = 0

# lists and dicts for categorization
high_usage_houses = []
campaign_targets = []
categories_report = []

# process everything in one single loop
for house, usage in units.items():
    # 1. check high usage (> 300)
    if usage > 300:
        high_usage_houses.append(f"{house} : {usage}")
        
    # 2. count eco houses (< 200)
    if usage < 200:
        eco_houses_count += 1
        
    # 3. track max consumption
    if usage > highest_units:
        highest_units = usage
        max_usage_house = house
        
    # 4. check campaign eligibility (> 400)
    if usage > 400:
        campaign_targets.append(house)
        
    # 5. categorize house status
    if usage < 200:
        status = "Low"
    elif usage <= 350:
        status = "Medium"
    else:
        status = "High"
    categories_report.append(f"{house} : {status}")

# printing the combined results
print("--- High Usage Houses (>300) ---")
for item in high_usage_houses:
    print(item)

print("\nHouses using < 200 units:", eco_houses_count)
print(f"Max consumption house: {max_usage_house} with {highest_units} units")
print("Houses targeted for campaign:", campaign_targets)

print("\n--- Usage Categories ---")
for report in categories_report:
    print(report)

