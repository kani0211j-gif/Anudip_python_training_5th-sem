#------------------------------------------------
# Email Validation & Domain Analytics System
#------------------------------------------------

#dictionary to store domain counts
domain_count = {}

#list to store invalid emails
invalid_emails = []

#------------------------------------------------
#to process 20 email addresses
for i in range(20):

    print("-----------------------------------------")
    email = input("Enter Email Address : ").strip()

    #to check empty email
    if email == "":
        print("Email cannot be empty.")
        continue

    #------------------------------------------------
    #to validate email

    valid = True

    #to check exactly one @
    if email.count("@") != 1:
        valid = False

    #to check . exists
    if "." not in email:
        valid = False

    #to check spaces
    if " " in email:
        valid = False

    #------------------------------------------------
    #to display invalid email

    if valid == False:

        print("Invalid Email :", email)
        invalid_emails.append(email)

        continue

    #------------------------------------------------
    #to extract username

    email_extract = email.split("@")

    username = email_extract[0]

    #------------------------------------------------
    #to extract domain and extension

    domain_extension = email_extract[1].split(".")

    domain = domain_extension[0]

    extension = domain_extension[-1]

    full_domain = email_extract[1]

    #------------------------------------------------
    #to count digits in username

    digit_count = 0

    for char in username:

        if char.isdigit():

            digit_count = digit_count + 1

    #------------------------------------------------
    #to count special characters in email

    special_character_count = 0

    for char in email:

        if not char.isalnum() and char != " ":

            special_character_count = special_character_count + 1

    #------------------------------------------------
    #to count emails belonging to each domain

    if full_domain in domain_count:

        domain_count[full_domain] = domain_count[full_domain] + 1

    else:

        domain_count[full_domain] = 1

    #------------------------------------------------
    #to display report for current email

    print("-----------------------------------------")
    print("Username :", username)
    print("Domain :", domain)
    print("Extension :", extension)

    print("Digits in Username :", digit_count)

    print("Special Characters :", special_character_count)

    print("Valid Email : True")
#------------------------------------------------
#to display invalid emails
print("INVALID EMAILS")
if len(invalid_emails) == 0:

    print("No Invalid Emails Found")

else:

    for email in invalid_emails:

        print(email)

#------------------------------------------------
#to display domain report

print("\n=========================================")
print("DOMAIN REPORT")
print("=========================================")

for key in domain_count:

    print(key, "->", domain_count[key], "users")

