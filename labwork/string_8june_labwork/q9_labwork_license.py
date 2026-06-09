'''Problem Statement
A software license key is entered:
ABCD-EFGH-IJKL-MNOP
Tasks
1. Verify there are exactly 4 group
2. Verify each group contains exactly 4 characters.
3. Count total letters.
4. Count vowels.
5. Remove hyphens and display the merged key.
6. Create a list containing all groups.
7. Display whether the key format is valid.
'''# to ask user to enter license key
license_key = input("Enter License Key: ").strip().upper()

# validating license key
if license_key == "":
    exit("License Key cannot be empty.")

print("-----------------------------------------")

# 6. Create a list containing all groups
groups = license_key.split("-")

print("Groups:", groups)

# 1. Verify there are exactly 4 groups
print("Number of Groups:", len(groups))

# 3. Count total letters
letter_count = 0

for ch in license_key:
    if ch.isalpha():
        letter_count += 1

print("Total Letters:", letter_count)

# 4. Count vowels
vowel_count = 0

for ch in license_key:
    if ch in "AEIOU":
        vowel_count += 1

print("Total Vowels:", vowel_count)

# 5. Remove hyphens and display merged key
merged_key = license_key.replace("-", "")

print("Merged Key:", merged_key)

# 2. Verify each group contains exactly 4 characters
group_valid = True

for group in groups:
    if len(group) != 4:
        group_valid = False

# 7. Display whether the key format is valid
if len(groups) == 4 and group_valid:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")
#output will be
'''Enter License Key: ABCD-EFGH-IJKL-MNOP
-----------------------------------------
Groups: ['ABCD', 'EFGH', 'IJKL', 'MNOP']
Number of Groups: 4
Total Letters: 16
Total Vowels: 4
Merged Key: ABCDEFGHIJKLMNOP
License Key Status: Valid'''

