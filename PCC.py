#1. Functions
def greet_user(): #Defining a Function. Uses def.
    """Display a simple greeting.""" #These are Docstrings. Python Documentation. 
    print("Hello!")
#greet_user() #Call of the function.

def greet_user2(username):
    """Display your the hello + username"""
    print("Hello, ", username, "!")
#greet_user2("David")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#How to use Python in the command console
# 1. cd + Paste the folder's direction: 
# Direction ;)
# 2. Name the project + .py: PCC.py
# 3. Clean the console: cls
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Exercises 8.1- 8.2
def displayMessage(): 
    """Function created to display a Message"""
    print("Hey everyone, I'm learning Python!")
#displayMessage()

def favoriteBook(title): 
    """Function created to display the favorite book"""
    print("One of my favorite books is:", title)
#favoriteBook("A Clockwork Orange")

#Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet(animal_type='hamster', pet_name='harry') #You pair the values.

#Default Values
def describe_pet(pet_name, animal_type='dog'):# dog is now a default value.
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet(pet_name='willie') # Just name one value.

#Exercises 8.3 - 8.4
def makeShirt(size, message):
    print("Your size of shirt is:", size, "and your message is:\n", message)
#makeShirt("m", "Vivan las Vegas")
#makeShirt("s", "Be positive as a Proton")

def makeShirt2(size="Large", message="I love Python"):
    print("Size:", size, "\nMessage:", message)
#makeShirt2()

def describeCity(name, country="Colombia"): 
    print(name,"is in", country)
    
#Return Values





# 2. Variables and Simple Data Type
def simpleMessage(): 
    simpleMessageVar = "Hey, I'm re-learning Python!"
    print(simpleMessageVar)
    
#Exercises 2.3 - 2.7
def cases(): 
    username = input("Please, enter your name: ")
    print(username.upper())
    print(username.lower())
    print(username.title())
#cases()

def famousQuote(): 
    author = "Some caped baldy once said, "
    quote = "Is that really... the limit of your power? "
    quote += "Do you honestly thing that you won't any stronger for the rest of your life? "
    quote += "Instead of sitting around frustrated, it's better to keep moving forward."    
    print(author + quote)
#famousQuote()

#Exercises 2.8 - 2.9
def numberEight(): 
    print(5 + 3)
    print(2**3)
    print(10-2)
    print(40/5)





#3. Lists
def listsIntroduction():
    firstList = [1, 2, 3, 4, 5, 6, 7, 8]
    print(firstList[0]) # Print 1
    print(firstList[-1]) # Print 6
    print("My brother was " + str(firstList[-1]) + ", two years ago.")
    
#Exercises 3.1 - 3.3
def names(): 
    names = ["Carlos", "Daniel", "Miguel", "Lucho"]
    for i in names: #The real exercise not uses a for loop.
        print("Hey, meet my friend: " + i)

#Exercises 3.4 - 3.7
def guestList(): 
    myList = ["Michael Jackson", "Stephen Howking", "Chespirito"]
    print("You're invited to my party, " + myList[0])
    print("You're invited to my party, " + myList[1])
    print("Estás invitado a mi fiesta, " + myList[-1])
#guestList()

def changingGuestList(): 
    myList = ["Michael Jackson", "Stephen Howking", "Chespirito"]
    print("You're invited to my party, " + myList[0])
    print("You're invited to my party, " + myList[1])
    print("Estás invitado a mi fiesta, " + myList[-1])
    print("\t I've heard, Michael Jackson cannot asist to my party.")
    myList[0] = "Miles Morales"
    print(myList)
    print("You're invited to my party, " + myList[0])
    print("You're invited to my party, " + myList[1])
    print("Estás invitado a mi fiesta, " + myList[-1])
#changingGuestList()

def moreGuests(): 
    myList = ["Michael Jackson", "Stephen Howking", "Chespirito"]
    myList[0] = "Miles Morales"
    print("\t I allow myself to announce, we found a bigger table")
    myList.insert(0, "Usain Bolt")
    myList.insert(2, "Will Smith")
    myList.append("Skootie Young")
    for i in myList: 
        print("You're invited to my party, " + i)
    print("\t Att. Davidop")
