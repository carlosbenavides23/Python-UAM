import random
import time


def generar_con_while(cantidad):
    suma = 0
    contador = 0

    inicio = time.perf_counter_ns()

    while contador < cantidad:
        numero = random.randint(0, 100)
        suma += numero
        contador += 1

    fin = time.perf_counter_ns()

    promedio = suma / cantidad
    tiempo = fin - inicio

    return promedio, tiempo


def generar_con_for(cantidad):
    suma = 0

    inicio = time.perf_counter_ns()

    for _ in range(cantidad):
        numero = random.randint(0, 100)
        suma += numero

    fin = time.perf_counter_ns()

    promedio = suma / cantidad
    tiempo = fin - inicio

    return promedio, tiempo


while True:
    print("\n" + "=" * 48)
    print("      GENERADOR DE NÚMEROS ALEATORIOS")
    print("=" * 48)
    print("1. Generar una cantidad aleatoria")
    print("2. Ingresar una cantidad específica")
    print("3. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        cantidad = random.randint(100, 1000)
        print(f"\nCantidad generada automáticamente: {cantidad}")

    elif opcion == "2":
        while True:
            try:
                cantidad = int(input("\nCantidad de números a generar: "))

                if cantidad > 0:
                    break

                print("La cantidad debe ser mayor que 0.")

            except ValueError:
                print("Ingrese un número entero válido.")

    elif opcion == "3":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nSeleccione una opción válida.")
        continue

    promedio_while, tiempo_while = generar_con_while(cantidad)
    promedio_for, tiempo_for = generar_con_for(cantidad)

    print("\n" + "=" * 48)
    print("                   RESULTADOS")
    print("=" * 48)

    print("\n[ WHILE ]")
    print(f"Cantidad : {cantidad}")
    print(f"Promedio : {promedio_while:.2f}")
    print(f"Tiempo   : {tiempo_while:,} ns")

    print("\n[ FOR ]")
    print(f"Cantidad : {cantidad}")
    print(f"Promedio : {promedio_for:.2f}")
    print(f"Tiempo   : {tiempo_for:,} ns")

    print("\n" + "=" * 48)

    input("\nPresione Enter para volver al menú...")
