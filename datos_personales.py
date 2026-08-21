# Se debe solicitar nombre, edad y carrera,
# y mostrar los datos organizados
# tambien validar los datos de acuerdo a su tipo de dato

nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    print("Por favor, ingrese un nombre válido (solo letras).")
    nombre = input("Ingrese su nombre: ")

edad = input("Ingrese su edad: ")

while not edad.isdigit():
    print("Por favor, ingrese un número válido para la edad.")
    edad = input("Ingrese su edad: ")

edad = int(edad)

carrera = input("Ingrese su carrera: ")

while not carrera.isalpha():
    print("Por favor, ingrese una carrera válida (solo letras).")
    carrera = input("Ingrese su carrera: ")

print(
    "Bienvenido, "
    + nombre
    + ". Tienes "
    + str(edad)
    + " años y estudias "
    + carrera
    + ". Bienvenido al sistema."
)
