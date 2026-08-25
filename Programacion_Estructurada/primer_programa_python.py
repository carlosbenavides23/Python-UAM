# El programa consiste en seleccionar 21 opciones de un menu que contiene
# miniprogramas de diferentes tipos, cada uno con su propia funcionalidad
# y validaciones.
#
# En caso posible, usar funciones reutilizables para evitar repetir codigo
# y mantener el programa organizado.
#
# Todos los miniprogramas deben tener sus validaciones de entrada y salida
# y mostrar los resultados de manera clara y ordenada.


# Funcion generica para leer un numero con validacion
def leer_numero(mensaje, entero=False):
    while True:
        entrada = input(mensaje)

        try:
            if entero:
                numero = int(entrada)
            else:
                numero = float(entrada)

            return numero

        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")


# Funcion reutilizable para mantener el resultado en pantalla
def pausar():
    input("\nPresione Enter para volver al menú...")


while True:
    print("\n=== MENÚ DE EJERCICIOS ===")
    print("1. Sumar dos números")
    print("2. Calcular el cuadrado de un número")
    print("3. Área de un rectángulo")
    print("4. Promedio de tres notas")
    print("5. Determinar par o impar")
    print("6. Determinar mayoría de edad")
    print("7. Mayor de tres números")
    print("8. Menor de tres números")
    print("9. Convertir horas a minutos")
    print("10. Calcular salario semanal")
    print("11. Área de un triángulo")
    print("12. Positivo, negativo o cero")
    print("13. Total de tres productos")
    print("14. Promedio de cuatro números")
    print("15. Mayor de tres números distintos")
    print("16. Tabla de multiplicar")
    print("17. Suma de los primeros 10 naturales")
    print("18. Determinar múltiplo de 5")
    print("19. Perímetro de un cuadrado")
    print("20. Clasificar por edad")
    print("0. Salir")

    opcion = leer_numero("\nSeleccione una opción: ", entero=True)

    if opcion == 0:
        print("Programa finalizado.")
        break

    if opcion < 1 or opcion > 20:
        print("Opción inválida.")
        continue

    # --------------------------------------------------
    # 1. Sumar dos números
    # --------------------------------------------------

    if opcion == 1:
        numero1 = leer_numero("Ingrese el primer número: ")
        numero2 = leer_numero("Ingrese el segundo número: ")

        suma = numero1 + numero2

        print(f"Resultado: {numero1} + {numero2} = {suma}")
        pausar()

    # --------------------------------------------------
    # 2. Cuadrado de un número
    # --------------------------------------------------

    elif opcion == 2:
        numero = leer_numero("Ingrese un número: ")

        cuadrado = numero**2

        print(f"El cuadrado de {numero} es {cuadrado}")
        pausar()

    # --------------------------------------------------
    # 3. Área de un rectángulo
    # --------------------------------------------------

    elif opcion == 3:
        base = leer_numero("Ingrese la base del rectángulo: ")
        altura = leer_numero("Ingrese la altura del rectángulo: ")

        if base <= 0 or altura <= 0:
            print("La base y la altura deben ser mayores que cero.")
            continue

        area = base * altura

        print(f"El área del rectángulo es {area}")
        pausar()

    # --------------------------------------------------
    # 4. Promedio de tres notas
    # --------------------------------------------------

    elif opcion == 4:
        nota1 = leer_numero("Ingrese la primera nota: ")
        nota2 = leer_numero("Ingrese la segunda nota: ")
        nota3 = leer_numero("Ingrese la tercera nota: ")

        if (
            nota1 < 0
            or nota1 > 100
            or nota2 < 0
            or nota2 > 100
            or nota3 < 0
            or nota3 > 100
        ):
            print("Las notas deben estar entre 0 y 100.")
            continue

        promedio = (nota1 + nota2 + nota3) / 3

        print(f"El promedio de las tres notas es {promedio:.2f}")
        pausar()

    # --------------------------------------------------
    # 5. Par o impar
    # --------------------------------------------------

    elif opcion == 5:
        numero = leer_numero("Ingrese un número: ", entero=True)

        if numero % 2 == 0:
            print(f"{numero} es un número par.")
        else:
            print(f"{numero} es un número impar.")

        pausar()

    # --------------------------------------------------
    # 6. Mayoría de edad
    # --------------------------------------------------

    elif opcion == 6:
        edad = leer_numero("Ingrese la edad de la persona: ", entero=True)

        if edad < 0:
            print("La edad no puede ser negativa.")
            continue

        if edad >= 18:
            print("La persona es mayor de edad.")
        else:
            print("La persona es menor de edad.")

        pausar()

    # --------------------------------------------------
    # 7. Mayor de tres números
    # --------------------------------------------------

    elif opcion == 7:
        numero1 = leer_numero("Ingrese el primer número: ")
        numero2 = leer_numero("Ingrese el segundo número: ")
        numero3 = leer_numero("Ingrese el tercer número: ")

        mayor = max(numero1, numero2, numero3)

        print(f"El número mayor es {mayor}.")
        pausar()

    # --------------------------------------------------
    # 8. Menor de tres números
    # --------------------------------------------------

    elif opcion == 8:
        numero1 = leer_numero("Ingrese el primer número: ")
        numero2 = leer_numero("Ingrese el segundo número: ")
        numero3 = leer_numero("Ingrese el tercer número: ")

        menor = min(numero1, numero2, numero3)

        print(f"El número menor es {menor}.")
        pausar()

    # --------------------------------------------------
    # 9. Horas a minutos
    # --------------------------------------------------

    elif opcion == 9:
        horas = leer_numero("Ingrese la cantidad de horas: ")

        if horas < 0:
            print("La cantidad de horas no puede ser negativa.")
            continue

        minutos = horas * 60

        print(f"{horas} horas equivalen a {minutos} minutos.")
        pausar()

    # --------------------------------------------------
    # 10. Salario semanal
    # --------------------------------------------------

    elif opcion == 10:
        horas_trabajadas = leer_numero("Ingrese las horas trabajadas: ")
        pago_por_hora = leer_numero("Ingrese el pago por hora: ")

        if horas_trabajadas < 0 or pago_por_hora < 0:
            print("Las horas trabajadas y el pago por hora no pueden ser negativos.")
            continue

        salario_semanal = horas_trabajadas * pago_por_hora

        print(f"El salario semanal es {salario_semanal:.2f}.")
        pausar()

    # --------------------------------------------------
    # 11. Área de un triángulo
    # --------------------------------------------------

    elif opcion == 11:
        base = leer_numero("Ingrese la base del triángulo: ")
        altura = leer_numero("Ingrese la altura del triángulo: ")

        if base <= 0 or altura <= 0:
            print("La base y la altura deben ser mayores que cero.")
            continue

        area = (base * altura) / 2

        print(f"El área del triángulo es {area}.")
        pausar()

    # --------------------------------------------------
    # 12. Positivo, negativo o cero
    # --------------------------------------------------

    elif opcion == 12:
        numero = leer_numero("Ingrese un número: ")

        if numero > 0:
            print(f"{numero} es positivo.")
        elif numero < 0:
            print(f"{numero} es negativo.")
        else:
            print("El número es cero.")

        pausar()

    # --------------------------------------------------
    # 13. Total de tres productos
    # --------------------------------------------------

    elif opcion == 13:
        producto1 = leer_numero("Ingrese el precio del primer producto: ")
        producto2 = leer_numero("Ingrese el precio del segundo producto: ")
        producto3 = leer_numero("Ingrese el precio del tercer producto: ")

        if producto1 < 0 or producto2 < 0 or producto3 < 0:
            print("Los precios no pueden ser negativos.")
            continue

        total = producto1 + producto2 + producto3

        print(f"El total a pagar es {total:.2f}.")
        pausar()

    # --------------------------------------------------
    # 14. Promedio de cuatro números
    # --------------------------------------------------

    elif opcion == 14:
        numero1 = leer_numero("Ingrese el primer número: ")
        numero2 = leer_numero("Ingrese el segundo número: ")
        numero3 = leer_numero("Ingrese el tercer número: ")
        numero4 = leer_numero("Ingrese el cuarto número: ")

        promedio = (numero1 + numero2 + numero3 + numero4) / 4

        print(f"El promedio es {promedio:.2f}.")
        pausar()

    # --------------------------------------------------
    # 15. Mayor de tres números distintos
    # --------------------------------------------------

    elif opcion == 15:
        numero1 = leer_numero("Ingrese el primer número: ")
        numero2 = leer_numero("Ingrese el segundo número: ")
        numero3 = leer_numero("Ingrese el tercer número: ")

        if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
            print("Los tres números deben ser distintos.")
            continue

        mayor = max(numero1, numero2, numero3)

        print(f"El número mayor es {mayor}.")
        pausar()

    # --------------------------------------------------
    # 16. Tabla de multiplicar
    # --------------------------------------------------

    elif opcion == 16:
        numero = leer_numero("Ingrese un número: ", entero=True)

        print(f"\nTabla de multiplicar del {numero}:")

        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")

        pausar()

    # --------------------------------------------------
    # 17. Suma de los primeros 10 naturales
    # --------------------------------------------------

    elif opcion == 17:
        suma = 0

        for i in range(1, 11):
            suma = suma + i

        print(f"La suma de los primeros 10 números naturales es {suma}.")
        pausar()

    # --------------------------------------------------
    # 18. Múltiplo de 5
    # --------------------------------------------------

    elif opcion == 18:
        numero = leer_numero("Ingrese un número: ", entero=True)

        if numero % 5 == 0:
            print(f"{numero} es múltiplo de 5.")
        else:
            print(f"{numero} no es múltiplo de 5.")

        pausar()

    # --------------------------------------------------
    # 19. Perímetro de un cuadrado
    # --------------------------------------------------

    elif opcion == 19:
        lado = leer_numero("Ingrese el lado del cuadrado: ")

        if lado <= 0:
            print("El lado debe ser mayor que cero.")
            continue

        perimetro = lado * 4

        print(f"El perímetro del cuadrado es {perimetro}.")
        pausar()

    # --------------------------------------------------
    # 20. Clasificar por edad
    # --------------------------------------------------

    elif opcion == 20:
        edad = leer_numero("Ingrese la edad de la persona: ", entero=True)

        if edad < 0:
            print("La edad no puede ser negativa.")
            continue

        if edad < 12:
            print("La persona es un niño.")
        elif edad < 18:
            print("La persona es un adolescente.")
        else:
            print("La persona es un adulto.")

        pausar()
