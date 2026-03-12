# 8. Tienda deportiva: contar productos caros

print("WELCOME TO THE SPORTSHOP\n")

articulo = 0

for i in range(0,6,1):
    precio = int(input("Cual es el valor de tu articulo?: "))

    if precio >= 0 and precio <= 99999:
        articulo = 0

    elif precio >= 100000:
        articulo = articulo + 1

    else:
        if precio < 0:
            print("Numero invalido")

    
print("\nTotal de productos mayor a $100000: ", articulo)

