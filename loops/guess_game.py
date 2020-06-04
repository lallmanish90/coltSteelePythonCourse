import random
random_number = random.randint(1, 10)  # numbers 1- 10
# handle user guesses
# if they guess correct, tell them they won
# otherwise tell them if they are too high or too low

# bonus - let player play again if they want!

guess = None
while guess != random_number:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess > random_number:
        print("TOO HIGH!")
    elif guess < random_number:
        print("TOO LOW!")
    else:
        print("YOU GOT IT!")
        play_again = input("do you want to play again ? (yes/no) ")
        if play_again == "yes":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thanks for playing!")
            break
print(random_number)
