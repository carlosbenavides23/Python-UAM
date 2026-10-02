# Reporte alineado de temperaturas y promedio semanal


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


def generar_reporte(temperaturas, dias):
    texto = f"{'Dia':<12} {'Manana':>9} {'Tarde':>9} {'Noche':>9} {'Promedio':>10}\n"
    texto += "-" * 53 + "\n"
    acumulado = 0
    cantidad = 0
    for f in range(len(temperaturas)):
        suma_dia = 0
        for temperatura in temperaturas[f]:
            suma_dia += temperatura
            acumulado += temperatura
            cantidad += 1
        promedio_dia = suma_dia / 3
        texto += (
            f"{dias[f]:<12} {temperaturas[f][0]:>9.2f} "
            f"{temperaturas[f][1]:>9.2f} {temperaturas[f][2]:>9.2f} "
            f"{promedio_dia:>10.2f}\n"
        )
    if cantidad > 0:
        etiqueta = (
            "Promedio semanal"
            if len(temperaturas) == 7
            else "Promedio de dias restantes"
        )
        texto += f"{etiqueta}: {acumulado / cantidad:.2f} °C\n"
    else:
        texto += "No hay temperaturas para calcular un promedio.\n"
    return texto


def main():
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    temperaturas = [
        [24, 31, 26],
        [25, 32, 27],
        [24, 30, 25],
        [23, 29, 24],
        [25, 33, 27],
        [26, 34, 28],
        [24, 31, 26],
    ]
    print("Columnas: 0=Manana, 1=Tarde, 2=Noche. Unidad: °C")
    mostrar_matriz(temperaturas)
    f, c = consultar_posicion(temperaturas)
    temperaturas[f][c] = leer_decimal("Nueva temperatura (-100 a 100 °C): ", -100, 100)
    mostrar_matriz(temperaturas)
    print(generar_reporte(temperaturas, dias))
    # Se calcula primero la semana completa. Eliminar un dia deja menos de 7 dias
    if confirmar("¿Desea eliminar el dia consultado?"):
        temperaturas.pop(f)
        dias.pop(f)
        mostrar_matriz(temperaturas)
        print(generar_reporte(temperaturas, dias))


if __name__ == "__main__":
    main()
