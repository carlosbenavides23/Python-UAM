# Eliminar todos los tickets cancelados sin saltarse filas consecutivas


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


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El texto no puede estar vacio.")


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


def retirar_cancelados(tickets):
    indice = 0
    while indice < len(tickets):
        if tickets[indice][2] == "Cancelado":
            tickets.pop(indice)
            # No se incrementa: la siguiente fila ocupa este mismo indice.
        else:
            indice += 1


def main():
    tickets = [
        [1, "Ana", "Atendido"],
        [2, "Luis", "Cancelado"],
        [3, "Maria", "Pendiente"],
    ]
    print("Columnas: 0=ID, 1=Nombre, 2=Estado")
    mostrar_matriz(tickets)
    f, c = consultar_posicion(tickets)
    # Actualizamos el nombre de la fila consultada para conservar los ID y estados.
    tickets[f][1] = leer_texto("Nuevo nombre de la persona consultada: ")
    estados = ["Atendido", "Cancelado", "Pendiente"]
    print("Estados: 0=Atendido, 1=Cancelado, 2=Pendiente")
    opcion = leer_entero("Estado de esa fila: ", 0, 2)
    tickets[f][2] = estados[opcion]
    mostrar_matriz(tickets)
    retirar_cancelados(tickets)
    print("Despues de eliminar los cancelados:")
    mostrar_matriz(tickets)


if __name__ == "__main__":
    main()
