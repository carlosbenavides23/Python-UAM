# --------------------------------------------------
# EJERCICIO 1 - Conversion de edad
# --------------------------------------------------


def ejercicio_1():
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Debe ingresar un número entero")
    else:
        print("Edad registrada:", edad)


# --------------------------------------------------
# EJERCICIO 2 - Division segura
# --------------------------------------------------


def ejercicio_2():
    try:
        dividendo = float(input("Dividendo: "))
        divisor = float(input("Divisor: "))
        resultado = dividendo / divisor

    except ValueError:
        print("Error: debe ingresar valores numéricos")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")

    else:
        print("Resultado:", resultado)


# --------------------------------------------------
# EJERCICIO 3 - Acceso a una lista
# --------------------------------------------------


def ejercicio_3():
    nombres = ["Ana", "Luis", "Marta"]

    try:
        posicion = int(input("Posición: "))
        print("Nombre:", nombres[posicion])

    except ValueError:
        print("La posición debe ser un número entero")

    except IndexError:
        print("La posición indicada no existe")


# --------------------------------------------------
# EJERCICIO 4 - Consulta de cliente
# --------------------------------------------------


def ejercicio_4():
    cliente = {"nombre": "María", "telefono": "8888-8888"}

    clave = input("Dato a consultar: ")

    try:
        print(cliente[clave])

    except KeyError:
        print("Ese dato no está registrado")


# --------------------------------------------------
# EJERCICIO 5 - Cierre garantizado
# --------------------------------------------------


def ejercicio_5():
    try:
        numero = int(input("Número: "))
        print("Resultado:", 100 / numero)

    except ValueError:
        print("Debe ingresar un número entero")

    except ZeroDivisionError:
        print("No se puede dividir entre cero")

    finally:
        print("Proceso finalizado")


# --------------------------------------------------
# EJERCICIO 6 - Precio de un producto
# --------------------------------------------------


def ejercicio_6():
    try:
        precio = float(input("Precio del producto: "))

    except ValueError:
        print("Error: debe ingresar un precio numérico")

    else:
        print("Precio registrado:", precio)


# --------------------------------------------------
# EJERCICIO 7 - Cantidad de productos
# --------------------------------------------------


def ejercicio_7():
    try:
        cantidad = int(input("Cantidad de productos: "))

    except ValueError:
        print("Error: la cantidad debe ser un número entero")

    else:
        print("Cantidad registrada:", cantidad)


# --------------------------------------------------
# EJERCICIO 8 - Calificacion
# --------------------------------------------------


def ejercicio_8():
    try:
        calificacion = float(input("Calificación: "))

    except ValueError:
        print("Error: debe ingresar una calificación numérica")

    else:
        if 0 <= calificacion <= 100:
            print("Calificación válida:", calificacion)
        else:
            print("La calificación debe estar entre 0 y 100")


# --------------------------------------------------
# EJERCICIO 9 - Edad para registro
# --------------------------------------------------


def ejercicio_9():
    try:
        edad = int(input("Edad: "))

    except ValueError:
        print("Error: la edad debe ser un número entero")

    else:
        if 0 <= edad <= 120:
            print("Edad registrada:", edad)
        else:
            print("La edad ingresada no es válida")


# --------------------------------------------------
# EJERCICIO 10 - Tres entradas consecutivas
# --------------------------------------------------


def ejercicio_10():
    nombre = input("Nombre: ")

    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Error: la edad debe ser un número entero")
        return

    try:
        salario = float(input("Salario: "))
    except ValueError:
        print("Error: el salario debe ser un número")
        return

    print("\nDatos registrados:")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Salario:", salario)


# --------------------------------------------------
# EJERCICIO 11 - Promedio de ventas
# --------------------------------------------------


def ejercicio_11():
    try:
        venta1 = float(input("Venta 1: "))
        venta2 = float(input("Venta 2: "))
        venta3 = float(input("Venta 3: "))

        ventas = [venta1, venta2, venta3]

        promedio = sum(ventas) / len(ventas)

    except ValueError:
        print("Error: todas las ventas deben ser numéricas")

    except ZeroDivisionError:
        print("Error: no existen ventas para calcular el promedio")

    else:
        print("Promedio de ventas:", promedio)


