# Ejercicio 6: eliminar todos los tickets cancelados
tickets = [[1, "Ana", "Atendido"], [2, "Luis", "Cancelado"], [3, "María", "Pendiente"]]

print("Tickets originales:")
for fila in tickets:
    print(fila)

indice = 0
while indice < len(tickets):
    if tickets[indice][2] == "Cancelado":
        tickets.pop(indice)
        # La siguiente fila ocupa este mismo índice
    else:
        indice += 1

print("\nTickets restantes:")
if not tickets:
    print("No quedan tickets.")
for fila in tickets:
    print(fila)
