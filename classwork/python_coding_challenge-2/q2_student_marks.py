'''Problem Statement
The marks obtained by students in the final examination are stored as follows:
Sample Data
marks = {
 "Anuj": 92,
 "Rahul": 76,
 "Priya": 88,
 "Neha": 64,
 "Amit": 58,
 "Sneha": 95,
 "Karan": 81,
 "Pooja": 73,
 "Rohit": 47,
 "Anjali": 90
}
Tasks
1. Display students scoring above 85 marks.
2. Find the topper.
3. Find the student with the lowest marks.
4. Calculate class average marks.
5. Generate grades:
o A (90+)
o B (75–89)
o C (50–74)
o F (<50)
6. Create a list of scholarship students (marks ≥ 90). '''
#---------------------------------------------------------------------
# to display students scoring above 85 marks
marks = {
 "Anuj": 92,
 "Rahul": 76,
 "Priya": 88,
 "Neha": 64,
 "Amit": 58,
 "Sneha": 95,
 "Karan": 81,
 "Pooja": 73,
 "Rohit": 47,
 "Anjali": 90
}
print("student scoring above than 85 marks : ")
for student,score in marks.items():
    if score > 85:
       print(student)
#------------------------------------------------------------------------
# to find the topper 
dict_items = list(marks.items())
topper = dict_items[0][0]
highest_marks = dict_items[0][1]
for item in dict_items:
    if item[1] > highest_marks:
        topper = item[0]
        highest_marks = item[1]
print("topper: ")
print(topper)
#----------------------------------------------------------------------------
#to find the student with lowest marks
student_lowest_marks = dict_items[0][0]
lowest_marks = dict_items[0][1]
for item in dict_items:
    if item[1] < lowest_marks:
        student_lowest_marks = item[0]
        lowest_marks = item[1]
print("student with lowest marks: ")
print(student_lowest_marks)
#------------------------------------------------------------------------------
# to calculate class average marks
total_marks = 0 
for student in marks:
    total_marks += marks[student]
average_marks = total_marks / len(marks)
print("class average marks: ",average_marks)
#--------------------------------------------------------------------------
# to generate grades 
grades = {}
for student,mark in marks.items():
    if mark >= 90:
        grades[student] = 'A'
    elif mark >= 75:
        grades[student] = 'B'
    elif mark >= 50:
        grades[student] = 'C'
    else:
        grades[student] = 'F'
print("grades: ")
print(grades)
#---------------------------------------------------------------------------
# to create a list of scholarship students (marks >= 90)
scholarship_students = []
for student,marks in marks.items():
    if marks >= 90:
        scholarship_students.append(student)
print("scholarship students : ")
print(scholarship_students)
#-------------------------------------------------------
#output will be
'''student scoring above than 85 marks : 
Anuj
Priya
Sneha
Anjali
topper: 
Sneha
student with lowest marks: 
Rohit
class average marks:  76.4
grades: 
{'Anuj': 'A', 'Rahul': 'B', 'Priya': 'B', 'Neha': 'C', 'Amit': 'C', 'Sneha': 'A', 'Karan': 'B', 'Pooja': 'C', 'Rohit': 'F', 'Anjali': 'A'}
scholarship students : 
['Anuj', 'Sneha', 'Anjali']'''


