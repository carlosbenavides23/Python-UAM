# Ejercicio 4: desglosar códigos usando segmentación de cadenas.

codigos = ["FAC-2026-ISC-0001", "FCE-2025-ADM-0002"]
componentes = []

for codigo in codigos:
    codigo = codigo.upper()
    if len(codigo) != 17:
        print("Código con longitud incorrecta:", codigo)
        continue
    if codigo[3] != "-" or codigo[8] != "-" or codigo[12] != "-":
        print("Código con separadores incorrectos:", codigo)
        continue

    facultad = codigo[0:3]
    anio = codigo[4:8]
    carrera = codigo[9:12]
    correlativo = codigo[13:17]

    if not facultad.isalpha() or not carrera.isalpha():
        print("La facultad y la carrera deben contener letras:", codigo)
        continue
    if not anio.isdecimal() or not correlativo.isdecimal():
        print("El año y el correlativo deben contener dígitos:", codigo)
        continue
    if int(anio) == 0 or int(correlativo) == 0:
        print("El año y el correlativo deben ser positivos:", codigo)
        continue

    componentes.append([facultad, anio, carrera, correlativo])

print("Facultad | Año | Carrera | Correlativo")
for fila in componentes:
    print(fila)
