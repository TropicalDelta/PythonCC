with open('piDigits.txt') as fileObject: 
    #primero se abre el archivo que se quiere examinar 'piDigits'
    #luego guarda lo que tiene el archivo dentro de un objeto llamado fileObject

    contents = fileObject.read() #Leemos lo que tiene el objeto y lo...
    #guardamos dentro de una variable
    print(contents.rstip()) #Imprimimos lo que ya ha sido leído y almacenado

    """
    Para encontrar un archivo en una direccion distina se usa:     
    with open(carpeta nueva\pythonFiles\piDigits.txt) as fo:
    """

#Ejemplo con una direccion general
filePath = '\C:Users\David\otherFiles\PythonProjects\fileText.txt'
with open(filePath) as fo: 
    print((fo.read()).strip()) #No estoy seguro si se puede aplicar 'rstrip' asi :T

#Leyendo linea por linea
filename = 'piDigits.txt'
with open(filename) as fo:
    lines = fo.readlines() #Lee cada linea y las añade a una lista
    for line in lines:
        print(line.rstrip()) #Imprime cada linea por separado

#Contenido de un archivo
filename = 'piDigits.txt'
with open(filename) as fo:
    lines = fo.readlines()

piString = ''
for line in lines:
    piString += line.strip() #Imprime una linea de texto si saltos de linea

print(piString)
print(len(piString))

#!Python guarda la informacion txt como texto, si se quiere trabajar con un...
#numero, se ha de convertir la informacion a usar a un entero 'int()' 'float'

#Determinar si un valor aparece dentro de un archivo
if "1592" in piString:
    print("Yep")
else: print("nah") 


      
    