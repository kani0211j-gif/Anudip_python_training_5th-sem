'''Problem Statement
A user enters a password.
Python@2026!
Tasks
Write a program to determine whether the password is Strong, Medium, or Weak.
Rules:
• Minimum length 8
• Contains at least:
o 1 uppercase letter
o 1 lowercase letter
o 1 digit
o 1 special character
Additionally:
1. Count uppercase letters.
2. Count lowercase letters.
3. Count digits.
4. Count special characters.
5. Display all digits separately.
6. Display all special characters separately.
Sample Output
Password: Python@2026!
Uppercase Letters: 1
Lowercase Letters: 5
Digits: 4
Special Characters: 2
Digits Found: ['2', '0', '2', '6']
Special Characters Found: ['@', '!']
Password Strength: Strong
'''
#--------------------------------------------------------
# to ask user to enter password
password = input("Enter Password: ").strip()

# validating password
if password == "":
    exit("Password cannot be empty.")

print("-----------------------------------------")

# 1. Count uppercase letters
upper_count = 0

for ch in password:
    if ch.isupper():
        upper_count += 1

print("Uppercase Letters:", upper_count)

# ------------------------------------------------

# 2. Count lowercase letters
lower_count = 0

for ch in password:
    if ch.islower():
        lower_count += 1

print("Lowercase Letters:", lower_count)

# ------------------------------------------------

# 3. Count digits
digit_count = 0
digit_list = []

for ch in password:
    if ch.isdigit():
        digit_count += 1
        digit_list.append(ch)

print("Digits:", digit_count)

# ------------------------------------------------

# 4. Count special characters
special_count = 0
special_list = []

for ch in password:
    if not ch.isalnum():
        special_count += 1
        special_list.append(ch)

print("Special Characters:", special_count)

# ------------------------------------------------

# 5. Display all digits separately
print("Digits Found:", digit_list)

# ------------------------------------------------

# 6. Display all special characters separately
print("Special Characters Found:", special_list)

# ------------------------------------------------

# Check password strength

if (len(password) >= 8 and
    upper_count >= 1 and
    lower_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):

    strength = "Strong"

elif len(password) >= 8 and (upper_count >= 1 or lower_count >= 1):
    
    strength = "Medium"

else:
    
    strength = "Weak"

# ------------------------------------------------

print("Password Strength:", strength)
    

