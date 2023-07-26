

def shipping_label(*args, **kwargs):
    for ship in args:
        print(ship, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('pin')}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="B-901",
               apt="Apex Apartment",
               city="Gurgaon",
               state="Haryana",
               pin="44552102")
