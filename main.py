op = input("Choose an operator(+-*/):")
num1 = float(input("Choose the first number:"))
num2 = float(input("Choose the second number:"))

if op == "+":
    print(f"The sum is: {round((num1 + num2), 3)}")
elif op == "-":
    print(f"The difference is: {num1 - num2}")
elif op == "*":
    print(f"The product is: {num1 * num2}")
elif op == "/":
    print(f"The division is: {num1 / num2} ")
else:
    print("Wrong input!")
