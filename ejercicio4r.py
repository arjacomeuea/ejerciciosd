# Preguntar al usuario los números ganadores
numeros_ganadores = []
print("Introduce los números ganadores de la lotería primitiva (6 números):")
for i in range(6):
    numero = int(input(f"Número {i+1}: "))
    numeros_ganadores.append(numero)

# Ordenar los números de menor a mayor
numeros_ganadores.sort()

# Mostrar los números ganadores ordenados
print("\nLos números ganadores ordenados de menor a mayor son:")
print(numeros_ganadores)
