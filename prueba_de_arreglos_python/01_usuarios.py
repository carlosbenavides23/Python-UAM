# Convertir una lista de usuarios en cadena y recuperar la lista.


def guardar_como_cadena(usuarios):
    # Una coma dentro de un usuario haria ambigua la recuperacion
    for usuario in usuarios:
        if not isinstance(usuario, str) or not usuario.strip() or "," in usuario:
            raise ValueError("Cada usuario debe ser texto no vacio y sin comas.")
    return ", ".join(usuarios)


def recuperar_desde_cadena(cadena):
    if not isinstance(cadena, str):
        raise ValueError("La cadena debe ser texto.")
    if not cadena.strip():
        return []
    usuarios = cadena.split(", ")
    guardar_como_cadena(usuarios)  # Valida los elementos recuperados
    return usuarios


def main():
    usuarios = ["admin", "jrobles", "mlopez"]
    print("Lista original:", usuarios)
    cadena = guardar_como_cadena(usuarios)
    print("Cadena:", cadena)
    print("Lista recuperada:", recuperar_desde_cadena(cadena))


if __name__ == "__main__":
    main()
