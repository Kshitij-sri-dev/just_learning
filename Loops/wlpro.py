# compound interest
principle = 0
interest = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print(f"Principle can't be less than or equal to zero.")
    else:
        break

while True:
    interest = float(input("Enter the interest amount: "))
    if interest < 0:
        print(f"Interest can't be less than or equal to zero.")
    else:
        break

while True:
    time = float(input("Enter the time amount: "))
    if time < 0:
        print(f"time can't be less than or equal to zero.")
    else:
        break

total = principle * pow((1+interest/100), time)
print(f"Balance after {time} is {total:.2f}")
