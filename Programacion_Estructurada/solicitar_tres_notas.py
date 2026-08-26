# solicitar tres notas
# validar 0-100
# controlar entradas no numéricas
# calcular promedio
# Utilizar finally
# Probar datos validos, limites e invalidos

# tres notas
notas = []

def nota_valida(nota):
    return 0 <= nota <= 100


# Solicitar tres notas al usuario
for i in range(3):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i + 1} (0-100): "))
            if nota_valida(nota):
                notas.append(nota)
                break
            else:
                print("Error: La nota debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número.")

# Calcular promedio
promedio = sum(notas) / len(notas)
print(f"\nPromedio de las notas: {promedio:.2f}")

# Utilizar finally
try:
    pass
finally:
    print("Proceso completado.")

