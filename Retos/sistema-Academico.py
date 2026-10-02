"""Sistema académico de consola.

Arquitectura: presentación (menú), lógica de aplicación (validaciones y
cálculos) y persistencia (SQLite) están separadas en funciones. SQLite ofrece
persistencia local y transacciones; guardar las notas como texto decimal evita
los errores de aproximación propios de los números float.
"""

import sqlite3
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path


BASE_DATOS = Path(__file__).with_name("sistema_academico.db")
NOTA_MINIMA = Decimal("0")
NOTA_MAXIMA = Decimal("100")


def conectar():
    """Abre la base de datos y prepara sus tablas si aún no existen."""
    conexion = sqlite3.connect(BASE_DATOS)
    conexion.execute("PRAGMA foreign_keys = ON")
    conexion.executescript(
        """
        CREATE TABLE IF NOT EXISTS estudiantes (
            id TEXT PRIMARY KEY,
            nombre TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS calificaciones (
            estudiante_id TEXT NOT NULL,
            parcial INTEGER NOT NULL CHECK (parcial > 0),
            nota TEXT NOT NULL,
            PRIMARY KEY (estudiante_id, parcial),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
        );
        """
    )
    return conexion


def leer_entero(mensaje, minimo=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"Ingrese un número igual o mayor que {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingrese un número entero válido.")


def leer_nota(mensaje="Nota (de 0 a 100): "):
    while True:
        try:
            # Se acepta coma o punto como separador decimal.
            nota = Decimal(input(mensaje).strip().replace(",", "."))
            if not nota.is_finite() or not NOTA_MINIMA <= nota <= NOTA_MAXIMA:
                print("La nota debe estar entre 0 y 100.")
                continue
            return nota
        except (InvalidOperation, ValueError):
            print("Ingrese una nota válida, por ejemplo 85.5.")


def registrar_estudiante(conexion):
    identificacion = input("Identificación del estudiante: ").strip()
    nombre = input("Nombre completo: ").strip()
    if not identificacion or not nombre:
        print("La identificación y el nombre son obligatorios.")
        return
    try:
        conexion.execute(
            "INSERT INTO estudiantes (id, nombre) VALUES (?, ?)",
            (identificacion, nombre),
        )
        conexion.commit()
        print("Estudiante registrado.")
    except sqlite3.IntegrityError:
        print("Ya existe un estudiante con esa identificación.")


def buscar_estudiante(conexion, identificacion):
    return conexion.execute(
        "SELECT id, nombre FROM estudiantes WHERE id = ?", (identificacion,)
    ).fetchone()


def ingresar_calificacion(conexion):
    identificacion = input("Identificación del estudiante: ").strip()
    estudiante = buscar_estudiante(conexion, identificacion)
    if estudiante is None:
        print("No se encontró ese estudiante. Regístrelo primero.")
        return
    parcial = leer_entero("Número de parcial: ")
    nota = leer_nota()
    conexion.execute(
        """INSERT INTO calificaciones (estudiante_id, parcial, nota)
           VALUES (?, ?, ?)
           ON CONFLICT(estudiante_id, parcial) DO UPDATE SET nota = excluded.nota""",
        (identificacion, parcial, str(nota)),
    )
    conexion.commit()
    print(f"Nota guardada para {estudiante[1]}, parcial {parcial}.")


def consultar_calificacion(conexion):
    identificacion = input("Identificación del estudiante: ").strip()
    estudiante = buscar_estudiante(conexion, identificacion)
    if estudiante is None:
        print("No se encontró ese estudiante.")
        return
    parcial = leer_entero("Número de parcial: ")
    fila = conexion.execute(
        "SELECT nota FROM calificaciones WHERE estudiante_id = ? AND parcial = ?",
        (identificacion, parcial),
    ).fetchone()
    if fila is None:
        print(f"No hay nota registrada para el parcial {parcial}.")
    else:
        print(f"{estudiante[1]} — parcial {parcial}: {fila[0]}")


def actualizar_calificacion(conexion):
    identificacion = input("Identificación del estudiante: ").strip()
    estudiante = buscar_estudiante(conexion, identificacion)
    if estudiante is None:
        print("No se encontró ese estudiante.")
        return
    parcial = leer_entero("Número de parcial cuya nota corregirá: ")
    anterior = conexion.execute(
        "SELECT nota FROM calificaciones WHERE estudiante_id = ? AND parcial = ?",
        (identificacion, parcial),
    ).fetchone()
    if anterior is None:
        print("No existe una nota para ese parcial; use la opción de ingresar nota.")
        return
    print(f"Nota actual: {anterior[0]}")
    nueva = leer_nota("Nueva nota: ")
    conexion.execute(
        "UPDATE calificaciones SET nota = ? WHERE estudiante_id = ? AND parcial = ?",
        (str(nueva), identificacion, parcial),
    )
    conexion.commit()
    print("Nota actualizada correctamente.")


def mostrar_resumen(conexion):
    identificacion = input("Identificación del estudiante: ").strip()
    estudiante = buscar_estudiante(conexion, identificacion)
    if estudiante is None:
        print("No se encontró ese estudiante.")
        return
    filas = conexion.execute(
        "SELECT parcial, nota FROM calificaciones "
        "WHERE estudiante_id = ? ORDER BY parcial",
        (identificacion,),
    ).fetchall()
    if not filas:
        print("El estudiante aún no tiene calificaciones.")
        return

    notas = [Decimal(fila[1]) for fila in filas]
    suma = sum(notas, Decimal("0"))
    promedio = Fraction(suma) / len(notas)
    print(f"\nCalificaciones de {estudiante[1]}:")
    for parcial, nota in filas:
        print(f"  Parcial {parcial}: {nota}")
    print(f"Suma total: {suma}")
    print(f"Promedio exacto: {promedio} (fracción irreducible)")


def main():
    conexion = conectar()
    opciones = {
        "1": ("Registrar estudiante", registrar_estudiante),
        "2": ("Ingresar calificación", ingresar_calificacion),
        "3": ("Consultar calificación por parcial", consultar_calificacion),
        "4": ("Corregir calificación existente", actualizar_calificacion),
        "5": ("Ver suma y promedio del estudiante", mostrar_resumen),
    }
    try:
        while True:
            print("\n=== Sistema académico ===")
            for numero, (descripcion, _) in opciones.items():
                print(f"{numero}. {descripcion}")
            print("0. Salir")
            seleccion = input("Seleccione una opción: ").strip()
            if seleccion == "0":
                print("Hasta luego.")
                break
            opcion = opciones.get(seleccion)
            if opcion is None:
                print("Opción no válida.")
            else:
                opcion[1](conexion)
    finally:
        conexion.close()


if __name__ == "__main__":
    main()