#moreGuests()

#Moving Items from One List to Another
usuariosNoConfirmados = ['Alicia', 'Brian', 'Candace']
usuariosConfirmados = []
while usuariosNoConfirmados:
    usuario = usuariosNoConfirmados.pop()
    usuariosConfirmados.append(usuario)
        
#Remover elementos repetidos de una lista
listaGenerica = []
while 'elementoRepetido' in listaGenerica:
    listaGenerica.remove('elementoRepetido')

"""Hard"""
def shrinkingGuestList():
    print("\tBad news, I cannot invite more than two persons to the dinner.")
    print("\tI'm so sorry.")
    
    myList = ["Michael Jackson", "Stephen Howking", "Chespirito"]
    myList[1] = "Miles Morales"

    myList.insert(0, "Usain Bolt")
    myList.insert(2, "Will Smith")
    myList.append("Skootie Young")
    
    print(myList)
    i = 0
    while i <= 3:
        myList.pop(-1)
        i += 1
    for i in myList: 
        print(i + ", you're still invited.")
    print(myList)  
    
    del myList[0]
    del myList[0]
    print("Empty list: " + str(myList)) #myList wasn't taken as string. 
    
def sortedList():
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(sorted(cars))

#18Nov21
#Exercises 3.8 - 3.10
def seeingTheWorld(): 
    places = ["Brazil", "España", "New York", "San Francisco", "Greek"]
    print(places)
    print("Sorted list: ")
    print(sorted(places))
    print(places)
    print("Alphabetical sorted list, reverse: ")
    print(sorted(places, reverse=True))
    print(places)
    places.reverse()
    print(places)
    places.reverse()
    print(places)
    places.sort()
    print(places)
    places.sort(reverse=True)
    print(places)
#seeingTheWorld()

def dinnerGuests(): 
    myList = ["Michael Jackson", "Stephen Howking", "Chespirito"]
    print(len(myList))
#dinnerGuests()





#4. Working with lists.
#Exercises 4.1 - 4.2
def pizzas(): 
    pizzaNames = ["Mushrooms", "Pineapple", "Pepperoni"]
    for pizza in pizzaNames: 
        print("I like " + pizza + " pizza!")
    print("I really love pizza")    

def animals(): 
    animalsList = ["Eagle", "Ostrich", "Velociraptor"]
    for animal in animalsList: 
        print(animal + "s has fierce claws")
    print("Any of this animals would make a great pet")

def squares(): 
    squaresList = []
    for value in range(1, 11):
        squaresList.append(value**2)
    print(squaresList)

def squaresComprehension(): 
    squares = [value**2 for value in range(1, 11)]
    print(squares)
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Concatenation format()
#var = "Hello World"
#print(f'This is cliché: {var}')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Exercises 4.3 - 4.9
def countingToTwenty(): 
    print( print(value) for value in range(1, 21))
    countingToTwenty()

def oneMillion(): 
    toMillion = list(range(1, 1000001))
    print(toMillion)
    oneMillion()

def summingAMillion(): 
    toMillion = list(range(1, 1000001))
    print(min(toMillion))
    print(max(toMillion))
    print(sum(toMillion))
    summingAMillion()

def oddNumbers():
    oddNumbersList = list(range(1, 21, 2))
    print(oddNumbersList)
    oddNumbers()

def Threes(): 
    ThreeMultiples = list(range(3, 31, 3))
    print(ThreeMultiples)
    Threes()

def cubes(): 
    cubesList = [value**3 for value in range(1,11)]
    print(cubesList)
    cubes()

#Copying a list. 
def copyAList():    
    myFoods = ["Pizza", "Falafel", "Carrot cake"]
    friendsFoods = myFoods[:]
    print(friendsFoods)

#20Nov21
#Exercises 4.10 - 4.12
def slices(): 
    names = ["Carlos", "Daniel", "Miguel", "Lucho"]
    print(names[0:3])
    print(names[1:3])
    print(names[-3:])

