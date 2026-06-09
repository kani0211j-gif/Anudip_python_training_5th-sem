'''Problem Statement
A user enters an email address:
rahul.sharma2026@gmail.com
Tasks
1. Extract username.
2. Extract domain name.
3. Extract extension.
4. Count digits present in username.
5. Count special characters.
6. Check whether:
   - Exactly one '@' exists.
   - At least one '.' exists after '@'.
7. Display Valid Email or Invalid Email.
---------------------------------------------------------
'''# to ask user to enter email
email = input("Enter Email: ").strip()

# validating email
if email == "":
    exit("Email cannot be empty.")

print("-----------------------------------------")

# 1. Extract username
username = email.split("@")[0]
print("Username:", username)

# 2. Extract domain name
domain = email.split("@")[1].split(".")[0]
print("Domain:", domain)

# 3. Extract extension
extension = email.split(".")[-1]
print("Extension:", extension)

# 4. Count digits present in username
digit_count = 0
for ch in username:
    if ch.isdigit():
        digit_count += 1
print("Digits Found:", digit_count)

# 5. Count special characters
special_count = 0
for ch in email:
    if not ch.isalnum() and ch != "@":
        special_count += 1
print("Special Characters Found:", special_count)

# 6. Check email rules
rule1 = email.count("@") == 1
after_at = email.split("@")[1]
rule2 = "." in after_at

# 7. Display Valid Email or Invalid Email
if rule1 and rule2:
    print("Email Status: Valid")
else:
    print("Email Status: Invalid")
#output will be
'''
Enter Email: rahul.sharma2026@gmail.com
-----------------------------------------
Username: rahul.sharma2026
Domain: gmail
Extension: com
Digits Found: 4
Special Characters Found: 2
Email Status: Valid'''
