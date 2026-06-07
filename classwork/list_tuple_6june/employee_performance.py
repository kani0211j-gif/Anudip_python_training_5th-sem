# Employee Performance Evaluation

employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# -------------------------------------
# Task 1: Employees scoring 80 or above

print("Employees Scoring 80 or Above:")

for record in employees:

    if(record[2] >= 80):
        print(record[0], record[1], record[2])

# -------------------------------------
# Task 2: Count employees needing improvement

count = 0

for record in employees:

    if(record[2] < 60):
        count += 1

print("\nEmployees Needing Improvement :", count)

# -------------------------------------
# Task 3: Highest Performer

highest = employees[0]

for record in employees:

    if(record[2] > highest[2]):
        highest = record

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])

# -------------------------------------
# Task 4: Names of employees scoring above 75

high_performers = []

for record in employees:

    if(record[2] > 75):
        high_performers.append(record[1])

print("\nHigh Performers:")
print(high_performers)

# -------------------------------------
# Task 5: Performance Categories

print("\nPerformance Categories:")

for record in employees:

    if(record[2] >= 90):
        print(record[1], "-> Excellent")

    elif(record[2] >= 75):
        print(record[1], "-> Good")

    elif(record[2] >= 60):
        print(record[1], "-> Average")

    else:
        print(record[1], "-> Needs Improvement")

