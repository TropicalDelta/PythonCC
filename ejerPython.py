#1. Pedir 10 numeros, sumarlos y mostrar el resultado en pantalla
def suma10Numeros():
    flag = 0
    resultado = 0
    #for n in range(0,10):
    while True:
        n = int(input("Ingrese un número: "))
        resultado = resultado + n
        flag += 1
        if flag == 10: break
    return resultado
#print(suma10Numeros())


#2. Pedir numeros hasta que el usuario ingrese un numero negativo
def numeroNegativo():
    listaN = [] 
    n = 0
    while n >= 0: 
        n = int(input("Ingrese un número: "))
        if n >= 0: listaN.append(n)
    print(listaN)
#numeroNegativo()


#3. Pedir 10 numeros y mostrar 10 primeros terminos de su tabla de multiplicar
def multiplicar10N():
    n = int(input("Número: "))
    for i in range(1,11):
        print(f"{n}x{i} = {n*i}")
#multiplicar10N()


#4. Pedir dos numeros por teclado y mostrar todos los numeros pares comprendidos entre ambos
def numPares(): 
    n = int(input("Número 1: "))
    n2 = int(input("Número 2: "))


    for i in range(n, n2+1):
        if i%2==0:
            print(i)

#numPares()            
    

        