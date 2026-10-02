"""Encuentra las temperaturas máxima y mínima de varias ciudades."""

# Cada fila representa una ciudad y cada columna un día de la semana.
ciudades = ["Managua", "León", "Matagalpa"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
temperaturas = [
    [32, 34, 31, 33, 35],
    [33, 35, 34, 36, 32],
    [24, 25, 23, 26, 24],
]

# Inicializamos ambos extremos con el primer dato de la matriz.
temperatura_maxima = temperaturas[0][0]
temperatura_minima = temperaturas[0][0]
ubicacion_maxima = (0, 0)
ubicacion_minima = (0, 0)

# Recorremos cada celda y actualizamos el extremo y su ubicación si corresponde.
for fila in range(len(temperaturas)):
    for columna in range(len(temperaturas[fila])):
        temperatura_actual = temperaturas[fila][columna]

        if temperatura_actual > temperatura_maxima:
            temperatura_maxima = temperatura_actual
            ubicacion_maxima = (fila, columna)

        if temperatura_actual < temperatura_minima:
            temperatura_minima = temperatura_actual
            ubicacion_minima = (fila, columna)

fila_maxima, columna_maxima = ubicacion_maxima
fila_minima, columna_minima = ubicacion_minima

print("Temperaturas registradas (°C):")
for indice, ciudad in enumerate(ciudades):
    print(f"{ciudad}: {temperaturas[indice]}")

print(
    f"\nMáxima: {temperatura_maxima} °C en {ciudades[fila_maxima]}, "
    f"{dias[columna_maxima]}"
)
print(
    f"Mínima: {temperatura_minima} °C en {ciudades[fila_minima]}, "
    f"{dias[columna_minima]}"
)
