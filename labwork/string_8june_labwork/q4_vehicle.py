'''A vehicle number plate is entered:
MH12AB4589
Tasks
Write a program to:
1. Extract state code.
2. Extract district code.
3. Extract vehicle series.
4. Extract vehicle number.
5. Count letters and digits separately.
6. Verify:
o First 2 characters must be alphabets.
o Next 2 must be digits.
o Next 2 must be alphabets.
o Last 4 must be digits.
7. Display whether the number plate is valid. '''
# to ask user to enter vehicle number
vehicle_no = input("Enter Vehicle Number: ").strip()

# validating vehicle number
if vehicle_no == "":
    exit("Vehicle Number cannot be empty.")

print("-----------------------------------------")

# 1. Extract state code
state_code = vehicle_no[0:2]

print("State Code:", state_code)

# ------------------------------------------------

# 2. Extract district code
district_code = vehicle_no[2:4]

print("District Code:", district_code)

# ------------------------------------------------

# 3. Extract vehicle series
series = vehicle_no[4:6]

print("Series:", series)

# ------------------------------------------------

# 4. Extract vehicle number
vehicle_number = vehicle_no[6:]

print("Vehicle Number:", vehicle_number)

# ------------------------------------------------

# 5. Count letters and digits separately

letter_count = 0
digit_count = 0

for ch in vehicle_no:

    if ch.isalpha():
        letter_count += 1

    elif ch.isdigit():
        digit_count += 1

print("Total Letters:", letter_count)
print("Total Digits:", digit_count)

# ------------------------------------------------

# 6. Verify vehicle number format

rule1 = vehicle_no[0:2].isalpha()

rule2 = vehicle_no[2:4].isdigit()

rule3 = vehicle_no[4:6].isalpha()

rule4 = vehicle_no[6:].isdigit() and len(vehicle_no[6:]) == 4

# ------------------------------------------------

# 7. Display whether number plate is valid

if rule1 and rule2 and rule3 and rule4:
    print("Vehicle Number Status: Valid")

else:
    print("Vehicle Number Status: Invalid")
    #-----------------------------------------
#output will be'
'''
Enter Vehicle Number: MH12AB4589
-----------------------------------------
State Code: MH
District Code: 12
Series: AB
Vehicle Number: 4589
Total Letters: 4
Total Digits: 6
Vehicle Number Status: Valid'''

