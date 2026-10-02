def solicitar_producto():
    while True:
        producto = input("Nombre del producto: ").strip()
        if producto:
            return producto
        print("El nombre del producto no puede estar vacio")


def solicitar_precio():
    while True:
        try:
            precio = float(input("Precio unitario en C$: "))
            if precio > 0:
                return precio
            print("El precio debe ser un numero mayor que cero.")
        except ValueError:
            print("Ingrese un precio numerico. Use punto para los decimales")


def solicitar_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                return cantidad
            print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Ingrese una cantidad entera, sin letras ni decimales")


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal):
    if subtotal >= 3000:
        descuento = subtotal * 0.08
    else:
        descuento = 0
    return descuento


def calcular_iva(subtotal, descuento):
    monto_con_descuento = subtotal - descuento
    iva = monto_con_descuento * 0.15
    return iva


def mostrar_factura(producto, subtotal, descuento, iva):
    total = subtotal - descuento + iva
    print("\n--- FACTURA DE FERRETERIA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: C$ {subtotal:.2f}")
    print(f"Descuento: C$ {descuento:.2f}")
    print(f"IVA (15%): C$ {iva:.2f}")
    print(f"Total: C$ {total:.2f}")


def main():
    producto = solicitar_producto()
    precio = solicitar_precio()
    cantidad = solicitar_cantidad()
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    iva = calcular_iva(subtotal, descuento)
    mostrar_factura(producto, subtotal, descuento, iva)


# sin if name, no se ejecuta el main, solo se ejecuta si se llama directamente al archivo
if __name__ == "__main__":
    main()
