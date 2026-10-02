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


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El texto no puede estar vacio.")


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


def matriz_a_texto(estudiantes):
    texto = f"{'Estudiante':<20} {'Nota 1':>8} {'Nota 2':>8}\n"
    texto += "-" * 38 + "\n"
    for fila in estudiantes:
        texto += f"{fila[0]:<20} {fila[1]:>8.2f} {fila[2]:>8.2f}\n"
    return texto


def main():
    estudiantes = [["Carlos", 85, 90], ["Ana", 95, 88], ["Luis", 70, 75]]
    mostrar_matriz(estudiantes)
    print(matriz_a_texto(estudiantes))
    f, c = consultar_posicion(estudiantes)
    if c == 0:
        estudiantes[f][c] = leer_texto("Nuevo nombre: ")
    else:
        estudiantes[f][c] = leer_decimal("Nueva nota (0 a 100): ", 0, 100)
    mostrar_matriz(estudiantes)
    eliminar_fila(estudiantes)
    print("Reporte final:\n" + matriz_a_texto(estudiantes))


if __name__ == "__main__":
    main()
