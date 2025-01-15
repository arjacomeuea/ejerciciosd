# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Preguntar al usuario las notas y almacenarlas en un diccionario
notas = {asignatura: input(f"¿Qué nota has sacado en {asignatura}? ") for asignatura in asignaturas}

# Mostrar las notas por pantalla
print("\nTus notas son:")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
