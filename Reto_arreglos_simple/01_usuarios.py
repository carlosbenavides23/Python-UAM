# Ejercicio 1: convertir una lista en cadena y recuperarla.
def guardar_como_cadena(usuarios):
    return ", ".join(usuarios)


def recuperar_usuarios(cadena):
    if cadena == "":
        return []
    return cadena.split(", ")


usuarios = ["admin", "jrobles", "mlopez"]
cadena = guardar_como_cadena(usuarios)
print("Lista:", usuarios)
print("Cadena:", cadena)
print("Lista recuperada:", recuperar_usuarios(cadena))
