'''
----------------------------------------------------
Problem Statement: Smart Electricity Billing System

units = {
 "House101": 320,
 "House102": 180,
 "House103": 510,
 "House104": 275,
 "House105": 150,
 "House106": 430,
 "House107": 220,
 "House108": 390,
 "House109": 145,
 "House110": 600
}

Tasks
1. Display houses consuming more than 400 units.
2. Find the highest-consuming house.
3. Find the lowest-consuming house.
4. Calculate total units consumed.
5. Create lists:
   Low Consumption (< 200)
   Medium Consumption (200–400)
   High Consumption (> 400)
6. Count houses eligible for an energy-saving campaign (consumption > 300).
----------------------------------------------------
'''

# creating a dictionary to store monthly electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

#--------------------------------------------------
# to display houses consuming more than 400 units

print("Houses Consuming More Than 400 Units :")

for house in units:
    if units[house] > 400:
        print(house)

#--------------------------------------------------
# to find the highest-consuming house

dict_items = list(units.items())

highest_house = dict_items[0][0]
highest_units = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_units:
        highest_house = item[0]
        highest_units = item[1]

print("Highest Consumption :")
print(highest_house, "(", highest_units, "units )")

#--------------------------------------------------
# to find the lowest-consuming house

lowest_house = dict_items[0][0]
lowest_units = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_units:
        lowest_house = item[0]
        lowest_units = item[1]

print("Lowest Consumption :")
print(lowest_house, "(", lowest_units, "units )")

#--------------------------------------------------
# to calculate total units consumed

total_units = 0

for value in units.values():
    total_units = total_units + value

print("Total Units Consumed :", total_units)

#--------------------------------------------------
# to create separate lists

low_consumption = []
medium_consumption = []
high_consumption = []

for house in units:

    if units[house] < 200:
        low_consumption.append(house)

    elif units[house] >= 200 and units[house] <= 400:
        medium_consumption.append(house)

    else:
        high_consumption.append(house)

#--------------------------------------------------
# to display all categories

print("Low Consumption :")
print(low_consumption)

print("Medium Consumption :")
print(medium_consumption)

print("High Consumption :")
print(high_consumption)

#--------------------------------------------------
# to count houses eligible for energy-saving campaign

count = 0

for value in units.values():
    if value > 300:
        count = count + 1

print("Eligible for Energy-Saving Campaign :", count)

#--------------------------------------------------
#output will be
'''
Houses Consuming More Than 400 Units :
House103
House106
House110
Highest Consumption :
House110 ( 600 units )
Lowest Consumption :
House109 ( 145 units )
Total Units Consumed : 3220
Low Consumption :
['House102', 'House105', 'House109']
Medium Consumption :
['House101', 'House104', 'House107', 'House108']
High Consumption :
['House103', 'House106', 'House110']
Eligible for Energy-Saving Campaign : 5
'''
