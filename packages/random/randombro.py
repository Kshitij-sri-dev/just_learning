import random

low = 1
high = 100
# options = ("rock", "paper", "scissor")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#
#
# # number = random.randint(low, high)
# # number = random.random() for random b/w 0 and 1
# random.shuffle(cards)
#
# print(cards)

guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low}- {high})"))
    guesses += 1
    if guess < number:
        print(f"{guess} is too low.")
    elif guess > number:
        print(f"{guess} is too high.")
    else:
        print(f"{guess} is correct.")
        break

print(guesses)
