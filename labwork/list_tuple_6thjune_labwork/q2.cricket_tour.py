# Given data
scores = [45, 78, 12, 100, 67, 8, 90, 55]

print("--- 2. Cricket Tournament Scorecard ---")

# 1. Count half-centuries and centuries
half_centuries_count = 0
centuries_count = 0
for runs in scores:
    if runs >= 50 and runs < 100:
        half_centuries_count = half_centuries_count + 1
    elif runs >= 100:
        centuries_count = centuries_count + 1

print("Half-Centuries:", half_centuries_count)
print("Centuries:", centuries_count)

# 2. Find the highest score
highest_score = scores[0]
for runs in scores:
    if runs > highest_score:
        highest_score = runs
print("Highest Score:", highest_score)

# 3. Display all scores below 20
print("Scores below 20:")
for runs in scores:
    if runs < 20:
        print("-", runs)

# 4. Calculate the average score
total_runs_sum = 0
for runs in scores:
    total_runs_sum = total_runs_sum + runs
average_score = total_runs_sum / len(scores)
print("Average Score:", average_score)
print("\n")

