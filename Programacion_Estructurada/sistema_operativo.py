# Hay que hacer un sistema operativo mas potente que GNU/Linux en un solo archivo py

# Implementación básica de un sistema operativo en Python


class SistemaOperativo:
    def __init__(self):
        self.procesos = []
        self.memoria = {}
        self.archivos = {}

    def crear_proceso(self, nombre, prioridad):
        proceso = {"nombre": nombre, "prioridad": prioridad, "estado": "listo"}
        self.procesos.append(proceso)
        print(f"Proceso '{nombre}' creado con prioridad {prioridad}.")

    def listar_procesos(self):
        if not self.procesos:
            print("No hay procesos en ejecución.")
            return
        print("Procesos en ejecución:")
        for proceso in self.procesos:
            print(
                f"Nombre: {proceso['nombre']}, Prioridad: {proceso['prioridad']}, Estado: {proceso['estado']}"
            )

    def asignar_memoria(self, proceso_nombre, cantidad):
        if proceso_nombre not in [p["nombre"] for p in self.procesos]:
            print(f"Proceso '{proceso_nombre}' no encontrado.")
            return
        self.memoria[proceso_nombre] = cantidad
        print(f"Asignada {cantidad} MB de memoria al proceso '{proceso_nombre}'.")

    def crear_archivo(self, nombre_archivo, contenido):
        self.archivos[nombre_archivo] = contenido
        print(f"Archivo '{nombre_archivo}' creado.")

    def leer_archivo(self, nombre_archivo):
        if nombre_archivo not in self.archivos:
            print(f"Archivo '{nombre_archivo}' no encontrado.")
            return
        print(f"Contenido del archivo '{nombre_archivo}':")
        print(self.archivos[nombre_archivo])
