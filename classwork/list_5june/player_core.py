# PLAYER SCORE

player_score = []

# input of score from user
for i in range(11):
    score = int(input("Enter the score of player {}: ".format(i + 1)))
    player_score.append(score)

# display the score of players
print("\n----- Player Scores -----")

for i in range(11):
    print("Player {} : {}".format(i + 1, player_score[i]))

# find highest score
highest_score = player_score[0]
highest_player = 1

for i in range(1, 11):
    if player_score[i] > highest_score:
        highest_score = player_score[i]
        highest_player = i + 1

print("\nHighest Score =", highest_score)
print("Player {} scored the highest.".format(highest_player))
    

