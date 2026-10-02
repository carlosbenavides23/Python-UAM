# Consultar un producto, actualizar su cantidad y eliminarlo con pop


def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
            else:
                return valor
        except ValueError:
            print("Ingrese un numero entero.")


def confirmar(mensaje):
    while True:
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Responda s o n.")


def mostrar_matriz(matriz):
    print("\nMatriz (los indices empiezan en 0):")
    if not matriz:
        print("[vacia]")
    for f in range(len(matriz)):
        print(f"Fila {f}: {matriz[f]}")


def consultar_posicion(matriz):
    if not matriz:
        print("No hay filas para consultar.")
        return None
    f = leer_entero("Fila a consultar: ", 0, len(matriz) - 1)
    if not matriz[f]:
        print("Esta fila no tiene elementos.")
        return None
    c = leer_entero("Columna a consultar: ", 0, len(matriz[f]) - 1)
    print(f"matriz[{f}][{c}] = {matriz[f][c]}")
    return f, c


def eliminar_fila(matriz):
    if not matriz:
        print("No hay filas para eliminar.")
        return
    if confirmar("¿Desea eliminar una fila?"):
        f = leer_entero("Fila a eliminar: ", 0, len(matriz) - 1)
        print("Fila eliminada:", matriz.pop(f))
        mostrar_matriz(matriz)


def main():
    inventario = [
        ["PROD-01", "Teclado", 15, 25.0],
        ["PROD-02", "Mouse", 20, 12.5],
        ["PROD-03", "Monitor", 8, 180.0],
    ]
    print("Columnas: 0=Codigo, 1=Producto, 2=Cantidad, 3=Precio")
    mostrar_matriz(inventario)
    f, c = consultar_posicion(inventario)
    nueva_cantidad = leer_entero("Nueva cantidad del producto consultado: ", 0)
    inventario[f][2] = nueva_cantidad
    mostrar_matriz(inventario)
    print("Elimine una fila si el producto esta descontinuado.")
    eliminar_fila(inventario)


if __name__ == "__main__":
    main()
