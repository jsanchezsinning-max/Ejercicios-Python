# 13. Cafetería: descuento por consumo

total_dia = 0

pedido = ""

while pedido != "salir":

    print("\nMENU")
    print("cafe - 4000")
    print("capuchino - 7000")
    print("pastel - 6000")

    pedido = input("Que deseas pedir? (o escribe salir): ")

    if pedido == "salir":
        break

    cantidad = int(input("Cuantos deseas?: "))

    if pedido == "cafe":
        precio = 4000

    elif pedido == "capuchino":
        precio = 7000

    elif pedido == "pastel":
        precio = 6000

    else:
        print("Producto no valido")
        continue

    total = precio * cantidad

    if total > 20000:
        descuento = total * 0.10
        total = total - descuento
        print("Se aplico descuento del 10% de: $", descuento)

    print("Total a pagar: $", total)

    total_dia += total


print("\nTotal vendido en el dia: ", total_dia)
