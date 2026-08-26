print("=" * 50)
print("         PROCESAMIENTO DE CALIFICACIONES")
print("=" * 50)


# Se usa while para validar la cantidad de estudiantes,
# ya que no sabemos cuántos intentos necesitara el usuario
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


# Se usa for porque conocemos previamente
# la cantidad exacta de estudiantes a procesar
for estudiante in range(1, cantidad + 1):
    # Se usa while para validar cada calificacion
    # La nota debe estar dentro del rango de 0 a 100
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

    # Clasificacion del estudiante
    # Se aprueba con una nota minima de 70
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1


promedio = suma_notas / cantidad


# Informe final
print("\n" + "=" * 50)
print("                INFORME DEL GRUPO")
print("=" * 50)

print(f"Cantidad de estudiantes : {cantidad}")
print(f"Promedio del grupo       : {promedio:.2f}")
print(f"Aprobados                : {aprobados}")
print(f"Reprobados               : {reprobados}")

print("=" * 50)
