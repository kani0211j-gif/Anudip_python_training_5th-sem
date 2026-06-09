'''1. Employee ID Validation and Analysis System
Problem Statement
A company generates employee IDs in the following format:
EMP2026ANUJ458
Tasks
Write a program to:
1. Count the number of uppercase letters.
2. Count the number of digits.
3. Extract the joining year.
4. Extract the employee name.
5. Check whether the ID follows these rules:
o Starts with "EMP"
o Contains exactly 4 digits for the year
o Ends with exactly 3 digits
6. Create a list containing all digits present in the ID.
7. Find the sum of all digits present in the ID.
8. Display whether the ID is valid or invalid.'''
#---------------------------------------------------------
#creating the employee ID
# to ask user to enter employee id
emp_id = input("Enter Employee ID: ").strip()

# validating employee id
if emp_id == "":
    exit("Employee ID cannot be empty.")

print("-----------------------------------------")

# 1. Count the number of uppercase letters
upper_count = 0

for ch in emp_id:
    if ch.isupper():
        upper_count += 1

print("Uppercase Letters:", upper_count)

# ------------------------------------------------

# 2. Count the number of digits
digit_count = 0

for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

print("Digits:", digit_count)

# ------------------------------------------------

# 3. Extract the joining year
joining_year = emp_id[3:7]

print("Joining Year:", joining_year)

# ------------------------------------------------

# 4. Extract the employee name
employee_name = emp_id[7:-3]

print("Employee Name:", employee_name)

# ------------------------------------------------

# 5. Check whether ID follows rules

rule1 = emp_id.startswith("EMP")

rule2 = joining_year.isdigit() and len(joining_year) == 4

rule3 = emp_id[-3:].isdigit()

# ------------------------------------------------

# 6. Create a list containing all digits
digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

print("Digit List:", digit_list)

# ------------------------------------------------

# 7. Find the sum of all digits
digit_sum = sum(digit_list)

print("Sum of Digits:", digit_sum)

# ------------------------------------------------

# 8. Display whether ID is valid or invalid

if rule1 and rule2 and rule3:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")
 

