#----------------------------------------------------------------------------------------
# Cricket Tournament Analytics System
# database of 30 cricket players
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 580, "matches": 12, "wickets": 1},
    "Gill": {"runs": 520, "matches": 11, "wickets": 0},
    "Rahul": {"runs": 410, "matches": 10, "wickets": 0},
    "Iyer": {"runs": 390, "matches": 11, "wickets": 2},
    "Hardik": {"runs": 350, "matches": 10, "wickets": 8},
    "Jadeja": {"runs": 310, "matches": 12, "wickets": 12},
    "Ashwin": {"runs": 180, "matches": 10, "wickets": 15},
    "Bumrah": {"runs": 70, "matches": 12, "wickets": 22},
    "Shami": {"runs": 60, "matches": 11, "wickets": 18},
    "Siraj": {"runs": 55, "matches": 12, "wickets": 16},
    "Kuldeep": {"runs": 90, "matches": 10, "wickets": 17},
    "Pant": {"runs": 470, "matches": 11, "wickets": 0},
    "Samson": {"runs": 330, "matches": 9, "wickets": 0},
    "Surya": {"runs": 510, "matches": 11, "wickets": 1},
    "Rinku": {"runs": 280, "matches": 9, "wickets": 0},
    "Tilak": {"runs": 295, "matches": 10, "wickets": 1},
    "Axar": {"runs": 240, "matches": 10, "wickets": 10},
    "Chahal": {"runs": 40, "matches": 8, "wickets": 14},
    "Arshdeep": {"runs": 30, "matches": 9, "wickets": 13},
    "Dhruv": {"runs": 260, "matches": 9, "wickets": 0},
    "Nitish": {"runs": 345, "matches": 10, "wickets": 6},
    "Abhishek": {"runs": 430, "matches": 10, "wickets": 2},
    "Washington": {"runs": 210, "matches": 10, "wickets": 9},
    "Mukesh": {"runs": 25, "matches": 8, "wickets": 11},
    "Prasidh": {"runs": 20, "matches": 8, "wickets": 10},
    "Avesh": {"runs": 35, "matches": 8, "wickets": 12},
    "Harshit": {"runs": 50, "matches": 8, "wickets": 9},
    "Sai": {"runs": 375, "matches": 10, "wickets": 1},
    "Mayank": {"runs": 290, "matches": 9, "wickets": 4}
}

#----------------------------------------------------------------------------------------
# menu driven system
while True:
    print("\n--------------CRICKET TOURNAMENT MENU -------------")
    print("1. Display all player statistics")
    print("2. Find highest run scorer")
    print("3. Find lowest run scorer")
    print("4. Calculate average runs")
    print("5. Find player with maximum wickets")
    print("6. Find all-rounders")
    print("7. Display players scoring above average")
    print("8. Generate categories")
    print("9. Generate team statistics")
    print("10. Display top 5 batsmen")
    print("11. Display top 5 bowlers")
    print("12. Award winners")
    print("13. Tournament Report")
    print("14. Exit")

    choice = input("Enter your choice : ")

    #------------------------------------------------
    # display all players
    if choice == '1':

        print("\n--- ALL PLAYER RECORDS ---")

        for player in players:
            print(player, ":", players[player])

    #------------------------------------------------
    # highest run scorer
    elif choice == '2':

        dict1 = list(players.items())

        highest_player = dict1[0][0]
        highest_runs = dict1[0][1]["runs"]

        for player in players:

            if players[player]["runs"] > highest_runs:

                highest_runs = players[player]["runs"]
                highest_player = player

        print("Highest Run Scorer :", highest_player)
        print("Runs :", highest_runs)

    #------------------------------------------------
    # lowest run scorer
    elif choice == '3':

        dict1 = list(players.items())

        lowest_player = dict1[0][0]
        lowest_runs = dict1[0][1]["runs"]

        for player in players:

            if players[player]["runs"] < lowest_runs:

                lowest_runs = players[player]["runs"]
                lowest_player = player

        print("Lowest Run Scorer :", lowest_player)
        print("Runs :", lowest_runs)

    #------------------------------------------------
    # average runs
    elif choice == '4':

        total = 0
        count = 0

        for player in players:

            total += players[player]["runs"]
            count += 1

        print("Average Runs :", total / count)

    #------------------------------------------------
    # maximum wickets
    elif choice == '5':

        dict1 = list(players.items())

        best_bowler = dict1[0][0]
        max_wickets = dict1[0][1]["wickets"]

        for player in players:

            if players[player]["wickets"] > max_wickets:

                max_wickets = players[player]["wickets"]
                best_bowler = player

        print("Best Bowler :", best_bowler)
        print("Wickets :", max_wickets)

    #------------------------------------------------
    # all rounders
    elif choice == '6':

        print("\n--- ALL ROUNDERS ---")

        for player in players:

            if players[player]["runs"] > 300 and players[player]["wickets"] > 5:

                print(player, ":", players[player])
 #------------------------------------------------
    # players above average
    elif choice == '7':

        total = 0
        count = 0

        for player in players:

            total += players[player]["runs"]
            count += 1

        avg = total / count

        print("\n--- PLAYERS ABOVE AVERAGE ---")

        for player in players:

            if players[player]["runs"] > avg:

                print(player, ":", players[player])
    #------------------------------------------------
    # categories
    elif choice == '8':

        print("\n--- PLAYER CATEGORIES ---")

        for player in players:

            runs = players[player]["runs"]

            if runs >= 500:
                category = "Star Performer"

            elif runs >= 350:
                category = "Good Performer"

            elif runs >= 200:
                category = "Average Performer"

            else:
                category = "Poor Performer"

            print(player, "=>", category)

    #------------------------------------------------
    # team statistics
    elif choice == '9':

        total_runs = 0
        total_wickets = 0
        total_matches = 0
        player_count = 0

        for player in players:

            total_runs += players[player]["runs"]
            total_wickets += players[player]["wickets"]
            total_matches += players[player]["matches"]
            player_count += 1

        print("\n--- TEAM STATISTICS ---")
        print("Total Players :", player_count)
        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)
        print("Total Matches :", total_matches)
