'''
2. Employee Performance Dashboard
Problem Statement
Employee performance scores are stored as:
performance = {
 "EMP101": 92,
 "EMP102": 78,
 "EMP103": 45,
 "EMP104": 88,
 "EMP105": 97,
 "EMP106": 56,
 "EMP107": 81,
 "EMP108": 64,
 "EMP109": 39,
 "EMP110": 73
}
Tasks
1. Display employees scoring above 80.
2. Count employees needing improvement (score < 60).
3. Find the top performer.
4. Calculate average performance score.
5. Create separate lists:
o Excellent (≥ 90)
o Good (75–89)
o Average (60–74)
o Poor (< 60) 
'''
#creating dictionaryyy
performance = {
 "EMP101": 92,
 "EMP102": 78,
 "EMP103": 45,
 "EMP104": 88,
 "EMP105": 97,
 "EMP106": 56,
 "EMP107": 81,
 "EMP108": 64,
 "EMP109": 39,
 "EMP110": 73
}
#------------------------------------------------
print("employee scoring above 80 :")

for employee in performance:
    if performance[employee] > 80:
        print(employee)
#------------------------------------------
#count of employee who needs improvement
count = 0 
for value in performance.values():
    if value<60:
        count = count+1
        print("Count employees needing improvement (score < 60): ",count)
#--------------------------------------------
#to find the top performer
dict_items = list(performance.items())

top_employee = dict_items[0][0]
top_score = dict_items[0][1]

for item in dict_items:
    if item[1] > top_score:
        top_employee = item[0]
        top_score = item[1]

print("Top Performer :", top_employee, "(", top_score, ")")

#--------------------------------------------------
# to calculate average performance score

total_score = 0

for score in performance.values():
    total_score = total_score + score

average_score = total_score / len(performance)

print("Average Score :", average_score)

#--------------------------------------------------
# to create separate lists

excellent = []
good = []
average = []
poor = []

for employee in performance:

    if performance[employee] >= 90:
        excellent.append(employee)

    elif performance[employee] >= 75 and performance[employee] <= 89:
        good.append(employee)

    elif performance[employee] >= 60 and performance[employee] <= 74:
        average.append(employee)

    else:
        poor.append(employee)

#--------------------------------------------------
# to display all categories

print("Excellent :")
print(excellent)

print("Good :")
print(good)

print("Average :")
print(average)

print("Poor :")
print(poor)

#--------------------------------------------------
#output
'''
employee scoring above 80 :
EMP101
EMP104
EMP105
EMP107
Count employees needing improvement (score < 60):  1
Count employees needing improvement (score < 60):  2
Count employees needing improvement (score < 60):  3
Top Performer : EMP105 ( 97 )
Average Score : 71.3
Excellent :
['EMP101', 'EMP105']
Good :
['EMP102', 'EMP104', 'EMP107']
Average :
['EMP108', 'EMP110']
Poor :
['EMP103', 'EMP106', 'EMP109']
'''
    

