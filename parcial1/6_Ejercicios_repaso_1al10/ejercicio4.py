# Solicitar dos números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Suma
suma = num1 + num2
print("Suma:", suma)

# Resta
resta = num1 - num2
print("Resta:", resta)

# Multiplicación
multiplicacion = num1 * num2
print("Multiplicación:", multiplicacion)

# División (se verifica si el divisor no es cero)
if num2 != 0:
    division = num1 / num2
    print("División:", division)
else:
    print("No se puede dividir entre cero.")

# Potencia
potencia = num1 ** num2
print("Potencia:", potencia)
