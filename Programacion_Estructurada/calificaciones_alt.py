import time


while True:
    print("=" * 50)
    print("         PROCESAMIENTO DE CALIFICACIONES")
    print("=" * 50)

    # Validar cantidad de estudiantes
    while True:
        try:
            cantidad = int(input("\nCantidad de estudiantes: "))

            if cantidad > 0:
                break

            print("La cantidad debe ser mayor que 0.")

        except ValueError:
            print("Ingrese un número entero válido.")

    suma_notas = 0
    aprobados = 0
    reprobados = 0

    # Inicio de la medicion del tiempo CPU
    inicio_cpu = time.process_time()

    # Se usa for porque conocemos la cantidad exacta
    # de estudiantes que se deben procesar
    for estudiante in range(1, cantidad + 1):
        # Validar cada calificacion
        while True:
            try:
                nota = float(input(f"\nCalificación del estudiante {estudiante}: "))

                if 0 <= nota <= 100:
                    break

                print("La calificación debe estar entre 0 y 100.")

            except ValueError:
                print("Ingrese una calificación válida.")

        # Acumulador de notas
        suma_notas += nota

        # Contadores de aprobados y reprobados
        if nota >= 70:
            aprobados += 1
        else:
            reprobados += 1

    # Fin de la medición del tiempo CPU
    fin_cpu = time.process_time()
    tiempo_cpu = fin_cpu - inicio_cpu

    promedio = suma_notas / cantidad

    # Informe final.
    print("\n" + "=" * 50)
    print("                INFORME DEL GRUPO")
    print("=" * 50)

    print(f"Cantidad de estudiantes : {cantidad}")
    print(f"Promedio del grupo       : {promedio:.2f}")
    print(f"Aprobados                : {aprobados}")
    print(f"Reprobados               : {reprobados}")
    print(f"Tiempo CPU utilizado     : {tiempo_cpu:.6f} segundos")

    print("=" * 50)

    while True:
        repetir = input("\n¿Desea procesar otro grupo? (s/n): ").lower()

        if repetir == "s" or repetir == "n":
            break

        print("Ingrese solamente 's' o 'n'.")

    if repetir == "n":
        print("\nPrograma finalizado.")
        break

    print()
