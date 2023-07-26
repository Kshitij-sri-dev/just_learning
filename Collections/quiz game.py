ques = ("How am I am alive?: ", "Who lays eggs?: ", "What is oxygen?: ",
        "Imagine dragons bones?: ", "What and how is planet?: ")

option = (("air", "hope", "water", "sigma"), ("Anyone", "animals",
           "birds", "aliens"), ("oxygen", "copium", "hopium", "dopium"),
          ("best song", "just imagine", "sigma male", "option"),
          ("earth", "jupiter", "pluto", "sun"))

answers = ("a", "d", "c", "d", "a")
guesses = []
score = 0
ques_no = 0
score = 0

for q in ques:
    print("---------------------")
    print(q)
    for op in option[ques_no]:
        print(op)
    guess = input("Your guess: ").lower()
    guesses.append(guess)
    if guess == answers[ques_no]:
        score += 1
        print('Correct')
    else:
        print("Incorrect")
        print(f"{(answers[ques_no])} is the correct answer.")
    ques_no += 1
print()
print("Result")
print()
print("Your guesses: ")
for x in guesses:
    print(x, end=" ")
print()
print("Your answers: ")
for y in answers:
    print(y, end=" ")
print()

score = (score / len(ques)) * 100
print(f"Your score is {score}%")
