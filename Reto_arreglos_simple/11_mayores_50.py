# Ejercicio 11: crear una lista con los valores mayores a 50.
matriz = [[10, 55, 90], [50, 72, 30], [100, 45, 55]]

print("Matriz:")
for fila in matriz:
    print(fila)

mayores = []
for fila in matriz:
    for valor in fila:
        if valor > 50:
            mayores.append(valor)

print("Valores mayores a 50:", mayores)
