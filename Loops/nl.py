
rows = int(input('Enter the number of rows:'))
column = int(input('Enter the column of rows:'))
symbol = input("Enter a symbol to use:")

for y in range(rows):
    for x in range(column):
        print(symbol, end="")
    print()
