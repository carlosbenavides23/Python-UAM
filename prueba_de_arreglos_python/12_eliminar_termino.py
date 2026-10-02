# Eliminar una o todas las apariciones de un termino de una matriz


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


def consultar_actualizar_numero(matriz):
    posicion = consultar_posicion(matriz)
    if posicion is not None:
        f, c = posicion
        matriz[f][c] = leer_decimal("Nuevo valor para esa posicion: ")
        mostrar_matriz(matriz)


def eliminar_termino(matriz, termino, eliminar_todos):
    eliminados = 0
    for fila in matriz:
        c = 0
        while c < len(fila):
            if fila[c] == termino:
                fila.pop(c)
                eliminados += 1
                if not eliminar_todos:
                    return eliminados
                # La siguiente posicion se desplazo a c; no avanzar aqui
            else:
                c += 1
    return eliminados


def main():
    matriz = [[10, 20, 30], [20, 20, 60], [70, 80, 20]]
    mostrar_matriz(matriz)
    consultar_actualizar_numero(matriz)
    termino = leer_decimal("Termino numerico a eliminar: ")
    todos = confirmar("¿Eliminar todas las apariciones? (n elimina solo la primera)")
    cantidad = eliminar_termino(matriz, termino, todos)
    if cantidad == 0:
        print("El termino no se encuentra en la matriz.")
    else:
        print("Elementos eliminados:", cantidad)
    mostrar_matriz(matriz)
    print("Al eliminar elementos, las filas pueden tener diferentes longitudes.")


if __name__ == "__main__":
    main()
