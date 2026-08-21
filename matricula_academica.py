# Programa de comprobante de matricula
# Se solicita entrada: nombre del estudiante, carrera,
# cantidad de asignaturas (int) y costo unitario de la asignatura (float)
# Procesamiento: Calcular el costo de la matricula (cantidad de asignaturas * costo unitario)
# Salida: Presentar un comprobante odernado usando f-strings y mostrando
# el total a pagar con dos decimales
# validacion de cada dato

# ENTRADA
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
while not nombre_estudiante.replace(" ", "").isalpha():
    print("Por favor, ingrese un nombre válido (solo letras y espacios).")
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")

carrera = input("Ingrese la carrera: ")
while not carrera.replace(" ", "").isalpha():
    print("Por favor, ingrese una carrera válida (solo letras y espacios).")
    carrera = input("Ingrese la carrera: ")

cantidad_asignaturas = input("Ingrese la cantidad de asignaturas: ")
while not cantidad_asignaturas.isdigit():
    print("Por favor, ingrese un número válido para la cantidad de asignaturas.")
    cantidad_asignaturas = input("Ingrese la cantidad de asignaturas: ")

costo_unitario = input("Ingrese el costo unitario de la asignatura: ")
while True:
    if costo_unitario.startswith("$"):
        costo_unitario = costo_unitario[1:]
    elif costo_unitario.startswith("C$"):
        costo_unitario = costo_unitario[2:]
    try:
        costo_unitario = float(costo_unitario)
        break
    except ValueError:
        print("Por favor, ingrese un número válido para el costo unitario.")
        costo_unitario = input("Ingrese el costo unitario de la asignatura: ")

# PROCESAMIENTO
costo_matricula = int(cantidad_asignaturas) * costo_unitario

# SALIDA
print("\nComprobante de Matrícula")
print(f"Nombre del estudiante: {nombre_estudiante}")
print(f"Carrera: {carrera}")
print(f"Cantidad de asignaturas: {cantidad_asignaturas}")
print(f"Costo unitario de la asignatura: ${costo_unitario:.2f}")
print(f"Total a pagar: ${costo_matricula:.2f}")
