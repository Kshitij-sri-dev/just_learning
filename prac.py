# import random
# import string
#
# plain = " " + string.punctuation + string.digits + string.ascii_letters
# plain = list(plain)
# key = plain.copy()
# random.shuffle(key)
# print(plain)
# print(key)
#
# #encrypt
# pl = input("Enter your text:")
# ch = ""
#
# for line in pl:
#     ch += key[plain.index(line)]
#
# print(ch)
# pl = ""
# for line in ch:
#     pl += plain[key.index(line)]
#
# print(pl)
########################

def shipping_address(*args, **kwargs):
    for arg in args:
        print(f"{arg}", end=" ")
    print()
    if "apartment" in kwargs and "PO" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apartment')}")
        print(f"{kwargs.get('PO')}")
    elif "PO" not in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apartment')}")
    elif "apartment" not in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('PO')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('pin')}")


shipping_address("Mr.", "Kshitij", "Srivastava",
                 street="B-901",
                 apartment="Apex Apartment",
                 city="Gurgaon",
                 state="Haryana",
                 pin="4588632")
