import random
from dice import roll_d4, roll_d8

winning_score = 3

# NAMES
player_names = [input(f"What is the name of Player {i+1}? ") for i in range(int(input("How many players? ")))]
number_of_players = len(player_names)

# WINS 
player_wins = [0] * number_of_players

# history of all rolls per player
player_rolls_history = [[] for _ in range(number_of_players)]
# ROLL HISTORY
player_rolls_d4_history = [[] for _ in range(number_of_players)]
player_rolls_d8_history = [[] for _ in range(number_of_players)]
player_totals_history = [[] for _ in range(number_of_players)]

# Game loop
gameover = False
rounds = 0

while not gameover:
    print(f"\nRound {rounds+1}:")
    current_rolls = []

    # each player rolls
    for i in range(number_of_players):
        r4, r8 = roll_d4(), roll_d8()
        total = r4 + r8

        # per player history
        player_rolls_history[i].append(total)
        player_rolls_d4_history[i].append(r4)
        player_rolls_d8_history[i].append(r8)
        player_totals_history[i].append(total)

        current_rolls.append(total)
        print(f"  {player_names[i]} rolled: D4={r4}, D8={r8}  (Total={total})")

    # determine round winners
    max_roll = max(current_rolls)
    winners = [player_names[i] for i, r in enumerate(current_rolls) if r == max_roll]
    for i, r in enumerate(current_rolls):
        if r == max_roll:
            player_wins[i] += 1

    print(f"Winners of this round: {', '.join(winners)}")
    print("Current wins:", ", ".join(f"{n}: {w}" for n, w in zip(player_names, player_wins)))

    # check for champion
    max_wins = max(player_wins)
    champs = [player_names[i] for i, w in enumerate(player_wins) if w == max_wins]
    if max_wins >= winning_score:
        if len(champs) == 1:
            print(f"\n {champs[0]} is the newest Battle of Dices Champion with {max_wins} wins!")
        else:
            print(f"\n It's a tie! Champions: {', '.join(champs)} with {max_wins} wins!")
        gameover = True
    else:
        print("This heated Battle of Dices is still going!")
        input("Press ENTER to play the next round...")

    rounds += 1

# Save results
filename = input("\nEnter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ", ".join(
            f"{player_names[i]} rolled D4={player_rolls_d4_history[i][round_number]}, "
            f"D8={player_rolls_d8_history[i][round_number]} (Total={player_totals_history[i][round_number]})"
            for i in range(number_of_players)
        )
        file.write(rolls_str + "\n")

print(f"Results saved to '{filename}'.")
