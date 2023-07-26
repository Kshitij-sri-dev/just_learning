
name = input('Enter your full name: ')

# Includes spaces
result = len(name)
print(result)

# find for first occurring and rfind for last occurring
res = name.rfind('i')
print(res)
print(name.lower())

# returns true only if all characters are digits.
# digit = name.isdigit()
# print(digit)


# returns true only if all characters are alphabets.
alpha = name.isalpha()
print(alpha)