# --------------------------------------------------
# EJERCICIO 12 - Descuento proporcional
# --------------------------------------------------


def ejercicio_12():
    try:
        monto = float(input("Monto: "))
        base = float(input("Base: "))

        porcentaje = (monto / base) * 100

    except ValueError:
        print("Error: debe ingresar valores numéricos")

    except ZeroDivisionError:
        print("Error: la base no puede ser cero")

    else:
        print("Porcentaje:", porcentaje, "%")


# --------------------------------------------------
# EJERCICIO 13 - Conversion de moneda
# --------------------------------------------------


def ejercicio_13():
    try:
        monto = float(input("Monto: "))
        tasa = float(input("Tasa de cambio: "))

        equivalente = monto * tasa

    except ValueError:
        print("Error: el monto y la tasa deben ser numéricos")

    else:
        print("Monto convertido:", equivalente)


# --------------------------------------------------
# EJERCICIO 14 - Tipos incompatibles
# --------------------------------------------------


def ejercicio_14():
    texto = "10"
    numero = 5

    print("Primero se intentará sumar una cadena y un número")

    try:
        resultado = texto + numero

    except TypeError:
        print("Se produjo TypeError")
        print("La cadena '10' y el número 5 son tipos incompatibles")
        print("Se corregirá convirtiendo la cadena a entero")

        resultado = int(texto) + numero

        print("Resultado corregido:", resultado)


# --------------------------------------------------
# EJERCICIO 15 - Calculo de comision
# --------------------------------------------------


def ejercicio_15():
    try:
        ventas = float(input("Total de ventas: "))
        porcentaje = float(input("Porcentaje de comisión: "))

        comision = ventas * porcentaje / 100

    except ValueError:
        # Se espera ValueError si la entrada no puede convertirse a float
        print("Error: ventas y porcentaje deben ser valores numéricos")

    else:
        print("Comisión:", comision)


# --------------------------------------------------
# EJERCICIO 16 - Indice de inventario
# --------------------------------------------------


def ejercicio_16():
    productos = ["Laptop", "Teclado", "Mouse", "Monitor", "Impresora"]

    print("\nInventario:")

    for indice in range(len(productos)):
        print(indice, "-", productos[indice])

    try:
        posicion = int(input("Posición a consultar: "))
        print("Producto:", productos[posicion])

    except ValueError:
        print("Error: debe ingresar una posición numérica")

    except IndexError:
        print("Error: esa posición no existe en el inventario")


# --------------------------------------------------
# EJERCICIO 17 - Diccionario de empleados
# --------------------------------------------------


def ejercicio_17():
    empleado = {"nombre": "Carlos", "cargo": "Programador", "salario": 15000}

    clave = input("Dato del empleado a consultar: ")

    try:
        print("Resultado:", empleado[clave])

    except KeyError:
        print("Error: esa información no existe")

    print("\nAlternativa utilizando get():")

    resultado = empleado.get(clave)

    if resultado is None:
        print("La clave tampoco fue encontrada con get()")
    else:
        print(resultado)


# --------------------------------------------------
# EJERCICIO 18 - Menu de opciones
# --------------------------------------------------


def ejercicio_18():
    print("\nMENÚ")
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("3. Finalizar")

    try:
        opcion = int(input("Seleccione una opción: "))

    except ValueError:
        print("Error: debe ingresar una opción numérica")

    else:
        if opcion == 1:
            print("Hola")

        elif opcion == 2:
            print("La opción fue ingresada correctamente")

        elif opcion == 3:
            print("Finalizando...")

        else:
            print("La opción no existe")


# --------------------------------------------------
# EJERCICIO 19 - Archivo de reportes
# --------------------------------------------------


