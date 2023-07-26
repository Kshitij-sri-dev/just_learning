import random

option = ("rock", "paper", "scissors")
running = True

while running:
    computer = random.choice(option)
    player = None
    while player not in option:
        player = input("Enter a choice (rock, paper, scissors:)")
    print(f"Player:{player} ")
    print(f"Computer:{computer} ")
    if player.lower() == "q":
        break
    elif player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissor":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    elif player == "scissor" and computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins.")

    while running:
        play = input("Want to play again:(y/n)").lower()
        if play == "n":
            running = False
            print("Thanks for playing!")
        elif not play == "y":
            print("Incorrect input!")
        else:
            print("Lets play again!")
    continue


