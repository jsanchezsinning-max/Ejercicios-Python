# 6. Parqueadero: cobro por horas

print("PARKING\n")
print("• 1 hour = 5000 \n• each additional hour = 3000\n")

time = int(input("Enter the hours of parking: "))

if time == 1:
    print("total amount payable: $5000")

else: 
    total = 5000 + (time - 1) * 3000

print("total amount payable: $",total)

