''' Daily Expense Tracker and Report Generator Problem Statement
Daily expenses are recorded in expenses.txt.
File Format
Food,450
Travel,300
Shopping,1200
Electricity,850
Internet,700
Entertainment,600
Medicine,400
Education,1500
Fuel,900
Miscellaneous,250
Requirements
Develop a program to:
1. Display all expenses.
2. Calculate total expenditure.
3. Find the category with highest and lowest spending.
4. Display expenses greater than ₹800.
5. Add a new expense category.
6. Update an existing expense amount.
7. Generate a summary report in report.txt containing:
o Total Expenses
o Highest Expense Category
o Lowest Expense Category
o Categories spending more than ₹800'''
#-----------------------------------------------------------------------------------------
# Function to display all expenses
def display_expenses():

    filev = open('expenses.txt', 'r')

    if not filev: #to check file is open or not
        exit("Error opening the file.")

    content = filev.read()

    if not content: #to check file is empty or not
        print("The file is empty.")
    else:
        print("Category, Amount")
        print(content)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to calculate total expenditure
def total_expense():

    filev = open('expenses.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    total = 0

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 2:
            continue

        total = total + int(data[1])

    print("Total Expenditure :", total)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to find highest and lowest expense category
def highest_lowest_expense():

    filev = open('expenses.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    high_category = ""
    high_amount = -1

    low_category = ""
    low_amount = 999999

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 2:
            continue

        amount = int(data[1])

        if amount > high_amount:

            high_amount = amount
            high_category = data[0]

        if amount < low_amount:

            low_amount = amount
            low_category = data[0]

    print("Highest Expense Category :", high_category)
    print("Amount :", high_amount)

    print("Lowest Expense Category :", low_category)
    print("Amount :", low_amount)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to display expenses greater than 800
def expenses_above_800():

    filev = open('expenses.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    found = False

    print("Expenses Greater Than 800")

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 2:
            continue

        if int(data[1]) > 800:

            print(line.strip())

            found = True

    if found == False:
        print("No record found.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to add a new expense category
def add_expense():

    category = input("Enter Expense Category : ")
    amount = input("Enter Amount : ")

    filev = open('expenses.txt', 'a')

    if not filev:
        exit("Error opening the file.")

    filev.write(category + "," + amount + "\n")

    print("Expense category added successfully.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to update expense amount
def update_expense():
    category = input("Enter Category to update : ")

    filev = open('expenses.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    filev.close()

    found = False

    for i in range(len(lines)):

        data = lines[i].strip().split(',')

        if len(data) != 2:
            continue

        if data[0].lower() == category.lower():

            new_amount = input("Enter New Amount : ")

            lines[i] = data[0] + "," + new_amount + "\n"

            found = True

            print("Expense updated successfully.")

    if found == False:
        print("Category not found.")

    filev = open('expenses.txt', 'w')

    for line in lines:
        filev.write(line)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to generate report in report.txt
def generate_report():

    filev = open('expenses.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    filev.close()

    total = 0

    high_category = ""
    high_amount = -1

    low_category = ""
    low_amount = 999999

    above_800 = []

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 2:
            continue

        amount = int(data[1])

        total = total + amount

        if amount > high_amount:

            high_amount = amount
            high_category = data[0]

        if amount < low_amount:

            low_amount = amount
            low_category = data[0]

        if amount > 800:

            above_800.append(data[0])

    filev = open('report.txt', 'w')

    filev.write("Total Expenses : " + str(total) + "\n")
    filev.write("Highest Expense Category : " + high_category + "\n")
    filev.write("Lowest Expense Category : " + low_category + "\n")
    filev.write("Categories Spending More Than 800\n")

    for category in above_800:
        filev.write(category + "\n")

    filev.close()

    print("Report generated successfully in report.txt")

#-----------------------------------------------------------------------------------------

# Main Menu
while True:

    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Find Highest and Lowest Expense")
    print("4. Display Expenses Greater Than 800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Report")
    print("8. Exit")

    choice = int(input("Enter your choice : "))
#-----------------------------------------------------------------------------------------
    if choice == 1:
        display_expenses()

    elif choice == 2:
        total_expense()

    elif choice == 3:
        highest_lowest_expense()

    elif choice == 4:
        expenses_above_800()

    elif choice == 5:
        add_expense()

    elif choice == 6:
        update_expense()

    elif choice == 7:
        generate_report()

    elif choice == 8:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")

#-----------------------------------------------------------------------------------------

