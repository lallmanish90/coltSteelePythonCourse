"""
this is just a refactored game from RockPaperScissor.py


"""
print("Rock, Paper, or Scissors?")
player1 = input("player1 make your move!: ")
print("Rock, Paper, or Scissors?")
player2 = input("player2 make your move!: ")

if player1 == "Rock":
    if player2 == "Scissors":
        print("player1 Wins!")
    elif player2 == "Paper":
        print("player2 wins!")

elif player1 == "Scissors":
    if player2 == "Rock":
        print("player2 wins!")
    elif player2 == "Paper":
        print("player1 wins!")

elif player1 == "Paper":
    if player2 == "Scissors":
        print("player2 wins! ")
    elif player2 == "Rock":
        print("player1 wins!")

elif player1 == player2:
    print("its a tie!")
else:
    print("somthing went wrong!")
