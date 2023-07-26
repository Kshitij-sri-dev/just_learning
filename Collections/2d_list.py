fruits = ["apple", "orange", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meat = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meat]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
