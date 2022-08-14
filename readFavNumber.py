import json
filename = 'data.json'

with open(filename) as fo:
    info = json.load(fo)

print(f"I know your favorite number!, It's {info}")
print(f"The double of that number is {int(info)*2}")