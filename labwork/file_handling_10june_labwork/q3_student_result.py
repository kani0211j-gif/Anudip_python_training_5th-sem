''' Student Result Processing System . Student Result Processing System
Problem Statement
Student marks are stored in results.txt.
File Format
S101,Anuj,85
S102,Rahul,72
S103,Priya,96
S104,Neha,68
S105,Amit,39
S106,Sneha,54
S107,Karan,91
S108,Pooja,78
S109,Rohit,47
S110,Anjali,88
Requirements
Write a program to:
1. Display all student records.
2. Search a student using Student ID.
3. Find topper and lowest scorer.
4. Calculate class average.
5. Count pass and fail students.
6. Generate grades:
o A (90+)
o B (75–89)
o C (40–74)
o F (<40)
7. Write grade reports into a new file named grades.txt. '''
#-----------------------------------------------------------------------------------------
# Function to display all student records
def display_students():

    filev = open('results.txt', 'r')

    if not filev: #to check file is open or not
        exit("Error opening the file.")

    content = filev.read()

    if not content: #to check file is empty or not
        print("The file is empty.")
    else:
        print("Student ID, Student Name, Marks")
        print(content)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to search a student using Student ID
def search_student():

    student_id = input("Enter Student ID to search: ")

    filev = open('results.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    found = False

    lines = filev.readlines()

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 3:
            continue

        if data[0] == student_id:

            print("Student Found")
            print("Student ID :", data[0])
            print("Student Name :", data[1])
            print("Marks :", data[2])

            found = True
            break

    if found == False:
        print("Student not found.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to find topper and lowest scorer
def topper_lowest():

    filev = open('results.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    topper_name = ""
    topper_marks = -1

    low_name = ""
    low_marks = 101

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 3:
            continue

        marks = int(data[2])

        if marks > topper_marks:

            topper_marks = marks
            topper_name = data[1]

        if marks < low_marks:

            low_marks = marks
            low_name = data[1]

    print("Topper :", topper_name, "-", topper_marks)
    print("Lowest Scorer :", low_name, "-", low_marks)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to calculate class average
def class_average():

    filev = open('results.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    total = 0
    count = 0

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 3:
            continue

        total = total + int(data[2])
        count = count + 1

    average = total / count

    print("Class Average :", average)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to count pass and fail students
def pass_fail():

    filev = open('results.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    pass_count = 0
    fail_count = 0

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 3:
            continue

        marks = int(data[2])

        if marks >= 40:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    print("Pass Students :", pass_count)
    print("Fail Students :", fail_count)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to generate grades and write in grades.txt
def generate_grades():

    filev = open('results.txt', 'r')

    if not filev:
        exit("Error opening the file.")

    lines = filev.readlines()

    filev.close()

    filev = open('grades.txt', 'w')

    for line in lines:

        data = line.strip().split(',')

        if len(data) != 3:
            continue

        marks = int(data[2])

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        filev.write(data[0] + "," + data[1] + "," + str(marks) + "," + grade + "\n")

    print("Grade report generated successfully in grades.txt")

    filev.close()
#-----------------------------------------------------------------------------------------
# Main Menu
while True:

    print("\n===== STUDENT RESULT PROCESSING SYSTEM =====")
    print("1. Display Student Records")
    print("2. Search Student")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grade Report")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    #-------------------------------------------------------------------------------------

    if choice == 1:
        display_students()

    elif choice == 2:
        search_student()

    elif choice == 3:
        topper_lowest()

    elif choice == 4:
        class_average()

    elif choice == 5:
        pass_fail()

    elif choice == 6:
        generate_grades()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
#-----------------------------------------------------------------------------------------

