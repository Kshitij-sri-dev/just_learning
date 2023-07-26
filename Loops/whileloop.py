
# name = input("Enter your name: ")
# while name == "":
#     print("You did not enter the name.")
#     name = input("Enter your name: ")
# print(f"Hello, {name}.")

# age = input("What's your age?: ")
# while not age.isnumeric() or int(age) < 0:
#     print("Are you from planet Earth?")
#     age = input("What's your age?: ")
# print(f"You are {age} yrs old.")

food = input("Enter a fruit you like (q to quit): ")
data = list()
while not food == "q":
    data.append(food)
    food = input("Enter a fruit you like (q to quit): ")
print(data)
