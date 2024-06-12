import funciones_peliculas

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
        funciones_peliculas.agregar_pelicula(pelicula, lista_peliculas)
    elif opcion == "2":
        pelicula = input("Ingrese el nombre de la película a remover: ")
        funciones_peliculas.remover_pelicula(pelicula, lista_peliculas)
    elif opcion == "3":
        funciones_peliculas.consultar_peliculas(lista_peliculas)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")