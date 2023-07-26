
foods = []
qty = []
prices = []
total = 0

while True:
    food = input("Enter a fruit a fruit to buy (press q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the the price: "))
        qty = float(input("Enter the quantity:"))
        total += price * qty
        foods.append(food)
        prices.append(price)

print('------Your Cart:--------')
for x in foods:
    print(x)
print(f"The total is Rs{total:,.2f}/-")
