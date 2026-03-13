#1. Heladería: sabor más pedido

print("BIENVENIDO\n")

vainilla = 0
chocolate = 0
fresa = 0

for i in range(0,5,1):
    print("Escoge tu sabor favorito")
    sabor = int(input("1. Vainilla  -  2. Chocolate  -  3. Fresa: " ))

    if sabor == 1:
        vainilla = vainilla + 1

    elif sabor == 2:
        chocolate = chocolate + 1

    elif sabor == 3:
        fresa = fresa + 1

print("\nCantidad de Helados de Vainilla", vainilla)
print("Cantidad de Helados de Chocolate", chocolate)
print("Cantidad de Helados de Fresa", fresa)
