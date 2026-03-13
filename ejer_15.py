# 15. Parqueadero: control de vehículos

carro = 0
moto = 0
total = 0

mayor_pago = 0
placa_mayor = ""

for i in range(0,8,1):

    placa = input("\nIngrese su placa: ")

    print("\nTARIFAS POR HORA:\n* CARRO = $4000\n* MOTO = $2000 ")
    vehiculo = input("\nTipo de Vehiculo?: Carro/Moto ").lower()
    
    hora = int(input("\nHoras de parqueo?: "))

    if vehiculo == "carro":
        carro += 1
        pago = 4000 * hora

    elif vehiculo == "moto":
        moto += 1
        pago = 2000 * hora

    else:
        print("Tipo de vehiculo invalido")
        continue

    total += pago

    if pago > mayor_pago:
        mayor_pago = pago
        placa_mayor = placa

print("\nTotal recaudado: $",total)
print("Carros ingresados: ",carro)
print("Motos ingresadas: ",moto)
print("Vehiculo que pago mas fue el de la placa: ", placa_mayor, "con $", mayor_pago)

print()
