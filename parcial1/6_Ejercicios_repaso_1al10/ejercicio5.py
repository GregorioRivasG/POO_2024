# Solicitar dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Verificar cuál es el número más pequeño y cuál es el más grande
start = min(num1, num2)
end = max(num1, num2)

# Mostrar todos los números entre los dos números ingresados
print("Números entre", num1, "y", num2, ":")

for i in range(start + 1, end):
    print(i, end=" ")
