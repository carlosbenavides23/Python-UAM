# Disenar un sistmea de seleccion robusto para un menu de servicios interactivo
# 1: Crear un menu de al menos 4 servicios
# 2: Solicitar el codigo de la opcion y mostrar la accion
# 3: Contemplar obligatoriamente una opcion no valida
# 4: Probar al menos tres entradas diferentes en ejecucion
# Pregunta final en comentarios: Utilizaste if/elif/else o match-case? Porque?

# MENU
print("Bienvenido al sistema de servicios")
print("Servicio 1")
print("Servicio 2")
print("Servicio 3")
print("Servicio 4")
print("Opcion no valida")

opcion = input("Ingrese el codigo de la opcion (1-5): ")

if opcion == "1":
    print("Ha seleccionado el Servicio 1")
elif opcion == "2":
    print("Ha seleccionado el Servicio 2")
elif opcion == "3":
    print("Ha seleccionado el Servicio 3")
elif opcion == "4":
    print("Ha seleccionado el Servicio 4")
elif opcion == "5":
    print("Ha seleccionado una opcion no valida")
else:
    print("Opcion invalida. Por favor, ingrese un numero del 1 al 5.")

# Respuesta: Utilice if/elif/else porque es la estructura más adecuada para manejar múltiples condiciones y valores específicos.
