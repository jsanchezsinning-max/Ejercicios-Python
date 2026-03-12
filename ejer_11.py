# 11. Heladería: factura de varios clientes

total_vendido = 0
clientes = 0

cono_contador = 0
vaso_contador = 0
banana_contador = 0

seguir = "si"

while seguir == "si":

    clientes += 1

    print("1. Cono - $3000")
    print("2. Vaso - $4000")
    print("3. Banana Split - $9000\n")

    producto = int(input("Seleccione producto: "))
    cantidad = int(input("Cantidad: "))

    if producto == 1:
        precio = 3000
        cono_contador += cantidad

    elif producto == 2:
        precio = 4000
        vaso_contador += cantidad

    elif producto == 3:
        precio = 9000
        banana_contador += cantidad

    total = precio * cantidad
    total_vendido += total

    print("\nTotal del cliente:", total)

    seguir = input("¿Hay otro cliente? (si/no): ")

if cono_contador > vaso_contador and cono_contador > banana_contador:
    mas_pedido = "Cono"

elif vaso_contador > banana_contador:
    mas_pedido = "Vaso"

else:
    mas_pedido = "Banana Split"

print("\nTotal vendido:", total_vendido)
print("\nClientes atendidos:", clientes)
print("\nProducto más pedido:", mas_pedido)
