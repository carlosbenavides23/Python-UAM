# Ejercicio 2: convertir una matriz de estudiantes en texto.
estudiantes = [["Carlos", 85, 90], ["Ana", 95, 88], ["Luis", 70, 75]]

print("Matriz original:")
for fila in estudiantes:
    print(fila)

texto = "Nombre | Nota 1 | Nota 2\n"
for fila in estudiantes:
    texto += f"{fila[0]} | {fila[1]} | {fila[2]}\n"

print("\nTexto generado:")
print(texto)
