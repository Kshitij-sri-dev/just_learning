
email = input("Enter your e-mail: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
domain = domain.replace(".com", "")

print(f"Your username is {username} and domain is {domain}.")
