# step 1
card_no = input("Enter your credit card no: ")
card_nos = card_no.replace('-', '').replace(' ', '')

# step 2
sum_odd = 0
for x in card_nos[::-2]:
    sum_odd += int(x)
print(sum_odd)

# step 3
y = 0
for x in card_nos[-2::-2]:
    x = int(x) * 2
    if x >= 10:
        y += 1 + (x % 10)
    else:
        y += x
print(y)

# step 4
y += sum_odd

# step 5
if not y % 10 == 0:
    print(f"{card_no} not valid.")
else:
    print(f"{card_no} valid.")
