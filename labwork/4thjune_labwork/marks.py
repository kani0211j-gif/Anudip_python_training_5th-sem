# Accept marks of 5 subjects

m1 = float(input("Enter marks of Subject 1 : "))
m2 = float(input("Enter marks of Subject 2 : "))
m3 = float(input("Enter marks of Subject 3 : "))
m4 = float(input("Enter marks of Subject 4 : "))
m5 = float(input("Enter marks of Subject 5 : "))

# Total and Percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Count failed subjects
fail_count = 0

if m1 < 40:
    fail_count += 1

if m2 < 40:
    fail_count += 1

if m3 < 40:
    fail_count += 1

if m4 < 40:
    fail_count += 1

if m5 < 40:
    fail_count += 1

# Grade
if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"

# Display Result
print("\n----- RESULT -----")
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Failed Subjects =", fail_count)



