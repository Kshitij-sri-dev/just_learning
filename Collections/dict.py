capitals = {"USA": "Washington DC",
            "India": "Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("India"))
# capitals.update({"Germany": "Berlin"})
# capitals.update({"India": "New Delhi"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key in capitals:
#     print(key)

# for values in capitals.values():
#     print(values)
for key, value in capitals.items():
    print(f"{key}:{value}")