#Los errores de ejecucion en un lenguaje de programacion se presentan cuando existe una anomalia o error dentro de la ejecucion del codigo, lo cual provoca que se detenga la ejecucion del mismo. Con el control y manejo de excepciones, sera posible minimizar o evitar la interrupcion del programa debido a una exepcion.

#Ejemplo 1 cuando una variable no se genera

# try: 
#  nombre=input("introduce el nombre completo de una persona: ")

#  if len(nombre)>0:
#     nombre_usuario="El nombre completo del usuario es: "+nombre
    
#  print(nombre_usuario)
# except:
#     print("es necesario introducir un nombre de usuario... verifica porfavor")
    
# x=3+4
# print("el valor de x es: "+str(x))

#Ejemplo 2 cuando se solicita un nuero y se ingresa otra cosa
"""
try:
    
    numero=int(input("ingrese un numero entero: "))

    if numero>0:
        print("soy un numero entero positivo")
    elif numero==0:
        print("soy un numero entero neutrp")
    else:
        print("soy un numero entero negativo")
except ValueError:
    print("introduce un valor numerico entero")
"""  
#Ejemplo 3 cuando se generan multiples excepciones
try:
    numero=int(input("introduce un numero: "))

    print("El cuadrado del numero es: "+str(numero*numero))
except ValueError:
    print("introduce un valor numerico entero")
except TypeError:
    print("Se debe convertir el nuero a entero")
else:
    print("No se presentan errores de ejecucion")
finally:
    print("Termino la ejecucion ")
