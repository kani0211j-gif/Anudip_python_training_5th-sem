'''2: Hospital Patient Record Management System
Problem Statement
A hospital maintains patient details in a file named patients.txt.
Sample Input/Data (patients.txt)
P101,Anuj,Normal
P102,Rahul,Critical
P103,Priya,Stable
P104,Neha,Critical
P105,Amit,Stable
P106,Sneha,Normal
P107,Karan,Critical
P108,Pooja,Stable
P109,Rohit,Normal
P110,Anjali,Stable
Tasks
1. Display all patient records.
2. Display critical patients.
3. Count patients under each status.
4. Search patient details using Patient ID.
5. Save critical patient records to critical_patients.txt. '''
# Hospital Patient Record Management System
#----------------------------------------
# Open file and read records

filev = open("patients.txt", "r")
if not filev: #to check file is open or not
     exit("Error opening the file.")

records = filev.readlines()
if not records: #to check file is empty or not
    print("The file is empty.")
    print(records)

filev.close()

#----------------------------------------
# 1. Display all patient records

print("All Patient Records :")

for record in records:

    print(record.strip())

#----------------------------------------
# 2. Display critical patients

print("\nCritical Patients :")

for record in records:

    data = record.strip().split(",")

    if data[2] == "Critical":

        print(data[1])

#----------------------------------------
# 3. Count patients under each status

normal = 0
stable = 0
critical = 0

for record in records:

    data = record.strip().split(",")

    if data[2] == "Normal":
        normal += 1

    elif data[2] == "Stable":
        stable += 1

    elif data[2] == "Critical":
        critical += 1

print("\nPatient Count :")
print("Normal :", normal)
print("Stable :", stable)
print("Critical :", critical)

#----------------------------------------
# 4. Search patient using Patient ID

search_id = input("\nEnter Patient ID : ")

found = False

for record in records:

    data = record.strip().split(",")

    if data[0] == search_id:

        print("\nPatient Found :")
        print(record.strip())

        found = True

        break

if found == False:

    print("Patient Not Found")

#----------------------------------------
# 5. Save critical patients to file

file = open("critical_patients.txt", "w")

for record in records:

    data = record.strip().split(",")

    if data[2] == "Critical":

        file.write(record)

file.close()

print("\nCritical Patient Report Generated Successfully.")
#-------------------------------------------------------------------
#output will be
'''All Patient Records :
P101,Anuj,Normal
P102,Rahul,Critical
P103,Priya,Stable
P104,Neha,Critical
P105,Amit,Stable
P106,Sneha,Normal
P107,Karan,Critical
P108,Pooja,Stable
P109,Rohit,Normal
P110,Anjali,Stable

Critical Patients :
Rahul
Neha
Karan

Patient Count :
Normal : 3
Stable : 4
Critical : 3

Enter Patient ID : p101
Patient Not Found

Critical Patient Report Generated Successfully.'''