def ejercicio_19():
    try:
        archivo = open("reportes.txt", "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()

    except FileNotFoundError:
        print("Error: no se encontró el archivo reportes.txt")

    else:
        print("\nContenido del archivo:")
        print(contenido)

    finally:
        print("La operación con el archivo terminó")


# --------------------------------------------------
# EJERCICIO 20 - Importacion controlada
# --------------------------------------------------


def ejercicio_20():
    try:
        import modulo_que_no_existe

    except ModuleNotFoundError:
        print("Error: Python no encontró el módulo")
        print("Revise:")
        print("- El nombre del módulo")
        print("- Si el módulo está instalado")
        print("- El entorno de Python utilizado")


# --------------------------------------------------
# MENU PRINCIPAL
# --------------------------------------------------


def mostrar_menu():
    print("\n" + "=" * 55)
    print("      EXCEPCIONES Y MANEJO DE ERRORES EN PYTHON")
    print("=" * 55)

    print(" 1. Conversión de edad")
    print(" 2. División segura")
    print(" 3. Acceso a una lista")
    print(" 4. Consulta de cliente")
    print(" 5. Cierre garantizado")
    print(" 6. Precio de un producto")
    print(" 7. Cantidad de productos")
    print(" 8. Calificación")
    print(" 9. Edad para registro")
    print("10. Tres entradas consecutivas")
    print("11. Promedio de ventas")
    print("12. Descuento proporcional")
    print("13. Conversión de moneda")
    print("14. Tipos incompatibles")
    print("15. Cálculo de comisión")
    print("16. Índice de inventario")
    print("17. Diccionario de empleados")
    print("18. Menú de opciones")
    print("19. Archivo de reportes")
    print("20. Importación controlada")
    print(" 0. Salir")

    print("=" * 55)


def main():
    ejercicios = {
        1: ejercicio_1,
        2: ejercicio_2,
        3: ejercicio_3,
        4: ejercicio_4,
        5: ejercicio_5,
        6: ejercicio_6,
        7: ejercicio_7,
        8: ejercicio_8,
        9: ejercicio_9,
        10: ejercicio_10,
        11: ejercicio_11,
        12: ejercicio_12,
        13: ejercicio_13,
        14: ejercicio_14,
        15: ejercicio_15,
        16: ejercicio_16,
        17: ejercicio_17,
        18: ejercicio_18,
        19: ejercicio_19,
        20: ejercicio_20,
    }

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

        except ValueError:
            print("Error: debe ingresar un número entero")
            continue

        if opcion == 0:
            print("Programa finalizado")
            break

        if opcion in ejercicios:
            print()
            ejercicios[opcion]()
        else:
            print("La opción seleccionada no existe")

        input("\nPresione Enter para continuar...")


main()


# --------------------------------------------------
# RESPUESTAS DE COMPRENSION
# --------------------------------------------------

# 1. Que es una excepcion y en que se diferencia de un error de sintaxis
#
# Una excepcion es un problema que ocurre durante la ejecucion del programa
# aunque el codigo sea sintacticamente valido
#
# Un error de sintaxis ocurre cuando el codigo no cumple las reglas del lenguaje
# y Python no puede interpretarlo correctamente


# 2. Que excepciones puedo reconocer en situaciones habituales
#
# ValueError ocurre cuando un valor no puede convertirse o utilizarse
# de la forma esperada
#
# TypeError ocurre cuando una operacion utiliza tipos incompatibles
#
# ZeroDivisionError ocurre cuando se intenta dividir entre cero
#
# IndexError ocurre cuando se intenta acceder a una posicion inexistente
# de una lista
#
# KeyError ocurre cuando se intenta acceder a una clave inexistente
# de un diccionario


# 3. Para que sirven try, except, else y finally
#
# try contiene el codigo que puede producir una excepcion
#
# except captura una excepcion especifica y permite controlar
# lo que debe hacer el programa cuando ocurre
#
# else se ejecuta solamente cuando el bloque try termina sin excepciones
#
# finally se ejecuta siempre haya ocurrido o no una excepcion


# 4. Que bloque utiliza Python para capturar excepciones
#
# Python utiliza except
#
# Python no utiliza catch para capturar excepciones


# --------------------------------------------------
# EXPLICACION DE UNA SOLUCION
# --------------------------------------------------
# --------------------------------------------------

# En el ejercicio de division segura pueden ocurrir dos excepciones diferentes
# ValueError puede ocurrir cuando una entrada no puede convertirse a numero
#
# TypeError puede ocurrir cuando se intenta realizar una operacion con tipos incompatibles
#
# ZeroDivisionError puede ocurrir cuando el divisor es cero
#
# Por eso se utilizan dos bloques except diferentes
#
# El bloque else muestra el resultado solamente cuando no ocurre ninguna excepcion
