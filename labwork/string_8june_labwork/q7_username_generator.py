'''7. Username Generator System
Problem Statement
A student enters:
Rahul Sharma
Tasks
Generate a username using the rules:
1. Remove spaces.
2. Convert to lowercase.
3. Append current year (2026).
4. If username length exceeds 12, keep only first 12 characters.
5. Count vowels in the generated username.
6. Count consonants.
7. Display username statistics.
Sample Output
Original Name: Rahul Sharma
Generated Username:
rahulsharma2026
Username Length: 15
Vowels: 5
Consonants: 10
Status: Username Generated Successfully'''
#-----------------------------------------------------
# to ask user to enter name
name = input("Enter Name: ").strip()

# validating name
if name == "":
    exit("Name cannot be empty.")

print("-----------------------------------------")

# 1. Remove spaces
username = name.replace(" ", "")

# 2. Convert to lowercase
username = username.lower()

# 3. Append current year
username = username + "2026"

print("Generated Username:", username)

# 4. If username length exceeds 12, keep only first 12 characters
if len(username) > 12:
    short_username = username[:12]
else:
    short_username = username

print("Username After Limit:", short_username)

# 5. Count vowels in generated username
vowel_count = 0

# 6. Count consonants
consonant_count = 0

for ch in username:
    if ch.isalpha():
        if ch in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

print("Username Length:", len(username))
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# 7. Display username statistics
print("Status: Username Generated Successfully")
#output will be
'''Enter Name: kanishka jain
-----------------------------------------
Generated Username: kanishkajain2026
Username After Limit: kanishkajain
Username Length: 16
Vowels: 5
Consonants: 7
Status: Username Generated Successfully'''


