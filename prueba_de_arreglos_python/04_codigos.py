# Desglosar codigos mediante segmentacion: FAC-2026-ISC-0001


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


def codigo_valido(codigo):
    # Tres letras, cuatro digitos, tres letras y cuatro digitos
    return (
        len(codigo) == 17
        and codigo[3] == "-"
        and codigo[8] == "-"
        and codigo[12] == "-"
        and codigo[0:3].isascii()
        and codigo[0:3].isalpha()
        and codigo[9:12].isascii()
        and codigo[9:12].isalpha()
        and codigo[4:8].isascii()
        and codigo[4:8].isdigit()
        and codigo[13:17].isascii()
        and codigo[13:17].isdigit()
        and int(codigo[4:8]) > 0
        and int(codigo[13:17]) > 0
    )


def leer_codigo(mensaje):
    while True:
        codigo = leer_texto(mensaje).upper()
        if codigo_valido(codigo):
            return codigo
        print("Formato requerido: FAC-2026-ISC-0001. Ano y correlativo positivos.")


def desglosar_codigo(codigo):
    if not codigo_valido(codigo):
        raise ValueError("Codigo invalido.")
    return [codigo[0:3], codigo[4:8], codigo[9:12], codigo[13:17]]


def main():
    codigos = []
    print("Ingrese codigos como FAC-2026-ISC-0001; escriba salir para terminar.")
    while True:
        codigo = leer_texto("Codigo: ").upper()
        if codigo == "SALIR":
            break
        if codigo_valido(codigo):
            codigos.append(codigo)
        else:
            print("Codigo invalido. Use tres letras y los guiones del ejemplo.")
    componentes = []
    for codigo in codigos:
        componentes.append(desglosar_codigo(codigo))
    print("Columnas: Facultad, Ano, Carrera, Correlativo")
    mostrar_matriz(componentes)
    posicion = consultar_posicion(componentes)
    if posicion is not None:
        f, c = posicion
        # Reemplazamos los componentes de la fila con otro codigo valido.
        componentes[f] = desglosar_codigo(leer_codigo("Nuevo codigo para esa fila: "))
        mostrar_matriz(componentes)
    eliminar_fila(componentes)


if __name__ == "__main__":
    main()
