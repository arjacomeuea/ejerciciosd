# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Mostrar los números en orden inverso separados por comas
print(", ".join(map(str, numeros[::-1])))
