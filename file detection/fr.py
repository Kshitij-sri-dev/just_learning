
try:
    with open('/home/kshitij/Documents/ex.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found.")
