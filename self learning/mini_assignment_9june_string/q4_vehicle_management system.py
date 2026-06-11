''': Vehicle Registration Verification System
Problem Statement
A transport department wants to verify vehicle registration numbers.
Store at least 20 vehicle numbers.
Example
MH12AB4589
DL05XY9988
KA03PQ1234
Requirements
For each registration number:
1. Extract state code.
2. Extract district code.
3. Extract series.
4. Extract vehicle number.
5. Count letters and digits.
6. Validate format:
o First 2 characters = Alphabets
o Next 2 characters = Digits
o Next 2 characters = Alphabets
o Last 4 characters = Digits
7. Display invalid registrations.
8. Count vehicles state-wise.
Challenge
Generate a state-wise report:
MH -> 6 Vehicles
DL -> 4 Vehicles
KA -> 5 Vehicles
UP -> 5 Vehicles'''
#-------------------------------------------------------------------
#to store vehicle numbers
vehicle_no = ["MH12AB4589",
    "DL05XY9988",
    "KA03PQ1234",
    "UP14CD5678",
    "MH20EF7890",
    "DL08GH4567",
    "KA11IJ2345",
    "UP32KL6789",
    "MH15MN1122",
    "DL09OP3344",
    "KA21QR5566",
    "UP70ST7788",
    "MH01UV9900",
    "DL10WX2233",
    "KA05YZ4455",
    "UP16AA6677",
    "MH22BB8899",
    "DL07CC1010",
    "KA09DD2020",
    "UP25EE3030"]
#---------------------------------------------
# validating vehicle number
if vehicle_no == "":
    exit("Vehicle Number cannot be empty.")

print("-----------------------------------------")
#---------------------------------------------
state_count = {}
invalid_registrations = []
#-----------------------------------------------------------
#using for loop extracting details
for vehicle in vehicle_no:
 #----------------------------------------------
# to extract state code
    state_code = vehicle[0:2]
    print("State Code :", state_code)
#--------------------------------------------------
#to extract district code
    district_code = vehicle[2:4]
    print("District Code :", district_code)
#------------------------------------------------------
#to extract series
    series = vehicle[4:6] 
    print("Series :", series)
#----------------------------------------------------------
#to extract vehicle number 
    vehicle_number = vehicle[6:]
    print("Vehicle Number :", vehicle_number)
#-----------------------------------------------------------
# Count Letters and Digits
    letter_count = 0
    digit_count = 0

    for ch in vehicle:

        if ch.isalpha():
            letter_count += 1

        elif ch.isdigit():
            digit_count += 1

    print("Letters :", letter_count)
    print("Digits :", digit_count)
#----------------------------------------------------------------
#to validate the code
valid = True

if not vehicle[0:2].isalpha():
        valid = False

if not vehicle[2:4].isdigit():
        valid = False

if not vehicle[4:6].isalpha():
        valid = False

if not vehicle[6:10].isdigit():
        valid = False

if len(vehicle) != 10:
        valid = False

if valid:
        print("Status : Valid")
else:
        print("Status : Invalid")
        invalid_registrations.append(vehicle)
#---------------------------------------------------------------
#state wise count
if state_code in state_count:
        state_count[state_code] += 1
else:
        state_count[state_code] = 1
#----------------------------------------------------------
# invalid registration 
print("INVALID REGISTRATIONS")
if len(invalid_registrations) == 0:
    print("No Invalid Registration Found")
else:
    for reg in invalid_registrations:
        print(reg)

# -----------------------------
# State Wise Report
# -----------------------------

print("STATE WISE REPORT")
for state in state_count:
    print(state, "->", state_count[state], "Vehicles")
#-------------------------------------------------------------
#output will be 
'''State Code : MH
District Code : 12
Series : AB
Vehicle Number : 4589
Letters : 4
Digits : 6
State Code : DL
District Code : 05
Series : XY
Vehicle Number : 9988
Letters : 4
Digits : 6
State Code : KA
District Code : 03
Series : PQ
Vehicle Number : 1234
Letters : 4
Digits : 6
State Code : UP
District Code : 14
Series : CD
Vehicle Number : 5678
Letters : 4
Digits : 6
State Code : MH
District Code : 20
Series : EF
Vehicle Number : 7890
Letters : 4
Digits : 6
State Code : DL
District Code : 08
Series : GH
Vehicle Number : 4567
Letters : 4
Digits : 6
State Code : KA
District Code : 11
Series : IJ
Vehicle Number : 2345
Letters : 4
Digits : 6
State Code : UP
District Code : 32
Series : KL
Vehicle Number : 6789
Letters : 4
Digits : 6
State Code : MH
District Code : 15
Series : MN
Vehicle Number : 1122
Letters : 4
Digits : 6
State Code : DL
District Code : 09
Series : OP
Vehicle Number : 3344
Letters : 4
Digits : 6
State Code : KA
District Code : 21
Series : QR
Vehicle Number : 5566
Letters : 4
Digits : 6
State Code : UP
District Code : 70
Series : ST
Vehicle Number : 7788
Letters : 4
Digits : 6
State Code : MH
District Code : 01
Series : UV
Vehicle Number : 9900
Letters : 4
Digits : 6
State Code : DL
District Code : 10
Series : WX
Vehicle Number : 2233
Letters : 4
Digits : 6
State Code : KA
District Code : 05
Series : YZ
Vehicle Number : 4455
Letters : 4
Digits : 6
State Code : UP
District Code : 16
Series : AA
Vehicle Number : 6677
Letters : 4
Digits : 6
State Code : MH
District Code : 22
Series : BB
Vehicle Number : 8899
Letters : 4
Digits : 6
State Code : DL
District Code : 07
Series : CC
Vehicle Number : 1010
Letters : 4
Digits : 6
State Code : KA
District Code : 09
Series : DD
Vehicle Number : 2020
Letters : 4
Digits : 6
State Code : UP
District Code : 25
Series : EE
Vehicle Number : 3030
Letters : 4
Digits : 6
Status : Valid
INVALID REGISTRATIONS
No Invalid Registration Found
STATE WISE REPORT
UP -> 1 Vehicles'''


     





