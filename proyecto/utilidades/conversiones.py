# Funciones para convertir unidades comunes


def convertir_longitud(valor: float, desde: str, hacia: str) -> float:
	# Convierte longitudes entre mm, cm, m y km
	factores = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
	return _convertir(valor, desde, hacia, factores)


def convertir_masa(valor: float, desde: str, hacia: str) -> float:
	# Convierte masas entre mg, g, kg y t
	factores = {"mg": 0.000001, "g": 0.001, "kg": 1.0, "t": 1000.0}
	return _convertir(valor, desde, hacia, factores)


def convertir_volumen(valor: float, desde: str, hacia: str) -> float:
	# Convierte volúmenes entre ml, l y m3.
	factores = {"ml": 0.001, "l": 1.0, "m3": 1000.0}
	return _convertir(valor, desde, hacia, factores)


def convertir_tiempo(valor: float, desde: str, hacia: str) -> float:
	# Convierte tiempo entre s, min, h y d
	factores = {"s": 1.0, "min": 60.0, "h": 3600.0, "d": 86400.0}
	return _convertir(valor, desde, hacia, factores)


def convertir_temperatura(valor: float, desde: str, hacia: str) -> float:
	# Convierte temperaturas entre Celsius, Fahrenheit y Kelvin
	unidades = {"c", "f", "k"}
	desde, hacia = desde.lower(), hacia.lower()
	if desde not in unidades or hacia not in unidades:
		raise ValueError("Unidades de temperatura no válidas: usa c, f o k")

	if desde == "c":
		celsius = valor
	elif desde == "f":
		celsius = (valor - 32) * 5 / 9
	else:
		celsius = valor - 273.15

	if hacia == "c":
		return celsius
	if hacia == "f":
		return celsius * 9 / 5 + 32
	return celsius + 273.15


def _convertir(valor: float, desde: str, hacia: str, factores: dict[str, float]) -> float:
	desde, hacia = desde.lower(), hacia.lower()
	if desde not in factores or hacia not in factores:
		disponibles = ", ".join(factores)
		raise ValueError(f"Unidades no válidas: usa {disponibles}")
	return valor * factores[desde] / factores[hacia]
