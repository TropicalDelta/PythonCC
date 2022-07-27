#Strings
name = "adam johnson"
print(name.title())
print(name.upper())
print(name.lower())
#print: function
#.title(): method: action that python cab perform on a piece of data
#Methods are always followed by a set of parentheses. 

print("\tPython") #To make a tab of the string.
print("Languages:\nPython\nC\nJavaScript") #To make a new line. 

favorite_language = " Python " #This string contain a space in the rigtht end.
favorite_language = favorite_language.rstrip() #This eliminate the right space.
favorite_language = favorite_language.lstrip() #This eliminate the left space.
favorite_language = favorite_language.strip() #Eliminate all the white space.

quote = "Steve Jobs once said:\n\tThe people who are crazy enough to\n\tthink the can change the world,\n\tare the ones who do."
print(quote)

#Para dividir una cadena de texto en palabras por separado: 
title = "Alice in Wonderland" 
title.split()
#//['Alice', 'in', 'Wonderland']





#Numbers
print(3 ** 2) #Two multiplication symbols represent exponents.
age = 5
message = "Happy Birthday, " + str(age) + ", baby!\n\t- I can't swim."
print (message)

print(3 / 2)





#List
names = ["Christian", "Amparo", "David", "Ilmer"] #Always with quotes.
print(names[-1].lower())#-1 is the last element in the list.
print("Hello, my name is " + names[2] + ". Good morning!")



colors = ['green', 'red', 'blue', 'yellow']
print(colors[0].upper())
print(colors[1].lower())
print(colors[2].title())
print(colors[3])
colors[0] = 'gray' #Changes the first element. 
colors.append('green') #Appends an element at the end of the list. 
colors.insert(0, 'violet') #Insert an element in any position. 
del colors[0] #Delete an element from the list.
print(colors)



animals = ["cat", "dog", "fish"]
print(animals)
popped_just_fish = animals.pop() #Remove the last item from a list.
print(popped_just_fish)
just_cat = animals.pop(0)
print(just_cat)
print(animals)



food = ["burger", "french fries", "hot dog"]
food.reverse()
print(food)



dinner = ["Luca", "Allan", "Josh"]
dinner.remove("Allan")
dinner.insert(1, "Laura")
dinner.insert(0, "Delta")
dinner.insert(1, "Bree")
dinner.append("Karla")
#dinner = [Delta, Bree, Luca, laura, Josh, Karla]

print("Hey... I only have room for two more of you.")

popped_Karla = dinner.pop()
popped_Josh = dinner.pop()
popped_Laura = dinner.pop()
popped_Luca = dinner.pop()

print("Sorry, Karla.")
print("Sorry, Josh.")
print("Sorry, Laura.")
print("Sorry, Luca.")
guest_1 = "You're still invited."
guest_2 = "You're still invited."

print("Hey " + dinner[0] + ". " + guest_1)
print("Hey " + dinner[1] + ". " + guest_2)
print(len(dinner)) #//2


kids = ["Joshua", "Marlon", "Wilder", "Allan", "Pony"]
kids.sort() #Changes the order of the list, permanently. In alphabebical order.
kids.sort(reverse=True) #Reverse the alphabetical order.
print(kids)



cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) #Changes the order of the list, temporarily. 

print("\nHere is the original list again:")
print(cars)



numbers = [0, 1, 2, 3, 4, 5]
numbers.reverse() #Reverses the order of the list. 
print(numbers)
print(len(numbers)) #Shows the list's length. //6



countries = ["USA", "Mexico", "Chile", "Great Bretain", "Japan"]
print(countries)
sorted_countries = sorted(countries) #Changes the order of the list. Temporarily.
sorted_countries.reverse() #Reverses the order of the list.
sorted_countries.reverse() #Reverses the order of the list. Again.
sorted_countries.sort() #Orders the list in alphabetical order.
sorted_countries.reverse()
print(sorted_countries)



magicians = ["alice", "david", "carolina"]
for magician in magicians: #Tells Python to pull a name from the list magicians, and store it in the variable magician.
    print(magician.title() + ", that was a great trick!") #“For every magician in the list of magicians, print the magician’s name.”
    print("\tI can't wait to see your next trick, " + magician.title() + ".\n")



favorite_food = ["Burger", "Arroz chino", "tomato's soup"]
for food in favorite_food:
    print("I like " + food + ".")
print("\nI like food!")


for value in range(1,6):#Starts in 1 and end at 6. 
    print(value)

numbers = list(range(1,6))#List function print a list of the range.
print(numbers)

even_numbers = list(range(2, 11, 2))#Print form 2 to 11. It adds 2 repeatedly until it reaches the end of the value.
print(even_numbers)

odd_numbers = list(range(3, 13, 3))
print(odd_numbers)



squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)



digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)#0
max(digits)#9
sum(digits)#45



for value in range(1, 21):
    print(value)

#for value in range(1, 1000000):
#   print(value)

cubes = [number**3 for number in range(1, 11)]
print(cubes)


my_foods = ["Pizza", "Hot dog", "cake"]
friends_foods = my_foods[:] #Copy a list.
print(friends_foods)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

places = ["home", "park", "grocery store", "pool", "church"]
print("The first three items in the list are: ")
for place in places[:3]:
    print(place.title())
print("The item from the middle of the list are: " + places[2])

print("The last three items in the list are: ")
for place in  places[-3:]:
    print(place)





#INPUT 
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?: " #takes the string that was stored in prompt and adds the new string onto the end.
name = input(prompt)
print("\nHello, " + name + "!")


oracion_1 = "Hola, espero que estés bien"
oracion_1 += ", Diana."
print(oracion_1)

#Tuple
dimensions = (200, 50) #Se puede sobreescribir pero no alterar los datos.
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 123 // Impossible. 

#Buffet
buffet = ("meat", "toast", "pop corn", "bocadillo", "coke")
for food in buffet:
    print(food.title())

#buffet[1] = "eggs"
buffet = ("\ncoffe", "toast", "pop corn", "chocolate", "coke")
for food in buffet:
    print(food.title())


num = int(input("Escriba un número entero: "))
cantidad_digitos = 0

while num != 0:
    num = int(num/10)
    cantidad_digitos = cantidad_digitos + 1
print("El número digitado tiene: " + str(cantidad_digitos))

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings #True. #in is used to check wheter a value is in a list. 
'pepperoni' in requested_toppings #False. 

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users: #not in.
    print(user.title() + ", you can post a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')





#Dictionaries
alien = {
    "color": "green",
    "type": "xenomorph",
    "points": 5
}
#print(alien["color"]) # // Green
alien["position"] = "Norte" # Para añadir un nuevo valor al diccionario. 
alien["position"] = "Sur" # Para modificar la posición. 
del alien["color"] # Elimina una pieza del diccionario. 
print(alien)

for key, value in alien(): # //Print every value and key in a dictionary
    print("\nKey: " + key)
    print("Value: " + value)


def miSumatoriaParaModulo(a,b):
    print(a+b)
