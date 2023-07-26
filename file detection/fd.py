import os

path = "/home/kshitij/Documents/binance.odt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file.")
else:
    print("location does not exist.")
