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