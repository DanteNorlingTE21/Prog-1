import random

running = True

while running:


    computer = random.choice(["Rock", "Paper", "Scissors"])

    user = input("rock, paper or scissors? ").capitalize()

    print("The computer chose", computer,"and the user chose", user +".")

    if user == "Exit":
        running = False
    elif user == computer:
        print("Draw....")
    elif user == "Rock" and computer == "Paper":
        print("Computer wins!!")
    elif user == "Rock" and computer == "Scissors":
        print("Player wins...")
    elif user == "Scissors" and computer == "Paper":
        print("Player wins...")
    elif user == "Scissors" and computer == "Rock":
        print("Computer wins!!")
    elif user == "Paper" and computer == "Rock":
        print("Player wins...")
    elif user == "Paper" and computer == "Scissor":
        print("Computer wins!!")
    else:
        print("invalid input")