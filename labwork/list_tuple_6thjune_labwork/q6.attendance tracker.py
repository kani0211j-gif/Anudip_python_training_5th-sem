# Given data
attendance = ['P', 'P', 'A', 'P', '', 'P', 'P', 'P', '', 'P', 'P', '', 'P', 'P', 'P']
# 1. Count present and absent days
present_count = 0
absent_count = 0

for day in attendance:
    if day == 'P':
        present_count = present_count + 1
    else:
        absent_count = absent_count + 1

print("Total Present Days:", present_count)
print("Total Absent Days:", absent_count)

# 2. Calculate attendance percentage
total_days_count = len(attendance)
attendance_percentage = (present_count / total_days_count) * 100
print("Attendance Percentage:", attendance_percentage, "%")

# 3. Determine eligibility (minimum 75% attendance)
if attendance_percentage >= 75:
    print("Eligibility Status: Eligible")
else:
    print("Eligibility Status: Not Eligible")

# 4. Display positions where the student was absent (1-based day number)
print("Absent on days:")
for i in range(len(attendance)):
    if attendance[i] == 'A' or attendance[i] == '':
        print("Day Number:", i + 1)
print("\n")

