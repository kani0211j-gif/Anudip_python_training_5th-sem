'''Employee Payroll Management System
Problem Statement
A company stores employee details in a text file named employees.txt.
File Format
EMP101,Anuj,45000
EMP102,Rahul,52000
EMP103,Priya,38000
EMP104,Neha,61000
EMP105,Amit,29000
EMP106,Sneha,55000
EMP107,Karan,47000
EMP108,Pooja,72000
EMP109,Rohit,33000
EMP110,Anjali,68000
Requirements
Create a menu-driven program to:
1. Display all employee records.
2. Search employee details using Employee ID.
3. Calculate the average salary.
4. Find the highest-paid and lowest-paid employee.
5. Display employees earning above ₹50,000.
6. Add a new employee record to the file.
7. Generate salary categories:
o High (₹60,000 and above)
o Medium (₹40,000–₹59,999)
o Low (Below ₹40,000) '''
# Employee Payroll Management System
#--------------------------------------------------
# Function to display all employee records
def display_records():

    filev = open("employees.txt", "r")

    line = filev.readline()

    print("\nEmployee Records")

    while line:

        data = line.strip().split(",")

        print("Employee ID :", data[0])
        print("Name        :", data[1])
        print("Salary      :", data[2])
        print("-----------------------------")

        line = filev.readline()

    filev.close()
#--------------------------------------------------
# Function to search employee
def search_employee():

    emp_id = input("Enter Employee ID : ")

    filev = open("employees.txt", "r")

    found = False

    line = filev.readline()

    while line:

        data = line.strip().split(",")

        if data[0] == emp_id:

            print("Employee Found")
            print("Employee ID :", data[0])
            print("Name        :", data[1])
            print("Salary      :", data[2])

            found = True
            break

        line = filev.readline()

    if found == False:
        print("Employee Not Found")

    filev.close()
#--------------------------------------------------
# Function to calculate average salary
def average_salary():

    filev = open("employees.txt", "r")

    line = filev.readline()

    total = 0
    count = 0

    while line:

        data = line.strip().split(",")

        total = total + int(data[2])
        count = count + 1

        line = filev.readline()

    filev.close()

    print("Average Salary :", total / count)
#--------------------------------------------------
# Function for highest and lowest salary
def highest_lowest_salary():

    filev = open("employees.txt", "r")

    line = filev.readline()

    first = line.strip().split(",")

    highest = first
    lowest = first

    line = filev.readline()

    while line:

        data = line.strip().split(",")

        if int(data[2]) > int(highest[2]):
            highest = data

        if int(data[2]) < int(lowest[2]):
            lowest = data

        line = filev.readline()

    filev.close()

    print("Highest Paid Employee :", highest)
    print("Lowest Paid Employee  :", lowest)
#--------------------------------------------------
# Function to show employees above 50000
def above_50000():

    filev = open("employees.txt", "r")

    line = filev.readline()

    print("\nEmployees earning above 50000")

    while line:

        data = line.strip().split(",")

        if int(data[2]) > 50000:
            print(data)

        line = filev.readline()

    filev.close()
#--------------------------------------------------
# Function to add employee
def add_employee():

    filev = open("employees.txt", "a")

    emp_id = input("Enter ID : ")
    name = input("Enter Name : ")
    salary = input("Enter Salary : ")

    filev.write("\n" + emp_id + "," + name + "," + salary)

    filev.close()

    print("Employee Added Successfully")
#--------------------------------------------------
# Function for salary categories
def salary_category():

    filev = open("employees.txt", "r")

    line = filev.readline()

    print("\nHigh Salary (>=60000)")
    print("Medium Salary (40000-59999)")
    print("Low Salary (<40000)")

    while line:

        data = line.strip().split(",")

        salary = int(data[2])

        if salary >= 60000:
            print("High :", data)

        elif salary >= 40000:
            print("Medium :", data)

        else:
            print("Low :", data)

        line = filev.readline()

    filev.close()
# Main Menu
#--------------------------------------------------

while True:

    print("\n1. Display Records")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest & Lowest Salary")
    print("5. Employees Above 50000")
    print("6. Add Employee")
    print("7. Salary Category")
    print("8. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        display_records()

    elif choice == "2":
        search_employee()

    elif choice == "3":
        average_salary()

    elif choice == "4":
        highest_lowest_salary()

    elif choice == "5":
        above_50000()

    elif choice == "6":
        add_employee()

    elif choice == "7":
        salary_category()

    elif choice == "8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")