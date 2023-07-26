user = input('Enter your username: ')

if len(user) > 12:
    print(f"Username can't be more than 12 characters")
elif not user.isalpha():
    print("Username must not contain digits, spaces or special characters.")
elif user.find(' ') == -1:
    print("Username must not contain spaces.")
else:
    print(f"Welcome,{user}")
 