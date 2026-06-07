quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# variables for counts and topper
low_scores_count = 0
total_quiz_marks = 0
quiz_topper = ""
max_marks = 0

# lists for filtered students
good_scorers = []
passed_students = []

# process everything in one loop
for student, score in quiz_scores.items():
    # 1. total for average
    total_quiz_marks += score
    
    # 2. check for good scorers (>= 15)
    if score >= 15:
        good_scorers.append(f"{student} : {score}")
        
    # 3. count students below 10
    if score < 10:
        low_scores_count += 1
        
    # 4. find the top performer
    if score > max_marks:
        max_marks = score
        quiz_topper = student
        
    # 5. check if passed (>= 10)
    if score >= 10:
        passed_students.append(student)

# calculate average score
batch_avg = total_quiz_marks / len(quiz_scores)

# print all outputs
print("--- Good Scorers (15+) ---")
for item in good_scorers:
    print(item)

print("\nStudents scored below 10:", low_scores_count)
print(f"Quiz Topper: {quiz_topper} with {max_marks} marks")
print("Passed students:", passed_students)
print("Class average:", batch_avg)

