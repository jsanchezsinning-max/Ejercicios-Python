# 7. Peluquería: turno del día

print("WELCOME TO THE BARBERSHOP\n")

print("Elige tu horario entre las 0 hrs y las 23 hrs\n")

hora_de_llegada = int(input("Ingresa tu hora de llegada?: "))

if hora_de_llegada >= 6 and hora_de_llegada <= 11:
    print("Tu turno sera en la mañana")

elif hora_de_llegada >= 12 and hora_de_llegada <= 17:
    print("Tu turno sera en la tarde")

elif hora_de_llegada >= 18 and hora_de_llegada <= 22:
    print("Tu horario sera en la noche")

else:
    print("Horario no disponible")