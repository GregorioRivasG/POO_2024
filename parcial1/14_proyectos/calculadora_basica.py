
import math

def solicitarNumeros():
    global n1, n2  
    n1 = float(input("Numero #1: "))
    n2 = float(input("Numero #2: "))

def operacionAritmetica(num1, num2, opcion):  
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{num1} + {num2} = {num1 + num2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{num1} - {num2} = {num1 - num2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{num1} * {num2} = {num1 * num2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        return f"{num1} / {num2} = {num1 / num2}"
    elif opcion == "5" or opcion == "**" or opcion == "POTENCIA":
        return f"{num1} ^ {num2} = {num1 ** num2}"
    elif opcion == "6" or opcion == "RAIZ" or opcion == "RAIZ CUADRADA":
        return f"Raiz cuadrada de {num1} = {math.sqrt(num1)}"

opcion = True    
while opcion:
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raíz Cuadrada \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion != "7":
        solicitarNumeros()
        print(operacionAritmetica(n1, n2, opcion))
    else:
        opcion = False
        print("Ejecucion terminada")
