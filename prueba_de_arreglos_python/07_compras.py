# Capturar ventas, generar un recibo y recuperar su matriz desde el texto


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


def leer_producto(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if nombre and "|" not in nombre and "\n" not in nombre and "\r" not in nombre:
            return nombre
        print("Ingrese un nombre no vacio y sin el separador |.")


def capturar_compras():
    ventas = []
    while True:
        producto = leer_producto("Producto (salir o n para terminar): ")
        if producto.lower() in ["salir", "n"]:
            break
        cantidad = leer_entero("Cantidad: ", 1)
        precio = round(leer_decimal("Precio unitario: ", 0), 2)
        try:
            subtotal = round(cantidad * precio, 2)
        except OverflowError:
            print("La compra es demasiado grande. Ingresela nuevamente.")
            continue
        if not isfinite(subtotal):
            print("La compra es demasiado grande. Ingresela nuevamente.")
            continue
        ventas.append([producto, cantidad, precio, subtotal])
    return ventas


def generar_recibo(ventas):
    texto = "RECIBO DE COMPRAS\n"
    texto += f"{'Producto':<20} | {'Cantidad':>8} | {'Precio':>10} | {'Subtotal':>10}\n"
    texto += "-" * 60 + "\n"
    total = 0
    for fila in ventas:
        texto += f"{fila[0]:<20} | {fila[1]:>8} | {fila[2]:>10.2f} | {fila[3]:>10.2f}\n"
        total += fila[3]
    texto += "-" * 60 + "\n"
    texto += f"TOTAL GENERAL: {total:.2f}\n"
    return texto


def recuperar_ventas(texto):
    lineas = texto.splitlines()
    separador = "-" * 60
    encabezado = (
        f"{'Producto':<20} | {'Cantidad':>8} | {'Precio':>10} | {'Subtotal':>10}"
    )
    if (
        len(lineas) < 5
        or lineas[0] != "RECIBO DE COMPRAS"
        or lineas[1] != encabezado
        or lineas[2] != separador
        or lineas[-2] != separador
        or not lineas[-1].startswith("TOTAL GENERAL: ")
    ):
        raise ValueError("El texto no tiene el formato del recibo.")
    ventas = []
    total = 0
    for linea in lineas[3:-2]:
        partes = linea.split("|")
        if len(partes) != 4:
            raise ValueError("Una venta debe tener cuatro campos.")
        nombre = partes[0].strip()
        cantidad = int(partes[1].strip())
        precio = float(partes[2].strip())
        subtotal = float(partes[3].strip())
        if (
            not nombre
            or cantidad <= 0
            or not isfinite(precio)
            or not isfinite(subtotal)
            or precio < 0
            or subtotal < 0
        ):
            raise ValueError("La venta contiene datos invalidos.")
        try:
            calculado = round(cantidad * precio, 2)
        except OverflowError:
            raise ValueError("La venta es demasiado grande.")
        if not isfinite(calculado) or abs(calculado - subtotal) > 0.001:
            raise ValueError("El subtotal no coincide con cantidad por precio.")
        ventas.append([nombre, cantidad, precio, subtotal])
        total += subtotal
    total_recibo = float(lineas[-1].split(":", 1)[1].strip())
    if (
        not isfinite(total_recibo)
        or not isfinite(total)
        or abs(total - total_recibo) > 0.001
    ):
        raise ValueError("El total general no coincide con las ventas.")
    return ventas


def main():
    ventas = capturar_compras()
    mostrar_matriz(ventas)
    posicion = consultar_posicion(ventas)
    if posicion is not None:
        f, c = posicion
        # El subtotal depende de la cantidad: siempre se recalcula
        while True:
            cantidad = leer_entero("Nueva cantidad de la venta consultada: ", 1)
            try:
                subtotal = round(cantidad * ventas[f][2], 2)
            except OverflowError:
                print("Cantidad demasiado grande.")
                continue
            if isfinite(subtotal):
                break
            print("Cantidad demasiado grande.")
        ventas[f][1] = cantidad
        ventas[f][3] = subtotal
        mostrar_matriz(ventas)
    eliminar_fila(ventas)
    recibo = generar_recibo(ventas)
    print("\n" + recibo)
    print("Matriz recuperada desde el recibo:")
    try:
        mostrar_matriz(recuperar_ventas(recibo))
    except ValueError as error:
        print("No se pudo recuperar el recibo:", error)


if __name__ == "__main__":
    main()
