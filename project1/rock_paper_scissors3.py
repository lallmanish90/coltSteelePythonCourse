import random
"""
This version uses randint to assign the variable

print("Rock, Paper, or Scissors?")
player2 = input("player2 make your move!: ")

"""
print("Rock, Paper, or Scissors?")
player1 = input("player1 make your move!: ")
rand_num = random.randint(0, 2)
if rand_num == 0:
    player2 = "Rock"
elif rand_num == 1:
    player2 = "Paper"
elif rand_num == 2:
    player2 = "Scissors"
#print("player2 picked " + player2 + "!")

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
