#2. Gimnasio: acceso por edad

print("WELCOME TO PERFORMANCE GYM\n")

age = int(input("Enter your Age: "))

if age >= 0 and age < 13:
    print("You can't enter")

elif age >= 13 and age < 18:
    print("Young class")

elif age >= 18 and age <= 59:
    print("General class")

elif age >= 60:
    print("Senior class")

else:
    print("Invalid Option")

    

