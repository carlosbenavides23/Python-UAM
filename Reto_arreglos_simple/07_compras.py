# Ejercicio 7: compras, recibo textual y recuperación de la matriz.
from math import isfinite


def generar_recibo(ventas):
    recibo = "RECIBO DE COMPRAS\nProducto | Cantidad | Precio | Subtotal\n"
    recibo += "-" * 50 + "\n"
    total = 0
    for fila in ventas:
        recibo += f"{fila[0]} | {fila[1]} | {fila[2]:.2f} | {fila[3]:.2f}\n"
        total += fila[3]
    recibo += "-" * 50 + "\n"
    recibo += f"TOTAL: {total:.2f}"
    return recibo


def recuperar_ventas(recibo):
    ventas = []
    lineas = recibo.splitlines()
    # Omitimos las tres líneas del encabezado y las dos del cierre.
    for linea in lineas[3:-2]:
        partes = linea.split("|")
        if len(partes) != 4:
            raise ValueError("La venta debe tener cuatro datos.")
        nombre = partes[0].strip()
        cantidad = int(partes[1])
        precio = float(partes[2])
        subtotal = float(partes[3])
        if (not nombre or cantidad <= 0 or not isfinite(precio)
                or not isfinite(subtotal) or precio < 0 or subtotal < 0):
            raise ValueError("La venta contiene datos inválidos.")
        if round(cantidad * precio, 2) != subtotal:
            raise ValueError("El subtotal es incorrecto.")
        ventas.append([nombre, cantidad, precio, subtotal])
    return ventas


ventas = []
while True:
    producto = input("Producto (salir o n para terminar): ").strip()
    if producto.lower() == "salir" or producto.lower() == "n":
        break
    if producto == "" or "|" in producto:
        print("Ingrese un nombre no vacío y sin el carácter |.")
        continue
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))
        if cantidad <= 0 or not isfinite(precio) or precio < 0:
            print("La cantidad debe ser positiva y el precio no negativo.")
            continue
        precio = round(precio, 2)
        subtotal = round(cantidad * precio, 2)
        if not isfinite(subtotal):
            print("La compra es demasiado grande.")
            continue
        ventas.append([producto, cantidad, precio, subtotal])
    except (ValueError, OverflowError):
        print("Ingrese una cantidad entera y un precio numérico válido.")

print("\nMatriz de ventas:")
for fila in ventas:
    print(fila)

recibo = generar_recibo(ventas)
print("\n" + recibo)

print("\nMatriz recuperada del recibo:")
for fila in recuperar_ventas(recibo):
    print(fila)
