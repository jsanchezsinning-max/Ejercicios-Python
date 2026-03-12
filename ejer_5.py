# 5. Tienda de mascotas: alimento por tipo de animal

print("WELCOME TO THE PET SHOP\n")

print("PETS\n")
print("DOG")
print("CAT")
print("RABBIT\n")

pet = input("what's your pet?").lower()

if pet == "dog":
    print("Give Dog Chow to your dog.")

elif pet == "cat":
    print("Give fish to your cat.")

elif pet == "rabbit":
    print("Give carrots to your rabbit.")

else:
    print("invalid option")