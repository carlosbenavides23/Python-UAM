# Recorrer una matriz y guardar en una lista los valores mayores a 50


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


def obtener_mayores_50(matriz):
    mayores = []
    for fila in matriz:
        for valor in fila:
            if valor > 50:
                mayores.append(valor)
    return mayores


def main():
    matriz = [[10, 55, 90], [50, 72, 30], [100, 45, 55]]
    mostrar_matriz(matriz)
    print("Valores mayores a 50:", obtener_mayores_50(matriz))
    consultar_actualizar_numero(matriz)
    eliminar_fila(matriz)
    print("Valores mayores a 50 despues de los cambios:", obtener_mayores_50(matriz))


if __name__ == "__main__":
    main()
