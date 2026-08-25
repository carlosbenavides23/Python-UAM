import random

# Lista de estudiantes de Programación Estructurada
estudiantes = [
    "GRETCHEN ZURIEL ABURTO CAMPOS",
    "FRANCISCO ALEJANDRO ALVAREZ GONZALEZ",
    "GUILLERMO BENJAMIN AYERDIS ROJAS",
    "CARLOS ALBERTO BENAVIDES SANDINO",
    "JOSE RENE BONILLA LINDO",
    "ALEX SANTIAGO CARBALLO JARQUIN",
    "CARLOS FERNANDO CASTILLO ROMERO",
    "RAUL ANTONIO CASTILLO ZAMORA",
    "CAMILO FRANCISCO CRUZ MONCADA",
    "LEAH MICHELLE DAVILA LACAYO",
    "WILLIAM ALEXANDER HAWKINS RAUDEZ",
    "MAURICIO ALEJANDRO LACAYO GALLEGOS",
    "SOFIA ISABELLA MARTINEZ CALERO",
    "DORIAN ZAMIR MARTINEZ LOPEZ",
    "ALEJANDRO JOSUE MONDRAGON HURTADO",
    "REYNALDO RAFAEL MONDRAGON HURTADO",
    "GYLBERT ANTONIO ORDOÑEZ GARCIA",
    "ALYSSA MARIE RODRIGUEZ MONGALO",
    "SHANE ALEJANDRO RODRIGUEZ VEGA",
    "ESMERALDA RODRIGUEZ-SALINAS RODRIGUEZ",
    "FRANCISCO ALEJANDRO SILVA MALDONADO",
    "EVENYER FERNANDO SOLORZANO LOPEZ",
    "JULISSA ALEJANDRA SOMARRIBA ARIAS",
    "MIGUEL MATIAS SUAREZ ARROLIGA",
    "JOCKSAND MATEO VALLADARES RAMIREZ",
]


print("=" * 65)
print("        ESTUDIANTES DE PROGRAMACIÓN ESTRUCTURADA")
print("=" * 65)

# Recorrer y mostrar la lista
for numero, estudiante in enumerate(estudiantes, start=1):
    print(f"{numero:2}. {estudiante}")

print("=" * 65)
print(f"Total de estudiantes: {len(estudiantes)}")
print("=" * 65)


# Seleccionar un estudiante al azar
seleccionado = random.choice(estudiantes)


print("\n" + "=" * 65)
print("              ESTUDIANTE SELECCIONADO")
print("=" * 65)

print(f"\n{seleccionado}")

print("\n" + "=" * 65)
