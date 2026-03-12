# 9. Spa: servicio disponible

print("WELCOME TO THE SPA\n")

print("Our Services:\n* MASAJE\n* FACIAL\n* MANICURE")

service = input("\nWhat service do you want today?: ").lower()

if service == "masaje" or service == "facial" or service == "manicure":
    print("SERVICE AVAILABLE")    

else:
    print("SERVICE NOT AVAILABLE")
