# Ejercicio 5: temperaturas de 7 días y promedio semanal.
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [
    [24, 31, 26], [25, 32, 27], [24, 30, 25], [23, 29, 24],
    [25, 33, 27], [26, 34, 28], [24, 31, 26]
]

print("Matriz de temperaturas:")
for fila in temperaturas:
    print(fila)

total = 0
cantidad = 0
reporte = f"{'Día':<12} {'Mañana':>8} {'Tarde':>8} {'Noche':>8} {'Promedio':>10}\n"
reporte += "-" * 50 + "\n"

for f in range(len(temperaturas)):
    suma_dia = 0
    for temperatura in temperaturas[f]:
        suma_dia += temperatura
        total += temperatura
        cantidad += 1
    promedio_dia = suma_dia / 3
    reporte += (f"{dias[f]:<12} {temperaturas[f][0]:>8.2f} "
                f"{temperaturas[f][1]:>8.2f} {temperaturas[f][2]:>8.2f} "
                f"{promedio_dia:>10.2f}\n")

if cantidad > 0:
    reporte += f"Promedio semanal: {total / cantidad:.2f} °C\n"
else:
    reporte += "No hay temperaturas registradas.\n"

print("\n" + reporte)
