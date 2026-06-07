# Sample Data provided in the PDF
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# To Display students scoring 80 or above
print("--- Students scoring 80 or above ---")
for student, score in marks.items():
    if score >= 80:
        print(student, ":", score)

# To Count the number of students who failed (marks < 40)
fail_count = 0
for score in marks.values():
    if score < 40:
        fail_count += 1
print("\nNumber of students who failed:", fail_count)

# To Find the highest scorer
highest_student = ""
highest_score = 0  # Initialize with a very low value
for student, score in marks.items():
    if score > highest_score:
        highest_score = score
        highest_student = student
print("\nHighest scorer:", highest_student, "with marks:", highest_score)

# T0 Create a list of students scoring between 60 and 75
students_60_to_75 = []
for student, score in marks.items():
    if 60 <= score <= 75:
        students_60_to_75.append(student)
print("\nStudents scoring between 60 and 75:", students_60_to_75)

# Task 5: Assign grades
print("\n--- Student Grades ---")
for student, score in marks.items():
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    print(student, ":", grade)

