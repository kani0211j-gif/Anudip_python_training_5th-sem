'''Problem Statement
Attendance of a student for 15 days is represented as:
PPAPPPAAPPPPAPP
Where:
P = Present
A = Absent
Tasks
1. Count Present and Absent days.
2. Calculate attendance percentage.
3. Find the longest consecutive streak of Presence.
4. Find the longest consecutive streak of Absence.
5. Determine whether attendance is below 75%
'''
# to ask user to enter attendance record
attendance = input("Enter Attendance Record: ").strip().upper()

# validating attendance record
if attendance == "":
    exit("Attendance record cannot be empty.")

print("-----------------------------------------")

# 1. Count Present and Absent days
present_days = attendance.count("P")
absent_days = attendance.count("A")

print("Present Days:", present_days)
print("Absent Days:", absent_days)

# 2. Calculate attendance percentage
total_days = len(attendance)
attendance_percentage = (present_days / total_days) * 100

print("Attendance Percentage:", round(attendance_percentage, 2), "%")

# 3. Find the longest consecutive streak of Presence
current_present = 0
longest_present = 0

for ch in attendance:
    if ch == "P":
        current_present += 1
        if current_present > longest_present:
            longest_present = current_present
    else:
        current_present = 0

print("Longest Present Streak:", longest_present)

# 4. Find the longest consecutive streak of Absence
current_absent = 0
longest_absent = 0

for ch in attendance:
    if ch == "A":
        current_absent += 1
        if current_absent > longest_absent:
            longest_absent = current_absent
    else:
        current_absent = 0

print("Longest Absent Streak:", longest_absent)

# 5. Determine whether attendance is below 75%
if attendance_percentage < 75:
    print("Attendance Status: Below 75%")
else:
    print("Attendance Status: Above 75%")
#--------------------------------------------------------
#output will be
'''Enter Attendance Record: PPAPPPAAPPPPAPP
-----------------------------------------
Present Days: 11
Absent Days: 4
Attendance Percentage: 73.33 %
Longest Present Streak: 4
Longest Absent Streak: 2
Attendance Status: Below 75%'''