def pizzas(): #Here's an example of comprehension
    pizzaNames = ["Mushrooms", "Pineapple", "Pepperoni"]
    friendsPizzas = pizzaNames[:]
    print(friendsPizzas)
    pizzaNames.append("Chorizo")
    friendsPizzas.append("Tomato")
    [print(pizza) for pizza in pizzaNames]
    [print(pizza) for pizza in friendsPizzas]

# Tuples
def tuplesIntroduction():
    
    dimensions = (200, 50)
    print("Original dimensions:")
    for dimension in dimensions:
        print(dimension)
        
    dimensions = (400, 100)
    print("\nModified dimensions:")
    for dimension in dimensions:
        print(dimension)
        
#Exercise 4.13
def buffet(): 
    menu = ("Steak", "Cheese", "Burger", "Pizza", "Bandeja paisa")
    menu = ("Steak", "Cheese", "Burger", "Pizza", "Bandeja paisa")
    [print (food) for food in menu]
    # menu[1] = "Rice" #Don't
    menu = ("Steak", "Rice", "Burger", "Pizza", "Tamal")
    [print (f'{food},') for food in menu]





#5. IF statements
#Exercises 5.1 - 5.2
def conditionalTest(): 
    car = 'Volks Wagen'
    print('Is car a Toyota? I predict False')
    print(car == 'Toyota')

def requestedPizza(): 
    requested_toppings = ['mushrooms', 'extra cheese']
    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms.")
    if 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")
    print("\nFinished making your pizza!")
#20Jul22
#If statements and lists
req_toppings = ["Mushrooms", "Green Peppers", "Extra Cheese"]
for req_topping in req_toppings: #Check for elements in list
    if req_topping == "Green Peppers":
        print("Sorry, we are out of green peppers right now")
    else: 
        print("Adding " + req_topping + ".")
    #if requested_toppings: //Sirve para confirmar si hay valores dentro de la lista





#6. Dictionaries
alien = {
    "color": "green", #Key | Value
    "points": 5 #Diccionario vacio alien={}
}
print(alien["color"]) #Para acceder a un valor del diccionario
alien["color"] = "blue" #Change the color of a key; add a new key and its value
#Cuando no existe un valor dentro de la clave:
print(alien.get("ship", "no existe una nave para los aliens")) #Buscamos pro SHIP
print(len(alien))
alien.clear() #Elimina todos los valores dentro del diccionario
print("color" in alien) #Verifica que existe un valor con True; False
del alien["color"] #Removes the color key
#Looping through a dictionary
for key,value in alien.items(): #Prints all elements in a dictionary
    print("\nKey: " + key)
    print("\nValue: " + value)
for key in sorted(alien.keys()): #Prints only keys in order
    print(key)
for values in alien.values(): #Prints only values; doesn't check for repeated values
    print(values)
for values in set(alien.values()): print(values) #Prints non-repeated values





#7. User input and while loops
message = input("Tell me something; ") #Input from a user; text
numericalMessage = int(input("Number: ")) #Receives a number
#While loops
while True:
    city = input("Enter a city: ")
    if city == 'quit':
        break #Stops the actual running
    else: print('I\'d love to go to ' + city.title() + "!" )
    #continue: Tells Python to ignore the rest of the loop and return to the beginning





#8. Functions.
#Valores por defecto: 
def describePet(name1, name2="Pedro"):
    print("This is not a pet: " + name1 + "This is a real name: "+ name2)
describePet("Luca") #Ignores the second paremeter

#Devolviendo un diccionario
def buildPerson(firstName, lastName):
    person = {
        'first': firstName,
        'last': lastName
    }
    return person

#Valores indefinidos dentro de una tupla
def makePizza (*toppings): #**toppings crea un diccionario vacio
    print(toppings)
makePizza('pepperoni') #Acepta solo un valor
makePizza('mushrooms', 'green peppers', 'extra cheese') #Acepta varios valores
#Impresion: ('mushrooms', 'green peppers', 'extra cheese')

