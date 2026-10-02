estudiantes_que_mas_odio = [
    {"nombre": "Evenyer Cochon", "notas": [10, 10, 0]},
    {"nombre": "Alex Caballo", "notas": [5, 5, 5]},
    {"nombre": "Camilo", "notas": [67, 67, 67]},
]

estudiantes_que_mas_quiero = [
    {"nombre": "Carlos Benavides", "notas": [100, 100, 100]},
    {"nombre": "Jose Rene Bonilla", "notas": [100, 100, 100]},
]

estudiantes_que_mas_odio + estudiantes_que_mas_quiero

print("Estudiantes que mas odio:")
for estudiante in estudiantes_que_mas_odio:
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Notas: {estudiante['notas']}")
    print()

print("Estudiantes que mas quiero:")
for estudiante in estudiantes_que_mas_quiero:
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Notas: {estudiante['notas']}")
    print()
