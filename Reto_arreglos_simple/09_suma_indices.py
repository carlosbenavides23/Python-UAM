# Ejercicio 9: crear una matriz con la suma de sus índices.
while True:
    try:
        filas = int(input("Número de filas: "))
        columnas = int(input("Número de columnas: "))
        if filas > 0 and columnas > 0:
            break
        print("Las dimensiones deben ser mayores que cero.")
    except ValueError:
        print("Ingrese dimensiones enteras.")

matriz = []
for f in range(filas):
    fila = []
    for c in range(columnas):
        fila.append(f + c)
    matriz.append(fila)

print("Matriz generada:")
for fila in matriz:
    print(fila)
