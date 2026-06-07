scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# show players with 50 or more runs
print("--- Players with 50+ runs ---")
for player, runs in scores.items():
    if runs >= 50:
        print(player, ":", runs)

# count total centuries scored
century_count = 0
for runs in scores.values():
    if runs >= 100:
        century_count += 1
print("\nTotal centuries:", century_count)

# find top scorer of match
top_scorer = ""
highest_run = 0
for player, runs in scores.items():
    if runs > highest_run:
        highest_run = runs
        top_scorer = player
print("\nHighest scorer:", top_scorer, "Runs:", highest_run)

# find players with runs below 30
low_scores = []
for player, runs in scores.items():
    if runs < 30:
        low_scores.append(player)
print("\nPlayers scored below 30:", low_scores)

# count players between 50 and 99 runs
between_50_99 = 0
for runs in scores.values():
    if runs >= 50 and runs <= 99:
        between_50_99 += 1
print("\nPlayers scored between 50 and 99:", between_50_99)

