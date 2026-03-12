# 3. Cafetería: total de una compra sencilla

print("WELCOME TO COFFE TIME\n")

print("MENÚ\n")
print("1. Café = $4000")
print("2. Té = $3500")
print("3. Jugo = $5000\n")

Bebida = int(input("Que deseas tomar el dia de hoy?: "))
cantidad = int(input("Cuantas bebidas deseas ordenar?: "))

if Bebida == 1:
    Bebida = 4000

elif Bebida == 2:
    Bebida = 3500

elif Bebida == 3:
    Bebida = 5000

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
total = Bebida * cantidad

print("Total a pagar: ",total)

"""        
print("WELCOME TO COFFE TIME\n")

print("MENÚ\n")
print("Café = $4000")
print("Té = $3500")
print("Jugo = $5000\n")

bebida = input("¿Qué deseas tomar el día de hoy?: ")
cantidad = int(input("¿Cuántas bebidas deseas ordenar?: "))

precio = 0

if bebida == "cafe":
    precio = 4000
elif bebida == "te":
    precio = 3500
elif bebida == "jugo":
    precio = 5000
else:
    print("Esa bebida no está en el menú")

total = precio * cantidad

print("Total a pagar:", total)

"""