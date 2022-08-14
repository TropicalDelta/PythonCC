#Ejemplo python para leer archivos json, escribir y esas vesches
import json

userNumber = input("Favorite number: ")
filename = 'data.json'

with open(filename, 'w') as fo:
    json.dump(userNumber, fo)

print("Your number has been restored!")

