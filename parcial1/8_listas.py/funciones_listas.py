"""
def agregar_pelicula(pelicula, lista_peliculas):
    lista_peliculas.append(pelicula)
    print(f"¡{pelicula} ha sido agregada a la lista de películas!")

def remover_pelicula(pelicula, lista_peliculas):
    if pelicula in lista_peliculas:
        lista_peliculas.remove(pelicula)
        print(f"¡{pelicula} ha sido removida de la lista de películas!")
    else:
        print(f"{pelicula} no se encuentra en la lista de películas.")

def consultar_peliculas(lista_peliculas):
    print("Lista de películas:")
    for pelicula in lista_peliculas:
        print(pelicula)
"""
# def menu(operacion, peliculas):
#     match (operacion):
#         case 1: 
#             peliculaAgregar = input("Ingrese el titulo de la pelicula a agregar: ")
#             peliculas.append(peliculaAgregar)
#         case 2:
#             peliculaQuitar = input("Ingrese el titulo de la pelicula a quitar: ")
#             peliculas.remove(peliculaQuitar)
#         case 3:
#             print("Peliculas")
#             print(peliculas)

paises=["Mexico","USA","Brasil","Japon"]
numeros=[2,100,3.1416,0.100]
varios=["Hola",True,100,10.22]

#ordennar lista
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#Agregar elemmentos
print(numeros)
numeros.innsert(len(numeros),100)
print(numeros)
numeros.append(100)

#Eliminar elementos
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#Buscar dentro de una lista un dato o un valor

encontrar="Brasil" in paises
print(encontrar)

#Dar la vuelta
print(varios)
varios.reverse
print(varios)

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)

#Vaciar una lista
print(varios)
varios.clear()
print(varios)
