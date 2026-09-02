# Operaciones basicas de geometria plana y espacial

from math import pi, sqrt


def _positivo(valor: float, nombre: str = "valor") -> float:
    # Valida y devuelve un valor positivo
    if valor <= 0:
        raise ValueError(f"{nombre} debe ser positivo")
    return valor


def area_circulo(radio: float) -> float:
    radio = _positivo(radio, "El radio")
    return pi * radio**2


def perimetro_circulo(radio: float) -> float:
    radio = _positivo(radio, "El radio")
    return 2 * pi * radio


def area_rectangulo(base: float, altura: float) -> float:
    return _positivo(base, "La base") * _positivo(altura, "La altura")


def perimetro_rectangulo(base: float, altura: float) -> float:
    base = _positivo(base, "La base")
    altura = _positivo(altura, "La altura")
    return 2 * (base + altura)


def area_triangulo(base: float, altura: float) -> float:
    return _positivo(base, "La base") * _positivo(altura, "La altura") / 2


def perimetro_triangulo(lado_a: float, lado_b: float, lado_c: float) -> float:
    lados = [
        _positivo(lado_a, "El lado A"),
        _positivo(lado_b, "El lado B"),
        _positivo(lado_c, "El lado C"),
    ]
    if 2 * max(lados) >= sum(lados):
        raise ValueError("Los lados no forman un triángulo válido")
    return sum(lados)


def distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def volumen_cubo(lado: float) -> float:
    return _positivo(lado, "El lado") ** 3


def volumen_esfera(radio: float) -> float:
    radio = _positivo(radio, "El radio")
    return 4 * pi * radio**3 / 3


def volumen_cilindro(radio: float, altura: float) -> float:
    return area_circulo(radio) * _positivo(altura, "La altura")
