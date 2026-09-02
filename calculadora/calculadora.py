import dividir
import multiplicar
import potenciar
import restar
import sumar


def main():
    operaciones = {
        "1": ("Sumar", sumar.sumar),
        "2": ("Restar", restar.restar),
        "3": ("Multiplicar", multiplicar.multiplicar),
        "4": ("Dividir", dividir.dividir),
        "5": ("Potenciar", potenciar.potenciar),
    }

    while True:
        print("\n--- CALCULADORA ---")
        for numero, (nombre, _) in operaciones.items():
            print(f"{numero}. {nombre}")
        print("0. Salir")

        opcion = input("Elige una opcion: ")
        if opcion == "0":
            print("Hasta luego.")
            break

        operacion = operaciones.get(opcion)
        if operacion is None:
            print("Opcion no valida.")
            continue

        try:
            resultado = operacion[1]()
            print(f"Resultado: {resultado}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
    input("Presiona Enter para salir...")
