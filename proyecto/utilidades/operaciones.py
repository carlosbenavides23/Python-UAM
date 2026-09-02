# Operaciones matematicas basicas


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede calcular el módulo con cero")
    return a % b


def potencia(a, b):
    return a**b
