# args
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3))


def display_name(*args):
    for name in args:
        print(name, end=" ")


display_name("Dr.", "Spongebob", "Squarepants", "III\n")


# kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="B-901",
              city="Gurgaon",
              state="Haryana",
              zip="122003")
