# Crear una matriz rectangular cuyo valor en [f][c] es f + c


from math import isfinite


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


def leer_decimal(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if not isfinite(valor):
                print("Ingrese un numero finito.")
            elif minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
            else:
                return valor
        except ValueError:
            print("Ingrese un numero; use punto para los decimales.")


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


def consultar_actualizar_numero(matriz):
    posicion = consultar_posicion(matriz)
    if posicion is not None:
        f, c = posicion
        matriz[f][c] = leer_decimal("Nuevo valor para esa posicion: ")
        mostrar_matriz(matriz)


def crear_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(f + c)
        matriz.append(fila)
    return matriz


def main():
    # Limite practico para que la matriz sea legible en consola
    filas = leer_entero("Cantidad de filas (1 a 20): ", 1, 20)
    columnas = leer_entero("Cantidad de columnas (1 a 20): ", 1, 20)
    matriz = crear_matriz(filas, columnas)
    mostrar_matriz(matriz)
    print("Cada posicion contiene inicialmente la suma de sus indices.")
    consultar_actualizar_numero(matriz)
    eliminar_fila(matriz)


if __name__ == "__main__":
    main()
