# 12. Gimnasio: promedio de rendimiento semanal

compromiso_bajo = 0
compromiso_medio = 0
compromiso_alto = 0

persona = 0

while persona <= 4:
    
    persona += 1

    name = input("Como te llamas?: ")
    day = int(input("\nCuantos dias entrenaste?: "))
    minutes = int(input("\nCuantos minutos entrenaste por dia?: ")) 
    print()   

    if day < 3:
        print(name, "\nTiene un compromiso bajo con el gym.")
        compromiso_bajo+= 1

    elif day >= 3 and day <= 4:
        print(name, "\nTiene un compromiso a medias con el gym.")
        compromiso_medio += 1

    elif  day >= 5:
        print(name, "\nTiene un compromiso alto con el gym.")
        compromiso_alto += 1

print("\nTotal de Usuarios con bajo compromiso: ", compromiso_bajo)
print("Total de Usuarios con un compromiso a medias: ", compromiso_medio)
print("Total de Usuarios con alto compromiso: ", compromiso_alto)

