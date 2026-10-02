# Expediente modular con registro, consulta, actualizacion y eliminacion


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


def buscar_id(grupo, identificador):
    for f in range(len(grupo)):
        if grupo[f][0] == identificador:
            return f
    return -1


def calcular_resultado(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    if promedio >= 70:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    return promedio, estado


def registrar_estudiante(grupo):
    while True:
        identificador = leer_texto("ID del estudiante: ").upper()
        if buscar_id(grupo, identificador) == -1:
            break
        print("Ese ID ya esta registrado.")
    nombre = leer_texto("Nombre: ")
    nota1 = leer_decimal("Nota 1 (0 a 100): ", 0, 100)
    nota2 = leer_decimal("Nota 2 (0 a 100): ", 0, 100)
    nota3 = leer_decimal("Nota 3 (0 a 100): ", 0, 100)
    promedio, estado = calcular_resultado(nota1, nota2, nota3)
    grupo.append([identificador, nombre, nota1, nota2, nota3, promedio, estado])
    print(f"Promedio: {promedio:.2f}. Estado: {estado}")


def mostrar_expediente(grupo):
    mostrar_matriz(grupo)
    print(
        f"{'ID':<12} {'Nombre':<20} {'Nota1':>7} {'Nota2':>7} {'Nota3':>7} {'Promedio':>9} Estado"
    )
    for fila in grupo:
        print(
            f"{fila[0]:<12} {fila[1]:<20} {fila[2]:>7.2f} {fila[3]:>7.2f} "
            f"{fila[4]:>7.2f} {fila[5]:>9.2f} {fila[6]}"
        )


def consultar_actualizar(grupo):
    posicion = consultar_posicion(grupo)
    if posicion is None:
        return
    f, c = posicion
    print("Puede editar: 1=Nombre, 2=Nota1, 3=Nota2, 4=Nota3")
    columna = leer_entero("Columna a actualizar de esa fila: ", 1, 4)
    if columna == 1:
        grupo[f][columna] = leer_texto("Nuevo nombre: ")
    else:
        grupo[f][columna] = leer_decimal("Nueva nota (0 a 100): ", 0, 100)
    promedio, estado = calcular_resultado(grupo[f][2], grupo[f][3], grupo[f][4])
    grupo[f][5] = promedio
    grupo[f][6] = estado
    mostrar_expediente(grupo)


def main():
    grupo = []
    print("Registre el primer estudiante para crear los datos base.")
    registrar_estudiante(grupo)
    mostrar_expediente(grupo)
    consultar_actualizar(grupo)
    eliminar_fila(grupo)
    while True:
        print(
            "\n1. Registrar  2. Mostrar  3. Consultar y actualizar  4. Eliminar  0. Salir"
        )
        opcion = leer_entero("Opcion: ", 0, 4)
        if opcion == 0:
            break
        elif opcion == 1:
            registrar_estudiante(grupo)
            mostrar_expediente(grupo)
        elif opcion == 2:
            mostrar_expediente(grupo)
        elif opcion == 3:
            mostrar_expediente(grupo)
            consultar_actualizar(grupo)
        elif opcion == 4:
            mostrar_expediente(grupo)
            eliminar_fila(grupo)


if __name__ == "__main__":
    main()
