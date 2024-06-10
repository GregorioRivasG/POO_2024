"""
List (Array)
son colecciones o conjuntos de datos/valor bajo un mismo nombre, para acceder a los valores
se hace con un indice numerico


Nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable permite miembros duplicados
"""
"""

#ejemplo 1- crear una lista de numeros e imprimir el contenido
numeros = [23,34]
print(numeros[0])

#recorrer una lista con un for
numeros = [23,34]
for i in numeros:
    print(i)

#recorrer una lista con while
numeros = [23,34]
i=0
while i<= len(numeros) -1:
    print(numeros[i])
    i+=1

#ejemplo 2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra

palabra = ["hola","utd", "como", "estas", "ok", "ok", "naranja"]
palabra_buscar = input("inserta palabra a buscar: ")

if palabra_buscar in palabra:
    for i, p in enumerate(palabra):
        if p == palabra_buscar:
            print(f"Encontré la palabra en la posición {i}")
else:
    print("No encontré la palabra en la lista")"""

#ejemplo 2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra

#palabras=["naranja","utd","america","azul"]
#palabra_buscar = input("Ingresa la palabra a buscar: ")

#if palabra_buscar==palabras:
# print("se encontro la palabra")
#else:
#    print("No se encontro la palabra")


"""    
#Ejemplo 3 Aqgregar y Eliminar elementos de una lista
# os.system("clear")

numeros=[23,34,23]
print(numeros)

#Agregar un elemento
numeros.append(100)
print(numeros)
numeros.insert(3,200)
print(numeros)

#Eliminar un elemento
numeros.remove(100) #Indicar el elemnento a borrar
numeros.pop(2) #indicar la posicion del elemento a borrar
print(numeros)
"""
"""
palabra_buscar = input("ingresa la palabra a buscar: ")

encontro=False

for i in palabras:
    if i=palabra_buscar:
        print("se encontro la palabra {palabra_buscar} en la posicion {palabras,index(i)}")
        encontro=True
        """
"""  
palabras=["naranja","utd","america","azul"]
palabra_buscar = input("Ingresa la palabra a buscar: ")
    
i=0        
while i<len(palabras):
    if palabras ==palabra_buscar:
        print(f"se encontro la palabra {palabra_buscar} en la posicion {1} ")

if not encontro:

    print("No se encontro la palabra a buscar")
    
"""

#Ejemplo 4  crear una lista multilinea [matriz] para agregar los nombres y los numeros telefonicos


# agenda = [
#     ("Carlos", 618123467),
#     ("Leo", 6678293),
#     ("Sebastian", 727357839),
#     ("Pedro", 672883293)
# ]

# for i, (nombre, numero) in enumerate(agenda, start=1):
#     print(f"{i}.- {nombre}: {numero}")
    
#ejemplo 5 crear un programa que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar pleiculas.
#Notas:
#Utilizar funciones y mandar llamar desde otro archivo
#Utilizar listas para almacenar los nombres de peliculas
# main.py

"""
import funciones_listas

lista_peliculas = []

while True:
    print("\n*** Gestión de Películas ***")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        pelicula = input("Ingrese el nombre de la película a agregar: ")
        funciones_listas.agregar_pelicula(pelicula, lista_peliculas)
    elif opcion == "2":
        pelicula = input("Ingrese el nombre de la película a remover: ")
        funciones_listas.remover_pelicula(pelicula, lista_peliculas)
    elif opcion == "3":
        funciones_listas.consultar_peliculas(lista_peliculas)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
"""       

# import os
# from funciones_listas import menu

# i = True
# peliculas = []

# while i == True:
#     print("""     .::     MENU DE OPCIONES        ::.     
#         1. AGREGAR PELICULAS
#         2. REMOVER PELICULAS
#         3. CONSULTAR PELICULAS
#         4. SALIR
#         """)
#     opcion = int(input("Elija una opcion: "))

#     if opcion == 4:
#         i = False
#         print("Ha terminado la ejecucion del progama.")
#     else:
#         menu(opcion, peliculas)
#         input("Presione una tecla para continuar...")
#         os.system("clear")
