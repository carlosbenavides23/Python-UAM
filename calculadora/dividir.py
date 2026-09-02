def dividir():
    dividendo = float(input("Dividendo: "))
    divisor = float(input("Divisor: "))
    if divisor == 0:
        raise ValueError("no se puede dividir entre cero.")
    return dividendo / divisor
