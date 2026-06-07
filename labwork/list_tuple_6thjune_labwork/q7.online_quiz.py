# Given data
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']
# creating counting variables
correct_answers_count = 0
wrong_answers_count = 0
incorrect_question_numbers = []
#generating loop for iteration of count
for i in range(len(correct)):
    if student[i] == correct[i]:
        correct_answers_count = correct_answers_count + 1
    else:
        wrong_answers_count = wrong_answers_count + 1
        incorrect_question_numbers.append(i + 1)

# 1. Calculate and display score
print("Final Quiz Score:", correct_answers_count, "/", len(correct))

# 2. Display incorrectly answered question numbers
print("Incorrect Question Numbers:", incorrect_question_numbers)

# 3. Count correct and wrong answers
print("Total Correct:", correct_answers_count)
print("Total Wrong:", wrong_answers_count)

# 4. Determine pass/fail (minimum 60%)
passing_percentage = (correct_answers_count / len(correct)) * 100
print("Percentage Obtained:", passing_percentage, "%")

if passing_percentage >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")
print("\n")

