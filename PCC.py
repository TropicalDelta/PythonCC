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


#Storing data - JSON file
import json 
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as fo:
    json.dump(numbers,fo) #To store the list of numbers in the file numbers.json
    json.load(fo) #Trae la informacion que tenemos en numbers.json

with open(filename) as fo:
    numbers = json.load(fo)
print(numbers)

#Json con datos de usuario
username = input('What is your name?')

filename = 'username.json'
with open(filename, 'w') as fo:
    json.dump(username, fo) #Guardamos la información del usuario dentro de username.json
    print('Well remmeber you when you came back, ' + username + ' !')

with open(filename) as fo:
    username = json.load(fo)
    print('Welcome + user')

#Excepciones dentro de un Json
def getStoresUsername():
    filename = 'username.json'
    try: 
        #Intentamos abrir el archivo
        with open(filename) as fo:
            username = json.load(fo)
        #Si no lo encontramos, creamos uno y lo llenamos
    except FileNotFoundError:
        username = input('whats your name?')
        with open(filename, 'w') as fo:
            json.dump(username, fo)
            print("Well remember you when you come back + username + !")
    else:#Si existe, leeemos y saludamos al usuario
        print("Welcome back + username + !")





#11. Testing code
import unittest      

def getFormattedName(first, middle, last): #A regular function just to test
#Anterior: def getFormattedName(first, last): #El programa funciona con este código; 
    #Anterior: fullName = first + ' ' + last
    fullName = first + ' ' + middle + ' ' + last 
    return fullName.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break 
    last = input("Please give me a last name: ")
    if last == 'q':
        break 

    formattedName = getFormattedName(first, last)
    print("\tNeatly formatted name: " + formattedName + ".")

