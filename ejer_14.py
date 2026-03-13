# 14. Cine: control de sala

capacidad_sala = int(input("\nCapacidad de la sala?: "))

niño = 0
adulto = 0
viejo = 0
personas_ingresadas = 0


while personas_ingresadas < capacidad_sala:

    opcion = input("\n¿Entra una persona? (si/no): ").lower()

    if opcion == "no":
        break

    edad = int(input("\nIngresa tu edad: "))
    personas_ingresadas += 1
    
    if edad >= 0 and edad <= 17:
        niño += 1

    elif edad >= 18 and edad <= 59:
        adulto += 1

    elif edad >= 60:
        viejo += 1

    else:
        print("\nOpcion Invalida")

print("\nTotal de personas ingresadas: ",personas_ingresadas)
print("Total Niños: ",niño)
print("Total Adultos: ",adulto)
print("Total de Adultos Mayores: ",viejo)

if personas_ingresadas == capacidad_sala:
    print("\nLa sala llego a su capacidad maxima")
else:
    print("\nLa sala NO llego a su maxima capacidad")
    print()

