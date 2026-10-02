# Encontrar extremos y todas sus posiciones mediante comparaciones


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


def encontrar_extremos(matriz):
    # El algoritmo no usa max(), min(), sum() ni sorted().
    encontrado = False
    posiciones_maximo = []
    posiciones_minimo = []
    f = 0
    for fila in matriz:
        c = 0
        for valor in fila:
            if not encontrado:
                maximo = valor
                minimo = valor
                posiciones_maximo = [[f, c]]
                posiciones_minimo = [[f, c]]
                encontrado = True
            else:
                if valor > maximo:
                    maximo = valor
                    posiciones_maximo = [[f, c]]
                elif valor == maximo:
                    posiciones_maximo.append([f, c])
                if valor < minimo:
                    minimo = valor
                    posiciones_minimo = [[f, c]]
                elif valor == minimo:
                    posiciones_minimo.append([f, c])
            c += 1
        f += 1
    if not encontrado:
        return None
    return maximo, posiciones_maximo, minimo, posiciones_minimo


def mostrar_extremos(matriz):
    resultado = encontrar_extremos(matriz)
    if resultado is None:
        print("La matriz no tiene numeros.")
    else:
        maximo, posiciones_maximo, minimo, posiciones_minimo = resultado
        print("Maximo:", maximo, "Posiciones [fila, columna]:", posiciones_maximo)
        print("Minimo:", minimo, "Posiciones [fila, columna]:", posiciones_minimo)


def main():
    matriz = [[15, 80, 15], [80, 45, 60], [22, 15, 80]]
    mostrar_matriz(matriz)
    mostrar_extremos(matriz)
    consultar_actualizar_numero(matriz)
    eliminar_fila(matriz)
    print("Extremos despues de los cambios:")
    mostrar_extremos(matriz)


if __name__ == "__main__":
    main()
