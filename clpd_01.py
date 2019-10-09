# Modified from "Prisoner's Dilemma (Simple version).ipynb"
#
#     Original:  khalilt93
# This version:  MDT        2019.10.09
#
# This is a command line version extracted from the jupyter notebook version. As a demo
# of command line play.

from random import choice, randint
from time   import sleep
from sys    import exit

introString = """

Welcome to the Prisoner's Dilemma Game!

   You must decide whether you want to cooperate or not cooperate with your partner.
   Based on the combination of your decisions you both will win certain amounts of money.
   If you both cooperate, you will both receive $2. If you both do not cooperate (defect), 
   you will both receive $1. However, if one of you cooperates while the other defects, 
   the person that cooperated will win $0 while the person that defected will win $3.
   
   You will play 10 rounds with each other total before final earnings are tallied.
   
   You are PLAYER 1
   
   Let's Begin!
"""

print(introString)

# Some silliness to make it look like there is a server with players somewhere:

new = input("\nAre you ready to start? Please enter y or n   ")
    
if new.upper() == "Y":
    print("\nConnecting to Game server. We will find a partner for you, HOLD ON.\n")
    print("Searching for player", end="", flush=True)
    for x in range(randint(12,24)):
        sleep(0.25)
        print(".", end="", flush=True)
    print("\nNew player found!\n")
else:
    print("\nSorry to see you go!\n\n")
    exit()

# Real game below this

game_on = True
while game_on:
    decision = ["c","d"]
    outcomes = []
    rounds   = 1
    player1_earnings = 0
    player2_earnings = 0
    num_coop_player1 = 0
    num_def_player1  = 0
    
    while rounds < 11:
        player1 = " "
        player2 = " "
        print("\nROUND {}".format(rounds))
        while player1.lower() not in decision:
            player1 = input("\nPlease make a decision to cooperate (c) or defect (d). (Type 'c' or 'd' for your responses):  ")

        
        print("\nWaiting for player 2 decision.\n\n")   # More subterfuge
        sleep(randint(1,4))            
            
            
        while player2.lower() not in decision:
            if rounds == 1:
                player2 = "c"
            if rounds == 2:
                player2 = choice(decision)
            if 8 >= rounds >= 3:
                if outcomes[-2:] == ["cc","cc"]:
                    player2 = "c"
                elif outcomes[-2:] == ["cc","cd"]:
                    player2 = "c"
                elif outcomes[-2:] == ["dc","dd"]:
                    player2 = "d"
                elif outcomes[-2:] == ["dd","dd"]:
                    player2 = "d"
                else:
                    player2 = choice(decision)
            if 8 >= rounds >= 5:
                if outcomes[-4:] == ["cc","cc","cc","cc"]:
                    player2 = "d"
            if rounds > 8:
                player2 = "d"

        if player1 == "c" and player2 == "c":
            player1_earnings += 2
            player2_earnings += 2
            num_coop_player1 += 1
            rounds           += 1
            outcomes         += ["cc"]

            print("\nBoth players chose to cooperate!")
            print("Player 1 has won $2 and Player 2 has won $2.")
            print("Player 1 has earned ${} total, Player 2 has earned ${} total.".format(player1_earnings,player2_earnings))

        if player1 == "c" and player2 == "d":
            player1_earnings += 0
            player2_earnings += 3
            num_coop_player1 += 1
            rounds           += 1
            outcomes         += ["cd"]

            print("\nPlayer 1 chose to cooperate, Player 2 chose to defect!")
            print("Player 1 has won $0 and Player 2 has won $3.")
            print("Player 1 has earned ${} total, Player 2 has earned ${} total.".format(player1_earnings,player2_earnings))

        if player1 == "d" and player2 == "c":
            player1_earnings += 3
            player2_earnings += 0
            num_def_player1  += 1
            rounds           += 1
            outcomes         += ["dc"]

            print("\nPlayer 1 chose to defect, Player 2 chose to cooperate!")
            print("Player 1 has won $3 and Player 2 has won $0.")
            print("Player 1 has earned ${} total, Player 2 has earned ${} total.".format(player1_earnings,player2_earnings))

        if  player1 == "d" and player2 == "d":
            player1_earnings += 1
            player2_earnings += 1
            num_def_player1  += 1
            rounds           += 1
            outcomes         += ["dd"]

            print("\nBoth players chose to defect!")
            print("Player 1 has won $1 and Player 2 has won $1.")
            print("Player 1 has earned ${} total, Player 2 has earned ${} total.".format(player1_earnings,player2_earnings))
        print(outcomes)

    print("\n\n\nOverall Game Results:\n")
    print("\nGreat game! Player 1 earned ${} total while Player 2 earned ${} total.".format(player1_earnings,player2_earnings))
    print("Player 1, you cooperated a total of {} times and defected a total of {} times.".format(num_coop_player1,num_def_player1))
    
    new = input("\nWould you like to play again? y/n   ")
    
    if new.upper() == "Y":
        print("\nWe will find a partner for you, HOLD ON.\n")
        print("Searching for player", end="", flush=True)
        for x in range(randint(12,32)):
            sleep(0.25)
            print(".", end="", flush=True)
        print("\nNew player found!\n")
        continue
        
    if new.upper() == "N":
        print("\nOK, Thanks for playing!")
        break

print("\n\nProgram Exiting...\n")
            