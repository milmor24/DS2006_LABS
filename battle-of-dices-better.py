#IMPORT "RANDOM" MODULE 
from dice import roll_d4
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

    print("Player 1 rolled a", (player1_roll))
    print("Player 2 rolled a", (player2_roll))

    input("\nPress ENTER to continue.")

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 Rolled a", (player1_roll),"!", "Thats higher than", (player2_roll))
        print("Player 1 wins this round!")
    elif player1_roll == player2_roll:
        print("Its a tie! Noone gets a point.")
    else:
        player2_wins = player2_wins + 1
        print("Player 2 Rolled a", (player2_roll),"!", "Thats higher than", (player1_roll))
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
