# ============================================================
# GUIA PRACTICA - SENTENCIAS DE CONTROL
# Programa con menu, funciones y validaciones
# ============================================================


# ============================================================
# FUNCIONES DE VALIDACION
# ============================================================


def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
                continue

            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
                continue

            return valor

        except ValueError:
            print("Ingrese un numero entero valido")


def leer_decimal(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
                continue

            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
                continue

            return valor

        except ValueError:
            print("Ingrese un numero valido")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("El texto no puede quedar vacio")


def leer_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta in ("si", "s"):
            return True

        if respuesta in ("no", "n"):
            return False

        print("Ingrese si o no")


def pausa():
    input("\nPresione Enter para continuar...")


# ============================================================
# EJERCICIOS CON IF
# ============================================================


def if_inventario_pulperia():
    print("\n--- Inventario de una pulperia ---")

    producto = leer_texto("Nombre del producto: ")
    existencia = leer_entero("Cantidad disponible: ", 0)

    if existencia < 5:
        print(f"Alerta: {producto} necesita reposicion")
    else:
        print(f"{producto} tiene suficiente existencia")


def if_promocion_tienda():
    print("\n--- Promocion de una tienda ---")

    monto = leer_decimal("Monto de la compra C$: ", 0)

    if monto > 1500:
        descuento = monto * 0.10
    else:
        descuento = 0

    total = monto - descuento

    print(f"Compra original: C${monto:.2f}")
    print(f"Descuento: C${descuento:.2f}")
    print(f"Total a pagar: C${total:.2f}")


def if_meta_ventas():
    print("\n--- Meta de ventas ---")

    meta = 4000
    ventas = leer_decimal("Total vendido C$: ", 0)

    if ventas >= meta:
        diferencia = ventas - meta
        print("La meta fue alcanzada")
        print(f"Se supero por C${diferencia:.2f}")
    else:
        diferencia = meta - ventas
        print("La meta no fue alcanzada")
        print(f"Faltaron C${diferencia:.2f}")


def if_entrega_comedor():
    print("\n--- Entrega de un comedor ---")

    compra = leer_decimal("Monto de la compra C$: ", 0)

    if compra >= 300:
        total = compra
        print("La entrega es gratuita")
    else:
        recargo = 40
        total = compra + recargo
        print(f"Se aplica un recargo de C${recargo:.2f}")

    print(f"Total a pagar: C${total:.2f}")


def if_peso_productos():
    print("\n--- Peso de productos ---")

    peso = leer_decimal("Peso del saco en kg: ", 0)

    if peso >= 46:
        print("El saco cumple con el peso esperado")
    else:
        print("El saco debe revisarse porque esta por debajo de 46 kg")


# ============================================================
# EJERCICIOS CON IF ANIDADOS
# ============================================================


def nested_credito_interno():
    print("\n--- Credito interno ---")

    registrado = leer_si_no("El cliente esta registrado? (si/no): ")

    if registrado:
        saldo = leer_decimal("Saldo pendiente C$: ", 0)

        if saldo <= 500:
            print("Credito disponible")
        else:
            print("Debe regularizar el saldo antes de recibir credito")
    else:
        print("Cliente no registrado")
        print("La compra debe realizarse de contado")


def nested_servicio_entrega():
    print("\n--- Servicio de entrega ---")

    zona = leer_entero("Zona de entrega\n1. Urbana\n2. Rural\nSeleccione: ", 1, 2)

    peso = leer_decimal("Peso del paquete en kg: ", 0)

    if zona == 1:
        if peso > 5:
            tarifa = 100
        else:
            tarifa = 60
    else:
        if peso > 5:
            tarifa = 180
        else:
            tarifa = 120

    print(f"Tarifa de entrega: C${tarifa:.2f}")


def nested_clasificacion_cafe():
    print("\n--- Clasificacion de cafe ---")

    humedad = leer_decimal("Porcentaje de humedad: ", 0, 100)

    if 10 <= humedad <= 12:
        defectos = leer_entero("Cantidad de defectos reportados: ", 0)

        if defectos <= 2:
            categoria = "Calidad alta"
        elif defectos <= 5:
            categoria = "Calidad media"
        else:
            categoria = "Calidad baja"

        print(f"Clasificacion: {categoria}")
    else:
        print("El lote no puede clasificarse")
        print("La humedad debe estar entre 10% y 12%")


def nested_reserva_hospedaje():
    print("\n--- Reserva de hospedaje ---")

    tarifa_noche = leer_decimal("Tarifa por noche C$: ", 0)
    noches = leer_entero("Cantidad de noches: ", 1)
    temporada_baja = leer_si_no("Es temporada baja? (si/no): ")

    subtotal = tarifa_noche * noches
    descuento = 0

    if temporada_baja:
        if noches >= 3:
            descuento = subtotal * 0.15
        else:
            descuento = subtotal * 0.05

    total = subtotal - descuento

    print(f"Subtotal: C${subtotal:.2f}")
    print(f"Descuento: C${descuento:.2f}")
    print(f"Total: C${total:.2f}")


def nested_venta_ferreteria():
    print("\n--- Venta de ferreteria ---")

    tipo = leer_entero(
        "Tipo de cliente\n1. Mayorista\n2. Minorista\nSeleccione: ", 1, 2
    )

    compra = leer_decimal("Monto de compra C$: ", 0)
    descuento = 0

    if tipo == 1:
        if compra >= 3000:
            descuento = compra * 0.12
    else:
        if compra >= 1000:
            descuento = compra * 0.05

    total = compra - descuento

    print(f"Compra: C${compra:.2f}")
    print(f"Descuento: C${descuento:.2f}")
    print(f"Total: C${total:.2f}")


# ============================================================
# EJERCICIOS CON FOR
# ============================================================


def for_ventas_minisuper():
    print("\n--- Ventas de un minisuper ---")

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    total = 0

    for dia in dias:
        venta = leer_decimal(f"Venta del {dia} C$: ", 0)
        total += venta

    promedio = total / 7

    print(f"Total semanal: C${total:.2f}")
    print(f"Promedio diario: C${promedio:.2f}")


def for_recepcion_cafe():
    print("\n--- Recepcion de cafe ---")

    peso_total = 0

    for saco in range(1, 6):
        peso = leer_decimal(f"Peso del saco {saco} en kg: ", 0)
        peso_total += peso
        print(f"Saco {saco} recibido")

    print(f"Peso total recibido: {peso_total:.2f} kg")


def for_revision_inventario():
    print("\n--- Revision de inventario ---")

    alertas = 0

    for numero in range(1, 9):
        print(f"\nProducto {numero}")

        nombre = leer_texto("Nombre: ")
        existencia = leer_entero("Existencia: ", 0)

        if existencia < 10:
            print(f"Alerta: {nombre} tiene inventario bajo")
            alertas += 1

    print(f"\nCantidad de productos con inventario bajo: {alertas}")


def for_produccion_pan():
    print("\n--- Produccion de pan ---")

    produccion_total = 0
    ventas_totales = 0

    for dia in range(1, 7):
        print(f"\nDia {dia}")

        produccion = leer_entero("Unidades producidas: ", 0)
        ventas = leer_entero("Unidades vendidas: ", 0)

        while ventas > produccion:
            print("Las ventas no pueden superar la produccion del dia")
            ventas = leer_entero("Unidades vendidas: ", 0)

        produccion_total += produccion
        ventas_totales += ventas

    sobrante = produccion_total - ventas_totales

    print(f"\nProduccion total: {produccion_total}")
    print(f"Ventas totales: {ventas_totales}")
    print(f"Producto sobrante: {sobrante}")


def for_evaluacion_servicio():
    print("\n--- Evaluacion del servicio ---")

    suma = 0
    valoraciones_altas = 0

    for numero in range(1, 11):
        calificacion = leer_entero(f"Calificacion del cliente {numero} (1-5): ", 1, 5)

        suma += calificacion

        if calificacion >= 4:
            valoraciones_altas += 1

    promedio = suma / 10

    print(f"Promedio: {promedio:.2f}")
    print(f"Valoraciones de 4 o 5: {valoraciones_altas}")


# ============================================================
# EJERCICIOS CON WHILE
# ============================================================


def while_cierre_caja():
    print("\n--- Cierre de caja ---")

    total = 0
    cantidad = 0

    while True:
        venta = leer_decimal("Monto de venta C$ (0 para terminar): ", 0)

        if venta == 0:
            break

        total += venta
        cantidad += 1

    print(f"Total recaudado: C${total:.2f}")
    print(f"Cantidad de ventas: {cantidad}")


def while_acceso_sistema():
    print("\n--- Acceso al sistema ---")

    clave_correcta = "python123"
    intentos = 0
    clave = ""

    while clave != clave_correcta:
        clave = input("Ingrese la clave: ")
        intentos += 1

        if clave != clave_correcta:
            print("Clave incorrecta")

    print("Acceso permitido")
    print(f"Intentos necesarios: {intentos}")


def while_cantidad_pedido():
    print("\n--- Cantidad de un pedido ---")

    cantidad = leer_entero("Cantidad de unidades entre 1 y 100: ", 1, 100)
    precio = leer_decimal("Precio por unidad C$: ", 0)

    total = cantidad * precio

    print(f"Cantidad: {cantidad}")
    print(f"Total del pedido: C${total:.2f}")


def while_combustible_reparto():
    print("\n--- Combustible de reparto ---")

    combustible = 8.0
    recorrido = 0

    while combustible > 0:
        print(f"\nCombustible disponible: {combustible:.2f} litros")

        if combustible <= 1:
            print("Alerta: combustible en nivel minimo")
            break

        consumo = leer_decimal("Consumo del recorrido en litros: ", 0.01)

        while consumo > combustible:
            print("El consumo no puede superar el combustible disponible")
            consumo = leer_decimal("Consumo del recorrido en litros: ", 0.01)

        combustible -= consumo
        recorrido += 1

    print(f"\nRecorridos registrados: {recorrido}")
    print(f"Combustible restante: {combustible:.2f} litros")


def while_reposicion_existencias():
    print("\n--- Reposicion de existencias ---")

    existencia = 3
    meta = 20

    while existencia < meta:
        print(f"Existencia actual: {existencia}")

        reposicion = leer_entero("Cantidad a reponer: ", 1)
        existencia += reposicion

    print(f"Meta alcanzada")
    print(f"Existencia final: {existencia}")


# ============================================================
# SUBMENUS
# ============================================================


def menu_if():
    while True:
        print("\n" + "=" * 60)
        print("                     EJERCICIOS CON IF")
        print("=" * 60)
        print("1. Inventario de una pulperia")
        print("2. Promocion de una tienda")
        print("3. Meta de ventas")
        print("4. Entrega de un comedor")
        print("5. Peso de productos")
        print("0. Volver al menu principal")

        opcion = leer_entero("Seleccione una opcion: ", 0, 5)

        if opcion == 0:
            break
        elif opcion == 1:
            if_inventario_pulperia()
        elif opcion == 2:
            if_promocion_tienda()
        elif opcion == 3:
            if_meta_ventas()
        elif opcion == 4:
            if_entrega_comedor()
        elif opcion == 5:
            if_peso_productos()

        pausa()


def menu_if_anidados():
    while True:
        print("\n" + "=" * 60)
        print("                 EJERCICIOS CON IF ANIDADOS")
        print("=" * 60)
        print("1. Credito interno")
        print("2. Servicio de entrega")
        print("3. Clasificacion de cafe")
        print("4. Reserva de hospedaje")
        print("5. Venta de ferreteria")
        print("0. Volver al menu principal")

        opcion = leer_entero("Seleccione una opcion: ", 0, 5)

        if opcion == 0:
            break
        elif opcion == 1:
            nested_credito_interno()
        elif opcion == 2:
            nested_servicio_entrega()
        elif opcion == 3:
            nested_clasificacion_cafe()
        elif opcion == 4:
            nested_reserva_hospedaje()
        elif opcion == 5:
            nested_venta_ferreteria()

        pausa()


def menu_for():
    while True:
        print("\n" + "=" * 60)
        print("                     EJERCICIOS CON FOR")
        print("=" * 60)
        print("1. Ventas de un minisuper")
        print("2. Recepcion de cafe")
        print("3. Revision de inventario")
        print("4. Produccion de pan")
        print("5. Evaluacion del servicio")
        print("0. Volver al menu principal")

        opcion = leer_entero("Seleccione una opcion: ", 0, 5)

        if opcion == 0:
            break
        elif opcion == 1:
            for_ventas_minisuper()
        elif opcion == 2:
            for_recepcion_cafe()
        elif opcion == 3:
            for_revision_inventario()
        elif opcion == 4:
            for_produccion_pan()
        elif opcion == 5:
            for_evaluacion_servicio()

        pausa()


def menu_while():
    while True:
        print("\n" + "=" * 60)
        print("                    EJERCICIOS CON WHILE")
        print("=" * 60)
        print("1. Cierre de caja")
        print("2. Acceso al sistema")
        print("3. Cantidad de un pedido")
        print("4. Combustible de reparto")
        print("5. Reposicion de existencias")
        print("0. Volver al menu principal")

        opcion = leer_entero("Seleccione una opcion: ", 0, 5)

        if opcion == 0:
            break
        elif opcion == 1:
            while_cierre_caja()
        elif opcion == 2:
            while_acceso_sistema()
        elif opcion == 3:
            while_cantidad_pedido()
        elif opcion == 4:
            while_combustible_reparto()
        elif opcion == 5:
            while_reposicion_existencias()

        pausa()


# ============================================================
# MENU PRINCIPAL
# ============================================================


def menu_principal():
    while True:
        print("\n" + "=" * 60)
        print("         GUIA PRACTICA - SENTENCIAS DE CONTROL")
        print("=" * 60)
        print("1. Ejercicios con if")
        print("2. Ejercicios con if anidados")
        print("3. Ejercicios con for")
        print("4. Ejercicios con while")
        print("0. Salir")

        opcion = leer_entero("Seleccione una opcion: ", 0, 4)

        if opcion == 0:
            print("\nPrograma finalizado")
            break
        elif opcion == 1:
            menu_if()
        elif opcion == 2:
            menu_if_anidados()
        elif opcion == 3:
            menu_for()
        elif opcion == 4:
            menu_while()


menu_principal()
