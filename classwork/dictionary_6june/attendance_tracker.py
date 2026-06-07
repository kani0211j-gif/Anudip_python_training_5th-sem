# Program to track student attendance using a dictionary

attendance_tracker = {}

# Take inputs for 30 students
for i in range(30):
    roll_number = input("Enter Student Roll Number: ")
    status = input("Enter Attendance Status (Present/Absent): ")
    attendance_tracker[roll_number] = status

print("\n--- List of Present Students ---")

# Display roll numbers of students who are present
for roll_number in attendance_tracker:
    if attendance_tracker[roll_number] == "Present":
        print(f"Roll Number: {roll_number}")

