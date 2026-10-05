# Ejercicio 3: consultar, actualizar y eliminar un producto.
inventario = [
    ["PROD-01", "Teclado", 15, 25.0],
    ["PROD-02", "Mouse", 20, 12.5],
    ["PROD-03", "Monitor", 8, 180.0]
]

print("Columnas: 0=Código, 1=Producto, 2=Cantidad, 3=Precio")
for f in range(len(inventario)):
    print(f, inventario[f])

# Consultar una posición. Los índices empiezan en cero.
while True:
    try:
        f = int(input("Fila a consultar: "))
        c = int(input("Columna a consultar: "))
        if 0 <= f < len(inventario) and 0 <= c < 4:
            break
        print("Fila o columna fuera de rango.")
    except ValueError:
        print("Ingrese índices enteros.")

print("Dato consultado:", inventario[f][c])

# Actualizar la cantidad de la fila consultada.
while True:
    try:
        cantidad = int(input("Nueva cantidad: "))
        if cantidad >= 0:
            break
        print("La cantidad no puede ser negativa.")
    except ValueError:
        print("Ingrese una cantidad entera.")

inventario[f][2] = cantidad
print("Inventario actualizado:")
for f in range(len(inventario)):
    print(f, inventario[f])

# -1 permite terminar sin eliminar productos.
while True:
    try:
        f = int(input("Fila del producto descontinuado (-1 para omitir): "))
        if f == -1:
            break
        if 0 <= f < len(inventario):
            print("Producto eliminado:", inventario.pop(f))
            break
        print("La fila no existe.")
    except ValueError:
        print("Ingrese un índice entero.")

print("Inventario final:")
for fila in inventario:
    print(fila)
