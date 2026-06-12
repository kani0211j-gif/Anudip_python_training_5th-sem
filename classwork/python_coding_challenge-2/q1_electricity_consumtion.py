'''Smart Electricity Billing System
Problem Statement
Monthly electricity consumption (units) of different houses in a residential society is stored as follows:
Sample Data
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
4. Calculate the total units consumed.
5. Create separate lists for:
o Low Consumption (< 200)
o Medium Consumption (200–400)
o High Consumption (> 400)
6. Count houses eligible for an energy-saving campaign (consumption > 300).'''
#-----------------------------------------------------------------------------------
#dictionary of input data  
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
#------------------------------------------------------------------------------------
#to display houses counsuming more than 400 units
print("houses consuming more thn 400 units: ")
for house,consumption in units.items():
    if consumption > 400:
       
        print("\n",house)
#----------------------------------------------------------------------------------
# to find the highest consuming house 
dict_items = list(units.items())
highest_consuming_house=dict_items[0][0]
highest_consumption=dict_items[0][1]
for item in dict_items:
    if item[1] > highest_consumption:
        highest_consuming_house=item[0]
        highest_consumption=item[1]
print("\nhighest consuming house: ")
print(highest_consuming_house)
#-------------------------------------------------------------------------------
#to find the lowest consuming house
lowest_consuming_house=dict_items[0][0]
lowest_consumption=dict_items[0][1]
for item in dict_items:
    if item[1]<lowest_consumption:
        lowest_consumption=item[1]
        lowest_consuming_house=item[0]
print("lowest consuming house: ")
print(lowest_consuming_house)
#--------------------------------------------------------------------------------
# to calculate the total units consumed
total_units = 0
for unit in units.values():
    total_units += unit
print("\ntotal units consumed: ",total_units)
#-------------------------------------------------------------------------------
#to create separate list 
low_consumption=[]
medium_consumption = []
high_consumption = []
for house,consumption in units.items():
    if consumption < 200:
        low_consumption.append(house)
    elif consumption >= 200 and consumption <= 400:
        medium_consumption.append(house)
    else: 
        high_consumption.append(house)
print("\nlow consumption: ")
print(low_consumption)
print("medium consumption: ")
print(medium_consumption)
print("high consumption: ")
print(high_consumption)
#--------------------------------------------------------------------------
# to count houses eligible for energy saving
eligible_house = 0
for house,consumption in units.items():
    if consumption > 300:
        eligible_house += 1
print("houses eligible for energy saving campaign: ",eligible_house)
#--------------------------------------------------------------------
#output will be
'''houses consuming more thn 400 units: 

 House103

 House106

 House110

highest consuming house: 
House110
lowest consuming house: 
House109

total units consumed:  3220

low consumption: 
['House102', 'House105', 'House109']
medium consumption: 
['House101', 'House104', 'House107', 'House108']
high consumption: 
['House103', 'House106', 'House110']
houses eligible for energy saving campaign:  5'''