class NamesTestCase(unittest.TestCase):
    def testFirstLastName(self):
        formattedName = getFormattedName('Janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')
        #La línea de arriba quiere decir que 'Corra el programa y el resultado debe ser este,
        #si lo es, bien; si no, dejamelo saber
    #Añadiendo más tests: Un test para chechar cómo sale con un nombre medio
    def tstFirstLastMiddleName(self):
        formattedName = getFormattedName(
            'Wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formattedName, 'Wolgang Amadeus Mozart')


unittest.main()
#Hemos cambiado con 'Antiguo' y ahora debería dar error el test






#Testing a Class: 222
#081222
##Repaso Cap 9; Classes

"""dog.py"""
class Dog(): #Definición de la clase 'Dog'
    def __init__(self, name, age): #Método: Cuando una función está dentro de una clase
        #Atributos
        self.name = name 
        self.age = age 
    def sit(self): 
        print(self.name.title() + " is now sitting.") 
    def rollOver(self): 
        print(self.name.title() + " rolled over.")

#A. Instancias de una clase
myDog = Dog('Willie', 6) #Creamos un perro llamado Willie con 6 años
print('My dogs name is ' + myDog.name.title() + ".")
print('My dogs is ' + str(myDog.age) + "years old.")
myDog.sit()
myDog.rollOver()

yourDog = Dog('Lucas', 8)
print('My dogs name is ' + yourDog.name.title() + ".")
print('My dogs is ' + str(yourDog.age) + "years old.")
yourDog.sit()
yourDog.rollOver()
######
"""car.py"""
class Car():
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometerReading = 0

    def getDescriptiveName(self): 
        longName = str(self.year) + ' ' + self.make + ' ' + self.model 
        return longName.title() 

    def readOdometer(self):
        print("This cas has " + str(self.odometerReading) + " miles on it.")

    def updateOdometer(self,mileage): #Creamos un metodo para modificar el valor del odometro
        self.odometerReading = mileage 
#Instancia
myNewCar = Car('audi', 'a4', 2016)
print(myNewCar.getDescriptiveName()) #Print 2016 Audi A4 
#Formas de modificar un atributo
myNewCar.odometerReading = 23  #Afectando a la variable
myNewCar.updateOdometer(23) #Usando un método 


#B. Herencia
class ElectricCar(Car): #Creates a new class from 'Car' class
    def __init__(self, make, model, year): 
        super().__init__(make, model, year) #Le da a la clase hija todos los 
                                            #atributos de la clase madre
        self.batterySize = 70 #Un atributo propio de la clase hija
    
    def describeBattery(self): #Metodo propio
        print("This car has a " + str(self.batterySize) + "-kWh battery.")

    def fillGasTank():
        print("This car doesn't need a gas tank!")
#Instancia
myTesla = ElectricCar('tesla', 'model s', 2016)
print(myTesla.getDescriptiveName())
myTesla.describeBattery() 


#C. Importar clases
#from car import Car // Quiere decir que de car.py importe la clase Car
#Luego podemos instanciar de esa clase: 
myNewCar = Car('Audi', 'a4, 2016') #Y seguirá funcionando
#Importar más clases: from car import Car, ElectricCar // Importamos Car y ElectricCar
#Importar todo un módulo: import Car //Importamos todo lo que hay en Car.py




#10. Files and Exceptions. 189/222
#Lee e imprime lo que hay en un archivo .txt
with open('piDigits.txt') as fileObject:
    contents = fileObject.read() #leemos el archivo
    print(contents.rstrip()) #Imprimimos lo que guardamos en contents

#Leer linea por linea 
fileName = 'piDigits.txt'
with open(fileName) as fo:
    for line in fo:
        print(line.rstrip()) 

#Una lista de lineas de un archivo
with open(fileName) as fo: 
    lines = fo.readlines() #Toma cada linea del texto y la guarda en una lista
piString = ''
for line in lines: 
    piString += line.strip() 
print(piString)

#Encontrar una cadena dentro de un archivo
if '41263512' in piString:
    print("41263512 existe en Pi")

#Ejercicio
filename = 'C:/Users/David Ordoñez/Documents/D.Software Pillar/PythonCC'
with open(filename) as fo: 
    lines = fo.readlines()
myPIString = ''
for line in lines:
    myPIString += line
mybday = '200803'
if mybday in myPIString:
    print(f'{mybday} is in the pi Digits')

#Escribir en un archivo
with open(filename, 'w') as fo: #Con w indicamos que vamos a escribir 'write'
    fo.write("I love Programming")
    fo.write("\nI love creating new games")
    #'w' elimina todo lo que haya en el archivo para escribir en blanco

with open(filename, 'a') as fo: #Para añadir contenido a el archivo 'apennd'
    fo.write("I also love finding meaning in large datasets. \n")
    fo.write("I love creating apps that can run in a browser. \n") 





#Exceptions
#Error de division
try:
    answer = (5/0) #Solo lo intenta, no devuelve el resultado
except ZeroDivisionError: 
    print("You cant divide by zero!") 
    #Ahora cuando dividamos por cero, no dara el error tipico y solo 
    #anunciara el texto que hemos introducido
else: print(answer) #Devuelve el resultado despues de haber intentado

#Error desubicacion del archivo
filename = 'alice.txt'
try:
    with open(filename) as fo: 
        content = fo.read()
except FileNotFoundError: 
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else: 
    words = content.split() 
    numWords = len(words) 
    print(f"The file {filename} has about {numWords} words.")





#JSON module
import json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
#Escribir en un archivo json
with open(filename, 'w') as fo: 
    json.dump(numbers, fo) #Store the list numbers in the json file

#Leer de un archivo json
with open(filename) as fo: 
    numbers = json.load(fo) #Cargamos del archivo los datos que contiene
print(numbers)





#11. Testing your Code
#Testing a Function
import unittest 

#Un programa promedio que une los nombres de una persona en un string
def get_formatted_name(first, last, middle=''):
    if middle: 
        full_name = first + ' ' + middle + ' ' + last 
    else: 
        full_name = first + ' ' + last 
    return full_name.title()

#Recibe los nombres
print("Enter 'q' at any time to quit.") 
while True:
    first = input("\nPlease give me a first name: ") 
    if first == 'q': break
    last = input("Please give me a last name: ") 
    if last == 'q': break
    formatted_name = get_formatted_name(first, last) 
    print("\tNeatly formatted name: " + formatted_name + '.')

#Clase que hace los tests
class NamesTestCase(unittest.TestCase):
    def test_FirstLastName(self): 
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') 
        #Assert verifica que lo que ingresas va a salir como se quiere

    def test_FirstLastMiddleName(self): 
        formatted_name = get_formatted_name('janis', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Janis Mozart Amadeus') 
        #Arriba dice; formatted_name debe ser igual a 'Janis Mozart Amadeus'
unittest.main() #Dice a Python que corra el test


#Testing a una clase
"""survey.py"""
class AnonymousSurvey(): 
    def __init__(self, question): 
        self.question = question
        self.responses = [] 
    
    def showQuestion(self): 
        print(question) 
    
    def storeResponse(self,newResponse):
        self.responses.append(newResponse)

    def showResults(self): 
        print("Survey Results: ")
        for response in self.responses: 
            print("- " + response)

#Main
question = "What language did you first learn to speak?"
mySurvey = AnonymousSurvey(question)
mySurvey.showQuestion()

print("Enter 'q' at any time to quit\n")
while True: 
    response = input("Language: ")
    if response == 'q': 
        break 
    mySurvey.storeResponse(response)
#Show the results
print("\nThank you to everyone who participated in the survey!")
mySurvey.showResults()

#Test de la encuesta
import unittest 
#Verifica que la respuesta si se guardo en la lista de respuestas
class TestAnonymousSurvey(unittest.TestCase): 
    
    def test_storeSingleResponse(self): 
        question = "What language did you first learn to speak?"
        mySurvey = AnonymousSurvey(question) #Hacemos la instancia de la clase
        mySurvey.storeResponse('English') 

        self.assertIn('English', mySurvey.responses) 
        #Verifica que 'English' si esta en las respuestas
    
    #Comprobar que si se guardaron 3 respuestas
    def test_storeThreeResponses(self):
        question = "What language did you first learn to speak?"
        mySurvey = AnonymousSurvey(question) #Instanciacion de la clase
        responses = ['English', 'Spanish' 'Mandarin']
        for response in responses: 
            mySurvey.storeResponse(response) 
        
        for response in responses: 
            self.assertIn(response, mySurvey.responses)
            #Verifica que si se guardaron las tres respuestas
unittest.main() 

#Setup; hacemos el codigo más corto y util para todo el codigo
import unittest
class TestAnonymousSurvey(unittest.TestCase): 
    def setUp(self): 
        question = "What language did you first learn to speak?"
        self.mySurvey = AnonymousSurvey(question) 
        self.responses = ['English', 'Spanish' 'Mandarin'] 
        #Crea una instancia de la encuesta
        #Crea una lista de respuestas a utilizar
        #Usa '.self' porque va a ser utilizado en cualquier parte de la clase

    def test_storeSingleResponse(self): 
        self.mySurvey.storeResponse(self.responses[0]) #Solo mira la primera palabra
        self.assertIn(self.responses[0], self.mySurvey.responses)

    def test_storeThreeResponses(self): 
        for response in self.responses:  #Checa por todas las palabras
            self.mySurvey.storeResponse(response) 
        for response in self.responses: 
            self.assertIn(response, self.mySurvey.reponses)
unittest.main()  