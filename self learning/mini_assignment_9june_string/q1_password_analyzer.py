''': Password Security Analyzer
Problem Statement
A cybersecurity company wants to analyze user passwords before allowing account creation.
The system should accept at least 15 passwords and generate a security report.
Requirements
For each password:
1. Count uppercase letters.
2. Count lowercase letters.
3. Count digits.
4. Count special characters.
5. Check minimum length (8 characters).
6. Check if spaces exist.
7. Determine password strength:
o Strong
o Medium
o Weak
8. Display repeated characters.
9. Count vowels and consonants.
10. Identify the most frequently occurring character.
Challenge
Generate a report showing:
Total Passwords Analyzed
Strong Passwords
Medium Passwords
Weak Passwords'''
# Password Security Analyzer
#------------------------------------------------
strong_passwords = 0
medium_passwords = 0
weak_passwords = 0

total_passwords = 15

for i in range(total_passwords):

    print("-----------------------------------------")
    password = input("Enter Password : ")

    # validation
    if password == "":
        print("Password cannot be empty.")
        continue

    uppercase = 0
    lowercase = 0
    digits = 0
    special_characters = 0
    spaces = 0
    vowels = 0
    consonants = 0

    frequency = {} #empty dictionary 

    #------------------------------------------------
    # character analysis
    for char in password:

        # frequency count
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

        # uppercase count
        if char.isupper():
            uppercase = uppercase + 1

        # lowercase count
        elif char.islower():
            lowercase = lowercase + 1

        # digit count
        elif char.isdigit():
            digits = digits + 1

        # space count
        elif char == " ":
            spaces = spaces + 1

        # special character count
        else:
            special_characters = special_characters + 1

        # vowels and consonants
        if char.isalpha():

            if char.lower() in "aeiou":
                vowels = vowels + 1

            else:
                consonants = consonants + 1
 #------------------------------------------------
    # password strength

    if (len(password) >= 8 and
        uppercase > 0 and
        lowercase > 0 and
        digits > 0 and
        special_characters > 0 and
        spaces == 0):

        strength = "Strong"
        strong_passwords = strong_passwords + 1

    elif len(password) >= 8:

        strength = "Medium"
        medium_passwords = medium_passwords + 1

    else:

        strength = "Weak"
        weak_passwords = weak_passwords + 1
#------------------------------------------------
    # repeated characters

    repeated_characters = ""

    for key in frequency:

        if frequency[key] > 1:
            repeated_characters = repeated_characters + key + " "
    #------------------------------------------------
    # most frequent character

    max_character = ""
    max_count = 0

    for key in frequency:

        if frequency[key] > max_count:

            max_count = frequency[key]
            max_character = key
    #------------------------------------------------
    # report

    print("-----------------------------------------")
    print("Password :", password)

    print("Uppercase Letters :", uppercase)
    print("Lowercase Letters :", lowercase)
    print("Digits :", digits)
    print("Special Characters :", special_characters)

    print("Password Length :", len(password))

    if len(password) >= 8:
        print("Minimum Length Check : Valid")
    else:
        print("Minimum Length Check : Invalid")

    if spaces > 0:
        print("Spaces Exist : Yes")
    else:
        print("Spaces Exist : No")

    print("Password Strength :", strength)

    print("Vowels :", vowels)
    print("Consonants :", consonants)

    if repeated_characters != "":
        print("Repeated Characters :", repeated_characters)
    else:
        print("Repeated Characters : None")

    print("Most Frequent Character :", max_character)
    print("Frequency :", max_count)
#----------------------------------------------
# Final Security Report
print("PASSWORD SECURITY REPORT")
print("Total Passwords Analyzed :", total_passwords)
print("Strong Passwords :", strong_passwords)
print("Medium Passwords :", medium_passwords)
print("Weak Passwords :", weak_passwords)

