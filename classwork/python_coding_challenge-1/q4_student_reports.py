'''School Report Card Generator
Problem Statement
Student marks are stored in marks.txt.
Sample Input/Data (marks.txt)
S101,Anuj,92
S102,Rahul,76
S103,Priya,88
S104,Neha,45
S105,Amit,58
S106,Sneha,95
S107,Karan,81
S108,Pooja,73
S109,Rohit,39
S110,Anjali,90
Tasks
1. Calculate grades for all students.
2. Generate a report card file report_card.txt.
3. Display topper details.
4. Count pass and fail students.
5. Display students eligible for merit certificates (marks ≥ 90). '''
#------------------------------------------------------------------------------------------
# to calculate grades for all students

file = open("marks.txt", "r")
if not file: #to check file is open or not
     exit("Error opening the file.")

records = file.readlines()
if not file: #to check file is open or not
     exit("Error opening the file.")
#---------------------------------------------

file.close()
#-----------------------------------------------
topper_name = ""
topper_marks = 0

pass_count = 0
fail_count = 0

report = open("report_card.txt", "w")

print("Merit Certificate Holders :")

for record in records:

    data = record.strip().split(",")

    sid = data[0]
    name = data[1]
    marks = int(data[2])

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    report.write(
        sid + "," + name + "," +
        str(marks) + "," + grade + "\n"
    )

    if marks > topper_marks:

        topper_marks = marks
        topper_name = name

    if marks >= 50:
        pass_count += 1
    else:
        fail_count += 1

    if marks >= 90:
        print(name)

report.close()
#------------------------------------------------------------------
#to print results
print("\nTopper :")
print(topper_name, "(", topper_marks, ")")

print("Passed Students :", pass_count)
print("Failed Students :", fail_count)

print("Report Cards Generated Successfully.")
#---------------------------------------------------------------
#output will be
'''Merit Certificate Holders :
Anuj
Sneha
Anjali

Topper :
Sneha ( 95 )
Passed Students : 8
Failed Students : 2
Report Cards Generated Successfully.'''
