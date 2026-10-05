# Ejercicio 10: máximo, mínimo y todas sus posiciones.
# Sin max(), min() ni otras funciones para calcular los extremos.
matriz = [[15, 80, 15], [80, 45, 60], [22, 15, 80]]

print("Matriz:")
for fila in matriz:
    print(fila)

encontrado = False
f = 0
for fila in matriz:
    c = 0
    for valor in fila:
        if not encontrado:
            maximo = valor
            minimo = valor
            posiciones_maximo = [[f, c]]
            posiciones_minimo = [[f, c]]
            encontrado = True
        else:
            if valor > maximo:
                maximo = valor
                posiciones_maximo = [[f, c]]
            elif valor == maximo:
                posiciones_maximo.append([f, c])
            if valor < minimo:
                minimo = valor
                posiciones_minimo = [[f, c]]
            elif valor == minimo:
                posiciones_minimo.append([f, c])
        c += 1
    f += 1

if encontrado:
    print("Máximo:", maximo, "Posiciones:", posiciones_maximo)
    print("Mínimo:", minimo, "Posiciones:", posiciones_minimo)
else:
    print("La matriz no contiene números.")
