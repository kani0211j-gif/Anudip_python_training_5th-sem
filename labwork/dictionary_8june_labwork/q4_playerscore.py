'''
----------------------------------------------------
Problem Statement: Cricket Tournament Statistics

runs = {
 "Virat": 645,
 "Rohit": 512,
 "Gill": 698,
 "Rahul": 435,
 "Hardik": 278,
 "Pant": 534,
 "Surya": 389,
 "Jadeja": 301,
 "Iyer": 455,
 "KL": 410
}

Tasks
1. Display players scoring more than 500 runs.
2. Find the Orange Cap winner.
3. Find the lowest scorer.
4. Calculate total runs scored.
5. Create a list of players scoring below 400.
6. Count players scoring between 400 and 600 runs.
----------------------------------------------------
'''

# creating a dictionary to store players and their runs
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

#--------------------------------------------------
# to display players scoring more than 500 runs

print("Players Scoring More Than 500 Runs :")

for player in runs:
    if runs[player] > 500:
        print(player)

#--------------------------------------------------
# to find the Orange Cap winner

dict_items = list(runs.items())

orange_cap_winner = dict_items[0][0]
highest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_runs:
        orange_cap_winner = item[0]
        highest_runs = item[1]

print("Orange Cap Winner :", orange_cap_winner, "(", highest_runs, ")")

#--------------------------------------------------
# to find the lowest scorer

lowest_scorer = dict_items[0][0]
lowest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_runs:
        lowest_scorer = item[0]
        lowest_runs = item[1]

print("Lowest Scorer :", lowest_scorer, "(", lowest_runs, ")")

#--------------------------------------------------
# to calculate total runs scored

total_runs = 0

for score in runs.values():
    total_runs = total_runs + score

print("Total Tournament Runs :", total_runs)

#--------------------------------------------------
# to create a list of players scoring below 400

below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("Players Scoring Below 400 :")
print(below_400)

#--------------------------------------------------
# to count players scoring between 400 and 600 runs

count = 0

for score in runs.values():
    if score >= 400 and score <= 600:
        count = count + 1

print("Players Between 400 and 600 Runs :", count)

#--------------------------------------------------

