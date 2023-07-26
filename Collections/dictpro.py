# shopping cart using dictionaries

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []

total = 0
print("-----menu------")
for key, value in menu.items():
        print(f"{key:10}:{value:.2f}")
print("---------------")

while True:
        food = input("Select an item (q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)
        qty = input("Enter the quantity:")
        while not qty.isnumeric():
                if not qty.isnumeric():
                        print("Enter the correct value")
                        qty = input("Enter the quantity:")
                else:
                        break
        total += menu.get(food) * int(qty)


for food in cart:
        print(food, end=" ")
print(total)
