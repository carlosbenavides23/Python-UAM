# Calcular el promedio de las 3 calificaciones
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def determinar_estado(promedio):
    if promedio >= 70:
        return "Aprobó"
    else:
        return "Reprobó"


while True:
    print("=" * 55)
    print("     REGISTRO DE ESTUDIANTES Y CALIFICACIONES")
    print("=" * 55)

    # Validar cantidad de estudiantes
    while True:
        try:
            cantidad = int(input("\nCantidad de estudiantes: "))

            if cantidad > 0:
                break

            print("La cantidad debe ser mayor que 0.")

        except ValueError:
            print("Ingrese un número entero válido.")

    aprobados = 0
    reprobados = 0
    suma_promedios = 0

    # promedio_mayor se inicializa en -1 para asegurar que cualquier promedio válido lo supere
    promedio_mayor = -1
    estudiante_mayor = ""

    # Contador para controlar el registro con while
    estudiante = 1

    while estudiante <= cantidad:
        print("\n" + "-" * 55)
        print(f"ESTUDIANTE {estudiante}")
        print("-" * 55)

        while True:
            nombre = input("Nombre: ").strip()

            if nombre != "":
                break

            print("El nombre no puede estar vacío.")

        nota1 = 0
        nota2 = 0
        nota3 = 0

        # Ingresar exactamente 3 calificaciones utilizando for
        for numero_nota in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Calificación {numero_nota}: "))

                    if 0 <= nota <= 100:
                        break

                    print("La calificación debe estar entre 0 y 100.")

                except ValueError:
                    print("Ingrese una calificación válida.")

            # Guardar cada nota sin utilizar listas
            if numero_nota == 1:
                nota1 = nota

            elif numero_nota == 2:
                nota2 = nota

            else:
                nota3 = nota

        promedio = calcular_promedio(nota1, nota2, nota3)

        estado = determinar_estado(promedio)

        if estado == "Aprobó":
            aprobados += 1
        else:
            reprobados += 1

        suma_promedios += promedio

        if promedio > promedio_mayor:
            promedio_mayor = promedio
            estudiante_mayor = nombre

        print("\nResultado:")
        print(f"Nombre   : {nombre}")
        print(f"Promedio : {promedio:.2f}")
        print(f"Estado   : {estado}")

        estudiante += 1

    promedio_general = suma_promedios / cantidad

    # Informe final
    print("\n" + "=" * 55)
    print("                  INFORME DEL GRUPO")
    print("=" * 55)

    print(f"Cantidad de estudiantes : {cantidad}")
    print(f"Aprobados                : {aprobados}")
    print(f"Reprobados               : {reprobados}")
    print(f"Promedio general         : {promedio_general:.2f}")
    print(f"Mejor estudiante         : {estudiante_mayor}")
    print(f"Promedio más alto        : {promedio_mayor:.2f}")

    print("=" * 55)

    # Preguntar si se desea registrar otro grupo
    while True:
        repetir = input("\n¿Desea registrar otro grupo? (s/n): ").strip().lower()

        if repetir == "s" or repetir == "n":
            break

        print("Ingrese solamente 's' o 'n'.")

    if repetir == "n":
        print("\nPrograma finalizado.")
        break

    print()