#------------------------------------------------
    # top 5 batsmen
    elif choice == '10':

        temp = players.copy()

        print("\n--- TOP 5 BATSMEN ---")

        for i in range(5):

            max_player = None
            max_runs = -1

            for player in temp:

                if temp[player]["runs"] > max_runs:

                    max_runs = temp[player]["runs"]
                    max_player = player

            print(max_player, ":", temp[max_player])

            del temp[max_player]

    #------------------------------------------------
    # top 5 bowlers
    elif choice == '11':

        temp = players.copy()

        print("\n--- TOP 5 BOWLERS ---")

        for i in range(5):

            max_player = None
            max_wickets = -1

            for player in temp:

                if temp[player]["wickets"] > max_wickets:

                    max_wickets = temp[player]["wickets"]
                    max_player = player

            print(max_player, ":", temp[max_player])

            del temp[max_player]

    #------------------------------------------------
    # award winners dictionary
    elif choice == '12':

        award_winners = {}

        for player in players:

            if players[player]["runs"] > 500 or players[player]["wickets"] > 15:

                award_winners[player] = players[player]

        print("\n--- AWARD WINNERS ---")

        for player in award_winners:

            print(player, ":", award_winners[player])

    #------------------------------------------------
    # tournament report
    elif choice == '13':

        dict1 = list(players.items())

        highest_player = dict1[0][0]
        highest_runs = dict1[0][1]["runs"]

        lowest_player = dict1[0][0]
        lowest_runs = dict1[0][1]["runs"]

        best_bowler = dict1[0][0]
        max_wickets = dict1[0][1]["wickets"]

        total_runs = 0
        total_wickets = 0
        total_matches = 0
        player_count = 0

        all_rounder_count = 0

        award_winners = {}

        for player in players:

            total_runs += players[player]["runs"]
            total_wickets += players[player]["wickets"]
            total_matches += players[player]["matches"]
            player_count += 1

            if players[player]["runs"] > highest_runs:

                highest_runs = players[player]["runs"]
                highest_player = player

            if players[player]["runs"] < lowest_runs:

                lowest_runs = players[player]["runs"]
                lowest_player = player

            if players[player]["wickets"] > max_wickets:

                max_wickets = players[player]["wickets"]
                best_bowler = player

            if players[player]["runs"] > 300 and players[player]["wickets"] > 5:

                all_rounder_count += 1

            if players[player]["runs"] > 500 or players[player]["wickets"] > 15:

                award_winners[player] = players[player]

        avg_runs = total_runs / player_count
        #-----------------------------------------------------------------
        print("      TOURNAMENT REPORT")
        print("Total Players :", player_count)

        print("Highest Run Scorer :", highest_player)
        print("Highest Runs :", highest_runs)

        print("Lowest Run Scorer :", lowest_player)
        print("Lowest Runs :", lowest_runs)

        print("Best Bowler :", best_bowler)
        print("Maximum Wickets :", max_wickets)

        print("Average Runs :", avg_runs)

        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)
        print("Total Matches :", total_matches)

        print("All Rounders :", all_rounder_count)

        print("Award Winners :", len(award_winners))
 #------------------------------------------------
    # exit
    elif choice == '14':
        print("Exiting Program...")
        break
#------------------------------------------------
    else:
        print("Invalid Choice")

