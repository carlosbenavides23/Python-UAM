# Ejercicio 8: registrar estudiantes, calcular promedio y estado.
from math import isfinite


def leer_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if isfinite(nota) and 0 <= nota <= 100:
                return nota
            print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Ingrese una nota numérica.")


def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def determinar_estado(promedio):
    if promedio >= 70:
        return "Aprobado"
    return "Reprobado"


def registrar_estudiante(grupo):
    identificador = input("ID del estudiante: ").strip()
    if identificador == "":
        print("El ID no puede estar vacío.")
        return
    for fila in grupo:
        if fila[0] == identificador:
            print("Ese ID ya está registrado.")
            return
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    nota1 = leer_nota("Nota 1: ")
    nota2 = leer_nota("Nota 2: ")
    nota3 = leer_nota("Nota 3: ")
    promedio = calcular_promedio(nota1, nota2, nota3)
    estado = determinar_estado(promedio)
    grupo.append([identificador, nombre, nota1, nota2, nota3, promedio, estado])
    print(f"Promedio: {promedio:.2f} - Estado: {estado}")


grupo = []
while True:
    opcion = input("\n1. Registrar estudiante  0. Terminar: ").strip()
    if opcion == "0":
        break
    elif opcion == "1":
        registrar_estudiante(grupo)
    else:
        print("Seleccione 1 o 0.")

print("\nExpediente del grupo:")
if not grupo:
    print("No hay estudiantes registrados.")
for fila in grupo:
    print(f"{fila[0]} | {fila[1]} | {fila[2]:.2f} | {fila[3]:.2f} | "
          f"{fila[4]:.2f} | {fila[5]:.2f} | {fila[6]}")
