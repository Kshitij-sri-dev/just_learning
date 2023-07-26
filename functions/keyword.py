def hello(greeting, title, first, last):
    print(f"{greeting}, {title}{first} {last}")

hello("Hello", first="Kshitij", last="Srivastava", title="Mr.")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}."


print(get_phone(country=input("Enter country code: "), area=input("Enter area code:"),
          first=input("Enter first 4 numbers:"), last=input("Enter last 4 numbers:")))