#IMPORT "RANDOM" MODULE 
from dice import roll_d4, roll_d8
# WELCOME MESSAGE

print("Welcome to the Battle of Dices!")

#VARIABLS FOR WINS
player1_wins = 0
player2_wins = 0
gameover = False
rounds = 0



#ROUND 1  (DICE ROLL)
while not gameover:
    rounds += 1
    input("PRESS ENTER TO ROLL THE DICE")

    player1_roll = roll_d4()
    player2_roll = roll_d4()
    player1_rollD8 = roll_d8()
    player2_rollD8 = roll_d8()

    #totals
    player1_total = player1_roll + player1_rollD8
    player2_total = player2_roll + player2_rollD8

    print(f"Player 1 rolled a D4 = {player1_roll} and a D8 = {player1_rollD8} (Total = {player1_total})")
    print(f"Player 2 rolled a D4 = {player2_roll} and a D8 = {player2_rollD8} (Total = {player2_total})")

    input("\nPress ENTER to continue.")

    if player1_total > player2_total:
        player1_wins += 1
        print(f"Player 1 rolled a total of {player1_total}! That's higher than {player2_total}")
        print("Player 1 wins this round!")
    elif player1_total == player2_total:
        print("Its a tie! Noone gets a point.")
    else:
        player2_wins = player2_wins + 1
        print(f"Player 2 Rolled a total of {player2_total}!Thats higher than", (player1_total))
        print("Player 2 wins this round!")

    #COUNT SCORE
    print("The score is Player1 =", player1_wins, " AGAINST", "Over Player2 =", player2_wins)

    #WHO WON
    if player1_wins == 3:
        print(f"Player 1 is the new GRANDMASTER IN DICES IN {rounds} ROUNDS")
        gameover = True
    elif player2_wins == 3:
        print(f"Player 2 is the new GRANDMASTER IN DICES IN {rounds} ROUNDS")
        gameover = True
    else:
        print(" ")
        print("THE BATTLE IS ONGOING, WHO WILL TAKE HOME THE VICTORY?")

# GAME OVER
    