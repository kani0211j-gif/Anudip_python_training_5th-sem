''': Employee Attendance Monitoring System
Problem Statement
Employee attendance records are stored in attendance.txt.
Sample Input/Data (attendance.txt)
EMP101,P
EMP102,A
EMP103,P
EMP104,P
EMP105,A
EMP106,P
EMP107,P
EMP108,A
EMP109,P
EMP110,P
Tasks
1. Count present and absent employees.
2. Display absent employee IDs.
3. Calculate attendance percentage.
4. Generate an absentee report in absent_report.txt.
5. Display employees eligible for attendance awards (100% attendance).'''
#------------------------------------------------------------------------
#to open the file  
file = open("attendance.txt","r")
if not file: #to check file is open or not
     exit("Error opening the file.")
records = file.readlines()
if not records: #to check file is empty or not
    print("The file is empty.")
#-------------------------------------------------------------------
file.close()
#------------------------------------------------------------
#to display absent emplyee-----------------------------------
present = 0
absent = 0

report = open("absent_report.txt","w")

print("Absent Employee IDs :")

for record in records:

    data = record.strip().split(",")

    if data[1] == "P":

        present += 1

    else:

        absent += 1

        print(data[0])

        report.write(record)

report.close()
#--------------------------------------------------------------------
attendance_percentage = (present / len(records)) * 100

print("\nPresent Employees :", present)
print("Absent Employees :", absent)
print("Attendance Percentage :", attendance_percentage,"%")

print("Absentee Report Generated Successfully.")

print("Attendance Award Eligibility :")
print("Not Applicable")
#-----------------------------------------------------------------------
#output will be
'''Absent Employee IDs :
EMP102
EMP105
EMP108

Present Employees : 7
Absent Employees : 3
Attendance Percentage : 70.0 %
Absentee Report Generated Successfully.
Attendance Award Eligibility :
Not Applicable'''

