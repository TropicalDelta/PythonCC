fileName = 'programming.txt'
with open(fileName, 'w') as fo: 
    #Usamos 'w' para indicar que vamos a escribir, pero...
    #si el archivo ya contiene texto, este se borrará
    #Es como crear un nuevo archivo
    fo.write('I love programming. ') #Escribimos en el objeto

    #!Si queremos escribir numeros, debemos usar str() para convertirlo
    #... a una cadena. 

    fo.write('I love creating new games. ') 


#Si se desea escribir en un archivo sin modificar lo ya existente se usa: 
with open(fileName, 'a') as fo: 
    fo.write("I also love finding meaning in large datasets.\n")
    fo.write('I love creating apps that can run in a browser.\n')
