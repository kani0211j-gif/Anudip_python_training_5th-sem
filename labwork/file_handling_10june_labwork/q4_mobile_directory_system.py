'''Mobile Contact Directory System
Problem Statement
Contacts are stored in contacts.txt.
File Format
Anuj,9876543210
Rahul,9876543211
Priya,9876543212
Neha,9876543213
Amit,9876543214
Sneha,9876543215
Karan,9876543216
Pooja,9876543217
Rohit,9876543218
Anjali,9876543219
Requirements
Create a menu-driven application to:
1. Display all contacts.
2. Search a contact by name.
3. Add a new contact.
4. Update an existing contact number.
5. Delete a contact.
6. Display contacts whose names start with a vowel.
7. Save all modifications back to the file. '''
#------------------------------------------------------------------
''' Mobile Contact Directory System '''
#-----------------------------------------------------------------------------------------
# Function to display all contacts
def display_contacts():

    filev = open('contacts.txt', 'r')

    if not filev: #to check file is open or not
        exit("Error opening the file.")

    content = filev.read()

    if not content: #to check file is empty or not
        print("The file is empty.")
    else:
        print("Name, Contact Number")
        print(content)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to search contact by name
def search_contact():

    name = input("Enter Name to search: ")

    filev = open('contacts.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    found = False

    lines = filev.readlines()

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 2:
            continue

        if data[0].lower() == name.lower():

            print("Contact Found")
            print("Name :", data[0])
            print("Number :", data[1])

            found = True
            break

    if found == False:
        print("Contact not found.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to add a new contact
def add_contact():

    name = input("Enter Name : ")
    number = input("Enter Contact Number : ")

    filev = open('contacts.txt', 'a')

    if not filev:
        exit("Error opening the file.")

    filev.write(name + "," + number + "\n")

    print("Contact added successfully.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to update contact number
def update_contact():

    name = input("Enter Name to update: ")

    filev = open('contacts.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    filev.close()

    found = False

    for i in range(len(lines)):

        data = lines[i].strip().split(',')

        if len(data) != 2:
            continue

        if data[0].lower() == name.lower():

            new_number = input("Enter New Contact Number : ")

            lines[i] = data[0] + "," + new_number + "\n"

            found = True

            print("Contact updated successfully.")

    if found == False:
        print("Contact not found.")

    filev = open('contacts.txt', 'w')

    for line in lines:
        filev.write(line)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to delete a contact
def delete_contact():

    name = input("Enter Name to delete: ")

    filev = open('contacts.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    filev.close()

    new_lines = []

    found = False

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 2:
            continue

        if data[0].lower() == name.lower():

            found = True

        else:

            new_lines.append(line)

    if found == True:

        filev = open('contacts.txt', 'w')

        for line in new_lines:
            filev.write(line)

        filev.close()

        print("Contact deleted successfully.")

    else:

        print("Contact not found.")
#-----------------------------------------------------------------------------------------
# Function to display contacts starting with vowels
def vowel_contacts():

    filev = open('contacts.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    found = False

    print("Contacts Starting With Vowel")

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 2:
            continue

        first_char = data[0][0].upper()

        if first_char in "AEIOU":

            print(line.strip())

            found = True

    if found == False:
        print("No contacts found.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Main Menu
while True:

    print("\n===== MOBILE CONTACT DIRECTORY SYSTEM =====")
    print("1. Display Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
 #-------------------------------------------------------------------------------------

    if choice == 1:
        display_contacts()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        vowel_contacts()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")

#-----------------------------------------------------------------------------------------