#Funciones en modulos: 
#Importar y exportar funciones en archivos externos 
#Debe ser un archivo .py
import pythoncc #Llamamos el programa en una misma direccion
"""Si se quiere una funcion en especifico se usa: from pythoncc import miSumatoriaParaModulo, otraFuncion, otraFuncion"""
pythoncc.miSumatoriaParaModulo(3,5) #Usamos una funcion dentro del otro programa (modulo)
"""sintaxis: nombreDelModulo.nombreDeLaFuncion()"""
#1. Cuando se quiere traer una funcion pero tiene el mismo nombre que otra...
#dentro del archivo: from pizza import makePizza as mp //Se usa 'as' y un alias
#2. Importar un modulo con un alias: import ModuloRandom as mr
#3. Importar todas las funciones de un modulo: from pizza import* //Ya no es necesario escribir pizza.nombreFuncion
#... solo nombreFuncion() y ya

#Definir una funcion larga: 
def functionName(
    parameter0, parameter1, paremeter2,
    parameter3, parameter4, parameter5):
    #Cuerpo de la funcion
    print(parameter0, parameter1, paremeter2,
    parameter3, parameter4, parameter5) 





#9. Classes
class Dog():

    def __init__ (self, name, age):
        #Es un método (funcion para clases)...
        # que corre siempre que se crea una instancia de la clase
        self.name = name #Cualquier variable con self es disponible...
        # para cualquier metodo en la clase 
        self.age = age 
        self.siblings = 2

    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def rollOver(self):
        print(self.name.title() + " rolled over!")


#Creando instancias
myDog = Dog('Willie', 6) #Creamos un perro llamado Willie;
#... Python guarda la instancia con los valores dentro de 'myDog'
#a. Accediendo a los atributos
print("My dog's name is " + myDog.name.title() + ".") #Accedemos al nombre del perro
print("My dog is " + str(myDog.age) + " years old.")

#b. Accediendo a los metodos
myDog.sit()
myDog.rollOver()

yourDog = Dog("Lucy", 3) #Segunda instancia
yourDog.sit()
yourDog.rollOver()

#Cambiando un atributo por medio de tres metodos
#1. 
myDog.age = 12
"""
Ejemplo Odometro; clase Car
    #Metodos para cambiar el valor del odometro
    #2. 
    def updateOdometer(self, mileage):
        self.odometer_reading = mileage 

    #3. 
    def incrementOdometer(self, miles):
        self.odometer_reading += miles 

myNewCar.updateOdometer(23) #Cambiamos el valor con un metodo
myNewCar.incrementOdometer(23500) #Cambiamos el valore del odometro, otra vez
myNewCar.incrementOdometer(100) #Cambiamos el valore del odometro, otra vez
"""
#El contenido para esta parte esta en los programas: 
#1. dog; conceptos basicos
#2. car; herencia
#3. myCar; clases como modulos





#10. Files and Exceptions
#Reading from a file

#Exceptions
#Basic example
try:
    print(5/0)
except ZeroDivisionError:
    print('You cant divide by zero!') 
#File not found exception
fileName = 'alicia.txt'
try:
    with open(fileName) as fo: 
        contents = fo.read()
except FileNotFoundError: 
    msg = "Sorry, the file " + fileName + " doesn't exist." 
    print(msg)

else:
    #Contar las palabras dentro de un archivo
    words = contents.split()
    numWords = len(words)
    print("The file has: " + numWords + " words.")

#Funcion para contar las palabras; contiene excepciones
def contarPalabras(filename): 
    try: 
        with open(filename) as fo:
            contents = fo.read()
    except FileNotFoundError: 
        msg = "Sorry, the file " + filename + " does not exist. "
        print(msg)
        #pass //Siempre se puede colocar un pass para 'fallar de forma silenciosa'
    else: 
        words = contents.split()
        numWords = len(words)
        print("File lenght : " + numWords)

filenames = ['Alice.txt', 'modyDick.txt', 'littleWomen.txt']
for filename in filenames: 
    contarPalabras(filename)
#contarPalabras(filename) 