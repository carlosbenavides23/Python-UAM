# Ejercicio 12: eliminar de una matriz todas las apariciones de un término.
from math import isfinite

matriz = [[10, 20, 30], [20, 20, 60], [70, 80, 20]]
print("Matriz original:")
for fila in matriz:
    print(fila)

while True:
    try:
        termino = float(input("Número a eliminar: "))
        if isfinite(termino):
            break
        print("Ingrese un número finito.")
    except ValueError:
        print("Ingrese un número válido.")

eliminados = 0
for fila in matriz:
    c = 0
    while c < len(fila):
        if fila[c] == termino:
            fila.pop(c)
            eliminados += 1
            # El siguiente elemento ocupa esta misma columna.
        else:
            c += 1

if eliminados == 0:
    print("El término no está en la matriz.")
else:
    print("Elementos eliminados:", eliminados)

print("Matriz final:")
for fila in matriz:
    print(fila)
